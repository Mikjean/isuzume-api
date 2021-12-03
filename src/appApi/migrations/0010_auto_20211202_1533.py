# Generated by Django 3.2.9 on 2021-12-02 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appApi', '0009_auto_20211202_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='district',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='is_public',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='laboratory',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='appApi.laboratory'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='province',
            field=models.CharField(choices=[('North', 'Doctor'), ('East', 'East'), ('West', 'West'), ('South', 'South')], default=None, max_length=55),
        ),
    ]
