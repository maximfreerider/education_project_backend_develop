# Generated by Django 2.2 on 2019-04-06 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registr', '0003_auto_20190406_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='name_of_package',
            field=models.CharField(blank=True, default=0, max_length=150, null=True),
        ),
    ]
