# Generated by Django 2.1.15 on 2021-04-14 18:29

import core.services
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.UUIDField(db_index=True, default=core.services.CommonService.generate_id, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('duration', models.IntegerField(default=0)),
                ('uploaded_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
