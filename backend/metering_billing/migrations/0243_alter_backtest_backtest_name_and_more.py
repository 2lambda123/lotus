# Generated by Django 4.0.5 on 2023-05-15 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("metering_billing", "0242_plancomponent_bulk_pricing_enabled_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="backtest",
            name="backtest_name",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="customer",
            name="customer_name",
            field=models.TextField(
                blank=True, help_text="The display name of the customer", null=True
            ),
        ),
        migrations.AlterField(
            model_name="historicalcustomer",
            name="customer_name",
            field=models.TextField(
                blank=True, help_text="The display name of the customer", null=True
            ),
        ),
        migrations.AlterField(
            model_name="historicalmetric",
            name="billable_metric_name",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="historicalmetric",
            name="event_name",
            field=models.TextField(
                help_text="Name of the event that this metric is tracking."
            ),
        ),
        migrations.AlterField(
            model_name="historicalmetric",
            name="property_name",
            field=models.TextField(
                blank=True,
                help_text="The name of the property of the event that should be used for this metric. Doesn't apply if the metric is of type 'counter' with an aggregation of count.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalorganization",
            name="organization_name",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="metric",
            name="billable_metric_name",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="metric",
            name="event_name",
            field=models.TextField(
                help_text="Name of the event that this metric is tracking."
            ),
        ),
        migrations.AlterField(
            model_name="metric",
            name="property_name",
            field=models.TextField(
                blank=True,
                help_text="The name of the property of the event that should be used for this metric. Doesn't apply if the metric is of type 'counter' with an aggregation of count.",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="organization_name",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="pricingunit",
            name="name",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="tag",
            name="tag_name",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="team",
            name="name",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="webhookendpoint",
            name="name",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="webhookendpoint",
            name="webhook_url",
            field=models.TextField(),
        ),
    ]
