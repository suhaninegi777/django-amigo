# Generated by Django 5.0.3 on 2024-05-01 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_postdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('sm', 'small'), ('lg', 'large'), ('md', 'Medium'), ('XL', 'Extra Large')], default='sm', max_length=9)),
                ('title', models.TextField()),
                ('rating', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='static/product_img')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.category')),
            ],
        ),
    ]
