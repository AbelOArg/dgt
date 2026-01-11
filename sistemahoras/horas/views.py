from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .forms import empleadoForm
from .models import empleado

def inicio(request):
    return  HttpResponse("<H1>BIENVENIDO AL INGRESO DE HORAS</H1>")

def go_to_admin(request):
    return redirect(reverse('admin:index'))

def principal(request):
    return render(request,'paginas/principal.html')

def altaempleado(request):
    formulario = empleadoForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        mensaje = "Empleado dado de alta correctamente"
        return render(request,'paginas/empleados/altaempleado.html',{'formulario':empleadoForm(), 'mensaje': mensaje})
    return render(request,'paginas/empleados/altaempleado.html',{'formulario':formulario})

def buscarempleado(request):
    if request.method == 'POST':
        afiliado = request.POST.get('afiliado')
        persona = empleado.objects.filter(afiliado=afiliado, is_active=True).first()

        if persona:
            return redirect("horas:modificarempleado",afiliado = persona.afiliado)
        else:
            messages.error(request,'No se encontro empleado con ese numero de afiliado')
    
    return render(request,'paginas/empleados/buscarempleado.html')



def modificarempleado(request,afiliado):
    persona = get_object_or_404(empleado,afiliado = afiliado)

    if request.method == "POST":
        action = request.POST.get("action")
        if action == "delete":
            persona.is_active = False
            persona.save()
            messages.success(request,'Empleado eliminado con exito')
            return redirect('horas:buscarempleado')

        
            form = empleadoForm(request.POST, instance=persona)
            if form.is_valid():
                form.save()
                messages.success(request,'Empleado modificado con exito')
                return redirect('horas:buscarempleado')
    else:
        form = empleadoForm(instance=persona)

    return render(request, "paginas/empleados/modificarempleado.html", {
        "form": form,
        "empleado": persona
    })
    

def verdatos(request):
    return render(request,'paginas/empleados/verdatos.html')

def descaso(request):
    return render(request,'paginas/reportes/descanso.html')

def extension(request):
    return render(request,'paginas/reportes/extension.html')

def secretaria(request):
    return render(request,'paginas/reportes/secretaria.html')