# Generated by Django 4.1.1 on 2022-11-25 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ApplyForm",
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
                ("submit_CV", models.FileField(upload_to="Files")),
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=100)),
                ("phone", models.IntegerField()),
                ("current_company", models.CharField(max_length=200)),
                ("linkedin", models.URLField()),
                ("twitter", models.URLField()),
                ("github", models.URLField()),
                ("portfolio", models.URLField()),
                ("cover_letter", models.CharField(max_length=200)),
                (
                    "Gender",
                    models.CharField(
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Other", "Other"),
                        ],
                        default="Male",
                        max_length=20,
                    ),
                ),
                (
                    "race",
                    models.CharField(
                        choices=[
                            (
                                "American Indian or Alaska Native",
                                "American Indian or Alaska Native",
                            ),
                            ("Asian", "Asian"),
                            ("Black or African American", "Black or African American"),
                            ("Hispanic or Latino", "Hispanic or Latino."),
                            (
                                "Native Hawaiian or Other Pacific Islander",
                                "Native Hawaiian or Other Pacific Islander",
                            ),
                            ("White", "White"),
                        ],
                        default="Asian",
                        max_length=200,
                    ),
                ),
                (
                    "veteran_status",
                    models.CharField(
                        choices=[
                            ("veteran", "I a am veteran"),
                            ("~Not a veteran", "I am not a veteran"),
                            ("Declined to self-identity", "Declined to self-identity"),
                        ],
                        default="veteran",
                        max_length=200,
                    ),
                ),
            ],
        ),
    ]
