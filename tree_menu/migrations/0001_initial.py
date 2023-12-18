# Generated by Django 4.1.5 on 2023-12-18 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название пункта меню')),
                ('description', models.TextField(blank=True, max_length=300, verbose_name='Описание')),
                ('url', models.CharField(blank=True, help_text='При пустом поле URL определяется дочерние меню, в ином случае переход на сторонний ресурс', max_length=255, verbose_name='URL стороннего ресурса')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='tree_menu.menu')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
                'ordering': ['id'],
            },
        ),
    ]