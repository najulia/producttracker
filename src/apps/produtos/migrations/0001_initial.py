# Generated by Django 5.0.1 on 2024-01-26 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300)),
                ('preco', models.FloatField()),
                ('descricao', models.TextField()),
                ('foto', models.CharField(max_length=1000)),
                ('em_estoque', models.BooleanField(default=False)),
            ],
        ),
    ]