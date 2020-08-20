# Generated by Django 3.1 on 2020-08-19 00:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
        ('receitas', '0002_auto_20200818_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='pessoa',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pessoas.pessoa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='receita',
            name='data_receita',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 18, 21, 46, 51, 246867)),
        ),
    ]