# Generated by Django 2.2 on 2020-04-15 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_auto_20200414_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]