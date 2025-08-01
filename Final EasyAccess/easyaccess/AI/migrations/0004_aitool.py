# Generated by Django 5.1.4 on 2025-01-12 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AI', '0003_documentation_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='AITool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='AITOol-images/')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('link', models.URLField()),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
    ]
