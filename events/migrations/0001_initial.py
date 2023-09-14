# Generated by Django 4.2.3 on 2023-07-13 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('qr_code', models.ImageField(blank=True, upload_to='qrcodes/')),
                ('date', models.DateField()),
            ],
        ),
    ]