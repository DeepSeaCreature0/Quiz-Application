# Generated by Django 5.0.4 on 2024-04-17 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_game', models.CharField(max_length=50)),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
