# Generated by Django 5.0 on 2024-01-25 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='meetup',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, to='meetups.participants'),
        ),
    ]