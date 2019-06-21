from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Review
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
# Create your views here.

def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
        review = Review.RATING_CHOICES
    except Album.DoesNotExsist:
            raise Http404("Album does not exsist")
    return render(request, 'music/detail.html', {'album': album}, {'review': review} )

def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

######################
##class DishCreate(CreateView):
    template_name = 'music/detail.html'
                                              
    #def review(request):
    restaurant = get(Album, pk=pk)
    review = Food(
    rating=request.POST['rating'],
    comment=request.POST['comment'],
    user=request.user,
    restaurant=restaurant)
    review.save()
    return HttpResponseRedirect(reverse('music:detail', args=(restaurant.id,)))