## crud_django

### Simples CRUD usando o Django e Bootstrap.

#### Passo 1

Crie e ative o ambiente virtual.

#### Windows

```python
python -m venv .venv
```

```powershell
.venv\Scripts\activate
```

#### Linux

```python
python -m venv .venv
```

```bash
source .venv/bin/activate
```

#### Passo 2

Instale os requisitos do projeto.

```python
pip install -r requirements.txt
```

#### Passo 3

Crie a nova migração de tabela para ser inserida no banco de dados.

```python
python manage.py makemigrations
```

#### Passo 4

Execute o migrate para inserir a migração definitivamente no banco.

````python
python manage.py migrate
````

#### Passo 5

Execute o servidor de desenvolvimento do Django.

```python
python manage.py runserver
```

#### Passo 6

Abra a url http://localhost:8000 em seu navegador.

