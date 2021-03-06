# Generated by Django 2.2 on 2022-01-25 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='house',
            old_name='name',
            new_name='property_name',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='name',
            new_name='property_name',
        ),
        migrations.RenameField(
            model_name='swaphouse',
            old_name='name',
            new_name='property_name',
        ),
        migrations.AddField(
            model_name='house',
            name='phone_number',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='house',
            name='town',
            field=models.CharField(default='town', max_length=200),
        ),
        migrations.AddField(
            model_name='property',
            name='town',
            field=models.CharField(default='town', max_length=200),
        ),
        migrations.AddField(
            model_name='swaphouse',
            name='phone_number',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='swaphouse',
            name='town',
            field=models.CharField(default='town', max_length=200),
        ),
        migrations.AlterField(
            model_name='property',
            name='phone_number',
            field=models.CharField(default='0', max_length=30),
        ),
    ]
