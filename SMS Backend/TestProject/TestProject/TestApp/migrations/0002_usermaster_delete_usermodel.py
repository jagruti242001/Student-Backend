# Generated by Django 4.2.2 on 2023-10-30 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
                ('created_at', models.DateField()),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='UserModel',
        ),
    ]
