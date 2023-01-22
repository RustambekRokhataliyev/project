# Generated by Django 4.1.3 on 2023-01-04 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='company_name',
            field=models.CharField(default='', max_length=255, verbose_name='Название компании'),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='', max_length=254, verbose_name='Почта'),
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default='', max_length=255, verbose_name='Имя покупателя'),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(default='', max_length=255, verbose_name='Фамилия покупателя'),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(default='', max_length=15, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='address_line_1',
            field=models.TextField(default='', verbose_name='Адрес 1'),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='address_line_2',
            field=models.TextField(default='', verbose_name='Адрес 2'),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='customer',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.customer', verbose_name='Покупатель'),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='order',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.order', verbose_name='Заказ'),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='state',
            field=models.TextField(default='', verbose_name='Штат'),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='town',
            field=models.TextField(default='', verbose_name='Город'),
        ),
    ]
