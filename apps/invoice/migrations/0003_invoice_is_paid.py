# Generated by Django 3.1.6 on 2021-02-10 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
