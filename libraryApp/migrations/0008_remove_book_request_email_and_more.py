# Generated by Django 5.0.4 on 2024-05-06 03:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0007_remove_book_price_cartitem'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_request',
            name='email',
        ),
        migrations.RemoveField(
            model_name='book_request',
            name='username',
        ),
        migrations.AddField(
            model_name='book_request',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
