# Generated by Django 5.0.1 on 2024-01-13 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("client_name", models.CharField(max_length=255)),
                ("client_email", models.EmailField(max_length=254)),
                ("client_project_manager", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="ProjectCode",
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
                ("project_code", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Vendor",
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
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="ProjectCreation",
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
                ("project_name", models.CharField(max_length=255)),
                ("project_manager", models.CharField(max_length=255)),
                ("client_project_manager", models.CharField(max_length=255)),
                ("incidence_rate", models.CharField(max_length=50)),
                ("loi", models.CharField(max_length=10)),
                ("scope", models.IntegerField()),
                ("target", models.CharField(max_length=100)),
                ("target_description", models.CharField(max_length=500)),
                ("selected_project_status", models.CharField(max_length=100)),
                ("online", models.CharField(max_length=100)),
                ("selected_div", models.CharField(max_length=100)),
                ("billing_comments", models.CharField(max_length=500)),
                ("security_check", models.BooleanField()),
                (
                    "project_code",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.projectcode",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProjectClient",
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
                ("project_code", models.CharField(max_length=255)),
                ("input_field", models.CharField(max_length=255)),
                ("country", models.CharField(max_length=100)),
                ("country_code", models.CharField(max_length=10)),
                ("scope", models.IntegerField()),
                ("test_link", models.URLField()),
                ("live_link", models.URLField()),
                ("check_country", models.BooleanField()),
                ("check_quota", models.BooleanField()),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.projectcreation",
                    ),
                ),
            ],
            options={
                "unique_together": {("project_code", "country_code")},
            },
        ),
    ]
