from .models import Survey  # models.pyからSurveyモデルをインポート
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
    # HttpResponseでCSVのレスポンスを作成
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="survey_data.csv"'

    # CSVの書き込み処理
    writer = csv.writer(response)
    
    # カラムヘッダーを追加
    writer.writerow(['題名', '遭遇場面', '遭遇回数', 'ミス回避要因'])
    
    # データベースからデータを取得してCSVに書き込む
    survey_data = Survey.objects.all()  # Surveyはアンケートデータのモデル名
    for data in survey_data:
        writer.writerow([data.title, data.scene, data.times, data.avoid_reason])
    
    return response


def delete_near_miss(request, pk):
    near_miss = get_object_or_404(NearMiss, pk=pk)
    if request.method == 'POST':
        near_miss.delete()
        return redirect('list_near_miss')
    return render(request, 'survey/confirm_delete.html', {'near_miss': near_miss})