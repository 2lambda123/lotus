# Generated by Django 4.0.5 on 2022-12-15 18:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0125_merge_20221215_1831"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accountsreceivabletransaction",
            name="related_txns",
            field=models.ManyToManyField(
                to="metering_billing.accountsreceivabletransaction"
            ),
        ),
    ]
