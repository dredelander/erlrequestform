# Generated by Django 3.2.7 on 2021-10-18 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todos_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
