# Generated by Django 4.0.5 on 2023-01-13 21:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "metering_billing",
            "0148_rename_payment_status_historicalinvoice_payment_status_old_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalinvoice",
            name="payment_status",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "Draft"), (2, "Voided"), (3, "Paid"), (4, "Unpaid")],
                default=4,
            ),
        ),
        migrations.AddField(
            model_name="invoice",
            name="payment_status",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "Draft"), (2, "Voided"), (3, "Paid"), (4, "Unpaid")],
                default=4,
            ),
        ),
    ]
