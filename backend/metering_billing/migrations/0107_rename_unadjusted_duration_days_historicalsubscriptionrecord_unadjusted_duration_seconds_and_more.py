# Generated by Django 4.0.5 on 2022-12-09 06:49

from django.db import migrations, models


def delete_dups(apps, schema_editor):
    Customer = apps.get_model("metering_billing", "Customer")
    for row in Customer.objects.all().order_by("pk"):
        org = row.organization
        email = row.email
        pk = row.pk
        others = Customer.objects.filter(organizaiton=org, email=email).exclude(pk=pk)
        others.delete()


class Migration(migrations.Migration):
    dependencies = [
        (
            "metering_billing",
            "0106_historicalorganization_webhooks_provisioned_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="historicalsubscriptionrecord",
            old_name="unadjusted_duration_days",
            new_name="unadjusted_duration_seconds",
        ),
        migrations.RenameField(
            model_name="subscriptionrecord",
            old_name="unadjusted_duration_days",
            new_name="unadjusted_duration_seconds",
        ),
        migrations.AddField(
            model_name="historicalsubscriptionrecord",
            name="usage_start_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="subscriptionrecord",
            name="usage_start_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
