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
        messages.success(request, "Empleado dado de alta correctamente")
        return render(request,'paginas/empleados/altaempleado.html',{'formulario':empleadoForm()})
    return render(request,'paginas/empleados/altaempleado.html',{'formulario':formulario})

def buscarempleado(request):
    afiliado = request.GET.get('afiliado')
    incluir_inactivos = request.GET.get('incluir_inactivos')

    if afiliado:
        queryset = empleado.objects.filter(afiliado=afiliado)

        if not incluir_inactivos:
            queryset = queryset.filter(is_active=True)

        persona = queryset.first()

        if persona:
            return redirect('horas:modificarempleado', afiliado=persona.afiliado)
        else:
            messages.error(request, 'No se encontró empleado con ese número de afiliado')

    return render(request, 'paginas/empleados/buscarempleado.html')

def mostrarempleado(request, afiliado):
    persona = get_object_or_404(empleado, afiliado=afiliado)
    form = empleadoForm(instance=persona)
    return render(request, 'paginas/empleados/mostrarempleado.html', {'empleado': persona, 'form': form})

def modificarempleado(request, afiliado):
    persona = get_object_or_404(empleado, afiliado=afiliado)

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "guardar":
            form = empleadoForm(request.POST, instance=persona)
            if form.is_valid():
                form.save()
                messages.success(request, 'Empleado modificado con éxito')
                return redirect('horas:buscarempleado')

        elif action == "desactivar":
            persona.is_active = False
            persona.save()
            messages.success(request, 'Empleado desactivado con éxito')
            return redirect('horas:buscarempleado')

        elif action == "activar":
            persona.is_active = True
            persona.save()
            messages.success(request, 'Empleado reactivado con éxito')
            return redirect('horas:modificarempleado', afiliado=persona.afiliado)

    else:
        form = empleadoForm(instance=persona)

    return render(request, 'paginas/empleados/modificarempleado.html', {
        'form': form,
        'empleado': persona
    })

    

def verdatosbuscar(request):
    afiliado = request.GET.get('afiliado')
    incluir_inactivos = request.GET.get('incluir_inactivos')

    if afiliado:
        queryset = empleado.objects.filter(afiliado=afiliado)

        if not incluir_inactivos:
            queryset = queryset.filter(is_active=True)
        persona = queryset.first()

        if persona:
                
            return redirect('horas:mostrarempleado', afiliado=persona.afiliado)

        else:
            messages.error(request, 'No se encontró empleado con ese número de afiliado')

    return render(request, 'paginas/empleados/verdatosbuscar.html')

def tipodecarga(request):
    return render(request,'paginas/tipodecarga.html')
    
def descaso(request):
    return render(request,'paginas/reportes/descanso.html')

def extension(request):
    return render(request,'paginas/reportes/extension.html')

def secretaria(request):
    return render(request,'paginas/reportes/secretaria.html')