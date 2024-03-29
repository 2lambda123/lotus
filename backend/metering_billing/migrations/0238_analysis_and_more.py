# Generated by Django 4.0.5 on 2023-03-22 04:23

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import metering_billing.utils.utils
import uuid


class Migration(migrations.Migration):

    dependencies = [
        (
            "metering_billing",
            "0237_remove_historicalorganization_subscription_filters_setting_provisioned_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Analysis",
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
                ("analysis_name", models.TextField()),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "time_created",
                    models.DateTimeField(default=metering_billing.utils.utils.now_utc),
                ),
                (
                    "analysis_id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                (
                    "kpis",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.TextField(
                            choices=[
                                ("total_revenue", "Total Revenue"),
                                ("average_revenue", "Average Revenue"),
                                ("new_revenue", "New Revenue"),
                                ("total_cost", "Total Cost"),
                                ("profit", "Profit"),
                                ("churn", "Churn"),
                            ]
                        ),
                        default=list,
                        size=None,
                    ),
                ),
                ("analysis_results", models.JSONField(blank=True, default=dict)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("running", "Running"),
                            ("completed", "Completed"),
                            ("failed", "Failed"),
                        ],
                        default="running",
                        max_length=40,
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="historical_analyses",
                        to="metering_billing.organization",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="historicalbacktestsubstitution",
            name="backtest",
        ),
        migrations.RemoveField(
            model_name="historicalbacktestsubstitution",
            name="history_user",
        ),
        migrations.RemoveField(
            model_name="historicalbacktestsubstitution",
            name="new_plan",
        ),
        migrations.RemoveField(
            model_name="historicalbacktestsubstitution",
            name="organization",
        ),
        migrations.RemoveField(
            model_name="historicalbacktestsubstitution",
            name="original_plan",
        ),
        migrations.RemoveField(
            model_name="historicalorganizationsetting",
            name="history_user",
        ),
        migrations.RemoveField(
            model_name="historicalorganizationsetting",
            name="organization",
        ),
        migrations.DeleteModel(
            name="HistoricalBacktest",
        ),
        migrations.DeleteModel(
            name="HistoricalBacktestSubstitution",
        ),
        migrations.DeleteModel(
            name="HistoricalOrganizationSetting",
        ),
    ]
