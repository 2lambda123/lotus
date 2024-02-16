# Generated by Django 4.0.5 on 2023-03-20 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "metering_billing",
            "0233_historicalinvoice_external_payment_obj_status_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalsubscriptionrecord",
            name="stripe_subscription_id",
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name="subscriptionrecord",
            name="stripe_subscription_id",
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="subscriptionrecord",
            name="billing_plan",
            field=models.ForeignKey(
                help_text="The plan associated with this subscription.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subscription_records",
                related_query_name="subscription_record",
                to="metering_billing.planversion",
            ),
        ),
        migrations.AddConstraint(
            model_name="subscriptionrecord",
            constraint=models.CheckConstraint(
                check=models.Q(("quantity__gt", 0)), name="quantity_gt_0"
            ),
        ),
        migrations.AddConstraint(
            model_name="subscriptionrecord",
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(
                        ("stripe_subscription_id__isnull", False),
                        ("billing_plan__isnull", True),
                    ),
                    models.Q(
                        ("stripe_subscription_id__isnull", True),
                        ("billing_plan__isnull", False),
                    ),
                    _connector="OR",
                ),
                name="stripe_subscription_id_xor_billing_plan",
            ),
        ),
    ]
