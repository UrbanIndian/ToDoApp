from django.shortcuts import render, redirect
from .models import list
from .forms import ListForm
from django.contrib import messages
# Create your views here.

def home(request):
	if request.method == 'POST':
		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			all_items = list.objects.all
			messages.success(request, 'Item has been added to the list!!')
			return render(request, 'home.html', {'all_items': all_items})
	else:
		all_items = list.objects.all
		return render(request, 'home.html', {'all_items': all_items})

def about(request):
	context = {'first_name': 'John', 'last_name': 'Elder'}
	return render(request, 'about.html', context)

def delete(request, list_id):
	item = list.objects.get(pk = list_id)
	item.delete()
	messages.success(request, 'Item has been deleted!!!')
	return redirect('home')

def cross_off(request, list_id):
	item = list.objects.get(pk = list_id)
	item.completed = True
	item.save()
	return redirect('home')

def uncross(request, list_id):
	item = list.objects.get(pk = list_id)
	item.completed = False
	item.save()
	return redirect('home')

def edit(request, list_id):
	if request.method == 'POST':
		item = list.objects.get(pk = list_id)
		form = ListForm(request.POST or None, instance = item)

		if form.is_valid():
			form.save()
			all_items=list.objects.all
			messages.success(request, 'Item has been added Edited!!')
			return redirect('home')
	else:
		item = list.objects.get(pk = list_id)
		return render(request, 'edit.html', {'item': item})