# Generated by Django 3.2.7 on 2021-10-05 02:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id_game', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('developer', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('realease_date', models.IntegerField()),
                ('create_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
