# Generated by Django 2.2.2 on 2019-08-31 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_readcomic_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spiderman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.TextField()),
            ],
        ),
    ]
