# Generated by Django 4.1.7 on 2023-03-06 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0013_stator_indexes"),
    ]

    operations = [
        migrations.AddField(
            model_name="domain",
            name="notes",
            field=models.TextField(blank=True, null=True),
        ),
    ]
