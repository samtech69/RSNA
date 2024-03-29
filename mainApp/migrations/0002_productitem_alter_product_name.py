# Generated by Django 4.2.2 on 2024-01-20 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60, unique=True)),
                ('description', models.TextField()),
                ('pic', models.ImageField(upload_to='uploads/items')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
