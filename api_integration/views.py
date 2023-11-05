from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests
from .forms import PacienteRegistroForm, MedicoRegistroForm, ReservaCitaForm
from datetime import datetime

# Create your views here.

################# INICIO #################
def home(request):
    return render(request, 'index.html')

def doctor(request):
    return render(request,'doctor.html')

def paciente(request):
    return render(request,'paciente.html')


################# PACIENTE #################
def registrar_paciente(request):
    error_message = None

    if request.method == "POST":
        form = PacienteRegistroForm(request.POST)
        if form.is_valid():
            data = {
                "rut": form.cleaned_data["rut"],
                "nombre": form.cleaned_data["nombre"],
                "apellido": form.cleaned_data["apellido"],
                "edad": form.cleaned_data["edad"],
                "email": form.cleaned_data["email"],
                "contrasena": form.cleaned_data["contrasena"],
            }
            response = requests.post(
                "https://arquitectura.sabravo.repl.co/api/paciente", json=data
            )

            if response.status_code == 201:
                return redirect("login_paciente")
            else:
                error_message = response.json().get("error", "Error en el registro.")
                return render(
                    request,
                    "registro.html",
                    {"form": form, "error_message": error_message},
                )
    else:
        form = PacienteRegistroForm()

    return render(request, "registro_paciente.html", {"form": form})


def login_paciente(request):
    error_message = None

    if request.method == "POST":
        # Procesa la informacion de inicio de sesion para paciente
        email = request.POST.get("email")
        contrasena = request.POST.get("contrasena")
        data = {"email": email, "contrasena": contrasena}
        response = requests.post(
            "https://arquitectura.sabravo.repl.co/api/login/paciente", json=data
        )

        if response.status_code == 200:
            return redirect("pagina_principal_paciente")
        else:
            error_message = response.json().get("error", "Credenciales invalidas.")

    return render(request, "login_paciente.html", {"error_message": error_message})


################# MEDICO #################


def registrar_medico(request):
    error_message = None

    if request.method == "POST":
        form = MedicoRegistroForm(request.POST)
        if form.is_valid():
            data = {
                "rut": form.cleaned_data["rut"],
                "nombre": form.cleaned_data["nombre"],
                "apellido": form.cleaned_data["apellido"],
                "edad": form.cleaned_data["edad"],
                "especialidad": form.cleaned_data["especialidad"],
                "email": form.cleaned_data["email"],
                "contrasena": form.cleaned_data["contrasena"],
            }
            response = requests.post(
                "https://arquitectura.sabravo.repl.co/api/medico", json=data
            )

            if response.status_code == 201:
                return redirect("login_medico")
            else:
                error_message = response.json().get("error", "Error en el registro.")
                return render(
                    request,
                    "registro_medico.html",
                    {"form": form, "error_message": error_message},
                )
    else:
        form = MedicoRegistroForm()
    return render(request, "registro_medico.html", {"form": form})


def login_medico(request):
    error_message = None

    if request.method == "POST":
        # Procesa la informacion de inicio de sesion para medico
        email = request.POST.get("email")
        contrasena = request.POST.get("contrasena")
        data = {"email": email, "contrasena": contrasena}
        response = requests.post(
            "https://arquitectura.sabravo.repl.co/api/login/medico", json=data
        )

        if response.status_code == 200:
            return redirect("pagina_principal_medico")
        else:
            error_message = response.json().get("error", "Credenciales invalidas.")

    return render(request, "login_medico.html", {"error_message": error_message})


############### LOGICA ##################
def pagina_principal_paciente(request):
    error_message = None

    if request.method == "POST":
        form = ReservaCitaForm(request.POST)
        if form.is_valid():
            paciente_id = form.cleaned_data["paciente_id"]
            medico_id = form.cleaned_data["medico_id"]
            fecha_hora = form.cleaned_data["fecha_hora"].isoformat()  # Convertir a cadena ISO 8601

            data = {
                "paciente_id": paciente_id,
                "medico_id": medico_id,
                "fecha_hora": fecha_hora,
            }
            response = requests.post(
                "https://arquitectura.sabravo.repl.co/api/reserva", json=data
            )

            if response.status_code == 201:
                return redirect("pagina_principal_paciente")
            else:
                error_message = response.json().get("error", "Error al reservar cita.")
    else:
        form = ReservaCitaForm()
        
    return render(request, 'pagina_principal_paciente.html', {'form': form, 'error_message': error_message})


def pagina_principal_medico(request):
    return render(request, "pagina_principal_medico.html")
