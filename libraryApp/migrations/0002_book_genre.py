# Generated by Django 5.0.1 on 2024-03-05 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(choices=[('Fiction', 'Fiction'), ('Non-Fiction', 'Non-Fiction'), ('Mystery', 'Mystery')], default='Fiction', max_length=20),
        ),
    ]