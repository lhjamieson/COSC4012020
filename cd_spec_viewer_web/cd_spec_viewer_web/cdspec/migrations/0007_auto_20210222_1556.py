# Generated by Django 3.0.10 on 2021-02-22 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdspec', '0006_auto_20210222_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specrun',
            name='number_of_amino_acids',
            field=models.IntegerField(verbose_name='Number of amino acids'),
        ),
    ]
