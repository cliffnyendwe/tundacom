# Generated by Django 2.2 on 2022-03-23 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
