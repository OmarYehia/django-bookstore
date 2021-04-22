# Generated by Django 3.2 on 2021-04-22 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210422_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='isbn',
            name='book',
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.isbn'),
        ),
    ]