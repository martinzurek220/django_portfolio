# Generated by Django 4.1.5 on 2023-02-04 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0007_alter_portfolio_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='procenta',
        ),
    ]