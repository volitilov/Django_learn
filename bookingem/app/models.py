from django.db import models

# ::::::::::::::::::::::::::::::::::::::::::::::::::::

class Category(models.Model):
    class Meta:
        db_table = 'categories'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    name = models.CharField(max_length=30, unique=True, verbose_name='название')
    description = models.TextField()

    def __str__(self):
        return self.name


class Good(models.Model):
    class Meta:
        db_table = 'goods'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
    
    name = models.CharField(max_length=50, unique=True, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    in_stock = models.BooleanField(default=True, db_index=True, verbose_name='в наличии')
    category = models.ForeignKey(Category, verbose_name='категория(и)', 
                    null=True, blank=True)


    def __str__(self):
        s = self.name
        if not self.in_stock:
            s = s + ' ( нет в наличии )'
        return s
