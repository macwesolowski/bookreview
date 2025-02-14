from django.db import migrations


def create_categories(apps, schema_editor):
    Kategoria = apps.get_model('main', 'Kategoria')
    GENRES = [
        ('biografia', 'Biografia'),
        ('biznes', 'Biznes'),
        ('dzieci', 'Dzieci'),
        ('fantastyka', 'Fantastyka'),
        ('historia', 'Historia'),
        ('informatyka', 'Informatyka'),
        ('komiks', 'Komiks'),
        ('kryminał', 'Kryminał'),
        ('kuchnia i diety', 'Kuchnia i diety'),
        ('literatura faktu', 'Literatura faktu'),
        ('literatura obyczajowa', 'Literatura obyczajowa'),
        ('literatura piękna obca', 'Literatura piękna obca'),
        ('literatura piękna polska', 'Literatura piękna polska'),
        ('nauka języków', 'Nauka języków'),
        ('nauki ścisłe, medycyna', 'Nauki ścisłe, medycyna'),
        ('poezja', 'Poezja'),
        ('poradniki', 'Poradniki'),
        ('prawo', 'Prawo'),
        ('religie i wyznania', 'Religie i wyznania'),
        ('rozwój osobisty', 'Rozwój osobisty'),
        ('sensacja', 'Sensacja'),
        ('sport i wypoczynek', 'Sport i wypoczynek'),
        ('sztuka', 'Sztuka'),
        ('thriller', 'Thriller'),
        ('turystyka i podróże', 'Turystyka i podróże'),
        ('zdrowie', 'Zdrowie'),
    ]
    for genre in GENRES:
        Kategoria.objects.get_or_create(nazwa=genre[1])


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_categories),
    ]
