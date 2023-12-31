# Generated by Django 4.0.5 on 2023-02-01 00:02

from decimal import Decimal

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0170_historicalsubscriptionrecord_quantity_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="RecurringCharge",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField()),
                (
                    "charge_timing",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "in_advance"), (2, "in_arrears")], default=1
                    ),
                ),
                (
                    "charge_behavior",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "prorate"), (2, "full")], default=1
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=10,
                        default=Decimal("0"),
                        max_digits=20,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="recurringcharge",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recurring_charges",
                to="metering_billing.organization",
            ),
        ),
        migrations.AddField(
            model_name="recurringcharge",
            name="plan_component",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recurring_charges",
                to="metering_billing.plancomponent",
            ),
        ),
        migrations.AddField(
            model_name="recurringcharge",
            name="plan_version",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recurring_charges",
                to="metering_billing.planversion",
            ),
        ),
        migrations.AddField(
            model_name="recurringcharge",
            name="pricing_unit",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="recurring_charges",
                to="metering_billing.pricingunit",
            ),
        ),
        migrations.AddConstraint(
            model_name="recurringcharge",
            constraint=models.UniqueConstraint(
                fields=("organization", "plan_version", "name"),
                name="unique_recurring_charge_name_in_plan_version",
            ),
        ),
    ]
