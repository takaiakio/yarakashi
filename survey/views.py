from django.shortcuts import render, get_object_or_404, redirect
from .models import NearMiss
from .forms import NearMissForm
import csv
from django.http import HttpResponse

def create_near_miss(request):
    if request.method == 'POST':
        form = NearMissForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_near_miss')
    else:
        form = NearMissForm()
    return render(request, 'survey/form.html', {'form': form})

def list_near_miss(request):
    near_misses = NearMiss.objects.all()
    return render(request, 'survey/list.html', {'near_misses': near_misses})

def detail_near_miss(request, pk):
    near_miss = get_object_or_404(NearMiss, pk=pk)
    return render(request, 'survey/detail.html', {'near_miss': near_miss})

def edit_near_miss(request, pk):
    near_miss = get_object_or_404(NearMiss, pk=pk)
    if request.method == 'POST':
        form = NearMissForm(request.POST, instance=near_miss)
        if form.is_valid():
            form.save()
            return redirect('detail_near_miss', pk=pk)
    else:
        form = NearMissForm(instance=near_miss)
    return render(request, 'survey/form.html', {'form': form})

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="near_miss_data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Title', 'Description', 'Encounters', 'Prevention'])

    for near_miss in NearMiss.objects.all():
        writer.writerow([near_miss.title, near_miss.description, near_miss.encounters, near_miss.prevention])

    return response


def delete_near_miss(request, pk):
    near_miss = get_object_or_404(NearMiss, pk=pk)
    if request.method == 'POST':
        near_miss.delete()
        return redirect('list_near_miss')
    return render(request, 'survey/confirm_delete.html', {'near_miss': near_miss})