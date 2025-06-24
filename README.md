# LinkedIn Token Retriever 🔐

*Autenticação OAuth 2.0 via LinkedIn com exibição de tokens e IDs úteis para automações.*

![MIT License](https://img.shields.io/github/license/seuusuario/linkedin_token)

---

## 📑 Índice

1. [Visão Geral](#visão-geral)
2. [Funcionalidades](#funcionalidades)
3. [Pré-requisitos](#pré-requisitos)
4. [Configuração do Ambiente](#configuração-do-ambiente)
5. [Execução](#execução)
6. [Estrutura do Projeto](#estrutura-do-projeto)
7. [Personalização](#personalização)
8. [Licença](#licença)

---

## Visão Geral

Este projeto é uma aplicação **Flask** simples para autenticar via **LinkedIn OAuth 2.0** e capturar os seguintes dados:

* Access Token
* Refresh Token (se aplicável)
* Tempo de expiração do token
* Person ID (ID do perfil pessoal)
* Organization ID (ID da página empresarial)

Ideal para desenvolvedores que precisam testar ou configurar integrações com a API do LinkedIn.

---

## Funcionalidades

* Autenticação com LinkedIn OAuth 2.0
* Visualização dos dados autenticados em interface web
* Suporte a múltiplos escopos (perfil, páginas, social sharing)

---

## Pré-requisitos

1. **Criar um aplicativo no LinkedIn Developer:**
   Acesse [LinkedIn Developer](https://www.linkedin.com/developers/apps)

   * Adicione os produtos:

     * "Sign In with LinkedIn"
     * "Marketing Developer Platform"
   * Copie seu `Client ID` e `Client Secret`
   * Defina o redirect URI para:

     ```http
     http://127.0.0.1:5000/callback
     ```

2. **Permissões necessárias (scopes):**

   * `openid profile email`
   * `r_organization_admin`
   * `r_organization_social`
   * `rw_organization_admin`
   * `w_organization_social`
   * `w_member_social`

3. **Crie o arquivo `.env` com as credenciais:**

   ```env
   LINKEDIN_CLIENT_ID=SEU_CLIENT_ID
   LINKEDIN_CLIENT_SECRET=SEU_CLIENT_SECRET
   LINKEDIN_REDIRECT_URI=http://127.0.0.1:5000/callback
   ```

---

## Configuração do Ambiente

```bash
# 1. Crie o ambiente virtual
python3 -m venv venv

# 2. Ative o ambiente
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# 3. Instale as dependências
pip install -r requirements.txt
```

---

## Execução

```bash
# Rode o app Flask
python app.py
```

Acesse no navegador:

```text
http://127.0.0.1:5000
```

---

## Estrutura do Projeto

```text
linkedin_token/
├── app.py               # Aplicação principal Flask
├── config.py            # Configurações OAuth e helpers
├── templates/           # Páginas HTML
│   ├── home.html        # Página inicial com botão de login
│   └── dashboard.html   # Exibição dos dados pós-login
├── .env                 # Variáveis de ambiente (não versionado)
├── requirements.txt     # Dependências do projeto
```

---

## Personalização

* **Templates**: edite `templates/home.html` e `dashboard.html` para mudar layout.
* **Escopos**: altere os escopos desejados em `config.py` para testar diferentes permissões.

---

## Licença

Distribuído sob a licença [MIT](LICENSE).
