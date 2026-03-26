from django.db import migrations, models


def seed_cost_estimation_rates(apps, schema_editor):
    CostEstimationRate = apps.get_model("employees", "CostEstimationRate")

    rows = [
        ("raw_material", "Lithium", "Category", "Chemical", "kg", 1200, 1),
        ("raw_material", "Cobalt", "Category", "Chemical", "kg", 2200, 2),
        ("raw_material", "Nickel", "Category", "Chemical", "kg", 950, 3),
        ("raw_material", "Graphite", "Category", "Anode", "kg", 320, 4),
        ("raw_material", "Electrolyte", "Category", "Liquid", "L", 150, 5),
        ("raw_material", "Separator", "Category", "Component", "pcs", 22, 6),
        ("raw_material", "Battery Casing", "Category", "Hardware", "pcs", 260, 7),
        ("manufacturing", "Mixing", "Machine Used", "Mixer Machine", "hr", 500, 1),
        ("manufacturing", "Coating", "Machine Used", "Coating Machine", "hr", 800, 2),
        ("manufacturing", "Drying", "Machine Used", "Oven", "hr", 600, 3),
        ("manufacturing", "Assembly", "Machine Used", "Assembly Line", "hr", 450, 4),
        ("manufacturing", "Testing", "Machine Used", "Testing Unit", "hr", 700, 5),
        ("labor", "Technician", "", "", "hr", 120, 1),
        ("labor", "Supervisor", "", "", "hr", 200, 2),
        ("labor", "Quality Inspector", "", "", "hr", 150, 3),
        ("testing", "Charge/Discharge", "", "", "test", 300, 1),
        ("testing", "Safety Test", "", "", "test", 500, 2),
        ("testing", "Cycle Life Test", "", "", "test", 800, 3),
        ("testing", "Performance Test", "", "", "test", 600, 4),
        ("packaging", "Packaging Material", "", "", "pcs", 50, 1),
        ("packaging", "Labeling", "", "", "pcs", 10, 2),
        ("packaging", "Transportation", "", "", "pcs", 80, 3),
        ("packaging", "Insurance", "", "", "pcs", 50, 4),
        ("overhead", "Electricity", "", "", "month", 50000, 1),
        ("overhead", "Water", "", "", "month", 8000, 2),
        ("overhead", "Factory Rent", "", "", "month", 120000, 3),
        ("overhead", "Maintenance", "", "", "month", 25000, 4),
    ]

    CostEstimationRate.objects.bulk_create(
        [
            CostEstimationRate(
                section=section,
                itemName=item_name,
                secondaryLabel=secondary_label,
                secondaryValue=secondary_value,
                unit=unit,
                rate=rate,
                displayOrder=display_order,
            )
            for section, item_name, secondary_label, secondary_value, unit, rate, display_order in rows
        ]
    )


def unseed_cost_estimation_rates(apps, schema_editor):
    CostEstimationRate = apps.get_model("employees", "CostEstimationRate")
    CostEstimationRate.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0009_salesservicerequest_clientimage_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CostEstimationRate",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("section", models.CharField(choices=[("raw_material", "Raw Material"), ("manufacturing", "Manufacturing Process"), ("labor", "Labor"), ("testing", "Testing"), ("packaging", "Packaging & Logistics"), ("overhead", "Overhead")], max_length=40)),
                ("itemName", models.CharField(max_length=120)),
                ("secondaryLabel", models.CharField(blank=True, default="", max_length=60)),
                ("secondaryValue", models.CharField(blank=True, default="", max_length=120)),
                ("unit", models.CharField(max_length=20)),
                ("rate", models.FloatField()),
                ("displayOrder", models.PositiveIntegerField(default=0)),
            ],
            options={
                "ordering": ("section", "displayOrder", "id"),
            },
        ),
        migrations.RunPython(seed_cost_estimation_rates, unseed_cost_estimation_rates),
    ]
