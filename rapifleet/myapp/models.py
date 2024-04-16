from django.db import models
from django_countries.fields import CountryField

class Person(models.Model):
    name =  models.TextField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.TextField(max_length=8, unique=True)
    idPhoto = models.FileField()

class Driver(Person):
    # TODO: Crear el directoriio para almacenar los archivos
    idDriver = models.TextField(primary_key=True, unique=True, blank=False, null=False)
    penalRecord = models.FileField()
    policeRecord = models.FileField()
    driverlicencePhoto = models.FileField()
    vehicle = models.ForeignKey('Vehicle', models.SET_NULL, null=True)
    
    
class Address(models.Model):
    id = models.AutoField(primary_key=True)
    country = CountryField()
    stateChoices = (
        ('Atlántida', 'Atlántida'),
        ('Choluteca', 'Choluteca'),
        ('Colón', 'Colón'),
        ('Comayagua', 'Comayagua'),
        ('Copán', 'Copán'),
        ('Cortés', 'Cortés'),
        ('El Paraíso', 'El Paraíso'),
        ('Francisco Morazán', 'Francisco Morazán'),
        ('Gracias a Dios', 'Gracias a Dios'),
        ('Intibucá', 'Intibucá'),
        ('Islas de la Bahía', 'Islas de la Bahía'),
        ('La Paz', 'La Paz'),
        ('Lempira', 'Lempira'),
        ('Ocotepeque', 'Ocotepeque'),
        ('Olancho', 'Olancho'),
        ('Santa Bárbara', 'Santa Bárbara'),
        ('Valle', 'Valle'),
        ('Yoro', 'Yoro')
    )
    state = models.CharField(choices=stateChoices, max_length=255)
    street = models.TextField()
    houseNumber = models.IntegerField()
    driverId = models.ForeignKey('Driver', on_delete=models.CASCADE)
    creationDate = models.DateTimeField(auto_now_add=True)

class Vehicle(models.Model):
    plate = models.TextField(max_length=7, blank=False, null=False, primary_key=True)
    year = models.DateField(blank=False, null=False)
    brand = models.TextField()
    colorType = (
        ('Blanco', 'Blanco'),
        ('Negro', 'Negro'),
        ('Gris', 'Gris'),
        ('Plateado', 'Plateado'),
        ('Azul', 'Azul'),
        ('Rojo', 'Rojo'),
        ('Blanco perlado', 'Blanco perlado'),
        ('Negro metálico', 'Negro metálico'),
        ('Gris oscuro', 'Gris oscuro'),
        ('Plateado metálico', 'Plateado metálico'),
        ('Azul oscuro', 'Azul oscuro'),
        ('Rojo metálico', 'Rojo metálico'),
        ('Blanco sólido', 'Blanco sólido'),
        ('Negro sólido', 'Negro sólido'),
        ('Gris claro', 'Gris claro'),
        ('Plateado brillante', 'Plateado brillante'),
        ('Azul claro', 'Azul claro'),
        ('Rojo brillante', 'Rojo brillante')
    )
    color = models.CharField(choices=colorType, blank=False, null=False, max_length=255)
    vinNumber = models.TextField(max_length=8)
    engineNumber = models.TextField(max_length=17)
    purchaseDate = models.DateField()
    purchaseKilometer = models.IntegerField()
    owner = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True, related_name='vehicles')


class DeliveryDocument(models.Model):
    vehicle = models.ForeignKey('Vehicle', null=True, blank=False, on_delete=models.SET_NULL)
    driver = models.ForeignKey('Driver', null=True, blank=False, on_delete=models.SET_NULL)
    deliveryDocument = models.FileField(null=False, blank=False)
    deliveryVideo = models.FileField(null=False, blank=False)
    date = models.DateField(auto_now_add=True)

class EmergencyContact(Person):
    driver_relation = models.ForeignKey('Driver', on_delete=models.CASCADE)

class Replacements(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False,blank=False)
    value = models.IntegerField(null=False,blank=False)
    owner_relation = models.ForeignKey('Person', on_delete=models.CASCADE, blank=False)
    commet = models.TextField(max_length=250)
    state = models.ForeignKey("State", on_delete=models.SET_NULL, null=True)
    
class State(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(max_length=15)

class sfgsd(models.Model):
    pass



