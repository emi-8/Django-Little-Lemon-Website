# Generated by Django 4.1.7 on 2023-03-15 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0002_menu_description"),
    ]

    operations = [
        migrations.RenameField(
            model_name="menu",
            old_name="description",
            new_name="menu_item_description",
        ),
    ]
