# Generated by Django 3.1.1 on 2021-04-16 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='tema',
            field=models.CharField(choices=[('literatura', 'lilteratura'), ('matematica', 'matematica')], default='Tema libro', max_length=50),
        ),
    ]
