# Generated by Django 4.2.2 on 2024-01-20 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pic', models.ImageField(upload_to='uploads/gallery')),
            ],
        ),
    ]
