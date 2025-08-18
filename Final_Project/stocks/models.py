from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
import datetime


class Stock(models.Model):
    logo = models.ImageField(upload_to="logos/")
    symbol = models.CharField(max_length=16, unique=True)
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    current_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    market_cap = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)
    year_founded = models.IntegerField(
        validators=[MaxValueValidator(datetime.date.today().year)],
        help_text="Year the company was founded"
    )

    class Meta:
        ordering = ["symbol"]

    def __str__(self) -> str:
        return f"{self.symbol} - {self.company_name}"


class Review(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating from 1 to 5 stars"
    )
    comment = models.TextField(max_length=500, help_text="Your review comment")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['stock', 'user']  # User can write one review per stock

    def __str__(self):
        return f"{self.user.username} - {self.stock.symbol} ({self.rating}/5)"