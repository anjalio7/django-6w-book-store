# Generated by Django 3.2.9 on 2022-08-01 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0002_alter_category_category_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subcategory',
            unique_together={('category_id', 'category_name')},
        ),
    ]
