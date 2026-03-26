from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0008_salesservicerequest_emailreferencenumber"),
    ]

    operations = [
        migrations.AddField(
            model_name="salesservicerequest",
            name="clientImage",
            field=models.FileField(blank=True, null=True, upload_to="sales-service/"),
        ),
        migrations.AddField(
            model_name="salesservicerequest",
            name="isActive",
            field=models.BooleanField(default=True),
        ),
    ]
