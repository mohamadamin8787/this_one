# Generated by Django 4.2.13 on 2024-06-20 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_category_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='counted_viwe',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
