# Generated by Django 4.2.3 on 2023-07-05 13:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("heroes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pcharacter",
            name="id",
            field=models.IntegerField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
    ]
