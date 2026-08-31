from django.db import models

# Create your models here.
class Item(models.Model):
    slug = models.SlugField('Унікальна назва', unique=True)
    title = models.CharField('Назва товару', max_length=200)
    image = models.CharField('Фото товару', max_length=50)
    desc = models.TextField('Опис товару')
    price = models.DecimalField('Ціна', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title
