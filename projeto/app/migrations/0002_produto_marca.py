# Generated by Django 5.1.1 on 2024-09-26 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='marca',
            field=models.CharField(default='null', max_length=50),
            preserve_default=False,
        ),
    ]
