# Generated by Django 4.0.5 on 2022-06-26 20:39

import uuid

import django.db.models.deletion
import django_countries.fields
import django_extensions.db.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('package_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Package Name')),
                ('shipping_date', models.DateField(verbose_name='Shipping Date')),
                ('arrival_date', models.DateField(verbose_name='Arrival Date')),
                ('status', models.CharField(choices=[('AD', 'Arrived'), ('PD', 'Pending'), ('OTW', 'On the way'), ('FD', 'Failed')], default='Pending', max_length=100, verbose_name='Status')),
                ('country_of_origin', models.CharField(blank=True, max_length=255, null=True, verbose_name='Country of origin')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipment_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Shipment',
                'ordering': ['-created'],
            },
        ),
    ]
