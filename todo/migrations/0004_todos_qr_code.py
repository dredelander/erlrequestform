# Generated by Django 3.2.7 on 2021-10-20 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todos_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='todos',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qr_codes'),
        ),
    ]