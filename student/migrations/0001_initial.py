# Generated by Django 4.1.5 on 2023-04-18 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('physics_marks', models.IntegerField()),
                ('chemistry_marks', models.IntegerField()),
                ('maths_marks', models.IntegerField()),
                ('computer_science_marks', models.IntegerField()),
            ],
        ),
    ]
