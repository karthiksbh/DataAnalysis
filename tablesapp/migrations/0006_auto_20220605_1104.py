# Generated by Django 3.2.8 on 2022-06-05 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tablesapp', '0005_rename_brazilain_male_modelvalues_brazilian_male'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelvalues',
            old_name='brazilian_female',
            new_name='brazillian_female',
        ),
        migrations.RenameField(
            model_name='modelvalues',
            old_name='brazilian_male',
            new_name='brazillian_male',
        ),
    ]
