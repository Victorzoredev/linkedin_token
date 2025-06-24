import os
import json
import requests
from pathlib import Path
from flask import Flask, redirect, request, session, url_for, render_template
from dotenv import load_dotenv
import time
from datetime import datetime, timezone

# Carrega variáveis do arquivo .env na raiz do projeto
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "supersecretkey")  # Recomenda-se definir FLASK_SECRET_KEY no .env

# -------------------------------------------------------
# Busca diretório principal e templates
# -------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"
app.template_folder = str(TEMPLATES_DIR)

# -------------------------------------------------------
# Variáveis de ambiente do LinkedIn (via dotenv)
# -------------------------------------------------------
LINKEDIN_CLIENT_ID     = os.getenv("LINKEDIN_CLIENT_ID")
LINKEDIN_CLIENT_SECRET = os.getenv("LINKEDIN_CLIENT_SECRET")
LINKEDIN_REDIRECT_URI  = os.getenv("LINKEDIN_REDIRECT_URI")
AUTH_URL               = os.getenv("LINKEDIN_AUTH_URL", "https://www.linkedin.com/oauth/v2/authorization")
TOKEN_URL              = os.getenv("LINKEDIN_TOKEN_URL", "https://www.linkedin.com/oauth/v2/accessToken")

# Verifica se todas as variáveis obrigatórias existem
required_envs = [
    "LINKEDIN_CLIENT_ID",
    "LINKEDIN_CLIENT_SECRET",
    "LINKEDIN_REDIRECT_URI",
]
missing = [name for name in required_envs if not os.getenv(name)]
if missing:
    raise RuntimeError(f"Variáveis de ambiente não configuradas: {', '.join(missing)}")

@app.route('/')
def home():
    linkedin_auth_url = (
        f"{AUTH_URL}?response_type=code"
        f"&client_id={LINKEDIN_CLIENT_ID}"
        f"&redirect_uri={LINKEDIN_REDIRECT_URI}"
        f"&scope=openid profile email r_basicprofile r_organization_admin "
        f"r_organization_social rw_organization_admin w_organization_social w_member_social"
    )
    return render_template('home.html', auth_url=linkedin_auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return "Erro ao obter código de autorização", 400

    token_response = requests.post(
        TOKEN_URL,
        data={
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': LINKEDIN_REDIRECT_URI,
            'client_id': LINKEDIN_CLIENT_ID,
            'client_secret': LINKEDIN_CLIENT_SECRET
        },
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )

    token_data = token_response.json()

    # Salva token_data completo em outputtoken.txt
    with open("outputtoken.txt", "a", encoding="utf-8") as f:
        f.write(json.dumps(token_data, ensure_ascii=False, indent=2))
        f.write("\n----\n")  # separador entre execuções

    if 'access_token' in token_data:
        # Calcula a data/hora de expiração
        expires_in = token_data.get('expires_in', 0)
        expires_at = int(time.time()) + int(expires_in)
        expires_at_str = datetime.utcfromtimestamp(expires_at).replace(tzinfo=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

        session['linkedin_token'] = token_data['access_token']
        session['expires_in'] = expires_in
        session['expires_at'] = expires_at
        session['expires_at_str'] = expires_at_str
        session['refresh_token'] = token_data.get('refresh_token', 'N/A')

        return f"""
            <h2>Token obtido com sucesso!</h2>
            <b>access_token:</b> {token_data['access_token']}<br>
            <b>refresh_token:</b> {session['refresh_token']}<br>
            <b>expires_in:</b> {expires_in} segundos<br>
            <b>expira em:</b> {expires_at_str}<br>
            <br>
            <a href="{url_for('get_ids')}">Continuar para obter IDs</a>
        """
    else:
        return f"Erro ao obter token: {json.dumps(token_data)}", 400

@app.route('/get_ids')
def get_ids():
    access_token = session.get('linkedin_token')
    if not access_token:
        return redirect(url_for('home'))

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    # Obtendo o ID da pessoa
    profile_response = requests.get("https://api.linkedin.com/v2/me", headers=headers)
    profile_data = profile_response.json()
    person_id = profile_data.get('id', 'N/A')

    # Obtendo o ID da empresa
    org_response = requests.get("https://api.linkedin.com/v2/organizationAcls?q=roleAssignee", headers=headers)
    org_data = org_response.json()
    elements = org_data.get('elements', [])
    org_id = 'N/A'
    if elements:
        org_urn = elements[0].get('organization', '')
        org_id = org_urn.split(':')[-1] if org_urn else 'N/A'

    return render_template(
        'dashboard.html',
        access_token=session['linkedin_token'],
        refresh_token=session['refresh_token'],
        expires_in=session['expires_in'],
        expires_at=session.get('expires_at_str', 'N/A'),
        person_id=person_id,
        org_id=org_id
    )

if __name__ == '__main__':
    app.run(debug=True)
