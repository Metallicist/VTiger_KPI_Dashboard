# Generated by Django 3.0.3 on 2020-11-30 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case_dashboard', '0002_auto_20201127_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cases',
            name='createdtime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='cases',
            name='modifiedtime',
            field=models.DateTimeField(),
        ),
    ]