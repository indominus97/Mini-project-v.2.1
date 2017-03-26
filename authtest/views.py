from django.http import HttpResponse
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template import loader
from .models import Worker


def worker_add(request):
	template = loader.get_template('profiles/signup.html')
	return HttpResponse(template.render(request))


class WorkerCreate(CreateView):
	model = Worker
	fields = ['name', 'ph_number', 'email', 'address', 'age', 'gender']



