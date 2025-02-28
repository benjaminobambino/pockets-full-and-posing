# Generated by Django 4.0.2 on 2022-02-05 23:34

from django.db import migrations

def seed(apps, schema_editor):
    Department = apps.get_model('pfp', 'Department')
    armory = Department(name = 'Armory', image = 'https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.pngmart.com%2Ffiles%2F3%2FMedieval-PNG-Transparent-Image.png&f=1&nofb=1')
    nobility = Department(name = 'Nobility', image = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.clipartqueen.com%2Fimage-files%2F224x376xmedieval-clipart-man-in-clothes-and-hat.png.pagespeed.ic.-JbaGePyZ8.png&f=1&nofb=1')
    peasantry = Department(name = 'Peasantry', image = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F6c%2F98%2Fbc%2F6c98bcd3e2746303f99c2ecd11e9ccf5.png&f=1&nofb=1')
    royalty = Department(name = 'Royalty', image = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2Fab%2Fa5%2Fd0%2Faba5d0a2450a35ade04022759aae740e.png&f=1&nofb=1')
    accessories = Department(name = 'Accessories', image = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.medievalcollectibles.com%2Fwp-content%2Fuploads%2F2019%2F03%2FST4256.png&f=1&nofb=1')
    armory.save()
    nobility.save()
    peasantry.save()
    royalty.save()
    accessories.save()

def fallow(apps, schema_editor):
    Department = apps.get_model('pfp', 'Department')
    Department.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('pfp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed, fallow)
    ]
