# Generated by Django 2.1 on 2018-09-03 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='cod_reserva',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
