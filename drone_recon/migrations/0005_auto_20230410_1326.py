# Generated by Django 3.1.8 on 2023-04-10 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drone_recon', '0004_auto_20230410_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trial',
            name='rt_classification',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='trial',
            name='rt_confidence',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
