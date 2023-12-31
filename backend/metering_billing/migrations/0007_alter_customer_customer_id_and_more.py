# Generated by Django 4.0.5 on 2022-09-06 23:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0006_merge_20220906_2201"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="customer_id",
            field=models.CharField(max_length=40),
        ),
        migrations.AlterUniqueTogether(
            name="customer",
            unique_together={("organization", "customer_id")},
        ),
    ]
