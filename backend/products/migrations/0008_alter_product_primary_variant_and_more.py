# Generated by Django 4.2 on 2023-10-16 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_rename_color_productvariation_productcolor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='primary_variant',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productvariation'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product_variation_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='products.productvariation'),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_variations', to='products.product'),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='cover_image',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productimage'),
        ),
    ]