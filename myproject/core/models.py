from django.db import models

STATUS = (
    ('0', ''),
    ('p', 'pendente'),
    ('c', 'cancelado'),
    ('a', 'aprovado'),
)


class Person(models.Model):
    name = models.CharField('nome', max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField('telefone', max_length=11, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return self.name
