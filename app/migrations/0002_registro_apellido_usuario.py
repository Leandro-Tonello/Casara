# Generated by Django 4.2.1 on 2023-06-19 15:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="registro",
            name="apellido_usuario",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]