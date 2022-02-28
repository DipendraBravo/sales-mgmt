# Generated by Django 4.0.2 on 2022-02-28 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=30)),
                ('edition', models.CharField(max_length=50)),
                ('unitprice', models.IntegerField()),
                ('in_stock', models.IntegerField()),
                ('image', models.ImageField(upload_to='cover/')),
                ('totalprice', models.IntegerField(blank=True)),
            ],
        ),
    ]
