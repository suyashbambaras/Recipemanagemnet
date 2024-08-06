# Generated by Django 5.0.7 on 2024-08-06 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('recipeid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('prep_time', models.IntegerField(help_text='Preparation time in minutes')),
                ('cook_time', models.IntegerField(help_text='Cooking time in minutes')),
                ('total_time', models.IntegerField(blank=True, help_text='Total time in minutes', null=True)),
                ('image', models.ImageField(upload_to='images')),
                ('category', models.CharField(choices=[('Veg', 'Vegetarian'), ('NonVeg', 'Non-Vegetarian')], default='Veg', max_length=6)),
            ],
        ),
    ]
