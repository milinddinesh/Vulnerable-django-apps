# Generated by Django 3.2.6 on 2021-10-29 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_document_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='filename',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
