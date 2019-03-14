# Generated by Django 2.0.6 on 2019-03-06 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_Nac', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pais', models.CharField(max_length=200)),
                ('Estado', models.CharField(max_length=200)),
                ('colonia', models.CharField(max_length=200)),
                ('delegacion', models.CharField(max_length=200)),
                ('calle', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=200)),
                ('Descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FormaPago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruta', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_modelo', models.CharField(max_length=200)),
                ('stock', models.IntegerField()),
                ('precio', models.FloatField()),
                ('descripcion', models.TextField()),
                ('color', models.ManyToManyField(to='store.Color')),
                ('foto', models.ManyToManyField(to='store.Foto')),
            ],
        ),
        migrations.CreateModel(
            name='Talla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fechaa_compra', models.DateTimeField()),
                ('total', models.FloatField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Cliente')),
                ('formaPago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.FormaPago')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='talla',
            field=models.ManyToManyField(to='store.Talla'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='direccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Direccion'),
        ),
    ]