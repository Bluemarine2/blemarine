from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.db import models
import random
from math import ceil
import json
from .models import person, body_style, make, transmission_type, drive_train, fuel_type, engine, drive, car, model, mImage, theme, favourite, blog_entry, Category, slide, trim, trim_year, plans, comentario2, distribuidor, anuncio, propiedad, tipo_image, tipo_objeto, tipo_propiedad, tipo_oferta, tipo_alquiler, pais, pais_estado, estado_propiedad, ciudad, car2, contacto, informacion_blog, categoria
from .forms import userForm, expForm, indexForm, signForm, slideForm, anuncioForm, contactos23Form, anunForm, newPlanForm, expForm2, contactoForm
from django.contrib.auth import(
    authenticate, login as auth_login,
    logout as auth_logout
)

def logUser(request):
    context = {
    "authenticated": False,
    "username": "",
    "is_admin": False,
    "is_dealer": False,
    "userobj": None,
    }
    if(request.user.is_authenticated()):
        current_user = request.user.get_username() #Este es el nombre de usuario
        auth_user = person.objects.filter(username=current_user)[0]
        context["userobj"] = auth_user
        context["username"] = auth_user.username
        context["is_admin"] = auth_user.is_staff
        context["is_dealer"] = auth_user.is_dealer
        context["authenticated"] = True
    else:
        print("User not authenticated")
    return context


def authUser(request, username, password):
	user = authenticate(username=username, password=password)
	if user is not None and user.is_active:
		print("USER " + user.get_short_name() + " IS LOGGED IN")
		auth_login(request, user)
	return user

def logSign(request, is_dealer):
    form = userForm()
    todo = {"url": "pages/login.html"}
    context = {"auth_error": False}
    context["is_dealer"] = is_dealer
    if request.method == 'POST':
        if request.POST.get('type') == "log":
            username = request.POST.get('form-username')
            password = request.POST.get('form-password')
            user = authUser(request, username, password)
            if user is not None:
                todo["redirect"] = '/' if not user.is_staff else '/admin'
            else:
                context["auth_error"] = True
        else:
            print("SIGN")
            form = userForm(request.POST, request.FILES)
            if form.is_valid():
                sign_up = form.save(commit=False)
                sign_up.password = make_password(form.cleaned_data['password'])
                sign_up.is_dealer = is_dealer
                sign_up.status = 1
                sign_up.save()
                authUser(request, form.cleaned_data['username'], form.cleaned_data['password'])
                todo["redirect"] = '/'
    context["form"] = form
    todo["context"] = context
    return todo


def paginate(obj_per_page, objects, page_number = 1):
    truncated_objs = None
    p_info = []
    try:
        obj_per_page = obj_per_page if obj_per_page != len(objects) and obj_per_page > 0 else 5
        max_pages = ceil(len(objects) / obj_per_page)
        if not(int(page_number) <= max_pages) or page_number < 1:
            page_number = 1
        truncated_objs = objects[((page_number - 1)*obj_per_page) : ((page_number)*obj_per_page)]
        return page_number, int(max_pages), truncated_objs
    except:
        return None

def Index(request):
    posible_results_offered = 10
    ordenation = {
    1: "-created_at",
    2: "created_at",
    3: "-year",
    4: "year",
    5: "-price",
    6: "price",
    }
    page = 1 if request.method != "GET" else request.GET.get("page") if request.GET.get("page") else 1
    obj_per_page = 10 if request.method != "GET" else request.GET.get("result") if request.GET.get("result") else 10
    order = 1 if request.method != "GET" else int(request.GET.get("filter")) if request.GET.get("filter") else 1
    context = logUser(request)
    context["result"] = int(obj_per_page)
    context["comentarios"] = comentario2.objects.all()
    context["anuncio"] = anuncio.objects.all()
    context["Tipo_objeto"] = tipo_objeto.objects.all()
    context["propiedad"] = propiedad.objects.all().order_by('index')
    context["makers"] = make.objects.all()
   # page, max_pages, context["anuncio"]  = paginate(obj_per_page = int(obj_per_page), page_number = int(page),  objects = anuncio.objects.filter(published=True).order_by(ordenation.get(order, "-created_at")) )
  #  context["max_pages_range"]= range(0, max_pages if max_pages else 1)
   # context["max_pages"] = max_pages if max_pages else 1
    #context["current_page"] = int(page) if (int(page) <= max_pages) else 1
    #context["load_result_range"] = range(1, posible_results_offered)
    context["filter"] = order
    context["form"] = indexForm()
    context["slides"] = slide.objects.all()
    context["all_photos"] = {}
    for c in context["anuncio"]:
        cars_p = (tipo_image.objects.filter(ranuncio = c))
        context["all_photos"][c.id] = cars_p

    return render(request,'pages/index.html', context)

def Advance(request):
    posible_results_offered = 10
    ordenation = {
    1: "-created_at",
    2: "created_at",
    3: "-year",
    4: "year",
    5: "-price",
    6: "price",
    }
    page = 1 if request.method != "GET" else request.GET.get("page") if request.GET.get("page") else 1
    obj_per_page = 10 if request.method != "GET" else request.GET.get("result") if request.GET.get("result") else 10
    order = 1 if request.method != "GET" else int(request.GET.get("filter")) if request.GET.get("filter") else 1
    context = logUser(request)
    context["result"] = int(obj_per_page)
    context["body_styles"] = body_style.objects.all().order_by('index')
    context["makers"] = make.objects.all()
    page, max_pages, context["cars"]  = paginate(obj_per_page = int(obj_per_page), page_number = int(page),  objects = anuncio.objects.filter(published=True).order_by(ordenation.get(order, "-created_at")) )
    context["max_pages_range"]= range(0, max_pages if max_pages else 1)
    context["max_pages"] = max_pages if max_pages else 1
    context["current_page"] = int(page) if (int(page) <= max_pages) else 1
    context["load_result_range"] = range(1, posible_results_offered)
    context["filter"] = order
    context["form"] = indexForm()
    context["slides"] = slide.objects.all()
    context["all_photos"] = {}
    for c in context["cars"]:
        cars_p = (mImage.objects.filter(rcar = c))
        context["all_photos"][c.id] = cars_p

    return render(request,'pages/advance.html', context)

def Login(request):
    todo = logSign(request, True) # <- REVISAR
    # if "redirect" in todo:
    return redirect("/")
    # return render(request, todo["url"], todo["context"])

def Search(request):
    if request.method == 'POST':
        if request.POST.get('type') == "simple":
            byear = request.POST.get("byear") if "byear" in request.POST else None
            city = request.POST.get("city") if "city" in request.POST else None
            fyear = request.POST.get("fyear")  if "fyear" in request.POST else None
            bprice = request.POST.get("bprice").replace(',', '')  if "bprice" in request.POST else None
            fprice = request.POST.get("fprice").replace(',', '')  if "fprice" in request.POST else None
            Miles = request.POST.get("Miles")  if "Miles" in request.POST else None
            condition = request.POST.get('condition')  if "condition" in request.POST else None
            make = request.POST.get('makefield')  if "makefield" in request.POST else request.POST.get('nmake') if "nmake" in request.POST else None
            model = request.POST.get('modelfield') if request.POST.get('modelfield') and int(request.POST.get('modelfield')) > 0  else None
            body = request.POST.get('body')  if "body" in request.POST else None
            # trunc_cars = paginate(obj_per_page = obj_per_page, page_number = int(page),  objects = car.objects.all())
            # context["max_pages"], context["cars"] = range(0, trunc_cars[0] if trunc_cars[0] else 1) , trunc_cars[1]
            context = logUser(request)
            context["form"] = indexForm()
            print(condition)
            context["cars"] = carSearch(body_id = body, byear = byear, fyear = fyear, bprice = bprice, fprice = fprice, miles = Miles, condition = condition, make_id = make, model_id = model, city = city)
            context["all_photos"] = {}
            for c in context["cars"]:
                cars_p = (tipo_image.objects.filter(ranuncio = c))
                context["all_photos"][c.id] = cars_p
    else:
        return redirect("/")
    return render(request,'pages/search.html', context)

def Sing_Up(request):
	return render(request,'pages/Sing_Up.html', logUser(request))

def crear_anuncio(request, body=None):
    user = None
    registered = False
    context = logUser(request)
    if request.method == 'POST':
        form = expForm2(request.POST, request.FILES)
        if form.is_valid():
            if not context["authenticated"]:
                user = createAnonymousUser()
                request.session["user"] = user.username
            else:
                registered = True
                # user = context["userobj"]
    return carCreation(request, body, registered=registered, user = user)

def Become(request):
    context = logUser(request)
    context["all_themes"] = theme.objects.all()
    context["plans"] = plans.objects.all()
    return render(request,'pages/become.html', context)

def car_detail(request, id = None, at_dealer = '', more_context = None):
    context = logUser(request)
    print(at_dealer)
    try:
        context['anuncio'] = anuncio.objects.get(id = id)
        context['dueno'] = context['anuncio'].dueno
        context["all_photos"] = (tipo_image.objects.filter(ranuncio = context['anuncio']))
        context['rest_of_anuncio'] = anuncio.objects.filter(~Q(id = context['anuncio'].id), dueno = context['dueno'])
    except:
        id = None
    if id:
        context["rest_of_cars_photos"] = {}
        for c in context["rest_of_anuncio"]:
            img = (tipo_image.objects.filter(ranuncio = c))
            context["rest_of_cars_photos"][c.id] = img[0] if len(img) else None
        try:
            context["features"] = json.loads(context['anuncio'].servicios ) 
            print(context["features"])
        except:
            context["features"] = []
        if more_context is not None:
            context.update(more_context)
    return render(request,('pages/Detail.html' if at_dealer == '' else at_dealer), context) if id is not None else redirect('/')
  
  
  
def categoria(request):
    if request.GET["prd"]:
      #mensaje="carros buscado: %r" %request.GET["prd"]
      producto=request.GET["prd"]
      if len(producto)>20:
        mensaje="caracter muy lleno"
      else:
      
         articulos=anuncio.objects.filter(tipo_objeto__icontains=producto)
      
      return render(request, "pages/categoria.html", {"articulos":articulos, "query":producto })
    else: 
      mensaje="No a introduccido nada" 


def useField(field):
    return False if field is None or field is '' else True

def checkNumberOfCars(user):
    return len(anuncio.objects.filter(dueno = user)) if user is not None else 0

def carCreation(request, body=None, registered = True, user = None):
    context = logUser(request)
    if not context["authenticated"] or (context["authenticated"] and checkNumberOfCars(context["userobj"]) < context["userobj"].cars_to_sell) or user:
        context["body_styles"] = propiedad.objects.all().order_by('index')
        if body is not None and body != '':
            for body_obj in context["body_styles"]:
                if body == body_obj.nombre.replace(" ", "_").replace("/", "_").replace("\'", "_"):
                    body = body_obj
                    break
            else:
                body = None
        form = expForm2()
        if body is not None and body != '':
            if request.method == 'POST':
                form = expForm2(request.POST, request.FILES)
                if form.is_valid():
                    # try:
                    print("YES anuncio creado")
                    _make = request.POST.get('makefield')
                    _model = request.POST.get('modelfield')
                    _trim = request.POST.get('trim')
                    _year = request.POST.get('year')
                    _pais_a = request.POST.get('pais_a')
                    _estados_a = request.POST.get('estados_a')
                    _municipios_a = (request.POST.get('municipios_a'))
                    _titulo_a = request.POST.get('titulo_a')
                    _descripción_a = (request.POST.get('descripción_a'))
                    _moneda_a = (request.POST.get('moneda_a'))
                    _priceaa = request.POST.get('priceaa')
                    _estado_a = request.POST.get('estado_a')
                    _lats = (request.POST.get('lats'))
                    _lons = (request.POST.get('lons'))
                    _especificaciones_a = request.POST.get('especificaciones_a')
                    _servicioss = (request.POST.get('servicioss'))
                    _image_a = request.FILES.getlist("image_a")
                    images = request.FILES.getlist("photo")
                     
                    print('make: ' + str(_make))
                    print('model: ' + str(_model))
                    print('trim: ' + str(_trim))
                    print('year: ' + str(_year))
                    print('pais: ' + str(_pais_a))
                    print('estado_pais: ' + str(_estados_a))
                    print('ciudad: ' + str(_municipios_a))
                    print('titulo: ' + str(_titulo_a))
                    print('description: ' + str(_descripción_a))
                    print('moneda: ' + str(_moneda_a))
                    print('precio: ' + str(_priceaa))
                    print('estado_propiedad: ' + str(_estado_a))
                    print('lat: ' + str(_lats))
                    print('lon: ' + str(_lons))
                    print('especificaciones: ' + str(_especificaciones_a))
                    print(_servicioss)
                    print('image: ' + str(_image_a))
                    print('images: ' + str(images))
                    print(request.FILES)
                    if int(_priceaa) > 1000000:
                        raise ValueError("Price is too big")
                    
                    makerobj = tipo_oferta.objects.get(id=_make)
                    if user:
                        user.save()
                    newCar = anuncio.objects.create(
                    dueno = context["userobj"] if context["authenticated"] else user,
                    categoria = body,
                    tipo_objeto = _year,
                    tipo_propiedad =_trim,
                    tipo_alquiler = tipo_alquiler.objects.get(tipo_oferta=makerobj, id=_model),
                    titulo = _titulo_a,
                    description = _descripción_a,
                    estado_propiedad = estado_propiedad.objects.get(id=_estado_a) if useField(_estado_a) else None,
                    especificaciones = _especificaciones_a,
                    pais = pais.objects.get(id=_pais_a) if useField(_pais_a) else None,
                    estado_pais = pais_estado.objects.get(id=_estados_a) if useField(_estados_a) else None,
                    ciudad = ciudad.objects.get(id=_municipios_a) if useField(_municipios_a) else None,
                    lat = _lats,
                    lon = _lons,
                    image = _image_a,                      
                    servicios = json.dumps(_servicioss),
                    moneda = _moneda_a,
                    precio = _priceaa,
                    )              
                    for file in images:
                        newImage = tipo_image.objects.create(image = file, ranuncio = newCar)                   
                    return redirect("/dashboard") if context["authenticated"] else createUserForCar(request)   
                    print(form.errors.as_json())
                    print("NO se puede crear mas anuncio")
            makers = make.objects.all()
            context["all_models"] = {}
            for maker in makers:
                maker_models = list(model.objects.filter(maker = maker))
                context["all_models"][maker.id] = maker_models
        context["form"] = form
    else:
        context["error"] = "No puedes crear mas anuncio. ¡Actualiza tu plan!"
    return (render(request, ('pages/add_inventory.html' if body is None else 'pages/add_cars.html'), context) if registered else render(request, ('pages/anunciocasa.html' if body is None else 'pages/create_listingF.html'), context) )


def carSearch(user = None, make_id = None, body_id = None, model_id = None, byear = None, fyear = None, bprice = None, fprice = None, miles = None, condition = None, off_price = False, ctrim = None, city = None):
    body_obj = propiedad.objects.get(id = body_id) if body_id is not None else None
    try:
        make_obj = tipo_oferta.objects.get(id=make_id) if make_id is not None else None
        print(make_obj)
        try:
            print(tipo_alquiler.objects.filter(tipo_oferta=make_obj))
            model_obj = tipo_alquiler.objects.filter(maker=make_obj, id=model_id) if model_id and make_obj else tipo_alquiler.objects.filter(tipo_oferta=make_obj) if make_obj else tipo_alquiler.objects.filter(id=model_id) if model_id else None
            print(model_obj)
            first_filtered_cars = anuncio.objects.filter(published=True, model = model_obj, body_s = body_obj) if body_obj is not None and model_obj is not None else anuncio.objects.filter(body = body_obj) if body_obj is not None else (anuncio.objects.filter(model__in = model_obj) if model_obj is not None else anuncio.objects.all())
            print(first_filtered_cars)
        except:
            if make_obj is not None:
                first_filtered_cars = anuncio.objects.filter(model__maker = make_obj)
            else:
                first_filtered_cars = anuncio.objects.filter(body_s = body_obj)
    except:
        first_filtered_cars = anuncio.objects.all()

    if user:
        first_filtered_cars = first_filtered_cars.filter(dueno = user)
    second_filtered_cars = first_filtered_cars

    if fprice and bprice:
        second_filtered_cars = first_filtered_cars.filter(Q(precio__lte = float(fprice)) & Q(precio__gte = float(bprice)))
        
    if condition and condition.lower() != "all":
        second_filtered_cars = second_filtered_cars.filter(Q(categoria = condition))


    if off_price:
        second_filtered_cars = second_filtered_cars.filter(off_price__isnull = False)
    if city:
        second_filtered_cars = second_filtered_cars.filter(pais = city)    
 
    # for _car in first_filtered_cars:
    #     print(str(_car.model.maker) + " " + str(_car.model) + " " + str(_car.owner) + " " +str( _car.price) + " " + str( _car.model.year) + " " + str(_car.mileage) + " " + str(_car.condition))

    # print("filtered data:")
    # for _car in second_filtered_cars:
    #     print(str(_car.model.maker) + " " + str(_car.model) + " " + str(_car.owner) + " " + str( _car.price) + " " + str( _car.model.year) + " " + str(_car.mileage) + " " + str(_car.condition))
    return second_filtered_cars

def logout(request):
    auth_logout(request)
    return redirect('/')

def sell(request):
    return render(request,'pages/sell.html', logUser(request))

def contact_us(request):
    data ={
    'form2': contactoForm()
    }
    
    if request.method == 'POST':
      formulario = contactoForm(data=request.POST)
      if formulario.is_valid():
        formulario.save()
        data["mensaje"] = "Conctato Guardado"
      else:
        data["form2"] = formulario
    
   
    return render(request,'pages/contact_us.html', data)

def Planes_servicios(request):
    return render(request,'pages/Planes_servicios.html', logUser(request))
def login2(request):
    posible_results_offered = 10
    ordenation = {
    1: "-created_at",
    2: "created_at",
    3: "-year",
    4: "year",
    5: "-price",
    6: "price",
    }
    page = 1 if request.method != "GET" else request.GET.get("page") if request.GET.get("page") else 1
    obj_per_page = 10 if request.method != "GET" else request.GET.get("result") if request.GET.get("result") else 10
    order = 1 if request.method != "GET" else int(request.GET.get("filter")) if request.GET.get("filter") else 1
    context = logUser(request)
    context["result"] = int(obj_per_page)
    context["body_styles"] = body_style.objects.all().order_by('index')
    context["makers"] = make.objects.all()
    page, max_pages, context["cars"]  = paginate(obj_per_page = int(obj_per_page), page_number = int(page),  objects = anuncio.objects.filter(published=True).order_by(ordenation.get(order, "-created_at")) )
    context["max_pages_range"]= range(0, max_pages if max_pages else 1)
    context["max_pages"] = max_pages if max_pages else 1
    context["current_page"] = int(page) if (int(page) <= max_pages) else 1
    context["load_result_range"] = range(1, posible_results_offered)
    context["filter"] = order
    context["form"] = indexForm()
    context["slides"] = slide.objects.all()
    context["all_photos"] = {}
    for c in context["cars"]:
        cars_p = (mImage.objects.filter(rcar = c))
        context["all_photos"][c.id] = cars_p

    return render(request,'pages/login2.html', context)

def guia(request):
    return render(request,'pages/guia.html', logUser(request))
  
def icontact_usi(request):
    data ={
    'form2': signForm()
  }
    
    if request.method == 'POST':
      formulario = signForm(data=request.POST)
      if formulario.is_valid():
        formulario.save()
        data["mensaje"] = "Conctato Guardado"
      else:
        data["form2"] = formulario
    
   
    
   
    return render(request,'pages/icontact_usi.html', data)

def pago(request):
    return render(request,'pages/pago.html', logUser(request))
  
def contar1(request):
  if request.method=="POST":
    
      subject=request.POST["name"]
      
      message=request.POST["name2"]
      
      email_from=settings.EMAIL_HOST_USER
      
      recipient_list=["itachijhon456@gmail.com"]
      
      send_mail(subject, message, email_from, recipient_list)
  else:
      mensaje="No a introduccido nada"
  return HttpResponse(mensaje)
    
def busqueda12(request):
    return render(request,'pages/busqueda12.html')
def buscar1(request):
    if request.GET["prd"]:
      #mensaje="carros buscado: %r" %request.GET["prd"]
      producto=request.GET["prd"]
      if len(producto)>20:
        mensaje="caracter muy lleno"
      else:
      
         articulos=distribuidor.objects.filter(nombre__icontains=producto)
      
      return render(request, "pages/resultado.html", {"articulos":articulos, "query":producto })
    else: 
      mensaje="No a introduccido nada" 
    return HttpResponse(mensaje)
def jobs(request):
    return render(request,'pages/jobs.html', logUser(request))

def car_reviews(request):
    context = logUser(request)
    context["informacion_blog"] = informacion_blog.objects.all()

    return render(request, ('pages/car_reviews.html'), context)
  

  
def press_room(request, id = None):
    context = logUser(request)
    goto_article = False
    context["blog_name"] = "Press room"

        
   
    return render(request,('pages/press_room.html' if not goto_article else "pages/post.html"), context)

def post(request):
    return render(request,'pages/post.html', logUser(request))

def create_listing(request, body=None):
    user = None
    registered = False
    context = logUser(request)
    if request.method == 'POST':
        form = expForm(request.POST, request.FILES)
        if form.is_valid():
            if not context["authenticated"]:
                user = createAnonymousUser()
                request.session["user"] = user.username
            else:
                registered = True
                # user = context["userobj"]
    return carCreation(request, body, registered=registered, user = user)


  
  
  
  
  
  
  
def create_listing2(request, body=None):
    user = None
    registered = False
    context = logUser(request)
    if request.method == 'POST':
        form = expForm2(request.POST, request.FILES)
        if form.is_valid():
            if not context["authenticated"]:
                user = createAnonymousUser()
                request.session["user"] = user.username
            else:
                registered = True
                # user = context["userobj"]
    return carCreation2(request, body, registered=registered, user = user)
  
  
def carCreation2(request, body=None, registered = True, user = None):
    context = logUser(request)
    if not context["authenticated"] or (context["authenticated"] and checkNumberOfCars(context["userobj"]) < context["userobj"].cars_to_sell) or user:
        context["body_styles"] = propiedad.objects.all().order_by('index')
        if body is not None and body != '':
            for body_obj in context["body_styles"]:
                if body == body_obj.nombre.replace(" ", "_").replace("/", "_").replace("\'", "_"):
                    body = body_obj
                    break
            else:
                body = None
        form = expForm2()
        if body is not None and body != '':
            if request.method == 'POST':
                form = expForm2(request.POST, request.FILES)
                if form.is_valid():
                    # try:
                    print("YES  anuncio creado")
                    _make = request.POST.get('makefield')
                    _model = request.POST.get('modelfield')
                    _trim = request.POST.get('trim')
                    _year = request.POST.get('year')
                    _pais_a = request.POST.get('pais_a')
                    _estados_a = request.POST.get('estados_a')
                    _municipios_a = (request.POST.get('municipios_a'))
                    _titulo_a = request.POST.get('titulo_a')
                    _descripción_a = (request.POST.get('descripción_a'))
                    _moneda_a = (request.POST.get('moneda_a'))
                    _priceaa = request.POST.get('priceaa')
                    _estado_a = request.POST.get('estado_a')
                    _lats = (request.POST.get('lats'))
                    _lons = (request.POST.get('lons'))
                    _especificaciones_a = request.POST.get('especificaciones_a')
                    _servicioss = (request.POST.get('servicioss'))
                    _image_a = request.FILES.get('image_a')
                    images = request.FILES.getlist("photo")
                    _youtube_a = request.POST.get('youtube_a')
                     
                    print('make: ' + str(_make))
                    print('model: ' + str(_model))
                    print('trim: ' + str(_trim))
                    print('year: ' + str(_year))
                    print('pais: ' + str(_pais_a))
                    print('estado_pais: ' + str(_estados_a))
                    print('ciudad: ' + str(_municipios_a))
                    print('titulo: ' + str(_titulo_a))
                    print('descripción: ' + str(_descripción_a))
                    print('moneda: ' + str(_moneda_a))
                    print('precio: ' + str(_priceaa))
                    print('estado_propiedad: ' + str(_estado_a))
                    print('lat: ' + str(_lats))
                    print('lon: ' + str(_lons))
                    print('especificaciones: ' + str(_especificaciones_a))
                    print(_servicioss)
                    print('image: ' + str(_image_a))
                    print('images: ' + str(images))
                    print('youtube' + str(_youtube_a))
                    print(request.FILES)
                    if int(_priceaa) > 1000000:
                        raise ValueError("Price is too big")
                    
                    makerobj = tipo_oferta.objects.get(id=_make)
                    if user:
                        user.save()
                    newCar = anuncio.objects.create(
                    dueno = context["userobj"] if context["authenticated"] else user,
                    categoria = body,
                    tipo_objeto = _year,
                    tipo_propiedad =_trim,
                    tipo_alquiler = tipo_alquiler.objects.get(tipo_oferta=makerobj, id=_model),
                    titulo = _titulo_a,
                    description = _descripción_a,
                    estado_propiedad = estado_propiedad.objects.get(id=_estado_a) if useField(_estado_a) else None,
                    especificaciones = _especificaciones_a,
                    pais = pais.objects.get(id=_pais_a) if useField(_pais_a) else None,
                    estado_pais = pais_estado.objects.get(id=_estados_a) if useField(_estados_a) else None,
                    ciudad = ciudad.objects.get(id=_municipios_a) if useField(_municipios_a) else None,
                    lat = _lats,
                    lon = _lons,
                    servicios = json.dumps(_servicioss),
                    image =  _image_a,
                    moneda = _moneda_a,
                    precio = _priceaa,
                    youtube = _youtube_a,  
                    published = registered,  
                         
                   
                    )
                    for file in images:
                        newImage = tipo_image.objects.create(image = file, ranuncio = newCar)                                       
                    return redirect("/dashboard") if context["authenticated"] else createUserForCar(request)   
                    print("NO anunio creado")
            makers = tipo_oferta.objects.all()
            context["all_models"] = {}
            for maker in makers:
                maker_models = list(tipo_alquiler.objects.filter(tipo_oferta = maker))
                context["all_models"][tipo_oferta.id] = maker_models
        context["form"] = form
    else:
        context["error"] = "No puedes crear mas anuncio. ¡Actualiza tu plan!"
    return (render(request, ('pages/add_inventory.html' if body is None else 'pages/add_cars.html'), context) if registered else render(request, ('pages/create_listing2.html' if body is None else 'pages/create_listingF2.html'), context) )

  

  
  
  
  
  
  
  
  
  
  
  
def createUserForCar(request):
    form = signForm()
    return render(request, 'pages/login.html', context={'form': form})

def create_normal_user(request):
    print("ENTRA")
    if request.method == "POST":
        form = signForm(request.POST)
        if form.is_valid():
            # userid = form.cleaned_data['userid']
            temporary_user_id = request.session["user"]
            try:
                username = form.cleaned_data['username']
                password = make_password(form.cleaned_data['password'])
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                # temporary_user = person.objects.filter(username = userid)
                the_car = anuncio.objects.get(dueno__username = temporary_user_id)
                print(the_car)
                the_user = person.objects.get(username = temporary_user_id)
                the_user.phone = phone
                the_user.username = username
                the_user.password = password
                the_user.email = email
                the_user.anonymous = False
                the_user.save()
                person.objects.get(username = temporary_user_id).delete()
                the_car.dueno = the_user
                the_car.published = True
                the_car.save()
                authUser(request, form.cleaned_data['username'], form.cleaned_data['password'])
            except Exception as e:
                print(e)
                form = signForm()
                error = "Username or email already in use"
                return render(request, 'pages/login.html', context={'form': form, 'error': error})
    return redirect('/')

def log(request):
    log = logSign(request, False)
    return render(request,log["url"], log["context"])

@login_required
def like(request):
    context = logUser(request)
    if request.method == "GET":
        id = request.GET.get("id")
        try:
            _car = anuncio.objects.get(id = id)
            already_liked = favourite.objects.filter(car = _car, user = context["userobj"])
            if not already_liked:
                favourite.objects.create(
                car = _car,
                user = context["userobj"],
                )
            return HttpResponse(status=201)
        except Exception as e:
            print(e)
    return HttpResponse(status=400)

@login_required
def unlike(request):
    context = logUser(request)
    if request.method == "GET":
        id = request.GET.get("id")
        try:
            _car = anuncio.objects.get(id = id)
            _liked = favourite.objects.get(car = _car, user = context["userobj"])
            _liked.delete()
            return HttpResponse(status=201)
        except Exception as e:
            print(e)
    return HttpResponse(status=400)


def createAnonymousUser():
    username = "user" + str(random.randint(1, 1000000))
    email = username+"@gmail.com"
    return person(username=username, anonymous=True, email = email)

def find_local_dealer(request):
    return render(request,'pages/find_local_dealer.html')

def find_local_search(request):
    context = logUser(request)    
    context["distribuidors"]=distribuidor.objects.all()
    
    

    return render(request,'pages/find_local_search.html', context)
  

def sitemap(request):
    return render(request,'pages/sitemap.html')
  
  
def lista_map(request):
    posible_results_offered = 10
    ordenation = {
    1: "-created_at",
    2: "created_at",
    3: "-year",
    4: "year",
    5: "-price",
    6: "price",
    }
    page = 1 if request.method != "GET" else request.GET.get("page") if request.GET.get("page") else 1
    obj_per_page = 10 if request.method != "GET" else request.GET.get("result") if request.GET.get("result") else 10
    order = 1 if request.method != "GET" else int(request.GET.get("filter")) if request.GET.get("filter") else 1
    context = logUser(request)
    context["result"] = int(obj_per_page)
    context["comentarios"] = comentario2.objects.all()
    context["anuncio"] = anuncio.objects.all()
    context["Tipo_objeto"] = tipo_objeto.objects.all()
    context["propiedad"] = propiedad.objects.all().order_by('index')
    context["makers"] = make.objects.all()
   # page, max_pages, context["anuncio"]  = paginate(obj_per_page = int(obj_per_page), page_number = int(page),  objects = anuncio.objects.filter(published=True).order_by(ordenation.get(order, "-created_at")) )
  #  context["max_pages_range"]= range(0, max_pages if max_pages else 1)
   # context["max_pages"] = max_pages if max_pages else 1
    #context["current_page"] = int(page) if (int(page) <= max_pages) else 1
    #context["load_result_range"] = range(1, posible_results_offered)
    context["filter"] = order
    context["form"] = indexForm()
    context["slides"] = slide.objects.all()
    context["all_photos"] = {}
    for c in context["anuncio"]:
        cars_p = (tipo_image.objects.filter(ranuncio = c))
        context["all_photos"][c.id] = cars_p

    return render(request,'pages/lista_map.html', context)


def terms_conditions(request):
    return render(request,'pages/terms_conditions.html')

def getModels(request):
    if request.method == "GET":
        models = None
        if request.GET.get("maker"):
            mid = request.GET.get("maker")
            try:
                mmaker = tipo_oferta.objects.get(id = mid)
                models = list(tipo_alquiler.objects.filter(tipo_oferta = mmaker))
                models = {m.id: m.__unicode__() for m, m in zip(models, models)}
            except Exception as e:
                print(e)
        return HttpResponse(json.dumps(models))
    return HttpResponse(status=400)

def gettrim(request):
    if request.method == "GET":
        trims = None
        user_ = None
        user_trims = []
        if request.GET.get("model"):
            mid = request.GET.get("model")
            try:
                user_id = request.GET.get("user")
                user_ = person.objects.get(username = user_id)
            except Exception as e:
                print("no user")
            try:
                imodel = tipo_alquiler.objects.get(id = mid)
                trims = list(t.nombre for t in tipo_propiedad.objects.filter(tipo_alquiler = imodel))

                if user_:
                    user_trims = list(ucar.trim for ucar in car2.objects.filter(tipo_alquiler = imodel, dueno = user_))

                if len(user_trims):
                    for extra_trim in user_trims:
                        if extra_trim not in trims:
                            trims.append(extra_trim)
                # trims = list((m.__unicode__(), m.__unicode__()) for m, m in zip(trims, trims))
                trims = {m: m for m, m in zip(trims, trims)}
            except Exception as e:
                print(e)
        return HttpResponse(json.dumps(trims))
    return HttpResponse(status=400)
def getyear(request):
    if request.method == "GET":
        trims_years = None
        if request.GET.get("model"):
            mid = request.GET.get("model")
            try:
                imodel = tipo_alquiler.objects.get(id = mid)
                trims = list(tipo_propiedad.objects.filter(tipo_alquiler = imodel))
                years = []
                for tr in trims:
                    t_y = tipo_objeto.objects.filter(tipo_propiedad = tr)
                    for y in t_y:
                        years.append(y.nombre)
                trims_years = {m: m for m, m in zip(years, years)}
            except Exception as e:
                print(e)
        return HttpResponse(json.dumps(trims_years))
    return HttpResponse(status=400)

  
  
  
  


  
  
  

  
  
  
  
  
  
def approved(request):
    context = logUser(request)
    context["body_styles"] = body_style.objects.all().order_by('index')
    return render(request,'pages/calculator.html', context)

def financing(request):
    context = logUser(request)
    context["body_styles"] = body_style.objects.all().order_by('index')
    return render(request,'pages/financing.html', context)
def listingsel(request):
    posible_results_offered = 10
    ordenation = {
    1: "-created_at",
    2: "created_at",
    3: "-year",
    4: "year",
    5: "-price",
    6: "price",
    }
    page = 1 if request.method != "GET" else request.GET.get("page") if request.GET.get("page") else 1
    obj_per_page = 10 if request.method != "GET" else request.GET.get("result") if request.GET.get("result") else 10
    order = 1 if request.method != "GET" else int(request.GET.get("filter")) if request.GET.get("filter") else 1
    context = logUser(request)
    context["result"] = int(obj_per_page)
    context["body_styles"] = body_style.objects.all().order_by('index')
    context["makers"] = make.objects.all()
    page, max_pages, context["cars"]  = paginate(obj_per_page = int(obj_per_page), page_number = int(page),  objects = anuncio.objects.filter(published=True).order_by(ordenation.get(order, "-created_at")) )
    context["max_pages_range"]= range(0, max_pages if max_pages else 1)
    context["max_pages"] = max_pages if max_pages else 1
    context["current_page"] = int(page) if (int(page) <= max_pages) else 1
    context["load_result_range"] = range(1, posible_results_offered)
    context["filter"] = order
    context["form"] = indexForm()
    context["slides"] = slide.objects.all()
    context["all_photos"] = {}
    for c in context["cars"]:
        cars_p = (mImage.objects.filter(rcar = c))
        context["all_photos"][c.id] = cars_p

    return render(request,'pages/listingsel.html', context)

def Company_Information(request):
    return render(request,'pages/Company_Information.html', logUser(request))
