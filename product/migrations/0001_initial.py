# Generated by Django 5.0.6 on 2024-06-21 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("brand", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("price", models.PositiveIntegerField(default=0)),
                ("image", models.CharField(blank=True, max_length=150, null=True)),
                ("link", models.CharField(blank=True, max_length=150, null=True)),
                ("view", models.PositiveIntegerField(default=0)),
                ("hidden", models.BooleanField(default=False)),
                (
                    "brand",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="brand.brand",
                    ),
                ),
            ],
            options={
                "unique_together": {("name", "brand")},
            },
        ),
    ]
