# Generated by Django 3.2 on 2021-04-13 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=70)),
                ('Course_Number', models.DecimalField(decimal_places=3, default=0.0, max_digits=5000)),
                ('Instructor_Name', models.TextField(blank=True, default='', max_length=400)),
                ('Duration', models.DurationField()),
            ],
        ),
    ]
