# Generated by Django 5.1.4 on 2025-01-18 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AI', '0009_remove_history_title_remove_history_title_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='title_link',
            field=models.URLField(max_length=500, null=True),
        ),
    ]
