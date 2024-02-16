# Generated by Django 4.0.5 on 2023-02-05 01:43

from django.db import migrations, models
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        (
            "metering_billing",
            "0176_remove_addonspecification_billing_frequency_one_time_recurring_flat_fee_timing_isnull_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="timezone",
            field=timezone_field.fields.TimeZoneField(default="UTC", use_pytz=True),
        ),
        migrations.AddField(
            model_name="customer",
            name="timezone_set",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="historicalcustomer",
            name="timezone",
            field=timezone_field.fields.TimeZoneField(default="UTC", use_pytz=True),
        ),
        migrations.AddField(
            model_name="historicalcustomer",
            name="timezone_set",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="historicalorganization",
            name="timezone",
            field=timezone_field.fields.TimeZoneField(default="UTC", use_pytz=True),
        ),
        migrations.AddField(
            model_name="organization",
            name="timezone",
            field=timezone_field.fields.TimeZoneField(default="UTC", use_pytz=True),
        ),
    ]
