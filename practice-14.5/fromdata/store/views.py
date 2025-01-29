from django.shortcuts import render, redirect
from .forms import contact_from

# Create your views here.
def homepage(request):
    if request.method == 'POST':
        form = contact_from(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # Access cleaned data
            name = form.cleaned_data['name']
            message = form.cleaned_data['comment']

            # Do something with the data (e.g., save to database, send email)
            print(f"Name: {name}, Message: {message}")

           
            return redirect('home_page')  # Ensure 'home_page' is correctly defined in urls.py

    else:
        form = contact_from()  # Ensure a fresh form for GET request

    return render(request, 'abc/home.html', {'forms': form})  # Fix dictionary key to match the template form name
