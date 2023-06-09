# Generated by Django 4.1.4 on 2023-02-27 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0009_remove_apply_yourname"),
    ]

    operations = [
        migrations.AlterField(
            model_name="apply",
            name="coverletter",
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name="apply",
            name="cv",
            field=models.FileField(blank=True, null=True, upload_to="service/cv/"),
        ),
        migrations.AlterField(
            model_name="apply",
            name="email",
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name="apply",
            name="link",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="apply",
            name="username",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
