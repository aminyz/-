# Generated by Django 4.2.7 on 2024-01-26 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image',
            field=models.ImageField(null=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='food',
            name='price',
            field=models.CharField(max_length=20, null=True),
        ),
    ]