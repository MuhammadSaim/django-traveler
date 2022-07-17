from django.shortcuts import render, get_object_or_404
from hotel.models.Hotel import Hotel
from hotel.models.HotelReviews import HotelReview
from hotel.forms.CreateReviewForm import CreateReviewForm
from textblob import TextBlob
from django.db.models import Sum
from django.contrib import messages


# Create your views here.


def home_view(request):
    hotels = Hotel.objects.filter(is_active=True).all().order_by('-total_emotion_rating')
    context = {
        'hotels': hotels
    }
    return render(request, 'hotel/home.html', context)


def hotel_detail_view(request, slug):
    hotel = get_object_or_404(Hotel, slug=slug)
    reviews = HotelReview.objects.filter(hotel=hotel).all().order_by('-id')
    form = CreateReviewForm(request.POST or None)
    if form.is_valid():
        has_review = HotelReview.objects.filter(user=request.user, hotel=hotel).first()
        if not has_review:
            HotelReview.objects.filter()
            rating = form.cleaned_data.get('rating')
            comment = form.cleaned_data.get('comment')
            image, sentiment, polarity = text_analyzer(comment)
            hotel.total_emotion_rating = hotel.total_emotion_rating + float("{:.2f}".format(polarity))
            HotelReview.objects.create(rating=rating, comment=comment, user=request.user, hotel=hotel, emoji=image, emotion=sentiment)
            total_sum_rating = HotelReview.objects.filter(hotel=hotel).aggregate(Sum('rating'))
            total_rating_count = HotelReview.objects.filter(hotel=hotel).count()
            hotel.total_rating = total_sum_rating['rating__sum'] / total_rating_count
            hotel.save()
            messages.add_message(request, messages.SUCCESS, "Your review is submitted successfully.")
        else:
            messages.add_message(request, messages.ERROR, "You already submit a review for this hotel.")

    context = {
        'hotel': hotel,
        'form': form,
        'reviews': reviews
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