from django import forms
from .models import person, body_style, make, transmission_type, drive_train, fuel_type, engine, drive, car, model, slide, plans, anuncio, tipo_image, comentario2, tipo_oferta, tipo_propiedad, estado_propiedad, pais, pais_estado, ciudad, car2, contacto, categoria, informacion_blog, anuncio


class anun22Form(forms.ModelForm):

  class Meta:
    model = anuncio
    fields = '__all__'



class blogForm(forms.ModelForm):
  titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  contenido = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
 
  class Meta:
    model = informacion_blog
    fields = '__all__'


class contactoForm(forms.ModelForm):
  
  nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  correo = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
  opciones_consulta = [('', "seleccione"),("0", "Sugerencia"),]
  tipo_consulta = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=opciones_consulta,)
  mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
  class Meta:
    model = contacto
    fields = '__all__'






class userForm(forms.ModelForm):
	class Meta:
		model = person
		fields = [
			'username',
			'email',
			'password',
			# 'phone',
			# 'image',
		]
		labels= {
			'username': 'Username',
			'email': 'Email',
			'password': 'Password',
			# 'phone': 'Phone',
			# 'image': 'Image',
		}

		widget = {
			'user': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'password': forms.TextInput(attrs={'class':'form-control'}),
			'userid': forms.HiddenInput(attrs={'class':'form-control'}),
			# 'phone': forms.TextInput(attrs={'class':'form-control'}),
			# 'image': forms.ImageField(),
		}
    

class contactos23Form(forms.ModelForm):
  class Meta:
    model = comentario2
    fields = ["nombre","email","deler","clasifi","asunto","comentario","fecha","image"]
class anuncioForm(forms.ModelForm):
  model = anuncio
  fields = '__all__'

class newPlanForm(forms.ModelForm):
	class Meta:
		model = plans
		fields = [
			'name',
			'image',
			'number_of_cars',
			'price',
		]
		labels= {
			'name': 'Nombre del plan',
			'image': 'Imagen asociada',
			'number_of_cars': 'Número máximo de carros',
			'price': 'Precio del plan',
		}
		error_messages = {
			'number_of_cars': {
				'unique': "Ya hay otro plan con ese número de carros",
			},
        }
		widget = {
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'image': forms.FileInput(attrs={'class':'form-control file'}),
			'number_of_cars': forms.TextInput(attrs={'class':'form-control'}),
			'price': forms.TextInput(attrs={'class':'form-control'}),
		}
class slideForm(forms.ModelForm):
	class Meta:
		model = slide
		fields = [
			'title_1',
			'title_2',
			'title_3',
			'url_1',
			'url_2',
			'url_3',
			'image',
		]
		labels= {
			'title_1': 'Title 1',
			'title_2': 'Title 2',
			'title_3': 'Title 3',
			'url_1': 'Url 1',
			'url_2': 'Url 2',
			'url_3': 'Url 3',
			'image': 'Image',
		}

		widget = {
			'image': forms.FileInput(attrs={'class':'file'}),
		}
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    
class userCreation(forms.Form):
	username = forms.CharField(
	required=True,
	label='Nombre de usuario*',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'username', 'name':'username',}),
	)
	first_name = forms.CharField(
	required=False,
	label='Nombre',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'fname', 'name':'fname',}),
	)
	last_name = forms.CharField(
	required=False,
	label='Apellido',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'lname', 'name':'lname',}),
	)
	password = forms.CharField(
	required=True,
	label='Contraseña*',
	widget=forms.PasswordInput(render_value = True, attrs={'class':'form-control', 'id':'psw', 'name':'psw',}),
	)
	email = forms.CharField(
	required=True,
	label='Correo*',
	widget=forms.EmailInput(attrs={'class':'form-control', 'id':'email', 'name':'email',}),
	)
	phone = forms.CharField(
	required=False,
	label='Teléfono',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'phone', 'name':'phone',}),
	)
	cell_phone = forms.CharField(required=False,
	label='Teléfono Celular',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'cell_phone', 'name':'cell_phone',}),
	)
	photo = forms.ImageField(required=False,
	label='Foto',
	widget=forms.FileInput(attrs={'class':'form-control', 'id':'photo', 'name':'photo',}),
	)
	address = forms.CharField(required=False,
	label='Dirección',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'address', 'name':'address',}),
	)
	description = forms.CharField(required=False,
	label='Descripción',
	widget=forms.Textarea(attrs={'rows':"4", 'cols':"50", 'class':'form-control', 'id':'cell_phone', 'name':'cell_phone',}),
	)
	facebook = forms.CharField(required=False,
	label='Facebook',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'facebook', 'name':'facebook',}),
	)
	twitter = forms.CharField(required=False,
	label='Twitter',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'twitter', 'name':'twitter',}),
	)
	instagram = forms.CharField(required=False,
	label='Instagram',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'instagram', 'name':'instagram',}),
	)
	youtube = forms.CharField(required=False,
	label='Youtube',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'youtube', 'name':'youtube',}),
	)
	google = forms.CharField(required=False,
	label='Google plus',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'google', 'name':'google',}),
	)
	pinterest = forms.CharField(required=False,
	label='Pinterest',
	widget=forms.TextInput(attrs={'class':'form-control', 'id':'pinterest', 'name':'pinterest',}),
	)

	user_type = forms.ChoiceField(
        required=True,
        label='Tipo de Usuario*',
		widget=forms.Select(attrs={'class':'form-control', 'id':'user_type', 'name':'user_type',}),
        choices=[("Private user", "Private user"), ("Dealer user", "Dealer user")],
    )


class signForm(forms.Form):
	username = forms.CharField(required=True, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(required=True, label='Correo', widget=forms.EmailInput(attrs={'class':'form-control'}))
	password = forms.CharField(required=True, label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
	phone = forms.CharField(required=True, label='Telefono', widget=forms.TextInput(attrs={'class':'form-control'}))

class MySelect(forms.Select):
    def render_option(self, selected_choices, option_value, option_label):
        return u'<option id=' + str(option_value)  + ' style="display:none" class=\' opts _' + (str(option_value)).replace('_', ' ')  + ' ' + ('' if str(option_value) != '' else 'no')  + '\' value=\'' + str(option_value) + '\' >' + str(option_label) + '</option>'

class indexForm(forms.Form):
	makers =estado_propiedad.objects.all()
	paiss =pais.objects.all()
	pais_options = [('', "pais"),]
	pais_options += ((str(element.id), element.nombre) for element in (paiss))
	moneda_aa = [('', "Seleccione la Moneda"),
								  ("$", "Dolar"),
								  ("MXN", "Peso Mexicano"),

								  ("EUR", "Euro"),
								  
								  ("RIC", "RIAL"),]
  

	 

	maker_options = [('', "estado propiedad"),]
	maker_options += ((str(element.id), element.nombre) for element in (makers))
	makefield = forms.ChoiceField(
        required=False,
        label='estado*',
		widget=forms.Select(attrs={'class':'form-control','id':'make', 'name':'make', 'onchange':'changeModels();'}),
        choices=maker_options,
    )
	models_options = [('', "Seleccione marca"),]
	year_options = [('', "Seleccione trim"),]
	trim_options = [('', "Seleccione modelp"),]
	modelfield = forms.ChoiceField(
        required=False,
        label='Model',
		widget=forms.Select(attrs={'class':'dropdown', 'id':'model', 'name':'model', 'onchange':'addInfo();'}),
        choices=models_options,
    )
	trim = forms.ChoiceField(
		required=False,
		label='Trim',
		widget=forms.Select(attrs={'class':'dropdown', 'id':'trim', 'name':'trim', 'onchange':'bringYears();'}),
		choices=trim_options,
	)
	city = forms.ChoiceField(
        required=False,
        label='Ciudad',
		widget=forms.Select(attrs={'class':'form-control', 'id':'city', 'name':'city'}),
        choices=pais_options,
    )
	year = forms.ChoiceField(
		required=False,
		label='Year',
		widget=forms.Select(attrs={'class':'dropdown', 'id':'year', 'name':'year'}),
		choices=moneda_aa,
	)
class anunForm(forms.Form):
	username = forms.CharField(required=True, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(required=True, label='Correo', widget=forms.EmailInput(attrs={'class':'form-control'}))
	password = forms.CharField(required=True, label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
	phone = forms.CharField(required=True, label='Telefono', widget=forms.TextInput(attrs={'class':'form-control'}))

  
class expForm(forms.Form):
	#Taking data from DB
	makers = tipo_oferta.objects.all()
	paiss = pais.objects.all()
	estados = pais_estado.objects.all()
	municipios = ciudad.objects.all()
	estado = estado_propiedad.objects.all()
	
	#Creating tuples
	maker_options = [('', "Marca"),]
	maker_options += ((str(element.id), element.nombre) for element in (makers))
	pais_options = [('', "pais"),]
	pais_options += ((str(element.id), element.nombre) for element in paiss)
 
	estados_options = [('', "estado"),]
	estados_options += ((str(element.id), element.nombre) for element in estados)
	municipios_options = [('', "Municipio"),]
	municipios_options += ((str(element.id), element.nombre) for element in municipios)
	drive_options = [('', "Estado Propiedad"),]
	drive_options += ((str(element.id), element.nombre) for element in estado)
	 
  
  
	models_options = [('', "Seleccione marca"),]
	trim_options = [('', "Seleccione modelo"),]
	trim_options2 = [('', "Seleccione modelo"),]
	year_options = [('', "Seleccione trim"),]

	moneda_aa = [('', "Seleccione la Moneda"),
								  ("$", "Dolar"),
								  ("MXN", "Peso Mexicano"),

								  ("EUR", "Euro"),
								  
								  ("RIC", "RIAL"),]
    



	#year = forms.IntegerField(required=True, label='Year*', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'year', 'type': 'text', 'placeholder': "year", 'aria-describedby': "sizing-addon2"}))
	year = forms.ChoiceField(
		required=True,
		label='propiedad*',
		widget=forms.Select(attrs={'class':'form-control', 'id':'year', 'name':'year'}),
		choices=year_options,
	)

	trim = forms.ChoiceField(
		required=True,
		label='tipo propiedad*',
		widget=forms.Select(attrs={'class':'form-control', 'id':'trim', 'name':'trim', 'onchange':'bringYears();'}),
		choices=trim_options,
	)
  

	makefield = forms.ChoiceField(
        required=True,
        label='tipo oferta*',
		widget=forms.Select(attrs={'class': "form-control", 'id':'make', 'name':'make', 'onchange':'changeModels();'}),
        choices=maker_options,
    )
	modelfield = forms.ChoiceField(
        required=True,
        label='tipo alquiler*',
		widget=forms.Select(attrs={'class':'form-control', 'id':'model', 'name':'model', 'onchange':'addInfo();'}),
        choices=models_options,
    )

  
  
	pais_a = forms.ChoiceField(
        required=True,
        label='Pais',
		widget=forms.Select(attrs={'class':'form-control', 'id':'pais_a', 'name':'pais_a',}),
		choices= pais_options,
    )
	estados_a = forms.ChoiceField(
        required=True,
        label='Estado',
		widget=forms.Select(attrs={'class':'form-control', 'id':'estados_a', 'name':'estados_a',}),
		choices= estados_options
    )
	municipios_a = forms.ChoiceField(
        required=True,
        label='Municipio',
		widget=forms.Select(attrs={'class':'form-control', 'id':'municipios_a', 'name':'municipios_a',}),
		choices= municipios_options
    )

 
  
	titulo_a = forms.CharField(required=True,  label='Titulo de la Propiedad*', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'titulo_a', 'type': 'text', 'placeholder': "titulo", 'aria-describedby': "sizing-addon2"}))
	descripción_a = forms.CharField(required=True, label='descripción*', widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'descripción_a', 'type': 'text', 'placeholder': "describa el anuncio", 'aria-describedby': "sizing-addon2"}))
	moneda_a = forms.ChoiceField(
        required=True,
        label='Seleccione Moneda*',
		widget=forms.Select(attrs={'class':'form-control', 'id':'moneda_a', 'name':'moneda_a',}),
		choices= moneda_aa
    )
	priceaa = forms.IntegerField(required=True, max_value=1000000,  label='Precio de la Propiedad ', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'pricea', 'type': 'text', 'placeholder': "Precio", 'aria-describedby': "sizing-addon2"}))
	estado_a = forms.ChoiceField(
        required=True,
        label='estado propiedad',
		widget=forms.Select(attrs={'class':'form-control', 'id':'estado_a', 'name':'estado_a',}),
		choices= drive_options
    )
	image_a = forms.FileField(required=True, label='imagen de portada', widget=forms.FileInput(attrs={ 'name': "image_a", 'id': "image_a", 'type': 'file', 'class': "dropzone upload-file text-center py-5", 'accept': "image"}))
	photo = forms.FileField(required=True, label='Fotos', widget=forms.FileInput(attrs={ 'name': "img", 'id': "img", 'type': 'file', 'class': "dropzone", 'multiple accept': "image"}))
	lats = forms.IntegerField(required=True, label='Latitud', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'lats', 'type': 'text', 'placeholder': "Latitud", 'aria-describedby': "sizing-addon2"}))
	lons = forms.IntegerField(required=True, label='Longitud', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'lons', 'type': 'text', 'placeholder': "Longitud", 'aria-describedby': "sizing-addon2"}))
	especificaciones_a = forms.CharField(required=True, label='especificaciones de su anuncio*', widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'especificaciones_a', 'type': 'text', 'placeholder': "especifique detalladamente todas las caracteristica de sus anuncio", 'aria-describedby': "sizing-addon2"}))
  
	copts = (
		('Ático', 'Ático'),
		('Cancha de baloncesto', 'Cancha de baloncesto'),
		('Portero', 'Portero'),
		('Patio delantero', 'Patio delantero'),
		('Vista al lago', 'Vista al lago'),
		('Vista al océano', 'Vista al océano'),
		('Espacio privado', 'Espacio privado'),
		('Rociadores', 'Rociadores'),
 		('Bodega', 'Bodega'),
		('Camaras de seguridad', 'Camaras de seguridad'),
  )
# (attrs={'id':'concom', 'name':'Convenience_Comfort',})
	servicioss = forms.MultipleChoiceField(
        required=False,
        label='servicioss',
		widget=forms.CheckboxSelectMultiple(attrs={'id':'servicioss', 'name':'servicioss',}),
		choices = copts
    )
  
  
  
	def is_valid(self):
		valid = super(expForm, self).is_valid()
		if self.fields["modelfield"]:
			if int(self["modelfield"].value()) < 0:
				del self.errors["modelfield"]
				self.add_error('modelfield', 'You have to choose a model')
				valid = False
			else:
				valid = True

		if self.fields["trim"]:
			try:
				if int(self["trim"].value()) < 0:
					del self.errors["trim"]
					self.add_error('trim', 'You have to choose a trim')
					valid = False
			except:
				valid = True


		return valid 
  
  
class expForm2(forms.Form):
	#Taking data from DB
	makers = tipo_oferta.objects.all()
	paiss = pais.objects.all()
	estados = pais_estado.objects.all()
	municipios = ciudad.objects.all()
	estado = estado_propiedad.objects.all()
	
	#Creating tuples
	maker_options = [('', "Marca"),]
	maker_options += ((str(element.id), element.nombre) for element in (makers))
	pais_options = [('', "pais"),]
	pais_options += ((str(element.id), element.nombre) for element in paiss)
 
	estados_options = [('', "estado"),]
	estados_options += ((str(element.id), element.nombre) for element in estados)
	municipios_options = [('', "Municipio"),]
	municipios_options += ((str(element.id), element.nombre) for element in municipios)
	drive_options = [('', "Estado Propiedad"),]
	drive_options += ((str(element.id), element.nombre) for element in estado)
	 
  
  
	models_options = [('', "Seleccione marca"),]
	trim_options = [('', "Seleccione modelo"),]
	trim_options2 = [('', "Seleccione modelo"),]
	year_options = [('', "Seleccione trim"),]

	moneda_aa = [('', "Seleccione la Moneda"),
								  ("$", "Dolar"),
								  ("MXN", "Peso Mexicano"),

								  ("EUR", "Euro"),
								  
								  ("RIC", "RIAL"),]
    



	#year = forms.IntegerField(required=True, label='Year*', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'year', 'type': 'text', 'placeholder': "year", 'aria-describedby': "sizing-addon2"}))
	year = forms.ChoiceField(
		required=True,
		label='propiedad*',
		widget=forms.Select(attrs={'class':'form-control', 'id':'year', 'name':'year'}),
		choices=year_options,
	)

	trim = forms.ChoiceField(
		required=True,
		label='tipo propiedad*',
		widget=forms.Select(attrs={'class':'form-control', 'id':'trim', 'name':'trim', 'onchange':'bringYears();'}),
		choices=trim_options,
	)
  

	makefield = forms.ChoiceField(
        required=True,
        label='tipo oferta*',
		widget=forms.Select(attrs={'class': "form-control", 'id':'make', 'name':'make', 'onchange':'changeModels();'}),
        choices=maker_options,
    )
	modelfield = forms.ChoiceField(
        required=True,
        label='tipo alquiler*',
		widget=forms.Select(attrs={'class':'form-control', 'id':'model', 'name':'model', 'onchange':'addInfo();'}),
        choices=models_options,
    )

  
  
	pais_a = forms.ChoiceField(
        required=True,
        label='Pais',
		widget=forms.Select(attrs={'class':'form-control', 'id':'pais_a', 'name':'pais_a',}),
		choices= pais_options,
    )
	estados_a = forms.ChoiceField(
        required=True,
        label='Estado',
		widget=forms.Select(attrs={'class':'form-control', 'id':'estados_a', 'name':'estados_a',}),
		choices= estados_options
    )
	municipios_a = forms.ChoiceField(
        required=True,
        label='Municipio',
		widget=forms.Select(attrs={'class':'form-control', 'id':'municipios_a', 'name':'municipios_a',}),
		choices= municipios_options
    )

	youtube_a = forms.CharField(required=False,  label='ingrese el link de youtube*', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'youtube_a', 'type': 'text', 'placeholder': "link de youtube", 'aria-describedby': "sizing-addon2"}))
 
  
	titulo_a = forms.CharField(required=True,  label='Titulo de la Propiedad*', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'titulo_a', 'type': 'text', 'placeholder': "titulo", 'aria-describedby': "sizing-addon2"}))
	descripción_a = forms.CharField(required=True, label='descripción*', widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'descripción_a', 'type': 'text', 'placeholder': "describa el anuncio", 'aria-describedby': "sizing-addon2"}))
	moneda_a = forms.ChoiceField(
        required=True,
        label='Seleccione Moneda*',
		widget=forms.Select(attrs={'class':'form-control', 'id':'moneda_a', 'name':'moneda_a',}),
		choices= moneda_aa
    )
	priceaa = forms.IntegerField(required=True, max_value=1000000,  label='Precio de la Propiedad ', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'pricea', 'type': 'text', 'placeholder': "Precio", 'aria-describedby': "sizing-addon2"}))
	estado_a = forms.ChoiceField(
        required=True,
        label='estado propiedad',
		widget=forms.Select(attrs={'class':'form-control', 'id':'estado_a', 'name':'estado_a',}),
		choices= drive_options
    )
	image_a = forms.FileField(required=True, label='imagen de portada', widget=forms.FileInput(attrs={ 'name': "image_a", 'id': "image_a", 'type': 'file', 'class': "dropzone upload-file text-center py-5", 'accept': "image"}))
	photo = forms.FileField(required=True, label='Fotos', widget=forms.FileInput(attrs={ 'name': "img", 'id': "img", 'type': 'file', 'class': "dropzone", 'multiple accept': "image"}))
	lats = forms.IntegerField(required=True, label='Latitud', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'lats', 'type': 'text', 'placeholder': "Latitud", 'aria-describedby': "sizing-addon2"}))
	lons = forms.IntegerField(required=True, label='Longitud', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'lons', 'type': 'text', 'placeholder': "Longitud", 'aria-describedby': "sizing-addon2"}))
	especificaciones_a = forms.CharField(required=True, label='especificaciones de su anuncio*', widget=forms.Textarea(attrs={'class': 'form-control', 'name': 'especificaciones_a', 'type': 'text', 'placeholder': "especifique detalladamente todas las caracteristica de sus anuncio", 'aria-describedby': "sizing-addon2"}))
  
	copts = (
		('Ático', 'Ático'),
		('Cancha de baloncesto', 'Cancha de baloncesto'),
		('Portero', 'Portero'),
		('Patio delantero', 'Patio delantero'),
		('Vista al lago', 'Vista al lago'),
		('Vista al océano', 'Vista al océano'),
		('Espacio privado', 'Espacio privado'),
		('Rociadores', 'Rociadores'),
 		('Bodega', 'Bodega'),
		('Camaras de seguridad', 'Camaras de seguridad'),
  )
# (attrs={'id':'concom', 'name':'Convenience_Comfort',})
	servicioss = forms.MultipleChoiceField(
        required=False,
        label='servicioss',
		widget=forms.CheckboxSelectMultiple(attrs={'id':'servicioss', 'name':'servicioss',}),
		choices = copts
    )
  
  
  
	def is_valid(self):
		valid = super(expForm2, self).is_valid()
		if self.fields["modelfield"]:
			if int(self["modelfield"].value()) < 0:
				del self.errors["modelfield"]
				self.add_error('modelfield', 'You have to choose a model')
				valid = False
			else:
				valid = True

		if self.fields["trim"]:
			try:
				if int(self["trim"].value()) < 0:
					del self.errors["trim"]
					self.add_error('trim', 'You have to choose a trim')
					valid = False
			except:
				valid = True


		return valid 
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  