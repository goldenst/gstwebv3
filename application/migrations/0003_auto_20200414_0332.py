# Generated by Django 2.2 on 2020-04-14 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20200414_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='collageGraduate',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='collagedegree',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='contactEmployer',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='graduated',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='highSchoolDegree',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='previousEmployerContact1',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='previousEmployerContact2',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='previousEmployerEnd1',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='previousEmployerEnd2',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='previousEmployerStart1',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='previousEmployerStart2',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='tradeSchoolDegree',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='tradeSchoolGraduate',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10, null=True),
        ),
    ]
