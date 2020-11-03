# Generated by Django 3.1.2 on 2020-10-20 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookId', models.IntegerField(primary_key=True, serialize=False)),
                ('bookTitle', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('releaseDate', models.DateTimeField()),
                ('topSeller', models.BooleanField()),
            ],
        ),
    ]
