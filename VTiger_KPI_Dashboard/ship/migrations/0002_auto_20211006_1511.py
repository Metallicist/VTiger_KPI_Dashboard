# Generated by Django 3.0.7 on 2021-10-06 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='products',
            name='length',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='products',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='products',
            name='width',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
