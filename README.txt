# LinkedIn Token Retriever / Recuperador de Token do LinkedIn

## English Version

This project is a Flask application that allows users to authenticate via LinkedIn, retrieve an access token, refresh token (if available), expiration time, person ID, and organization ID.

### Features

- LinkedIn OAuth 2.0 authentication
- Retrieval of Access Token and Refresh Token
- Token expiration time tracking
- Retrieval of Person ID (personal profile ID)
- Retrieval of Organization ID (company page ID)
- Simple web interface to display the data

---

### Prerequisites

Before running the project, ensure you have the following set up:

1. **Create a LinkedIn Developer App:**
   - Go to [LinkedIn Developer](https://www.linkedin.com/developers/apps)
   - Create a new app and fill in the required details.
   - Add the following products to your app:
     - "Sign In with LinkedIn"
     - "Marketing Developer Platform"
   - Copy the `Client ID` and `Client Secret`.
   - Set the redirect URL to: `http://127.0.0.1:5000/callback`

2. **Set the required scopes:**
   - Ensure the following permissions are selected:
     - `openid profile email`
     - `r_basicprofile`
     - `r_organization_admin`
     - `r_organization_social`
     - `rw_organization_admin`
     - `w_organization_social`
     - `w_member_social`

3. **Create and configure the `.env` file**

Create a `.env` file in the root directory with the following content:

```
LINKEDIN_CLIENT_ID=YOUR_CLIENT_ID
LINKEDIN_CLIENT_SECRET=YOUR_CLIENT_SECRET
LINKEDIN_REDIRECT_URI=http://127.0.0.1:5000/callback
```

4. **Create and activate a virtual environment (venv)**

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

---

### Installation and Execution

1. Clone the repository:

```bash
git clone https://github.com/yourusername/linkedin_token.git
cd linkedin_token
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask application:

```bash
python app.py
```

4. Open in your browser:

```plaintext
http://127.0.0.1:5000
```

---

### Project Structure

```
linkedin_token/
│-- app.py               # Main Flask application
│-- config.py            # Configuration settings
│-- templates/
│   ├── home.html         # Authentication page
│   ├── dashboard.html    # Data display page
│-- .env                  # Environment variables
│-- requirements.txt      # Project dependencies
```

---

### Customization

- You can edit the HTML templates in the `templates/` directory to customize the appearance.
- To modify the requested scopes, update the authentication URL in `app.py`.

---

### License

This project is licensed under the [MIT License](LICENSE).

---

## Versão em Português

Este projeto é uma aplicação Flask que permite autenticar usuários via LinkedIn, obter um token de acesso, um token de atualização (se disponível), tempo de expiração, ID da pessoa e ID da organização associada.

### Funcionalidades

- Autenticação via LinkedIn OAuth 2.0
- Obtenção do Access Token e Refresh Token
- Rastreamento do tempo de expiração do token
- Obtenção do Person ID (ID do perfil pessoal)
- Obtenção do Organization ID (ID da página da empresa)
- Interface web simples para visualizar os dados

---

### Pré-requisitos

Antes de rodar o projeto, certifique-se de que possui os seguintes itens configurados:

1. **Criar um aplicativo no LinkedIn Developer:**
   - Acesse [LinkedIn Developer](https://www.linkedin.com/developers/apps)
   - Crie um novo aplicativo e preencha os detalhes necessários.
   - Adicione os seguintes produtos ao seu aplicativo:
     - "Sign In with LinkedIn"
     - "Marketing Developer Platform"
   - Copie o `Client ID` e o `Client Secret`.
   - Defina a URL de redirecionamento para: `http://127.0.0.1:5000/callback`

2. **Configurar os escopos necessários:**
   - Certifique-se de selecionar as seguintes permissões:
     - `openid profile email`
     - `r_basicprofile`
     - `r_organization_admin`
     - `r_organization_social`
     - `rw_organization_admin`
     - `w_organization_social`
     - `w_member_social`

3. **Criar e configurar o arquivo `.env`**

Crie um arquivo `.env` no diretório raiz com o seguinte conteúdo:

```
LINKEDIN_CLIENT_ID=SEU_CLIENT_ID
LINKEDIN_CLIENT_SECRET=SEU_CLIENT_SECRET
LINKEDIN_REDIRECT_URI=http://127.0.0.1:5000/callback
```

4. **Criar e ativar um ambiente virtual (venv)**

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

---

### Instalação e execução

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/linkedin_token.git
cd linkedin_token
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute a aplicação Flask:

```bash
python app.py
```

4. Acesse no navegador:

```plaintext
http://127.0.0.1:5000
```

---

### Estrutura do projeto

```
linkedin_token/
│-- app.py               # Código principal Flask
│-- config.py            # Configurações
│-- templates/
│   ├── home.html         # Página de autenticação
│   ├── dashboard.html    # Página de exibição de dados
│-- .env                  # Variáveis de ambiente
│-- requirements.txt      # Dependências do projeto
```

---

### Licença

Este projeto é licenciado sob a [MIT License](LICENSE).