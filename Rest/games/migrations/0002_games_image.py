# Generated by Django 3.2.7 on 2021-10-05 18:48

from django.db import migrations, models
import games.models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=games.models.upload_image),
        ),
    ]
