# Generated by Django 4.2.10 on 2024-02-28 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_delete_venue_alter_article_venues'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]