from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0010_costestimationrate"),
    ]

    operations = [
        migrations.CreateModel(
            name="CostEstimationSheet",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("taxPercentage", models.FloatField(default=0)),
                ("profitMarginPercentage", models.FloatField(default=0)),
                ("rawMaterialTotal", models.FloatField(default=0)),
                ("processTotal", models.FloatField(default=0)),
                ("laborTotal", models.FloatField(default=0)),
                ("testingTotal", models.FloatField(default=0)),
                ("packagingTotal", models.FloatField(default=0)),
                ("overheadTotal", models.FloatField(default=0)),
                ("miscellaneousTotal", models.FloatField(default=0)),
                ("subtotal", models.FloatField(default=0)),
                ("taxAmount", models.FloatField(default=0)),
                ("profitMarginAmount", models.FloatField(default=0)),
                ("finalBatteryCost", models.FloatField(default=0)),
                ("costPerUnit", models.FloatField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "salesServiceRequest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="costEstimationSheets",
                        to="employees.salesservicerequest",
                    ),
                ),
            ],
            options={
                "ordering": ("-created_at", "-id"),
            },
        ),
        migrations.CreateModel(
            name="CostEstimationSheetRow",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "section",
                    models.CharField(
                        choices=[
                            ("raw_material", "Raw Material"),
                            ("manufacturing", "Manufacturing Process"),
                            ("labor", "Labor"),
                            ("testing", "Testing"),
                            ("packaging", "Packaging & Logistics"),
                            ("overhead", "Overhead"),
                            ("miscellaneous", "Miscellaneous"),
                        ],
                        max_length=40,
                    ),
                ),
                ("itemName", models.CharField(max_length=120)),
                ("secondaryLabel", models.CharField(blank=True, default="", max_length=60)),
                ("secondaryValue", models.CharField(blank=True, default="", max_length=120)),
                ("unit", models.CharField(blank=True, default="", max_length=20)),
                ("rate", models.FloatField(default=0)),
                ("quantity", models.FloatField(default=0)),
                ("total", models.FloatField(default=0)),
                ("displayOrder", models.PositiveIntegerField(default=0)),
                (
                    "sheet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rows",
                        to="employees.costestimationsheet",
                    ),
                ),
            ],
            options={
                "ordering": ("section", "displayOrder", "id"),
            },
        ),
    ]
