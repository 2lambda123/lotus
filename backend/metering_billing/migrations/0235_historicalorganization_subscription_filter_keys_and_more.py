# Generated by Django 4.0.5 on 2023-03-21 04:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "metering_billing",
            "0234_historicalsubscriptionrecord_stripe_subscription_id_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalorganization",
            name="subscription_filter_keys",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.TextField(),
                blank=True,
                default=list,
                help_text="Allowed subscription filter keys",
                size=None,
            ),
        ),
        migrations.AddField(
            model_name="organization",
            name="subscription_filter_keys",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.TextField(),
                blank=True,
                default=list,
                help_text="Allowed subscription filter keys",
                size=None,
            ),
        ),
    ]
