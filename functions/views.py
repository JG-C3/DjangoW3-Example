from django.shortcuts import render
from random import *
import datetime

# Create your views here.
def index(request):
    return render(request, "index.html")

def image(request):
    return render(request, "image.html")

def lucky(request):
    number = randint(1, 100)
    context = {
        "number": number,
    }

    return render(request, "lucky.html", context)

def birthday(request):
    today = datetime.date.today()
    year = today.year
    month = today.month
    day = today.day

    b_month = 1
    b_day = 1

    if (b_month > month):
        b_year = year
    elif (b_month == month) and (b_day >= day):
        b_year = year
    else:
        b_year = year + 1

    birthday = datetime.date(b_year, b_month, b_day)

    d_day = birthday - today
    d_day = d_day.days

    context = {
        "year": year,
        "month": month,
        "day": day,
        "b_month": b_month,
        "b_day": b_day,
        "d_day": d_day,
    }

    return render(request, "birthday.html", context)

def table(request):
    contents = [
        "불고기",
        "파스타",
        "칼국수",
        "치킨",
        "비빔밥",
    ]
    context = {
        "contents": contents,
    }
    return render(request, "table.html", context)
