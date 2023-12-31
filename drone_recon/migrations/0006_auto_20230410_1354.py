# Generated by Django 3.1.8 on 2023-04-10 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drone_recon', '0005_auto_20230410_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='strategy',
        ),
        migrations.RemoveField(
            model_name='session',
            name='strategy_radio',
        ),
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prompt', models.CharField(max_length=1000)),
                ('response', models.CharField(max_length=1000)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='strategies', to='drone_recon.session')),
            ],
        ),
    ]
