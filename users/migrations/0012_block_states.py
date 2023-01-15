# Generated by Django 4.1.4 on 2023-01-15 20:04

import django.utils.timezone
from django.db import migrations, models

import stator.models
import users.models.block


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0011_announcement"),
    ]

    operations = [
        migrations.AddField(
            model_name="block",
            name="include_notifications",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="block",
            name="state",
            field=stator.models.StateField(
                choices=[
                    ("new", "new"),
                    ("sent", "sent"),
                    ("awaiting_expiry", "awaiting_expiry"),
                    ("undone", "undone"),
                    ("undone_sent", "undone_sent"),
                ],
                default="new",
                graph=users.models.block.BlockStates,
                max_length=100,
            ),
        ),
        migrations.AddField(
            model_name="block",
            name="state_attempted",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="block",
            name="state_changed",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="block",
            name="state_locked_until",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="block",
            name="state_ready",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="block",
            name="uri",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterUniqueTogether(
            name="block",
            unique_together={("source", "target", "mute")},
        ),
    ]
