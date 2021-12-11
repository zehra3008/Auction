# Generated by Django 3.1.5 on 2021-03-19 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=62)),
                ('bid', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('Cars', 'Cars'), ('Paintings', 'Paintings'), ('Vintage glassware', 'Vintage glassware'), ('Musical instruments', 'Musical instruments'), ('Collectibles', 'Collectibles'), ('Books', 'Books'), ('Other', 'Other')], max_length=62)),
                ('note', models.CharField(max_length=100, null=True)),
                ('created_on', models.DateTimeField(auto_now=True, null=True)),
                ('product_img', models.ImageField(blank=True, null=True, upload_to='product_img')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserBid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userbid', models.IntegerField(default=0)),
                ('product', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auction.activelist')),
            ],
        ),
    ]
