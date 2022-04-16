from django.db import models


class User(models.Model):
    user_id = models.CharField(verbose_name='User ID', max_length=100)
    first_name = models.CharField(verbose_name='First name', max_length=20, null=True, blank=True)
    last_name = models.CharField(verbose_name='Last name', max_length=20, null=True, blank=True)
    username = models.CharField(verbose_name='Username', max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.user_id


class Category(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Caregory', max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Test(models.Model):
    question = models.TextField(verbose_name='Question')
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Caregory', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Tests'

    def __str__(self):
        return self.question


class Answers(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    test = models.ForeignKey(Test, verbose_name='Test', on_delete=models.CASCADE)
    answer = models.TextField(verbose_name='Answer')

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __str__(self):
        return self.answer