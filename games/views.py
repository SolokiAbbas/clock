from django.shortcuts import render

# Create your views here.
def forced(request):
    return render(request, 'games/forced.html')

def collision(request):
    return render(request, 'games/collision.html')

def particle(request):
    return render(request, 'games/particle.html')
