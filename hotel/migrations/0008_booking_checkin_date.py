# Generated by Django 2.2 on 2022-04-02 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_auto_20220323_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='checkin_date',
            field=models.DateField(null=True),
        ),
    ]