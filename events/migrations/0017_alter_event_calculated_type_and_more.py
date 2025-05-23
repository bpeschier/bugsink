# Generated by Django 4.2.19 on 2025-02-08 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0016_truncate_exception_type_128"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="calculated_type",
            field=models.CharField(blank=True, default="", max_length=128),
        ),
        migrations.AlterField(
            model_name="event",
            name="calculated_value",
            field=models.TextField(blank=True, default="", max_length=1024),
        ),
    ]
