# Generated by Django 4.0.5 on 2023-01-15 08:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "metering_billing",
            "0159_rename_batch_rounding_type_pricetier_batch_rounding_type_old_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="pricetier",
            name="batch_rounding_type",
            field=models.PositiveSmallIntegerField(
                blank=True,
                choices=[
                    (1, "Round Up"),
                    (2, "Round Down"),
                    (3, "Round Nearest"),
                    (4, "No Rounding"),
                ],
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="pricetier",
            name="type",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "Flat"), (2, "Per Unit"), (3, "Free")], default=1
            ),
            preserve_default=False,
        ),
    ]
