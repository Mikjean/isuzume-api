# Generated by Django 3.2.9 on 2021-12-02 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appApi', '0010_auto_20211202_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='accepted_insurance',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='appApi.insurance'),
        ),
    ]