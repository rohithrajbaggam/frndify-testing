# Generated by Django 4.0.2 on 2022-02-08 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page_profile',
            field=models.ImageField(blank=True, default='group.png', upload_to='page_profile'),
        ),
    ]
