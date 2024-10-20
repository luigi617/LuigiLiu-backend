# Generated by Django 4.0.3 on 2024-10-19 21:41

import apps.article.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('url_name', models.CharField(blank=True, max_length=255, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to=apps.article.models.pdf_location)),
                ('cover_img', models.ImageField(blank=True, null=True, upload_to=apps.article.models.cover_location)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='articles', to='article.articlecategory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
