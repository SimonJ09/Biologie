# Generated by Django 4.2.6 on 2023-10-27 08:46

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MonModel",
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
                ("nom", models.CharField(max_length=100)),
                ("prenom", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                (
                    "sexe",
                    models.CharField(
                        choices=[("M", "Masculin"), ("F", "Féminin")], max_length=1
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("profession", models.CharField(max_length=100)),
                ("pays", models.CharField(max_length=100)),
                (
                    "situation_matrimoniale",
                    models.CharField(
                        choices=[
                            ("C", "Célibataire"),
                            ("M", "Marié(e)"),
                            ("D", "Divorcé(e)"),
                            ("V", "Veuf/Veuve"),
                        ],
                        max_length=1,
                    ),
                ),
                ("contact", models.TextField()),
            ],
        ),
    ]
