# Generated by Django 2.2 on 2020-08-23 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stateOfCharge', models.CharField(max_length=100)),
                ('depthOfCharge', models.CharField(max_length=100)),
                ('timeStamp', models.CharField(max_length=100)),
            ],
        ),
    ]