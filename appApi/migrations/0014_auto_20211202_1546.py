# Generated by Django 3.2.9 on 2021-12-02 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appApi', '0013_alter_hospital_accepted_insurance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='is_public',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='province',
            field=models.CharField(blank=True, choices=[('North', 'North'), ('East', 'East'), ('West', 'West'), ('South', 'South')], max_length=55, null=True),
        ),
    ]