# Generated by Django 2.2.12 on 2021-12-14 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_logo', models.ImageField(upload_to='images')),
            ],
        ),
    ]