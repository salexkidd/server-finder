# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255, help_text='name')),
                ('ip_address', models.GenericIPAddressField(null=True, blank=True, help_text='IP Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
