# Generated by Django 2.2 on 2020-02-14 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
        ('damages', '0006_auto_20200120_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='damage',
            name='driver',
        ),
        migrations.AddField(
            model_name='damage',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='employees.Employee'),
            preserve_default=False,
        ),
    ]
