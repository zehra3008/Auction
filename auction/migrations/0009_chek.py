# Generated by Django 3.1.5 on 2021-03-20 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0008_watchlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='chek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
