# Generated by Django 3.1.1 on 2021-04-16 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0005_auto_20210416_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='link',
            field=models.CharField(max_length=200),
        ),
    ]
