# Generated by Django 5.1.7 on 2025-03-28 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date', models.DateTimeField()),
                ('signature', models.CharField(max_length=200)),
            ],
        ),
    ]
