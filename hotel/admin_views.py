from django.shortcuts import render, redirect
from .models import Hotel
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from hotel.forms.CreateHotelForm import CreateHotelForm
from django.contrib import messages


@login_required
def all_hotels(request):
    if request.user.role != 'admin':
        return redirect('home')

    hotels = Hotel.objects.filter(is_active=True).all().order_by('id')
    paginator = Paginator(hotels, per_page=10)
    page_number = request.GET.get('page')
    hotels = paginator.get_page(page_number)
    context = {
        'hotels': hotels
    }
    return render(request, 'hotel/admin/hotels.html', context)


@login_required
def hotel_create(request):
    if request.user.role != 'admin':
        return redirect('home')

    form = CreateHotelForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save(commit=True)
        messages.add_message(request, messages.SUCCESS, "Hotel is created successfully.")

    context = {
        'form': form
    }

    return render(request, 'hotel/admin/create.html', context)


