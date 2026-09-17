# Catálogo Pessoal de Jogos

Um sistema web desenvolvido em **Python + Django** para cadastrar, visualizar, pesquisar, filtrar, editar e excluir jogos de um catálogo pessoal.

## Tecnologias utilizadas

* Python
* Django
* SQLite
* HTML
* CSS
* Git e GitHub

---

## Requisitos

Antes de instalar o projeto, é necessário ter instalado:

* **Python 3.10 ou superior**
* **Git**

Para verificar se o Python está instalado:

```bash
python --version
```

Para verificar o Git:

```bash
git --version
```

---

## Instalação

### 1. Baixe o projeto

Abra o **Git Bash** ou o terminal e execute:

```bash
git clone https://github.com/D-allves/softwere-django.git
```

Depois entre na pasta:

```bash
cd softwere-django
```

---

### 2. Crie o ambiente virtual

No Windows:

```bash
python -m venv venv
```

---

### 3. Ative o ambiente virtual

No **Git Bash**:

```bash
source venv/Scripts/activate
```

No **CMD**:

```cmd
venv\Scripts\activate
```

No **PowerShell**:

```powershell
venv\Scripts\Activate.ps1
```

Quando o ambiente estiver ativado, aparecerá algo parecido com:

```text
(venv)
```

no início da linha do terminal.

---

### 4. Instale o Django

Com o ambiente virtual ativado:

```bash
pip install django
```

---

### 5. Configure o banco de dados

Execute:

```bash
python manage.py migrate
```

Esse comando cria as tabelas necessárias para o funcionamento do sistema.

---

### 6. Inicie o servidor

Execute:

```bash
python manage.py runserver
```

Se tudo estiver correto, aparecerá uma mensagem semelhante a:

```text
Starting development server at http://127.0.0.1:8000/
```

---

### 7. Acesse o sistema

Abra o navegador e acesse:

```text
http://127.0.0.1:8000/
```

O sistema estará funcionando na sua máquina.

---

## Funcionalidades

O sistema permite:

* Adicionar jogos
* Visualizar jogos cadastrados
* Editar jogos
* Excluir jogos
* Pesquisar jogos pelo nome
* Filtrar jogos por status
* Ordenar jogos pela nota
* Visualizar a quantidade total de jogos
* Visualizar a média das notas

---

## Estrutura do projeto

```text
softwere-django/
│
├── catalogo/
│   ├── migrations/
│   ├── templates/
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

---

## Importante

A pasta `venv` não precisa ser enviada para o GitHub.

Depois de baixar o projeto, o usuário deve criar seu próprio ambiente virtual seguindo os passos deste README.

O projeto utiliza **SQLite**, portanto não é necessário instalar MySQL, PostgreSQL ou outro banco de dados.

---

## Parando o servidor

Para parar o servidor Django, pressione:

```text
CTRL + C
```

---

## Executando novamente

Quando quiser iniciar o projeto novamente:

```bash
cd softwere-django
```

Ative o ambiente virtual:

```bash
source venv/Scripts/activate
```

Depois execute:

```bash
python manage.py runserver
```

Acesse novamente:

```text
http://127.0.0.1:8000/
```

---

## Projeto

**Catálogo Pessoal de Jogos**

Projeto desenvolvido para fins de estudo em **Análise e Desenvolvimento de Sistemas (ADS)**.
