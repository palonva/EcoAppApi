# Generated by Django 3.0.6 on 2020-05-22 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cor', '0008_auto_20200522_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='image',
            field=models.ImageField(upload_to='Components/Images'),
        ),
    ]