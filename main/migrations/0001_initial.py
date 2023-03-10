# Generated by Django 4.1.5 on 2023-01-21 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Category',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Sarlavha')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='news/photo', verbose_name='Rasm')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Kritilgan vaqti')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti')),
                ('is_published', models.BooleanField(default=True, verbose_name='Nashr etilgan')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Kategoriya')),
            ],
            options={
                'verbose_name': 'New',
                'ordering': ['-created_at'],
            },
        ),
    ]
