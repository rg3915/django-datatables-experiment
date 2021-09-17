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
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```

## Reescrevendo o projeto a partir da base

```
git clone https://github.com/rg3915/django-datatables-experiment.git --branch base
cd django-datatables-experiment
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
```


```python
# models.py
class Person(models.Model):
    ...
    status = models.CharField(
            max_length=1,
            choices=STATUS,
            default='p'
        )
```


```python
# create_data.py
def create_person():
    aux_list = []
    Person.objects.all().delete()
    for _ in range(100):
        name = f'{fake.first_name()} {fake.last_name()}'
        email = f'{slugify(name)}@email.com'
        phone = gen_phone()
        status = gen_status()  # <---
        obj = Person(
            name=name,
            email=email,
            phone=phone,
            status=status,  # <---
        )
        aux_list.append(obj)
```

Após remodelar `models.py` faça


```
python manage.py makemigrations
python manage.py migrate
python manage.py create_data
```

