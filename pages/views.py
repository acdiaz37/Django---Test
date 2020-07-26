from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm

"""
PARA VERIFICAR QUE ALGUIEN PERTENEZCA AL STAFF USAR DECORADOR @

OTROS DECORADORES ---
login_required
permison_required
DOCS
https://docs.djangoproject.com/en/2.0/topics/auth/default/#the-login-required-decorator

"""

class StaffRequieredMixin(object):
   #este mixin requerira que el usuario sea del staff
   @method_decorator(staff_member_required)
   def dispatch(self, request, *args, **kwargs):      
      return super(StaffRequieredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class PageListView(ListView):
   model = Page

class PageDetailView(DetailView):
   model = Page

#clase para crear contenido
@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
   #se crea el modelo
   model= Page
   #atributo que carga el nuevo formuilario creado para no usar el default de Django
   form_class= PageForm   
   #pagina a la que redirije una vez se crea una pagina
   success_url = reverse_lazy('pages:pages')   
   #redise;ando funcion dispatch para que valide si un usuario esta logueado

#clase para actualizar contenido
@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
   #se crea el modelo
   model= Page
   #se parametrizan los campos que se pueden editar dentro del modelo
   form_class= PageForm
   #sufijo del nombre del template que actualiza
   template_name_suffix = '_update_form'
   
   #se redefine el metodo que lleva el objeto interno para poderlo manejar
   def get_success_url(self):
      return reverse_lazy('pages:update', args=[self.object.id])+ '?ok'

#clase para eliminar contenido
@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
   model=Page
   success_url = reverse_lazy('pages:pages')
