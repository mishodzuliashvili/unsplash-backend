# Generated by Django 4.2.3 on 2023-07-21 03:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("photoItem", "0002_photoitem_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photoitem",
            name="link",
            field=models.CharField(max_length=500),
        ),
    ]
