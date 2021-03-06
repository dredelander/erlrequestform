# Generated by Django 3.2.7 on 2021-10-11 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reqdate', models.DateTimeField(auto_now_add=True)),
                ('qty', models.IntegerField()),
                ('part', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('duedate', models.DateField()),
                ('vendor', models.CharField(max_length=50)),
                ('refnum', models.CharField(max_length=25)),
                ('toapprove', models.BooleanField(default=False)),
                ('tobill', models.BooleanField(default=False)),
                ('datecompleted', models.DateTimeField(blank=True, null=True)),
                ('rush', models.BooleanField(default=False)),
                ('billed', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
