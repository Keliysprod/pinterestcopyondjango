from django.shortcuts import render, redirect
from .models import Customer,Pins, Category
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy

from django.http import HttpResponseRedirect
from django.core.exceptions import ImproperlyConfigured

from .forms import PinsForm
from .forms import CommentsForm
from django.db.models import Q 

def MainPage(request):
    return render(request, 'pins/main_page.html')

class Category(ListView):
    model=Category
    context_object_name='all_category'
    template_name='pins/category.html'

class PinsView(ListView):
    model=Pins
    context_object_name='all_pins'
    template_name='pins/pinslist.html'

    def get_queryset(self):
        return Pins.objects.filter(category__slug=self.kwargs.get('slug'))
    

class PinsDetail(DetailView, FormMixin):
    model = Pins
    template_name='pins/pins_detail.html'
    context_object_name= 'pin'
    
    form_class = CommentsForm
    success_url= reverse_lazy('main_page')
    

    def post(self,request,*args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.pin=self.get_object()
        self.object.save()
        return super().form_valid(form)


class Register(CreateView):
    template_name='registration/register.html'
    form_class=UserCreationForm
    success_url=reverse_lazy('successreg')

    def get_success_url(self):
        if not self.success_url:
            raise ImproperlyConfigured("NO url to redirect")
        return str(self.success_url)


    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)
	    

def Success(request):
    return render(request, 'registration/success.html')


class AllPins(ListView):
    model = Pins
    template_name='pins/all_pins.html'
    context_object_name= 'pins'


class Search(ListView):
    template_name = 'pins/all_pins.html'
    context_object_name= 'news' # -> allpins
    paginate_by=5


    def get_queryset(self):
        return Pins.objects.filter(pic_name__icontains=self.request.GET.get('q'))
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context 
    

#создать
def post_create(request):
    form = PinsForm
    if request.method == 'POST':
        form = PinsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
       'form' : form 
    }
    return render(request, 'post_create.html', context)

#Удалить
def post_delete(request, pk):
    computer = Pins.objects.get(slug=pk)
    computer.delete()
    return redirect('/')

