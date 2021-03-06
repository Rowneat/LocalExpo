# Generated by Django 2.1.7 on 2019-03-18 01:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Contact',
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=4)),
                ('comment', models.TextField()),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=100)),
                ('Product_type', models.CharField(max_length=50)),
                ('Instock', models.CharField(max_length=4)),
                ('Price', models.CharField(max_length=10)),
                ('Product_desc', models.TextField()),
                ('Created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'Products',
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('repassword', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Contact', models.CharField(max_length=50)),
                ('Location', models.CharField(max_length=50)),
                ('Registration_no', models.CharField(max_length=50)),
                ('CitizenShip_no', models.CharField(max_length=50)),
                ('Bank_acc', models.CharField(max_length=50)),
                ('Mailing_address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'vendor',
            },
        ),
    ]
