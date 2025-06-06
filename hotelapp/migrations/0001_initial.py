# Generated by Django 3.1.5 on 2021-01-07 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('category', models.CharField(choices=[('AC', 'AC'), ('NAC', 'NAC'), ('KING', 'KING'), ('QUEEN', 'QUEEN'), ('DELUX', 'DELUX')], max_length=225)),
                ('beds', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
        ),
    ]
