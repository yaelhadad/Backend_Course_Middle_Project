from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from .models import Stock, Review
from .utils import update_stock_data, generate_ai_summary


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('stocks:stock_list')
    else:
        form = UserCreationForm()
    return render(request, 'stocks/signup.html', {'form': form})


def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, 'stocks/stock_list.html', {'stocks': stocks})


def stock_detail(request, symbol):
    stock = get_object_or_404(Stock, symbol=symbol)
    if not stock.last_updated or (timezone.now() - stock.last_updated) > timedelta(minutes=60):
        update_stock_data(stock)
        stock.last_updated = timezone.now()
        stock.save()
    ai_summary = None

    # Only authenticated users can use AI features
    if request.method == "POST" and "ai_summary" in request.POST and request.user.is_authenticated:
        ai_summary = generate_ai_summary(stock)

    # Handle reviews - only for authenticated users
    if request.method == "POST" and "review_submit" in request.POST and request.user.is_authenticated:
        try:
            rating = request.POST.get('rating')
            comment = request.POST.get('comment')

            if rating and comment:
                review, created = Review.objects.get_or_create(
                    stock=stock,
                    user=request.user,
                    defaults={'rating': int(rating), 'comment': comment}
                )
                if not created:
                    # Update existing review
                    review.rating = int(rating)
                    review.comment = comment
                    review.save()
                    messages.success(request, 'Your review has been updated!')
                else:
                    messages.success(request, 'Your review has been added!')
            else:
                messages.error(request, 'Please provide both rating and comment.')
        except Exception:
            # Handle case where Review table doesn't exist yet
            messages.error(request, 'Review feature is not available yet. Please contact administrator.')

    # Get all reviews for this stock (with error handling)
    try:
        reviews = stock.reviews.all()
        user_review = None
        if request.user.is_authenticated:
            try:
                user_review = Review.objects.get(stock=stock, user=request.user)
            except Review.DoesNotExist:
                pass
    except Exception:
        # Handle case where Review table doesn't exist yet
        reviews = []
        user_review = None

    return render(request, "stocks/stock_detail.html", {
        "stock": stock,
        'ai_summary': ai_summary,
        'reviews': reviews,
        'user_review': user_review
    })








