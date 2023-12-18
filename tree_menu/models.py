from django.db import models


class Menu(models.Model):
    name = models.CharField(
        'Название пункта меню', max_length=50, unique=True)
    description = models.TextField(
        'Описание', max_length=300, blank=True)
    url = models.CharField(
        verbose_name='URL стороннего ресурса',
        help_text='При пустом поле URL определяется дочерние меню, в ином случае переход на сторонний ресурс',
        max_length=255, blank=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='menu_items')

    class Meta:
        ordering = ['id']
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        return self.name
