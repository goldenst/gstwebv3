# Generated by Django 2.2 on 2020-04-15 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20200414_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='start',
            field=models.CharField(max_length=100),
        ),
    ]
