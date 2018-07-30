from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from .models import Image


class IndexView(generic.ListView):
	template_name = 'image/index.html'
	context_object_name = 'all_images'

	def get_queryset(self):
		return Image.objects.all()


class ImageCreate(CreateView):
	model= Image
	fields= ['name', 'file']

class ImageUpdate(UpdateView):
	model= Image
	fields= ['name', 'file']

class ImageDelete(DeleteView):
	model= Image
	success_url= reverse_lazy('image:index')



