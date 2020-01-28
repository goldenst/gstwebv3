# Generated by Django 2.2 on 2020-01-06 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='cdl',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='cdlexp',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='cell',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='tsac',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='wm23',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='wm45',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='wm67',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='wm89',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='hireDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
