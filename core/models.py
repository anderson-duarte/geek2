from django.db import models
from stdimage.models import StdImageField


class Base(models.Model):
    criado = models.DateField(verbose_name='Criação', auto_now_add=True)
    modificado = models.DateField(verbose_name='Atualizado', auto_now=True)
    ativo = models.BooleanField(verbose_name='Ativo?', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONES_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )

    servico = models.CharField(verbose_name='Serviço', max_length=100)
    descricao = models.TextField(verbose_name='Descrição', max_length=200)
    icone = models.CharField(verbose_name='Icone', max_length=20, choices=ICONES_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField(verbose_name='Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField(verbose_name='Nome', max_length=100)
    cargo = models.ForeignKey(Cargo, verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField(verbose_name='Bio', max_length=200)
    imagem = StdImageField(verbose_name='Imagem', upload_to='equipe', variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField(verbose_name='Facebook', max_length=100, default='#')
    twitter = models.CharField(verbose_name='Twitter', max_length=100, default='#')
    instagran = models.CharField(verbose_name='Instagran', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Recurso(Base):
    RECURSOS_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-layers', 'Camadas'),
        ('lni-laptop-phone', 'PC'),
        ('lni-leaf', 'Folha'),
        ('lni-rocket', 'Foguete'),
    )

    recurso = models.CharField(verbose_name='Recurso', max_length=100)
    descricao = models.TextField(verbose_name='Descrição', max_length=200)
    icone = models.CharField(verbose_name='Icone', max_length=20, choices=RECURSOS_CHOICES)

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return self.recurso