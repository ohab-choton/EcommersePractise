# Generated by Django 5.1.5 on 2025-01-23 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_productattribute_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='brands/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categeries/'),
        ),
    ]
