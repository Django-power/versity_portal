# Generated by Django 3.0 on 2019-12-14 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
        ('cource', '0003_auto_20191214_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courcelab',
            name='bulding',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pages.Bulding'),
        ),
    ]
