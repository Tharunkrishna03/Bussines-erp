from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0007_salesservicerequest"),
    ]

    operations = [
        migrations.AddField(
            model_name="salesservicerequest",
            name="emailReferenceNumber",
            field=models.CharField(blank=True, default="", max_length=100),
        ),
    ]
