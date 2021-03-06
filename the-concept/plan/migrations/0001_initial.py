# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 18:53
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('concept', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commitment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='name')),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('start', models.DateField()),
                ('end', models.DateField(blank=True, null=True)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concept.Exercise')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommitmentMilestone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='name')),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('date', models.DateField()),
                ('commitment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.Commitment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='name')),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='name')),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='commitmentmilestone',
            name='milestone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.Milestone'),
        ),
        migrations.AddField(
            model_name='commitment',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plan.Plan'),
        ),
    ]
