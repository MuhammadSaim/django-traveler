from django.shortcuts import render

# Create your views here.


def home_view(request):
    data_lists = [
        'hotel',
        'restaurants',
        'motel',
        'guest',
        'vacation',
        'resorts',
        'hill station',
        'hut',
        'camp',
    ]
    context = {
        'data': data_lists
    }
    return render(request, 'hotel/home.html', context)
