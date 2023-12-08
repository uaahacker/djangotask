# Generated by Django 4.2.6 on 2023-12-07 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flyerapp', '0014_rename_cart_carte_alter_products_product_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carte',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carts', to='flyerapp.products'),
        ),
        migrations.AlterField(
            model_name='carte',
            name='usr_cos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='carts', to=settings.AUTH_USER_MODEL),
        ),
    ]