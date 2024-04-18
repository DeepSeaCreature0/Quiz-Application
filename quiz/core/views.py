from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import ResponseForm
from .models import Response

def home_view(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_name = request.POST.get('user_name')
        return redirect('quiz', user_id=user_id, user_name=user_name)
    return render(request, 'home.html')

def quiz_view(request, user_id, user_name):
    existing_response = Response.objects.filter(user_id=user_id).first()
    if request.method == 'POST':
        form = ResponseForm(request.POST, instance=existing_response)
        if form.is_valid():
            response = form.save(commit=False)
            response.user_name = user_name
            response.user_id = user_id
            response.submission_date = timezone.now()
            response.save()
            return redirect('success', favorite_game=form.cleaned_data['favorite_game'])
    else:
        form = ResponseForm(instance=existing_response)
    return render(request, 'quiz.html', {'form': form})

def success_view(request, favorite_game):
    return render(request, 'success.html', {'favorite_game': favorite_game})
