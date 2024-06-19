from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Stadium, Booking, Pitch
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models import Session


def Home(request):
    ground = Stadium.objects.all()
    data = {"ground": ground}
    return render(request, "bms/index.html", data)


@login_required(login_url="login")
def ground_detail(request, ground_slug):
    ground = get_object_or_404(Stadium, slug=ground_slug)

    available_pitches = Pitch.objects.filter(stadium=ground)

    context = {
        "ground": ground,
        "available_pitches": available_pitches,
    }

    if request.method == "POST":
        date = request.POST.get("date")
        time = request.POST.get("time")
        pitch_category = request.POST.get("pitch")
        user = request.user
        email = user.email
        pitch = Pitch.objects.get(stadium=ground, category=pitch_category)
        amount = int(float(pitch.price) * 100)
        client = razorpay.Client(
            auth=("rzp_test_LaoznaLwKIfu0M", "gMQXAubjFfQFJOXpnhYtEkmd")
        )
        payment = client.order.create(
            {"amount": amount, "currency": "INR", "payment_capture": "1"}
        )
        booking = Booking(
            user=user,
            stadium=ground,
            pitch=pitch,
            date=date,
            time=time,
            email=email,
            order_id=payment["id"],
        )
        booking.save()

        request.session["booking_id"] = booking.id

        if booking.is_duplicate_booking():
            messages.error(
                request,
                "Oops... This Slot is already Booked By Any Other User,Please Select different Slot.",
            )
            booking.delete()
            return render(request, "bms/ground_detail.html", context)
        elif booking.is_existing_booking():
            messages.error(request, "Oops... You have already booked this slot.")
            booking.delete()
            return render(request, "bms/ground_detail.html", context)
        else:
            return render(request, "bms/payment.html", {"payment": payment})
            # return render(request, "success_page.html", {"booking": booking})

    return render(request, "bms/ground_detail.html", context)


def Register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        pass1 = request.POST["password"]
        pass2 = request.POST["confirmpassword"]

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already Taken.....")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "EmailId is already Taken.....")
                return redirect("register")
            else:
                user = User.objects.create_user(
                    username=username, password=pass1, email=email
                )
                user.save()
                login(request, user)
                messages.success(request, "Registration successful.")
                next_url = request.POST.get("next")
                return redirect(next_url) if next_url else redirect("home")
        else:
            messages.error(request, "Password coudn't Match.....")
            return redirect("register")

    return render(request, "bms/register.html")


def Login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['username'] = username
            request.session.save()
            messages.success(request, "Login successful.")
            next_url = request.POST.get("next")
            return redirect(next_url) if next_url else redirect("home")
        else:
            messages.error(request, "Invalid login credentials.")
            return redirect("login")
    else:
        return render(request, "bms/login.html")


def Logout(request):
    logout(request)
    Session.objects.filter(session_key = request.session.session_key).delete()
    return redirect("home")


@csrf_exempt
def Payment(request):
    if request.method == "POST":
        a = request.POST
        order_id = ""
        for key, val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break

        booking = Booking.objects.filter(order_id=order_id).first()
        booking.paid = True
        booking.save()

    return render(request, "bms/success_page.html")


def Success(request):
    return render(request, "bms/success_page.html")
