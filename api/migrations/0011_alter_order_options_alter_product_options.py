# Generated by Django 4.1 on 2022-08-25 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_order_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id']},
        ),
    ]
