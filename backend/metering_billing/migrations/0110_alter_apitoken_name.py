# Generated by Django 4.0.5 on 2022-12-11 22:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0109_alter_event_idempotency_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apitoken",
            name="name",
            field=models.CharField(
                default=None,
                help_text="A free-form name for the API key. Need not be unique. 50 characters max.",
                max_length=50,
            ),
        ),
    ]
