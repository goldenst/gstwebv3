# Generated by Django 2.2 on 2020-04-14 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('middleName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('address2', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
                ('position', models.CharField(choices=[('driver', 'Driver'), ('service', 'Service'), ('dispatcher', 'Dispatcher')], default='driver', max_length=100)),
                ('hours', models.CharField(choices=[('full', 'Full Time'), ('part', 'Part Time'), ('temp', 'Temp Work')], default='full', max_length=100)),
                ('avalibility', models.CharField(max_length=100)),
                ('start', models.BooleanField(default=False)),
                ('reliableTransportation', models.BooleanField(default=False)),
                ('over18', models.BooleanField(default=False)),
                ('drivingPosition', models.BooleanField(default=False)),
                ('leaglyAbleToWork', models.BooleanField(default=False)),
                ('essentialfuncrtons', models.BooleanField(default=False)),
                ('currentltEmployed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10)),
                ('contactEmployer', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10)),
                ('highSchool', models.CharField(blank=True, max_length=100, null=True)),
                ('highSchoolCity', models.CharField(blank=True, max_length=100, null=True)),
                ('graduated', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10)),
                ('highYearsattend', models.CharField(blank=True, max_length=100, null=True)),
                ('highSchoolDegree', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10)),
                ('collage', models.CharField(blank=True, max_length=100, null=True)),
                ('collageCity', models.CharField(blank=True, max_length=100, null=True)),
                ('collageGraduate', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10)),
                ('collageYearsAttend', models.CharField(blank=True, max_length=100, null=True)),
                ('collagedegree', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10)),
                ('tradeSchool', models.CharField(blank=True, max_length=100, null=True)),
                ('tradeSchoolCity', models.CharField(blank=True, max_length=100, null=True)),
                ('tradeSchoolGraduate', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10)),
                ('tradeSchoolYearsAttend', models.CharField(blank=True, max_length=100, null=True)),
                ('tradeSchoolDegree', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10)),
                ('previousEmployer1', models.CharField(blank=True, max_length=100, null=True)),
                ('typeofbuisness1', models.CharField(blank=True, max_length=100, null=True)),
                ('prevEmplouerAddress1', models.CharField(blank=True, max_length=100, null=True)),
                ('previousEmployerPhone1', models.CharField(blank=True, max_length=100, null=True)),
                ('previousEmployerSupervisor1', models.CharField(blank=True, max_length=100, null=True)),
                ('previousEmployerRateofpay1', models.CharField(blank=True, max_length=100, null=True)),
                ('previousEmployerDuties1', models.CharField(blank=True, max_length=100, null=True)),
                ('previousEmployerReason1', models.CharField(blank=True, max_length=100, null=True)),
                ('previousEmployerStart1', models.DateField()),
                ('previousEmployerEnd1', models.DateField()),
                ('previousEmployerContact1', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10)),
                ('previousEmployer2', models.CharField(blank=True, max_length=100, null=True)),
                ('typeofbuisness2', models.CharField(blank=True, max_length=100, null=True)),
                ('prevEmplouerAddress2', models.CharField(blank=True, max_length=100, null=True)),
                ('previousEmployerPhone2', models.CharField(blank=True, max_length=100, null=True)),
                ('previousEmployerSupervisor2', models.CharField(blank=True, max_length=100, null=True)),
                ('previousEmployerRateofpay2', models.CharField(blank=True, max_length=100, null=True)),
                ('previousEmployerDuties2', models.CharField(blank=True, max_length=100, null=True)),
                ('previousEmployerReason2', models.CharField(blank=True, max_length=100, null=True)),
                ('previousEmployerStart2', models.DateField()),
                ('previousEmployerEnd2', models.DateField()),
                ('previousEmployerContact2', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10)),
                ('previousEmployer3', models.CharField(blank=True, max_length=100, null=True)),
                ('typeofbuisness3', models.CharField(blank=True, max_length=100, null=True)),
                ('prevEmplouerAddress3', models.CharField(blank=True, max_length=100, null=True)),
                ('previousEmployerPhone3', models.CharField(blank=True, max_length=100, null=True)),
                ('previousEmployerSupervisor3', models.CharField(blank=True, max_length=100, null=True)),
                ('previousEmployerRateofpay3', models.CharField(blank=True, max_length=100, null=True)),
                ('previousEmployerDuties3', models.CharField(blank=True, max_length=100, null=True)),
                ('previousEmployerReason3', models.CharField(blank=True, max_length=100, null=True)),
                ('previousEmployerStart3', models.DateField()),
                ('previousEmployerEnd3', models.DateField()),
                ('previousEmployerContact3', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10)),
            ],
        ),
    ]
