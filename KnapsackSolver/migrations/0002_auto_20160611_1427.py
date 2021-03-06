# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KnapsackSolver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='UOM',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='classification',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='code',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='common_name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='drought_tolerance',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='genus',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='irrigation',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='latin_name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='light',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='maintainence_cost_after_initial_handing_over',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='maintainence_cost_during_execution',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='material_cost',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='max_height',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='max_life_cycle',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='max_roots',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='max_spread',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='min_height',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='min_life_cycle',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='min_roots',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='min_spread',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='plant_type',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='planting_cost',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='salt_tolerance',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='serial_number',
            field=models.CharField(blank=True, max_length=5, unique=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='soil_ph',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='plant',
            name='species',
            field=models.TextField(blank=True),
        ),
    ]
