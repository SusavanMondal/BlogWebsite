# Generated by Django 4.1.7 on 2023-07-23 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                # ('description1', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='about/')),
            ],
        ),
    ]
