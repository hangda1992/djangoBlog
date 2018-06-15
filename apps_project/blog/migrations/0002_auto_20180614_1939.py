# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-14 19:39
from __future__ import unicode_literals

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExampleModel',
        ),
        migrations.DeleteModel(
            name='Tt',
        ),
        migrations.RemoveField(
            model_name='markdownarticle',
            name='field',
        ),
        migrations.AddField(
            model_name='markdownarticle',
            name='article_content',
            field=mdeditor.fields.MDTextField(null=True),
        ),
    ]
