# Generated by Django 2.2.12 on 2021-12-22 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
