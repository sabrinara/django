# Generated by Django 4.2.7 on 2024-01-07 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musicians', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicians.musician')),
            ],
        ),
    ]
