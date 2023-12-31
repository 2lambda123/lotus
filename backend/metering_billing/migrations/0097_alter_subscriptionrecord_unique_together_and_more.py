# Generated by Django 4.0.5 on 2022-12-04 20:05

from django.db import migrations, models

import metering_billing.utils.utils


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0096_historicalsubscription_subscription_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="subscriptionrecord",
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name="historicalsubscriptionrecord",
            name="subscription_id",
        ),
        migrations.AddField(
            model_name="historicalsubscriptionrecord",
            name="subscription_record_id",
            field=models.CharField(
                blank=True,
                default=metering_billing.utils.utils.subscription_record_uuid,
                max_length=100,
            ),
        ),
        migrations.AddField(
            model_name="subscriptionrecord",
            name="subscription_record_id",
            field=models.CharField(
                blank=True,
                default=metering_billing.utils.utils.subscription_record_uuid,
                max_length=100,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="subscriptionrecord",
            unique_together={("organization", "subscription_record_id")},
        ),
        migrations.RemoveField(
            model_name="subscriptionrecord",
            name="subscription_id",
        ),
    ]
