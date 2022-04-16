from django.db import models


class Category(models.Model):
    title = models.CharField(verbose_name='Title', max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Title', max_length=50)

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.title


class Ads(models.Model):
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, verbose_name='Subcategory', on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Description')
    date = models.DateField(verbose_name='Date')

    class Meta:
        verbose_name = 'Ad'
        verbose_name_plural = 'Ads'

    def __str__(self):
        return self.description