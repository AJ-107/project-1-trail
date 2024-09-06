from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "Sell": "This is the sell section",
    "BestSellers": "We are the best sellers",
    "Mobiles": "This is the mobile section",
    "TodaysDeals": "Checkout the today's deals here",
    "CustomerService": "Need Help? Feel free to reach us out",
    "Electronics": "This is electronics section",
    "Fashion": "This is fashion section",
    "NewReleases": "Checkout the new releases here",
    "Home&Kitchen": "Checkout the home and kitchen appliances here",
    "AmazonPay": "This is amazon pay section",
    "Computers": "This is computer section",
    "Books": "This is books section"
}

# Create your views here.

def index1(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # "<li><a href="...">January</a></li><li><a href="...">February</a></li>..."

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")