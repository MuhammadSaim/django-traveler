from django.shortcuts import render, get_object_or_404
from hotel.models.Hotel import Hotel
from hotel.models.HotelReviews import HotelReview
from hotel.forms.CreateReviewForm import CreateReviewForm
from textblob import TextBlob
from django.db.models import Sum
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from hotel.models.Reservation import Reservation
from hotel.models.HotelImage import HotelImage


# Create your views here.


def home_view(request):
    cities = Hotel.objects.order_by().values('city').distinct()
    hotels = Hotel.objects.filter(is_active=True)
    if request.GET.get('q'):
        hotels = hotels.filter(name__icontains=request.GET.get('q'))
    else:
        if request.GET.get('price'):
            hotels = hotels.filter(price__lte=request.GET.get('price'))
        if request.GET.get('rating'):
            hotels = hotels.filter(total_rating__lte=request.GET.get('rating'))
        if request.GET.get('city'):
            hotels = hotels.filter(city__exact=request.GET.get('city'))
    hotels = hotels.all().order_by('-total_emotion_rating')
    context = {
        'hotels': hotels,
        'cities': cities
    }
    return render(request, 'hotel/home.html', context)


def hotel_detail_view(request, slug):
    hotel = get_object_or_404(Hotel, slug=slug)
    gallery = HotelImage.objects.filter(hotel=hotel).all()
    gallery_count = range(gallery.count() + 1)
    reviews = HotelReview.objects.filter(hotel=hotel).all().order_by('-id')
    total_location = HotelReview.objects.filter(hotel=hotel).aggregate(Sum('location'))['location__sum']
    print(total_location)
    total_value_of_money = HotelReview.objects.filter(hotel=hotel).aggregate(Sum('value_of_money'))['value_of_money__sum']
    total_cleanliness = HotelReview.objects.filter(hotel=hotel).aggregate(Sum('cleanliness'))['cleanliness__sum']
    total_services = HotelReview.objects.filter(hotel=hotel).aggregate(Sum('services'))['services__sum']
    print(total_location)
    form = CreateReviewForm(request.POST or None)
    if form.is_valid():
        HotelReview.objects.filter()
        location = form.cleaned_data.get('location')
        value_of_money = form.cleaned_data.get('value_of_money')
        cleanliness = form.cleaned_data.get('cleanliness')
        services = form.cleaned_data.get('services')
        avg_rating = (float(location) + float(value_of_money) + float(services) + float(cleanliness)) / 4.0
        comment = form.cleaned_data.get('comment')
        image, sentiment, polarity = text_analyzer(comment)
        hotel.total_emotion_rating = hotel.total_emotion_rating + float("{:.2f}".format(polarity))
        HotelReview.objects.create(location=location, value_of_money=value_of_money, cleanliness=cleanliness,
                                   services=services, avg_rating=avg_rating, comment=comment, user=request.user,
                                   hotel=hotel, emoji=image, emotion=sentiment)
        total_sum_rating = HotelReview.objects.filter(hotel=hotel).aggregate(Sum('avg_rating'))
        total_rating_count = HotelReview.objects.filter(hotel=hotel).count()
        hotel.total_rating = total_sum_rating['avg_rating__sum'] / total_rating_count
        hotel.save()
        messages.add_message(request, messages.SUCCESS, "Your review is submitted successfully.")

    context = {
        'hotel': hotel,
        'form': form,
        'reviews': reviews,
        'total_location': total_location,
        'total_value_of_money': total_value_of_money,
        'total_cleanliness': total_cleanliness,
        'total_services': total_services,
        'gallery': gallery,
        'gallery_count': gallery_count
    }
    return render(request, 'hotel/hotel_details.html', context)


def text_analyzer(text):
    text_blob = TextBlob(text)
    return get_analysis(text_blob.sentiment)


def get_analysis(sentiment):
    if sentiment.polarity > 0.4:
        if 0.4 >= sentiment.polarity <= 0.6:
            return "neutral.png", "Neutral", sentiment.polarity
        if 0.6 >= sentiment.polarity <= 0.8:
            return "satisfied.png", "Happy", sentiment.polarity
        if sentiment.polarity > 0.8:
            return "smile.png", "Very Happy", sentiment.polarity
    else:
        return "sad.png", "Very Angry", sentiment.polarity


@login_required
def make_reservation(request, slug):
    hotel = get_object_or_404(Hotel, slug=slug)
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        total_price = request.POST.get('total_price')
        Reservation.objects.create(start_date=start_date, end_date=end_date, total_price=total_price, hotel=hotel, user=request.user)
        messages.add_message(request, messages.SUCCESS, "Your hotel reservation is complete successfully.")
    context = {
        'hotel': hotel
    }
    return render(request, 'hotel/create_reservation.html', context)


@login_required
def reservations_view(request):
    if request.user.role == 'admin':
        reservations = Reservation.objects.all().order_by('-id')
    else:
        reservations = Reservation.objects.filter(user=request.user).all().order_by('-id')
    paginator = Paginator(reservations, per_page=10)
    page_number = request.GET.get('page')
    reservations = paginator.get_page(page_number)
    context = {
        'reservations': reservations
    }
    return render(request, 'hotel/reservations.html', context)
