# Generated by Django 4.1 on 2022-08-20 16:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('time_out', models.DateTimeField(null=True)),
                ('cost', models.FloatField(default=0.0)),
                ('pickup', models.BooleanField(default=False)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='board.category')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('DI', 'Директор'), ('AD', 'Администратор'), ('CO', 'Повар'), ('CA', 'Кассир'), ('CL', 'Уборщик')], default='CA', max_length=2)),
                ('full_name', models.CharField(max_length=255)),
                ('labor_contract', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('time_out', models.DateTimeField(null=True)),
                ('cost', models.FloatField(default=0.0)),
                ('pickup', models.BooleanField(default=False)),
                ('complete', models.BooleanField(default=False)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.product')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.staff')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='board.ProductOrder', to='board.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.staff'),
        ),
    ]