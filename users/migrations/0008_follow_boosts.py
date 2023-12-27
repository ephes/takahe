# Generated by Django 4.1.4 on 2022-12-29 19:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0007_remove_invite_email_invite_expires_invite_uses"),
    ]

    operations = [
        migrations.AddField(
            model_name="follow",
            name="boosts",
            field=models.BooleanField(
                default=True, help_text="Also follow boosts from this user"
            ),
        ),
    ]
