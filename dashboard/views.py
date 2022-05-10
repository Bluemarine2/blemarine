from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import random
from math import ceil
from apps.forms import userForm, expForm, indexForm, signForm, userCreation, slideForm, newPlanForm, blogForm, contactoForm, anunForm, anun22Form
import json
from apps.models import person, body_style, make, transmission_type, drive_train, fuel_type, engine, drive, car, model, mImage, theme, favourite, slide, trim, trim_year, plans, anuncio, tipo_image, categoria, informacion_blog
from apps.views import carCreation, logUser, useField, checkNumberOfCars, authUser


@login_required
def delete_car(request, id, username = None):
    context = logUser(request)
    # context["slides"] = slide.objects.all()
    try:
        user = person.objects.get(username = username) if username is not None and context["is_admin"] else context["userobj"]
        user_car = anuncio.objects.get(id=id, dueno=user)
        user_car.delete()
    except Exception as e:
        print(e)
    return redirect("/dashboard/manage/" + username) if username is not None and context["is_admin"] else redirect("/dashboard/Inventory")

@login_required
def sold_car(request, id, username = None):
    context = logUser(request)
    # context["slides"] = slide.objects.all()
    try:
        user = person.objects.get(username = username) if username is not None and context["is_admin"] else context["userobj"]
        user_car = anuncio.objects.get(id=id, dueno=user)
        user_car.sold = not user_car.sold
        user_car.published = not user_car.published
        user_car.save()
    except Exception as e:
        print(e)
    return redirect("/dashboard/manage/" + username) if username is not None and context["is_admin"] else redirect("/dashboard/sold_inventory")

@login_required
def edit_car(request, id, username = None):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    try:
        user = person.objects.get(username = username) if username is not None and context["is_admin"] else context["userobj"]
        user_car = anuncio.objects.get(id=id, dueno=user)
        if request.method == 'POST':
            form = expForm(request.POST, request.FILES)
            if form.is_valid():
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
                print(request.FILES)
                
                makerobj = tipo_oferta.objects.get(id=_make)
                
                user_car.categoria = body
                user_car.tipo_objeto = _year
                user_car.tipo_propiedad =_trim
                user_car.tipo_alquiler = tipo_alquiler.objects.get(tipo_oferta=makerobj, id=_model)
                user_car.titulo = _titulo_a
                user_car.description = _descripción_a
                user_car.estado_propiedad = estado_propiedad.objects.get(id=_estado_a) if useField(_estado_a) else None
                user_car.especificaciones = _especificaciones_a
                user_car.pais = pais.objects.get(id=_pais_a) if useField(_pais_a) else None
                user_car.estado_pais = pais_estado.objects.get(id=_estados_a) if useField(_estados_a) else None
                user_car.ciudad = ciudad.objects.get(id=_municipios_a) if useField(_municipios_a) else None
                user_car.lat = _lats
                user_car.lon = _lons
                user_car.servicios = json.dumps(_servicioss)
                user_car.image =  _image_a
                user_car.moneda = _moneda_a
                user_car.precio = _priceaa
              
                
 

                user_car.save()
                for file in images:
                    newImage = tipo_image.objects.create(image = file, ranuncio = user_car)
                return redirect("/dashboard/manage/" + username) if username is not None and context["is_admin"] else redirect("/dashboard")
        else:

            data = {
              'pais_a': user_car.pais.id if user_car.pais is not None else '',
              'estados_a': user_car.estado_pais.id if user_car.estado_pais is not None else '',
              'municipios_a': user_car.ciudad.id if user_car.ciudad is not None else '',
              'titulo_a': user_car.titulo,
              'descripción_a': user_car.description,
              'moneda_a': user_car.moneda,
              'priceaa': user_car.precio,
              'estado_a': user_car.estado_propiedad.id if user_car.estado_propiedad is not None else '',
              'lats': user_car.lat,
              'lons': user_car.lon,
              'especificaciones_a': user_car.especificaciones,
              'image_a': user_car.image,
              'servicioss': json.loads(user_car.servicios) if user_car.servicios else '',
              
              
                   
      
                    }
            
            form = expForm()
 

            context["car_edit_images"] = tipo_image.objects.filter(ranuncio__id = user_car.id)

            form.initial = data
            form.fields["photo"].required = False
            
        context['form'] = form
    except Exception as e:
        print(e)
    return render(request, 'pages/add_cars.html', context)

@login_required
def add_inventory(request, body=None):
    return carCreation(request, body)
  

def blog_cre(request):
    data ={
    'form2': blogForm()
    }
    
    if request.method == 'POST':
      formulario = blogForm(data=request.POST)
      if formulario.is_valid():
        formulario.save()
        data["mensaje"] = "Blog Guardado"
      else:
        data["form2"] = formulario
    
       
    return render(request,'pages/blog_cre.html', data)

  
@login_required
def Inventory(request):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    context["cars"] = (anuncio.objects.filter(dueno=context["userobj"], published = True, sold = False))
    context["all_photos"] = {}
    for c in context["cars"]:
        cars_p = (tipo_image.objects.filter(ranuncio = c))
        context["all_photos"][c.id] = cars_p
    # print(context["all_photos"])
    return render(request,'pages/inventory.html', context)

@login_required
def Backend(request):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    context["cars2"] = (favourite.objects.filter(user_id=context["userobj"], ))
    context["cars"] = (anuncio.objects.filter(dueno=context["userobj"], published = True, sold = False))
    context["all_photos"] = {}
    for c in context["cars"]:
        cars_p = (tipo_image.objects.filter(ranuncio = c))
        context["all_photos"][c.id] = cars_p
    # print(context["all_photos"])
    return render(request,'pages/backend.html', context)

@login_required
def sold_inventory(request):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    context["cars"] = (anuncio.objects.filter(dueno=context["userobj"], published = True, sold = False))
    context["all_photos"] = {}
    for c in context["cars"]:
        cars_p = (tipo_image.objects.filter(ranuncio = c))
        context["all_photos"][c.id] = cars_p
    return render(request,'pages/sold_inventory.html', context)



@login_required
def my_favourites(request):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    favo = favourite.objects.filter(user = context["userobj"])
    context["cars"] = list()
    context["all_photos"] = {}
    for el in favourite.objects.filter(user = context["userobj"]):
        context["cars"].append(el.car)
        cars_p = (mImage.objects.filter(rcar = el.car))
        context["all_photos"][el.car.id] = cars_p

    return render(request,'pages/my_favourites.html', context)

@login_required
def inventory_analysis(request):
    return render(request,'pages/inventory_analysis.html', logUser(request))
  
@login_required
def pago(request):
    return render(request,'pages/pago.html', logUser(request))

@login_required
def website(request):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    if context["is_dealer"]:
        context["all_themes"] = theme.objects.all()
        if request.method == "POST":
            try:
                new_theme = theme.objects.get(name = request.POST.get('change'))
                person.objects.filter(username = context["userobj"].username).update(utheme = new_theme)
                context["message"] = "Theme changed"
                context["current"] = new_theme
            except:
                context["message"] = "A terrible error has happened"
                context["current"] = context["userobj"].utheme if context["userobj"].utheme is not None else theme.objects.filter(name = "A1001")
        else:
            context["current"] = context["userobj"].utheme if context["userobj"].utheme is not None else theme.objects.filter(name = "A1001")

    return render(request,'pages/website.html', context) if context["is_dealer"] else redirect("/dashboard")

@login_required
def profile(request):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    if request.method == "POST":
        if context["userobj"].check_password(request.POST.get('old_psw')):
            first_name = request.POST.get('fname')
            last_name = request.POST.get('lname')
            raw_new_psw = request.POST.get('new_psw')
            new_psw = make_password(raw_new_psw)
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            cell_phone = request.POST.get('cphone')
            address = request.POST.get('address')
            description = request.POST.get('description')
            photo = request.FILES.get('img')

            if context["userobj"].first_name != first_name and first_name is not None and first_name != '':
                person.objects.filter(username = context["userobj"].username).update(first_name = first_name)
            if context["userobj"].last_name != last_name and last_name is not None and last_name != '':
                person.objects.filter(username = context["userobj"].username).update(last_name = last_name)
            if context["userobj"].phone != phone and phone is not None and phone != '':
                person.objects.filter(username = context["userobj"].username).update(phone = phone)
            if context["userobj"].cell_phone != cell_phone and cell_phone is not None and cell_phone != '':
                person.objects.filter(username = context["userobj"].username).update(cell_phone = cell_phone)
            if context["userobj"].address != address and address is not None and address != '':
                person.objects.filter(username = context["userobj"].username).update(address = address)
            if context["userobj"].description != description and description is not None and description != '':
                person.objects.filter(username = context["userobj"].username).update(description = description)
            if photo is not None:
                user = person.objects.get(username = context["userobj"].username)
                user.image.save(photo.name, photo)

            if raw_new_psw is not None and raw_new_psw != '':
                person.objects.filter(username = context["userobj"].username).update(password = new_psw)
                authUser(request, context["userobj"].username, raw_new_psw)
            context = logUser(request)
            context["message"] = "Info updated"
        else:
            context["message"] = "Wrong password. You need to enter your password in order to change your info"

    return render(request,'pages/profile.html', context)

@login_required
def edit_user(request, username):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    if context["is_admin"]:
        context["title"] = "Edit user " + username
        context["edit_user"] = True
        try:
            user = person.objects.get(username = username)
        except Exception as e:
            return redirect("/dashboard/all_users")
        context["form"] = userCreation(initial={'username': user.username, 'password': "Not so fast", 'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name,'address': user.address,'description': user.description, 'phone': user.phone, 'cell_phone': user.cell_phone, 'user_type': 'Private user' if not user.is_dealer else 'Dealer user',
        'facebook': user.facebook, 'twitter': user.twitter, 'instagram': user.instagram, 'google': user.google, 'pinterest': user.pinterest, 'youtube': user.youtube})
        if request.method == "POST":
            context["form"] = userCreation(request.POST, request.FILES)
            print(context["form"])
            if context["form"].is_valid():
                print("ES VÁLIDO")
                username = context["form"].cleaned_data['username']
                first_name = context["form"].cleaned_data['first_name']
                last_name = context["form"].cleaned_data['last_name']
                psw = context["form"].cleaned_data['password']
                email = context["form"].cleaned_data['email']
                phone = context["form"].cleaned_data['phone']
                cell_phone = context["form"].cleaned_data['cell_phone']
                user_type = context["form"].cleaned_data['user_type']
                address = context["form"].cleaned_data['address']
                description = context["form"].cleaned_data['description']
                facebook = context["form"].cleaned_data['facebook']
                twitter = context["form"].cleaned_data['twitter']
                instagram = context["form"].cleaned_data['instagram']
                google = context["form"].cleaned_data['google']
                pinterest = context["form"].cleaned_data['pinterest']
                youtube = context["form"].cleaned_data['youtube']
                photo = request.FILES.get('photo')

                if user.first_name != first_name and first_name is not None and first_name != '':
                    person.objects.filter(username = user.username).update(first_name = first_name)
                if user.last_name != last_name and last_name is not None and last_name != '':
                    person.objects.filter(username = user.username).update(last_name = last_name)
                if user.phone != phone and phone is not None and phone != '':
                    person.objects.filter(username = user.username).update(phone = phone)
                if user.cell_phone != cell_phone and cell_phone is not None and cell_phone != '':
                    person.objects.filter(username = user.username).update(cell_phone = cell_phone)
                if user.address != address and address is not None and address != '':
                    person.objects.filter(username = user.username).update(address = address)
                if user.description != description and description is not None and description != '':
                    person.objects.filter(username = user.username).update(description = description)
                if user.facebook != facebook and facebook is not None and facebook != '':
                    person.objects.filter(username = user.username).update(facebook = facebook)
                if user.twitter != twitter and twitter is not None and twitter != '':
                    person.objects.filter(username = user.username).update(twitter = twitter)
                if user.instagram != instagram and instagram is not None and instagram != '':
                    person.objects.filter(username = user.username).update(instagram = instagram)
                if user.google != google and google is not None and google != '':
                    person.objects.filter(username = user.username).update(google = google)
                if user.pinterest != pinterest and pinterest is not None and pinterest != '':
                    person.objects.filter(username = user.username).update(pinterest = pinterest)
                if user.youtube != youtube and youtube is not None and youtube != '':
                    person.objects.filter(username = user.username).update(youtube = youtube)
                if user.is_dealer == (user_type == "Private user"):
                    person.objects.filter(username = user.username).update(is_dealer = (user_type != "Private user"))

                if photo is not None:
                    user = person.objects.get(username = user.username)
                    user.image.save(photo.name, photo)
                context["message"] = "User " + username + " updated!"

    return render(request,'pages/create_user.html', context) if context["is_admin"] else redirect('/dashboard')

@login_required
def all_users(request, type = None):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    if context["is_admin"]:
        if request.method == 'POST':
            try:
                if request.POST.get('delete') is not None:
                    user = person.objects.get(username = request.POST.get('delete'))
                    context["message"] = "El usuario " + user.username + " ha sido eliminado :("
                    user.delete()
                elif request.POST.get('upgrade') is not None:
                    user = person.objects.get(username = request.POST.get('upgrade'))
                    context["message"] = "¡El usuario " + user.username + " Es ahora distribuidor!"
                    plan = plans.objects.all().first()
                    if plan:
                        person.objects.filter(username = request.POST.get('upgrade')).update(is_dealer = True, cars_to_sell = plan.number_of_cars)
                    else:
                        person.objects.filter(username = request.POST.get('upgrade')).update(is_dealer = True)
                elif request.POST.get('edit') is not None:
                    return redirect("/dashboard/edit_user/"+request.POST.get('edit'))
                elif request.POST.get('down') is not None:
                    user = person.objects.get(username = request.POST.get('down'))
                    context["message"] = "¡El usuario " + user.username + " es ahora vendedor privado!"
                    person.objects.filter(username = request.POST.get('down')).update(is_dealer = False)
                elif request.POST.get('manage') is not None:
                    return redirect("/dashboard/manage/"+request.POST.get('manage'))
                elif request.POST.get('theme') is not None and request.POST.get('theme') != '':
                    info = request.POST.get('theme').split('|')
                    user = info[0]
                    theme_name = info[1]
                    user = person.objects.get(username = user)
                    new_theme = theme.objects.get(name = theme_name)
                    person.objects.filter(username = user).update(utheme = new_theme)
                    context["message"] = "Usuario " + user.username + " está usando el tema " + theme_name + " ahora"
                elif request.POST.get('plan') is not None:
                    info = request.POST.get('plan').split('|')
                    user = info[0]
                    plan_id = info[1]
                    user = person.objects.get(username = user)
                    new_plan = plans.objects.get(id = plan_id)
                    person.objects.filter(username = user).update(cars_to_sell = new_plan.number_of_cars)
                    context["message"] = "Usuario " + user.username + " está usando el plan " + str(new_plan)  + " ahora"
            except Exception as e:
                print(e)
        context["all_themes"] = theme.objects.all()
        context["plans"] = plans.objects.all()
        context["all_users"] = person.objects.filter(~Q(username = 'admin'), anonymous = False) if type is None else (person.objects.filter(~Q(username = 'admin'), anonymous = False, is_dealer = (type == "dealer")) if type == "dealer" or type == "private" else person.objects.filter(~Q(username = 'admin'), anonymous = False))

    return render(request,'pages/all_users.html', context) if context["is_admin"] else redirect('/dashboard')

@login_required
def new(request, type = None):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    if context["is_admin"]:
        context["title"] = "Create new " + ("" if type is None else type) + " user!"
        initial = {} if type is None else {'user_type': "Dealer user"} if type == "dealer" else {'user_type': "Private seller"} if type == "private" else {}
        context["show_selection"] = True if type is not None else False
        context["form"] = userCreation(initial = initial)
        context["edit_user"] = False
        if request.method == "POST":
            context["form"] = userCreation(request.POST, request.FILES)
            if context["form"].is_valid():
                username = context["form"].cleaned_data['username']
                first_name = context["form"].cleaned_data['first_name']
                last_name = context["form"].cleaned_data['last_name']
                psw = context["form"].cleaned_data['password']
                email = context["form"].cleaned_data['email']
                phone = context["form"].cleaned_data['phone']
                user_type = context["form"].cleaned_data['user_type']
                cell_phone = context["form"].cleaned_data['cell_phone']
                description = context["form"].cleaned_data['description']
                address = context["form"].cleaned_data['address']
                facebook = context["form"].cleaned_data['facebook']
                twitter = context["form"].cleaned_data['twitter']
                instagram = context["form"].cleaned_data['instagram']
                google = context["form"].cleaned_data['google']
                pinterest = context["form"].cleaned_data['pinterest']
                youtube = context["form"].cleaned_data['youtube']

                photo = request.FILES.get('photo')
                try:
                    new_user = person.objects.create(username = username,
                    password = make_password(psw),
                    first_name = first_name,
                    last_name = last_name ,
                    email = email,
                    phone = phone,
                    cell_phone = cell_phone,
                    description = description,
                    address = address,
                    facebook = facebook,
                    twitter = twitter,
                    instagram = instagram,
                    google = google,
                    pinterest = pinterest,
                    youtube = youtube,
                    image = photo,
                    is_dealer = (user_type != "Private user")
                    )
                    context["message"] = "User " + username + " created!. Want to create a new one?"
                    context["form"] = userCreation()
                except Exception as e:
                    print(e)
                    context["message"] = "Username or email already in use"
    return render(request,'pages/create_user.html', context) if context["is_admin"] else redirect('/dashboard')

@login_required
def manage(request, username):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    if context["is_admin"]:
        user = None
        try:
            user = person.objects.get(username = username)
        except:
            return redirect("/dashboard/all_users")
        context["client"] = user.username
        context["all_cars"] = anuncio.objects.filter(dueno=user.username)
        context["cars_photos"] = {}
        for c in context["all_cars"]:
            img = (tipo_image.objects.filter(ranuncio = c))
            context["cars_photos"][c.id] = img[0] if len(img) else None
        if request.method == 'POST':
            try:
                if request.POST.get('delete') is not None:
                    car_id = request.POST.get('delete').split('|')
                    return redirect("/dashboard/delete/" + car_id[1] + "/" + car_id[0])
                elif request.POST.get('sold') is not None:
                    car_id = request.POST.get('sold').split('|')
                    return redirect("/dashboard/sold/" + car_id[1] + "/" + car_id[0])
                elif request.POST.get('edit') is not None:
                    car_id = request.POST.get('edit').split('|')
                    return redirect("/dashboard/edit/" + car_id[1] + "/" + car_id[0])
            except:
                pass
    return render(request,'pages/manage.html', context) if context["is_admin"] else redirect('/dashboard')

@login_required
def blog_car_reviews(request):
    return render(request,'pages/blog_car_reviews.html', logUser(request))

@login_required
def blog_press_room(request):
    return render(request,'pages/blog_press_room.html', logUser(request))

@login_required
def blog_buying_guide(request):
    return render(request,'pages/blog_buying_guide.html', logUser(request))

@login_required
def article(request):
    return render(request,'pages/article.html', logUser(request))

@login_required
def slideFunction(request, id = None):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    context["title"] = "New slide" if not id else "Slide " + id
    obj_slide = None
    # redirect_to = False
    try:
        if id:
            obj_slide = slide.objects.get(id = id)
    except:
        obj_slide = None
    if request.method == "POST":
        new_slide = slideForm(request.POST, request.FILES) if not obj_slide else slideForm(request.POST, request.FILES, instance = obj_slide)
        if new_slide.is_valid():
            new_slide.save()
            context["form"] = slideForm()
            context["message"] = "Slide agregado"
            # redirect_to = True
        else:
            context["form"] = new_slide
    else:
        context["form"] = slideForm(instance = obj_slide) if obj_slide else slideForm()
    return render(request,'pages/slide.html', context) #if not redirect_to else redirect("/dashboard/slide")

@login_required
def plans_function(request):
    context = logUser(request)
    if context["is_admin"]:
        context["plans"] = plans.objects.all()
        context["plan_form"] = newPlanForm
        if request.method == 'POST':
            if request.POST.get('delete') is not None:
                try:
                    plan_id = request.POST.get('delete')
                    plans.objects.get(id = plan_id).delete()
                    context["message"] = "Se ha eliminado el plan con éxito"
                except Exception as e:
                    print("Error while deleting plan")
            elif request.POST.get('edit') is not None:
                try:
                    plan_id = request.POST.get('edit')
                    request.session["edit_plan"] = plan_id
                    context["plan_form"] = newPlanForm(instance = plans.objects.get(id = plan_id))
                    context["check"] = True
                except Exception as e:
                    print("Error while editing plan")
            else:
                if 'edit_plan' in request.session :
                    try:
                        created_plan = newPlanForm(request.POST, request.FILES, instance = plans.objects.get(id = request.session["edit_plan"]))
                    except Exception as e:
                        created_plan = newPlanForm(request.POST, request.FILES)
                else:
                    created_plan = newPlanForm(request.POST, request.FILES)

                if created_plan.is_valid():
                    created_plan.save()
                    if 'edit_plan' in request.session :
                        del request.session["edit_plan"]
                else:
                    context["plan_form"] = created_plan
                    context["check"] = True
        return render(request,'pages/plans.html', context)
    else:
        return redirect("/dashboard")

@login_required
def logo(request):
    context = logUser(request)
    context["slides"] = slide.objects.all()
    if request.method == 'POST':
        try:
            images = request.FILES
            logo = list(images.values())[0]
            user = person.objects.get(username = context["userobj"].username)
            user.logo.save(context["userobj"].username, logo)
        except:
            pass
        print("Logo changed")
    return redirect("/dashboard/website")

@login_required
def manager(request):
    return render(request,'pages/manager.html', logUser(request))

@login_required
def editterms(request):
    return render(request,'pages/editterms.html', logUser(request))

@login_required
def Edit_Company_Information(request):
    return render(request,'pages/Edit_Company_Information.html', logUser(request))
