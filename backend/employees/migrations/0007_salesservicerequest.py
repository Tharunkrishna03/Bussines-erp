from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0006_openingstock_item_created_at_openingstockrow"),
    ]

    operations = [
        migrations.CreateModel(
            name="SalesServiceRequest",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("referenceNo", models.CharField(max_length=20, unique=True)),
                ("requestDate", models.DateField()),
                ("requiredDeliveryDate", models.DateField()),
                ("clientName", models.CharField(max_length=120)),
                ("companyName", models.CharField(max_length=160)),
                ("phoneNo", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("itemName", models.CharField(max_length=160)),
                ("quantity", models.PositiveIntegerField()),
                ("unit", models.CharField(max_length=40)),
                ("paymentTerms", models.CharField(max_length=80)),
                ("taxPreference", models.CharField(max_length=80)),
                ("deliveryLocation", models.CharField(max_length=200)),
                ("deliveryMode", models.CharField(max_length=80)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
