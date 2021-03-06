# Generated by Django 4.0.2 on 2022-03-04 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookmanagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('contact', models.CharField(max_length=20)),
                ('book_quantity', models.IntegerField()),
                ('delivered_status', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookmanagement.book')),
            ],
        ),
    ]
