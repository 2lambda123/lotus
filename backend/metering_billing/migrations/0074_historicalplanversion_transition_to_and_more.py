# Generated by Django 4.0.5 on 2022-11-15 00:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0073_event_cust_id_alter_event_customer_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalplanversion",
            name="transition_to",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="metering_billing.plan",
            ),
        ),
        migrations.AddField(
            model_name="planversion",
            name="transition_to",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="transition_from",
                to="metering_billing.plan",
            ),
        ),
        migrations.AlterField(
            model_name="planversion",
            name="replace_with",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="metering_billing.planversion",
            ),
        ),
    ]
