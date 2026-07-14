from django.shortcuts import render

def customer_search(request):
    return render(
        request,
        "customers/search.html",
    )
