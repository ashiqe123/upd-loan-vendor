# Generated by Django 3.2.22 on 2024-01-13 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20240108_0535'),
    ]

    operations = [
        migrations.AddField(
            model_name='salarydetails1',
            name='leave_deduction',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
