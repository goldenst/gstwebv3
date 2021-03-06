# Generated by Django 2.2 on 2020-02-14 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aaaDriverNumber', models.CharField(blank=True, max_length=8, null=True)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('zipCode', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=200, null=True, unique=True)),
                ('driversLicence', models.CharField(blank=True, max_length=10, null=True)),
                ('dlExpire', models.DateField()),
                ('cellphone', models.CharField(max_length=10)),
                ('homePhone', models.CharField(blank=True, max_length=10, null=True)),
                ('hiredate', models.DateField()),
                ('emergencyContact', models.CharField(blank=True, max_length=100, null=True)),
                ('emerContactPhone', models.CharField(blank=True, max_length=10, null=True)),
                ('emerContactRelation', models.CharField(blank=True, max_length=20, null=True)),
                ('isDriver', models.BooleanField(default=False)),
                ('isDispatcher', models.BooleanField(default=False)),
                ('isManager', models.BooleanField(default=False)),
                ('termDate', models.DateField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
