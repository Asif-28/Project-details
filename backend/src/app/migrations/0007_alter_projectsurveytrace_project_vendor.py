# Generated by Django 5.0.1 on 2024-01-30 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0006_projectvendor_index_key_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projectsurveytrace",
            name="project_vendor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="app.projectvendor"
            ),
        ),
    ]
