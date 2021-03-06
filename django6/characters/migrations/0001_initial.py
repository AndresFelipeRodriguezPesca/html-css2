# Generated by Django 3.2.8 on 2021-10-24 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('path', models.FileField(upload_to='media')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'characters',
            },
        ),
    ]
