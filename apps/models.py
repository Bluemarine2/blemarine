from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#Clases o Tablas Independientes
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager
from django.core.validators import MaxValueValidator
from django.db import models
import json
# from .forms import MultiSelectFormField

class CustomUserManager(BaseUserManager):
	def _create_user(self, username, email, is_staff=False, is_superuser=False, password=None, is_dealer=False, **extra_fields):
		if not email:
			raise ValueError('Email needed')

		user = self.model(email=self.normalize_email(email),
		username=username,
		is_dealer=is_dealer,
		is_staff=is_staff,
		is_superuser=is_superuser,
		last_login=timezone.now(),
		**extra_fields)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, username, password, email, is_dealer=False, **extra_fields):
		return self._create_user(email=email,
		username=username,
		password=password,
		is_dealer=is_dealer,
		**extra_fields)

	def create_superuser(self, username, password, email, **extra_fields):
		return self._create_user(email=email,
		username=username,
		password=password,
		is_staff=True,
		is_superuser=True,
		**extra_fields)
  
class propiedad(models.Model):
  nombre = models.CharField(max_length=80, unique=True)
  image = models.ImageField(upload_to="propiedad/")
  index = models.IntegerField(default=1)
  def __unicode__(self):
          return self.nombre
  def __str__(self):
          return self.nombre

class tipo_oferta(models.Model):
  nombre = models.CharField(max_length=80, unique=True)
  def __unicode__(self):
          return self.nombre
  def __str__(self):
          return self.nombre
    
class tipo_alquiler(models.Model):
  nombre = models.CharField(max_length=80)
  tipo_oferta =models.ForeignKey('tipo_oferta',on_delete=models.CASCADE,)
  def __unicode__(self):
          return self.nombre
  def __str__(self):
          return self.nombre
    
class tipo_propiedad(models.Model):
  nombre = models.CharField(max_length=80)
  tipo_alquiler =models.ForeignKey('tipo_alquiler',on_delete=models.CASCADE,)
  tipo_ofertas =models.ForeignKey('tipo_oferta',on_delete=models.CASCADE,)
  def __unicode__(self):
          return self.nombre
  def __str__(self):
          return self.nombre
    
class tipo_objeto(models.Model):
  nombre = models.CharField(max_length=80)
  tipo_propiedad = models.ForeignKey('tipo_propiedad',on_delete=models.CASCADE,)
  def __unicode__(self):
          return self.nombre
  def __str__(self):
          return self.nombre
class estado_propiedad(models.Model):
  nombre = models.CharField(max_length=80)
  def __unicode__(self):
         return self.nombre
  def __str__(self):
         return self.nombre
class pais(models.Model):
  nombre = models.CharField(max_length=80)
  def __unicode__(self):
         return self.nombre
  def __str__(self):
         return self.nombre
    
class pais_estado(models.Model):
  nombre = models.CharField(max_length=80)
  pais = models.ForeignKey('pais',on_delete=models.CASCADE,)
  def __unicode__(self):
         return self.nombre
  def __str__(self):
         return self.nombre
class ciudad(models.Model):
  nombre = models.CharField(max_length=80)
  pais_estado = models.ForeignKey('pais_estado',on_delete=models.CASCADE,)
  def __unicode__(self):
         return self.nombre
  def __str__(self):
         return self.nombre    
    

class tipo_image(models.Model):
  image = models.ImageField(upload_to="anuncio/propiedad/")
  ranuncio = models.ForeignKey('anuncio',on_delete=models.CASCADE,)
  def url(self):
           return self.image.url
  def __unicode__(self):
           return self.image.url + " - " + self.ranuncio.dueno.username + "-" + self.ranuncio.titulo
  def __str__(self):
           return self.image.url + " - " + self.ranuncio.dueno.username + "-" + self.ranuncio.titulo
  
class anuncio(models.Model):
	dueno = models.ForeignKey(
        'person',
        on_delete=models.CASCADE,
    )
	tipo_objeto = models.CharField(max_length=80)
	categoria = models.ForeignKey('propiedad', null=True, blank=True)
	tipo_alquiler = models.ForeignKey('tipo_alquiler')
	tipo_propiedad = models.CharField(max_length=80)
	titulo = models.CharField(max_length=80)  
	description = models.TextField()
	estado_propiedad = models.ForeignKey('estado_propiedad')
	especificaciones = models.TextField()
	pais = models.ForeignKey('pais')
	estado_pais = models.ForeignKey('pais_estado')
	ciudad = models.ForeignKey('ciudad')
	lat = models.CharField(max_length=80, default="1")
	lon = models.CharField(max_length=80, default="1") 
	youtube = models.TextField(default="#") 
	servicios = models.CharField(max_length=8000)  
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	moneda = models.CharField(max_length=80)
	precio = models.IntegerField(validators=[MaxValueValidator(1000000)])
	image = models.ImageField(upload_to="anuncio2/anuncio2/")
	published = models.BooleanField(default=True)
	sold = models.BooleanField(default=False)
  
  
  

	def __unicode__(self):
		return self.dueno.username  + ": " + self.tipo_alquiler.nombre + ": " + self.titulo
	def __str__(self):
		return self.dueno.username  + ": " + self.tipo_alquiler.nombre + ": " + self.titulo
  
 
  
class distribuidor(models.Model):
  nombre=models.CharField(max_length=40)
  email=models.EmailField()
  image=models.ImageField(upload_to="dirt/")
  clasificacion=models.CharField(max_length=50)
  categoria=models.CharField(max_length=2)
  tipo=models.CharField(max_length=30)
  telefono=models.CharField(max_length=30)
  ubicacion=models.CharField(max_length=90)
  
class comentario2(models.Model):
  nombre=models.CharField(max_length=40)
  email=models.EmailField()
  deler=models.CharField(max_length=80)
  clasifi=models.CharField(max_length=160)
  asunto=models.CharField(max_length=180)
  comentario=models.CharField(max_length=140)
  fecha=models.DateTimeField()
  image=models.ImageField(upload_to="con/")  
  
class person(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(max_length=80, primary_key=True)
	email = models.EmailField(unique=True)
	first_name = models.CharField(max_length=80, blank = True, null=True)
	last_name = models.CharField(max_length=80, blank = True, null=True)
	username = models.CharField(max_length=80, primary_key=True)
	anonymous = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_dealer = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	image = models.ImageField(upload_to="users/", blank = True, null=True)
	logo = models.ImageField(upload_to="logo/", blank = True, null=True)
	phone = models.CharField(max_length=80, default='0')
	cell_phone = models.CharField(max_length=80, blank = True, null=True)
	objects = CustomUserManager()
	utheme = models.ForeignKey('theme', blank = True, null=True)
	address = models.CharField(max_length=160, blank = True, null=True)
	description = models.CharField(max_length=140, blank = True, null=True)
	facebook = models.CharField(max_length=140, default="#")
	instagram = models.CharField(max_length=140, default="#")
	twitter = models.CharField(max_length=140, default="#")
	pinterest = models.CharField(max_length=140, default="#")
	google = models.CharField(max_length=140, default="#")
	youtube = models.CharField(max_length=140, default="#")
	cars_to_sell = models.IntegerField(default=5)
	REQUIRED_FIELDS = ['email']
	USERNAME_FIELD = 'username'
	def get_short_name(self):
	 	return self.username
	def get_email(self):
		return self.email
	def __unicode__(self):
		return self.username
	def __str__(self):
		return self.username

  
  
class favourite(models.Model):
	user = models.ForeignKey(
        'person',
        on_delete=models.CASCADE,
    )
	car = models.ForeignKey(
        'anuncio',
        on_delete=models.CASCADE,
    )
	def __unicode__(self):
		return self.user.username + " <3 " + self.car.__unicode__()
	def __str__(self):
		return self.user.username + " <3 " + self.car.__str__()

class theme(models.Model):
	name = models.CharField(max_length=15, unique=True)
	image = models.ImageField(upload_to="themes/", blank=True, null=True)
	number_of_cars = models.IntegerField(default=5)
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name
class plans(models.Model):
	name = models.CharField(max_length=15)
	image = models.ImageField(upload_to="plans/")
	number_of_cars = models.IntegerField(unique = True)
	price = models.FloatField()
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name
class Category(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
		return self.name
	def __str__(self):
		return self.name

class blog_entry(models.Model):
	title = models.CharField(max_length=150)
	image = models.ImageField(upload_to="blog/", blank=True, null=True)
	content = models.TextField()
	category = models.ForeignKey(Category)
	published = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.title
	def __str__(self):
		return self.title

class body_style(models.Model):
	description = models.CharField(max_length=80, unique=True)
	image = models.ImageField(upload_to="photos/")
	index = models.IntegerField(default=1)
	def __unicode__(self):
		return self.description
	def __str__(self):
		return self.description

class make(models.Model):
	description = models.CharField(max_length=80, unique=True)
	def __unicode__(self):
		return self.description
	def __str__(self):
		return self.description

class model(models.Model):
	description = models.CharField(max_length=80)
	maker = models.ForeignKey(
        'make',
        on_delete=models.CASCADE,
    )
	def __unicode__(self):
		return self.description
	def __str__(self):
		return self.description

class trim(models.Model):
	description = models.CharField(max_length=80)
	model = models.ForeignKey(
        'model',
        on_delete=models.CASCADE,
    )
	def __unicode__(self):
		return self.description
	def __str__(self):
		return self.description

class trim_year(models.Model):
	year = models.IntegerField()
	trim = models.ForeignKey(
        'trim',
        on_delete=models.CASCADE,
    )
	def __unicode__(self):
		return str(self.year) + "(" + self.trim.description + ")"
	def __str__(self):
		return str(self.year) + "(" + self.trim.description + ")"


class slide(models.Model):
	image = models.ImageField(upload_to="slide/")
	title_1 = models.CharField(max_length=80)
	title_2 = models.CharField(max_length=80)
	title_3 = models.CharField(max_length=80)
	url_1 = models.CharField(max_length=80, default = "#")
	url_2 = models.CharField(max_length=80, default = "#")
	url_3 = models.CharField(max_length=80, default = "#")
	def __unicode__(self):
		return self.title_1 + " " + self.title_2 + " " + self.title_3
	def __str__(self):
		return self.title_1 + " " + self.title_2 + " " + self.title_3

class transmission_type(models.Model):
	description = models.CharField(max_length=80, unique=True)
	def __unicode__(self):
		return self.description
	def __str__(self):
		return self.description

class drive_train(models.Model):
	description = models.CharField(max_length=80, unique=True)
	def __unicode__(self):
		return self.description
	def __str__(self):
		return self.description

class fuel_type(models.Model):
	description = models.CharField(max_length=80, unique=True)
	def __unicode__(self):
		return self.description
	def __str__(self):
		return self.description

class engine(models.Model):
	description = models.CharField(max_length=80, unique=True)
	def __unicode__(self):
		return self.description
	def __str__(self):
		return self.description

class drive(models.Model):
	description = models.CharField(max_length=80, unique=True)
	def __unicode__(self):
		return self.description
	def __str__(self):
		return self.description

class mImage(models.Model):
	image = models.ImageField(upload_to="photos/cars")
	rcar = models.ForeignKey(
        'car',
        on_delete=models.CASCADE,
    )
	def url(self):
		return self.image.url
	def __unicode__(self):
		return self.image.url + " - " + self.rcar.owner.username + " - " + self.rcar.model.description
	def __str__(self):
		return self.image.url + " - " + self.rcar.owner.username + " - " + self.rcar.model.description

class MultiSelectField(models.Field):
    foo = models.CharField(max_length=2000)
    def setfoo(self, x):
        self.foo = json.dumps(x)
    def getfoo(self, x):
        return json.loads(self.foo)

class car(models.Model):
	owner = models.ForeignKey(
        'person',
        on_delete=models.CASCADE,
    )
	year = models.IntegerField()
	body_s = models.ForeignKey('body_style', null=True, blank=True)
	model = models.ForeignKey('model')
	trim = models.CharField(max_length=80)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	transmission = models.ForeignKey('transmission_type')
	transmission_des = models.TextField()
	drive_t = models.ForeignKey('drive_train')
	engine_des = models.CharField(max_length=100, blank=True)
	fuel_t = models.ForeignKey('fuel_type')
	city_MPG = models.CharField(max_length=100, default = "Santo Domingo")
	highway_MPG = models.CharField(max_length=100, blank=True)
	published = models.BooleanField(default=True)
	sold = models.BooleanField(default=False)
	conditions = (
        ('Nuevo', 'Nuevo'),
        ('Usado', 'Usado'),
        ('Certificado', 'Certificado'),
    )
	condition = models.CharField(
		max_length=100,
		choices=conditions
	)
	mileage = models.FloatField()
	lat = models.FloatField(default = 1)
	lon = models.FloatField(default = 1)
	price = models.IntegerField(validators=[MaxValueValidator(1000000)])
	off_price = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(500000)])
	stock_number = models.IntegerField(null=True, blank=True, default = 1, validators=[MaxValueValidator(1000)])
	engine_t = models.ForeignKey('engine')
	drive = models.ForeignKey('drive', null=True, blank=True)
	doors = (
        (2, 'Dos'),
        (3, 'Tres'),
        (4, 'Cuatro'),
		(5, 'Cinco'),
    )
	doors = models.IntegerField(choices=doors, null=True, blank=True)
	colors = (
		("Negro", "Negro"),
		("Azul", "Azul"),
		("Marrón", "Marrón"),
		("Dorado", "Dorado"),
		("Gris", "Gris"),
		("Verde", "Verde"),
		("Blanco oscuro", "Blanco oscuro"),
		("Rojo", "Rojo"),
		("Plateado", "Plateado"),
		("Blanco", "Blanco"),
		("Violeta", "Violeta"),
		("Naranja", "Naranja"),
		("Otro", "Otro"))
	exterior_color = models.CharField(max_length=20, choices=colors, blank=True)
	interior_color = models.CharField(max_length=20, choices=colors, blank=True)
	exterior_color_des = models.CharField(max_length=100, blank=True)
	interior_color_des = models.CharField(max_length=100, blank=True)
	interior_ops = (
        ('Tela', 'Tela'),
        ('Cuero', 'Cuero'),
        ('No aplica', 'No aplica'),
		('Otro', 'Otro'),
    )
	interior_fabric = models.CharField(
		max_length=100,
		choices=interior_ops,
		blank=True
	)
	comfort = models.CharField(max_length=2000, blank=True)
	entertainment = models.CharField(max_length=2000, blank=True)
	luxury = models.CharField(max_length=2000, blank=True)
	miscellaneous = models.CharField(max_length=2000, blank=True)
	def __unicode__(self):
		return self.owner.username  + ": " + self.model.maker.description + ": " + self.model.description
	def __str__(self):
		return self.owner.username  + ": " + self.model.maker.description + ": " + self.model.description
  
  
  
  
  
  
  
class car2(models.Model):
	dueno = models.ForeignKey(
        'person',
        on_delete=models.CASCADE,
    )
	tipo_objeto = models.CharField(max_length=80)
	categoria = models.ForeignKey('propiedad', null=True, blank=True)
	tipo_alquiler = models.ForeignKey('tipo_alquiler')
	tipo_propiedad = models.CharField(max_length=80)
	titulo = models.CharField(max_length=80)  
	description = models.TextField()
	estado_propiedad = models.ForeignKey('estado_propiedad')
	especificaciones = models.TextField()
	pais = models.ForeignKey('pais')
	estado_pais = models.ForeignKey('pais_estado')
	ciudad = models.ForeignKey('ciudad')
	lat = models.CharField(max_length=80, default="1")
	lon = models.CharField(max_length=80, default="1") 
	servicios = models.CharField(max_length=8000)  
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	moneda = models.CharField(max_length=80)
	precio = models.IntegerField(validators=[MaxValueValidator(1000000)])
	image = models.ImageField(upload_to="anuncio2/anuncio2/")
  

	def __unicode__(self):
		return self.dueno.username  + ": " + self.tipo_alquiler.tipo_oferta.nombre + ": " + self.tipo_alquiler.nombre
	def __str__(self):
		return self.dueno.username  + ": " + self.tipo_alquiler.tipo_oferta.nombre + ": " + self.tipo_alquiler.nombre

  
opciones_consulta = [
  [0, "consulta"],
  [1, "reclamo"],
  [2, "sugerencia"],
  [3, "felicitaciones"]
  
]  


class contacto(models.Model):    
    nombre = models.CharField(max_length= 90)
    apellido = models.CharField(max_length = 90)
    correo = models.EmailField(unique=False)
    telefono = models.CharField(max_length= 90)
    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()
    aviso = models.BooleanField()
    
    def __str__(self):
      return self.nombre
class categoria(models.Model):
  nombre = models.CharField(max_length=80)
  def __unicode__(self):
         return self.nombre
  def __str__(self):
         return self.nombre
      

class informacion_blog(models.Model):
	titulo = models.CharField(max_length=150)
	image = models.ImageField(upload_to="infor/", blank=True, null=True)
	contenido = models.TextField()
	categoria = models.ForeignKey(categoria)
	publicado = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.titulo
	def __str__(self):
		return self.titulo
    
  
