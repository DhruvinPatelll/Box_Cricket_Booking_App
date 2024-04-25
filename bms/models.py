from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Stadium(models.Model):
    name = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    image = models.ImageField(upload_to="grd/")
    address = models.CharField(max_length=300, null=True)
    slug = models.SlugField(unique=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name


class Pitch(models.Model):
    category = models.CharField(max_length=100)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    shape = models.TextField()

    def __str__(self):
        return self.category


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    pitch = models.ForeignKey(Pitch, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TextField()
    order_id = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    paid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.pitch.price
        super().save(*args, **kwargs)

    def is_duplicate_booking(self):
        duplicate_bookings = Booking.objects.filter(
            stadium=self.stadium, pitch=self.pitch, date=self.date, time=self.time
        ).exclude(user=self.user)

        return duplicate_bookings.exists()

    def is_existing_booking(self):
        existing_bookings = Booking.objects.filter(
            stadium=self.stadium,
            pitch=self.pitch,
            date=self.date,
            time=self.time,
            user=self.user,
        )

        if self.id:
            existing_bookings = existing_bookings.exclude(id=self.id)
        return existing_bookings.exists()

    def __str__(self):
        return f"{self.stadium} is booked by {self.user}"