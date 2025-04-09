# Generated by Django 5.2 on 2025-04-09 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_alter_author_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='bio_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='bio_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='bio_uz',
            field=models.TextField(blank=True, null=True),
        ),
    ]
