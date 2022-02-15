# Django_Rest
Projeto simples com intuito de aprendizagem utilizando as tecnologias Python,Django e Django REST Framework.


# Instalação

## Linux

### Ambiente Virtual
```
python3 -m venv venv
source venv/bin/activate
```

Instalar dependências
```
pip install -r requirements.txt
```

Na primeira instalação criar migrations
```
cd Rest
python manage.py makemigrations
python manage.py migrate
```

Criar superusuario
```
python manage.py createsuperuser
```

Iniciar Django
```
python manage.py runserver
```
