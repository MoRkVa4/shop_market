# Generated by Django 4.2 on 2023-04-27 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Название товара')),
                ('descr', models.TextField(verbose_name='Описание товара')),
                ('price', models.IntegerField(verbose_name='Стоимость товара')),
                ('quantity', models.IntegerField(verbose_name='Кол-во товара')),
                ('is_available', models.BooleanField(default=True, verbose_name='Есть в наличии?')),
                ('slug', models.SlugField()),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.category')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
