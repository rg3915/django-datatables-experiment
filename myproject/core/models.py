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
    status = models.CharField(
        max_length=1,
        choices=STATUS,
        default='p'
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

    def __str__(self):
        return self.name

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'status': self.get_status_display(),
        }
