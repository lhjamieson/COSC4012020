# Generated by Django 3.0.10 on 2021-02-19 15:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdspec', '0003_auto_20201101_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specrun',
            name='source_file',
            field=models.FileField(upload_to='cdspecruns', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['csv'])]),
        ),
    ]