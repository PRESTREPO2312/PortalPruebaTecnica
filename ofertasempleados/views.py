from django.shortcuts import render,redirect
from rest_framework import viewsets
from .models import Empresa, Oferta, Usuario, Postulacion
from .serializers import EmpresaSerializer, OfertaSerializer, UsuarioSerializer, PostulacionSerializer
from .forms import RegistroForm,OfertaForm,LoginForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class OfertaViewSet(viewsets.ModelViewSet):
    queryset = Oferta.objects.all()
    serializer_class = OfertaSerializer
    template_name = 'ofertas.html' 
    def list(self, request, *args, **kwargs):
        ofertas = self.get_queryset()
        return render(request, self.template_name, {'ofertas': ofertas})

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PostulacionViewSet(viewsets.ModelViewSet):
    queryset = Postulacion.objects.all()
    serializer_class = PostulacionSerializer


class RegistroUsuario(CreateView):
    model = RegistroForm
    template_name = 'registro.html'
    form_class = RegistroForm  
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Inicia sesión automáticamente después del registro
        return redirect('/ofertas')
    

def homes(request):
    return render(request, 'home.html')


@method_decorator(login_required, name='dispatch')
class CrearOfertaView(View):
    template_name = 'crear_oferta.html'

    def dispatch(self, request, *args, **kwargs):
        # Personaliza la redirección si el usuario no está autenticado
        if not request.user.is_authenticated:
            return redirect('/login')  # Reemplaza 'nombre_de_la_url_del_login'

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = OfertaForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = OfertaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Oferta creada exitosamente.')
            return redirect('/ofertas')

        return render(request, self.template_name, {'form': form})
    
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                return redirect('/ofertas') 
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/home')