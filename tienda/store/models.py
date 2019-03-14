from django.db import models

# Create your models here.

class Talla(models.Model):

    TALLA_CHICA = 'CHI'
    TALLA_MEDIANA = 'MED'
    TALLA_GRANDE = 'GRD'

    TALLA_CHOICES = (
        (TALLA_CHICA, 'CHICA'),
        (TALLA_MEDIANA, 'MEDIANA'),
        (TALLA_GRANDE, 'GRANDE'),
    )

    talla = models.CharField(max_length=3, choices=TALLA_CHOICES )
    cantidad = models.IntegerField()

    def __str__(self):
        return self.talla

class Foto(models.Model):

    TYPE_SLYDER = 'SLD'
    TYPE_PRINCIPAL = 'PRC'

    STATUS_CHOICES = (
        (TYPE_SLYDER, 'SLYDER'),
        (TYPE_PRINCIPAL, 'PRINCIPAL'),
    )

    Type_Image = models.CharField(max_length=3, choices=STATUS_CHOICES, default=TYPE_SLYDER)
    url_image = models.CharField(max_length=200)

    def __str__(self):
        return self.url_image

class Color(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class FormaPago(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Direccion(models.Model):
    Pais = models.CharField(max_length=200)
    Estado = models.CharField(max_length=200)
    colonia = models.CharField(max_length=200)
    delegacion = models.CharField(max_length=200)
    calle = models.CharField(max_length=200)
    numero = models.CharField(max_length=200)
    Descripcion = models.TextField()

    def __str__(self):
        return self.calle


class Producto( models.Model ):
    
    talla = models.ManyToManyField( Talla )
    color =  models.ManyToManyField(Color)
    foto = models.ManyToManyField(Foto)
    nombre_modelo = models.CharField(max_length=200)
    precio = models.FloatField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre_modelo

class Cliente( models.Model ):
    nombre = models.CharField( max_length=200)
    direccion = models.ForeignKey(Direccion, on_delete = models.CASCADE)
    fecha_Nac = models.DateField()
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    cantidad = models.IntegerField()
    formaPago = models.ForeignKey(FormaPago, on_delete = models.CASCADE)
    fechaa_compra = models.DateTimeField()
    total = models.FloatField()

    def Comprar(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.producto

