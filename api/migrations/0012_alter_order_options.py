# Generated by Django 4.1 on 2022-08-28 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_order_options_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['date']},
        ),
    ]