# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='fqdn',
            field=models.CharField(null=True, blank=True, help_text='FQDN', max_length=255),
            preserve_default=True,
        ),
    ]
