# Generated by Django 4.2.16 on 2024-12-04 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_sugars', '0003_auto_20241204_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodsugarrecord',
            name='basal_insulin',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bloodsugarrecord',
            name='bolus_insulin',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
