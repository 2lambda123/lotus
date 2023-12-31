# Generated by Django 4.0.5 on 2022-12-15 05:15

import django.db.models.deletion
from django.db import migrations, models

import metering_billing.utils.utils


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0120_auto_20221215_0411"),
    ]

    operations = [
        migrations.CreateModel(
            name="UsageEvent",
            fields=[
                ("cust_id", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "event_name",
                    models.CharField(
                        help_text="String name of the event, corresponds to definition in metrics",
                        max_length=100,
                    ),
                ),
                (
                    "time_created",
                    models.DateTimeField(
                        help_text="The time that the event occured, represented as a datetime in ISO 8601 in the UTC timezome."
                    ),
                ),
                (
                    "properties",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        help_text="Extra metadata on the event that can be filtered and queried on in the metrics. All key value pairs should have string keys and values can be either strings or numbers. Place subscription filters in this object to specify which subscription the event should be tracked under",
                        null=True,
                    ),
                ),
                (
                    "idempotency_id",
                    models.CharField(
                        default=metering_billing.utils.utils.event_uuid,
                        help_text="A unique identifier for the specific event being passed in. Passing in a unique id allows Lotus to make sure no double counting occurs. We recommend using a UUID4. You can use the same idempotency_id again after 7 days",
                        max_length=255,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "inserted_at",
                    models.DateTimeField(default=metering_billing.utils.utils.now_utc),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="metering_billing.customer",
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="metering_billing.organization",
                    ),
                ),
            ],
            options={
                "db_table": "metering_billing_usageevent",
                "managed": False,
            },
        ),
        migrations.AddIndex(
            model_name="usageevent",
            index=models.Index(
                fields=["organization", "event_name", "customer", "time_created"],
                name="metering_bi_organiz_c0b441_idx",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="usageevent",
            unique_together={("idempotency_id", "time_created")},
        ),
    ]
