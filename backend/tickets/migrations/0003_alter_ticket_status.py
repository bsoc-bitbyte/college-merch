# Generated by Django 4.2 on 2023-12-10 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_alter_ticket_buyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('purchased', 'Purchased'), ('failed', 'Purchase Failed'), ('cancelled', 'Cancelled')], max_length=100),
        ),
    ]