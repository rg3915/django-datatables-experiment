# django-datatables-experiment

Experiment with Django and DataTables.

[Video no YouTube](https://www.youtube.com/watch?v=NeZ39HE_zKg)


## Como rodar este projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/django-datatables-experiment.git
cd django-datatables-experiment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```