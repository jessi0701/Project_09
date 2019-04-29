from django.shortcuts import render,redirect
from .models import Movie,Score
from .forms import ScoreForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
# Create your views here.
def list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/list.html',{'movies':movies})
    
def detail(request,id):
    movie = Movie.objects.get(id=id)
    score_form = ScoreForm()
    return render(request,'movies/detail.html',{'movie':movie,'score_form':score_form})

@login_required
@require_POST
def score_create(request,id):
    score_form = ScoreForm(request.POST)
    if score_form.is_valid():
        score = score_form.save(commit=False)
        score.user = request.user
        score.movie = Movie.objects.get(id=id)
        score_form.save()
        return redirect("movies:detail",id)
        
@login_required
@require_POST
def score_delete(request, movie_id, score_id):
    score = Score.objects.get(id=score_id)
    if score.user == request.user:
        score.delete()
    return redirect("movies:detail", movie_id)
    
    
        