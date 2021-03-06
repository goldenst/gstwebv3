# Generated by Django 2.2 on 2020-04-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='previousEmployerContact3',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='previousEmployerEnd3',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='previousEmployerStart3',
            field=models.DateField(blank=True, null=True),
        ),
    ]
