# Generated by Django 3.0.3 on 2020-03-09 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='demonio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('partecuerpo', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(max_length=100)),
            ],
        ),
    ]
