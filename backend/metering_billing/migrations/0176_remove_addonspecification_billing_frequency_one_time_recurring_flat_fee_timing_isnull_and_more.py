# Generated by Django 4.0.5 on 2023-02-03 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("metering_billing", "0175_merge_20230202_0606"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="addonspecification",
            name="billing_frequency_one_time_recurring_flat_fee_timing_isnull",
        ),
        migrations.RemoveField(
            model_name="addonspecification",
            name="recurring_flat_fee_timing",
        ),
        migrations.AddField(
            model_name="invoicelineitem",
            name="associated_plan_component",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="line_items",
                to="metering_billing.plancomponent",
            ),
        ),
        migrations.AddField(
            model_name="invoicelineitem",
            name="associated_recurring_charge",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="line_items",
                to="metering_billing.recurringcharge",
            ),
        ),
        migrations.AlterField(
            model_name="historicalinvoice",
            name="payment_status",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "draft"), (2, "voided"), (3, "paid"), (4, "unpaid")],
                default=4,
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubscriptionrecord",
            name="flat_fee_behavior",
            field=models.CharField(
                choices=[
                    ("refund", "Refund"),
                    ("charge_prorated", "Prorate"),
                    ("charge_full", "Charge Full"),
                ],
                default=None,
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="payment_status",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "draft"), (2, "voided"), (3, "paid"), (4, "unpaid")],
                default=4,
            ),
        ),
        migrations.AlterField(
            model_name="pricetier",
            name="batch_rounding_type",
            field=models.PositiveSmallIntegerField(
                blank=True,
                choices=[
                    (1, "round_up"),
                    (2, "round_down"),
                    (3, "round_nearest"),
                    (4, "no_rounding"),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="pricetier",
            name="type",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "flat"), (2, "per_unit"), (3, "free")]
            ),
        ),
        migrations.AlterField(
            model_name="subscriptionrecord",
            name="flat_fee_behavior",
            field=models.CharField(
                choices=[
                    ("refund", "Refund"),
                    ("charge_prorated", "Prorate"),
                    ("charge_full", "Charge Full"),
                ],
                default=None,
                max_length=20,
                null=True,
            ),
        ),
    ]
