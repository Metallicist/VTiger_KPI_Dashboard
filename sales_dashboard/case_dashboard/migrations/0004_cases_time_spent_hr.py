# Generated by Django 3.0.3 on 2020-12-02 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case_dashboard', '0003_auto_20201130_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='cases',
            name='time_spent_hr',
            field=models.CharField(default='0 Days, 0 Hours, 0 Minutes', max_length=75),
            preserve_default=False,
        ),
    ]
