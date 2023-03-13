# Generated by Django 3.2.12 on 2023-02-20 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0004_motorcycle_motorcycle_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='MotorcycleReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('review_text', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('motorcycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garage.motorcycle')),
            ],
        ),
    ]
