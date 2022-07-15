from django.shortcuts import render, redirect, get_object_or_404
from hotel.models.Hotel import Hotel
from hotel.models.HotelImage import HotelImage
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from hotel.forms.CreateHotelForm import CreateHotelForm
from django.contrib import messages


@login_required
def all_hotels(request):
    if request.user.role != 'admin':
        return redirect('home')

    hotels = Hotel.objects.all().order_by('-id')
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


@login_required
def hotel_delete(request, slug):
    if request.user.role != 'admin':
        return redirect('home')
    hotel = get_object_or_404(Hotel, slug=slug)
    hotel.delete()
    return redirect('admin.hotels')


@login_required
def hotel_status(request, slug):
    if request.user.role != 'admin':
        return redirect('home')
    hotel = get_object_or_404(Hotel, slug=slug)
    if hotel.is_active:
        hotel.is_active = False
    else:
        hotel.is_active = True
    hotel.save(update_fields=['is_active'])
    return redirect('admin.hotels')


@login_required
def hotel_edit(request, slug):
    if request.user.role != 'admin':
        return redirect('home')
    hotel = get_object_or_404(Hotel, slug=slug)
    form = CreateHotelForm(request.POST or None, request.FILES or None, instance=hotel)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Your Hotel is updated successfully.")

    context = {
        'form': form,
        'hotel': hotel
    }
    return render(request, 'hotel/admin/edit.html', context)


@login_required
def hotel_gallery(request, slug):
    if request.user.role != 'admin':
        return redirect('home')
    hotel = get_object_or_404(Hotel, slug=slug)
    images = HotelImage.objects.filter(hotel=hotel)

    if request.method == 'POST':
        upload_images = request.FILES.getlist('image')
        for u_img in upload_images:
            HotelImage.objects.create(hotel=hotel, image=u_img)
        messages.add_message(request, messages.SUCCESS, "Gallery is updated successfully.")

    context = {
        'hotel': hotel,
        'images': images,
    }
    return render(request, 'hotel/admin/gallery.html', context)


@login_required
def hotel_gallery_delete(request, id, slug):
    if request.user.role != 'admin':
        return redirect('home')
    image = get_object_or_404(HotelImage, id=id)
    image.delete()
    return redirect('admin.hotel.gallery', slug)
