# Generated by Django 5.0.1 on 2024-01-29 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0004_produto_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=models.SlugField(max_length=200),
        ),
    ]