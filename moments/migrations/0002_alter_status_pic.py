# Generated by Django 3.2.3 on 2021-05-28 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='pic',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]