# Generated by Django 4.0.2 on 2022-02-06 00:51

from django.db import migrations

def seed(apps, schema_editor):
    Department = apps.get_model('pfp', 'Department')
    Item = apps.get_model('pfp', 'Item')

    Item(department = armory, name = "Shield", description = "Protect yourself like and knight—and look like one, too.", image = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F1c%2Fbe%2F0a%2F1cbe0a54d719b0a4b2f880db45ce7c28.png&f=1&nofb=1", price = 100, quantity = 250, size = "S, M, L, XL").save()


class Migration(migrations.Migration):

    dependencies = [
        ('pfp', '0002_auto_20220206_0036'),
    ]

    operations = [
    ]
