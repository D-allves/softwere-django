# Catálogo Pessoal de Jogos

Um sistema web desenvolvido em Python + Django para cadastrar, visualizar, pesquisar, filtrar, editar e excluir jogos de um catálogo pessoal. O acesso ao catálogo é protegido por **login**.

## Tecnologias utilizadas

* Python
* Django
* SQLite
* HTML
* CSS
* Git e GitHub

## Requisitos

Antes de instalar o projeto, é necessário ter instalado:

* Python 3.10 ou superior
* Git

Para verificar se o Python está instalado:

```
python --version
```

Para verificar o Git:

```
git --version
```

## Instalação

### 1. Baixe o projeto

Abra o Git Bash ou o terminal e execute:

```
git clone https://github.com/D-allves/softwere-django.git
```

Depois entre na pasta:

```
cd softwere-django
```

### 2. Crie o ambiente virtual

No Windows:

```
python -m venv venv
```

### 3. Ative o ambiente virtual

No Git Bash:

```
source venv/Scripts/activate
```

No CMD:

```
venv\Scripts\activate
```

No PowerShell:

```
venv\Scripts\Activate.ps1
```

Quando o ambiente estiver ativado, aparecerá algo parecido com:

```
(venv)
```

no início da linha do terminal.

### 4. Instale o Django

Com o ambiente virtual ativado:

```
pip install django
```

### 5. Configure o banco de dados

Execute:

```
python manage.py migrate
```

Esse comando cria as tabelas necessárias para o funcionamento do sistema.

### 6. Inicie o servidor

Execute:

```
python manage.py runserver
```

Se tudo estiver correto, aparecerá uma mensagem semelhante a:

```
Starting development server at http://127.0.0.1:8000/
```

### 7. Acesse o sistema

Abra o navegador e acesse:

```
http://127.0.0.1:8000/
```

Como o catálogo é protegido, você será redirecionado para a tela de login. Entre com o usuário que já está cadastrado no sistema:

| Campo   | Valor      |
|---------|------------|
| Usuário | `Admin`    |
| Senha   | `admin123` |

O Django diferencia letras maiúsculas e minúsculas, então digite o usuário exatamente como acima, com **A** maiúsculo.

Depois de entrar, você será levado ao catálogo de jogos.

## Login e logout

* **Login:** `http://127.0.0.1:8000/login/`
* **Logout:** botão **Sair** no canto superior direito do catálogo
* Quem tentar acessar qualquer página do catálogo sem estar logado é redirecionado automaticamente para a tela de login.

## Funcionalidades

O sistema permite:

* Fazer login e logout
* Proteger todas as páginas do catálogo com autenticação
* Adicionar jogos
* Visualizar jogos cadastrados
* Editar jogos
* Excluir jogos
* Pesquisar jogos pelo nome
* Filtrar jogos por status
* Ordenar jogos pela nota
* Visualizar a quantidade total de jogos
* Visualizar a média das notas

## Estrutura do projeto

```
softwere-django/
│
├── catalogo/
│   ├── migrations/
│   ├── templates/
│   │   └── catalogo/
│   │       ├── adicionar_jogo.html
│   │       ├── editar_jogo.html
│   │       ├── lista_jogos.html
│   │       └── login.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
├── README.md
└── venv/
```

## Importante

* A pasta `venv` não precisa ser enviada para o GitHub.
* Depois de baixar o projeto, o usuário deve criar seu próprio ambiente virtual seguindo os passos deste README.
* O projeto utiliza SQLite, portanto não é necessário instalar MySQL, PostgreSQL ou outro banco de dados.
* O usuário `Admin` já está salvo no banco de dados do projeto (`db.sqlite3`), por isso não é necessário criar um usuário para entrar.
* Esse usuário e essa senha servem apenas para testes locais e estudo.
* Se o catálogo abrir sem pedir login, pode ser que você já esteja logado (o navegador guarda a sessão) ou que exista outro servidor antigo rodando na porta 8000. Teste em uma janela anônima.

## Parando o servidor

Para parar o servidor Django, pressione:

```
CTRL + C
```

## Executando novamente

Quando quiser iniciar o projeto novamente:

```
cd softwere-django
```

Ative o ambiente virtual:

```
source venv/Scripts/activate
```

Depois execute:

```
python manage.py runserver
```

Acesse novamente:

```
http://127.0.0.1:8000/
```

Entre com o usuário `Admin` e a senha `admin123`.

## Projeto

Catálogo Pessoal de Jogos

Projeto desenvolvido para fins de estudo em Análise e Desenvolvimento de Sistemas (ADS).
