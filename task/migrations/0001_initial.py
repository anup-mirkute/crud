# Generated by Django 4.1.6 on 2023-03-31 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Anonymous', max_length=20)),
                ('email', models.EmailField(default='anonymous@mail.com', max_length=254)),
                ('address', models.TextField(default='anonymous address', max_length=128)),
            ],
        ),
    ]
