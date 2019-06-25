from django.shortcuts import render,get_object_or_404
from .models import Home,Worker,Category
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	homes = Home.objects.all()
	return render(request, "index.html", {'homes':homes})
'''
def index1(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	worker = Worker.objects.all()
		if category_slug:
			category = get_object_or_404(Category, slug=category_slug)
			worker = worker.filter(category=category)
	return render(request, 'index1.html', {'category': category,'categories': categories, 'worker':worker})'''

def detail(request,id=None):
	worker = get_object_or_404(Worker,id=id,slug=slug)
	return render(request,'index2',{'worker':worker})

def furni(request):
	homes = Home.objects.all()
	return render(request, "head/furni.html", {'homes':homes})

def worker(request):
	worker = Worker.objects.all()
	return render(request, "head/worker.html", {'worker':worker})

def calculator(request):
	return render(request, "head/calculator.html", {})

def cal(request):
	return render(request, "head/cal.html", {})

def desc(request):
	worker = Worker.objects.all()
	return render(request, "head/desc.html", {'worker' :worker})

@login_required()
def detail1(request,id=None):
	worker = get_object_or_404(Worker,id=id)
	context = {
		'worker':worker
	}
	template = 'detail.html'
	return render(request,template,context)