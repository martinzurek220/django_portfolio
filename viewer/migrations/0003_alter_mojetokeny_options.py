# Generated by Django 4.1.5 on 2023-02-03 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0002_alter_mojetokeny_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mojetokeny',
            options={'ordering': ['-dolarova_hodnota', 'nazev']},
        ),
    ]