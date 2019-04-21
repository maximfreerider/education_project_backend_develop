

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registr', '0002_auto_20190406_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='name_of_package',
            field=models.CharField(blank=True, default=None, max_length=150, null=True),
        ),
    ]
