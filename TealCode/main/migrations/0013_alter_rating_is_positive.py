# Generated by Django 3.2.9 on 2021-11-22 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_rating_is_positive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='is_positive',
            field=models.BooleanField(),
        ),
    ]