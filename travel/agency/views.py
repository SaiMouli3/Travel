from django.shortcuts import render, redirect
from .models import Travel_details , Packages ,Selection
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# def user_details(request):
#     return render(request, 'agency/details.html')
@login_required
def travel_details(request):
    if request.method == 'POST':
        from_location = request.POST.get('fromLocation')
        to_location = request.POST.get('toLocation')
        start_date = request.POST.get('startDate')
        end_date = request.POST.get('endDate')
        trip_type = request.POST.get('tripType')

        request.session['from_location'] = from_location
        request.session['to_location'] = to_location
        request.session['start_date'] = start_date
        request.session['end_date'] = end_date
        request.session['trip_type'] = trip_type

        travel_details = Travel_details(
            user = request.user,
            depature = from_location,
            destination = to_location,
            start_date = start_date,
            end_date = end_date,
            trip_type = trip_type
        )
        travel_details.save()
        return redirect('agency:packages')

    return render(request,'agency/details.html')


def packages(request):
    if all(key in request.session for key in ['from_location', 'to_location', 'start_date', 'end_date', 'trip_type']):
        from_location = request.session.get('from_location')
        to_location = request.session.get('to_location')
        start_date = request.session.get('start_date')
        end_date = request.session.get('end_date')
        trip_type = request.session.get('trip_type')

    pack = Packages.objects.filter(dep__iexact=from_location, des__iexact=to_location)

    return render(request,'agency/packages.html',{'pack': pack})


def select_package(request):
    if request.method == 'POST':
        selected_package_id = request.POST.get('selected_p')
        selected_package = Packages.objects.get(id=selected_package_id)
        print(f"Selected Package ID: {selected_package_id}")
        print(f"Selected Package Price: {selected_package.price}")
        selected = Selection(user=request.user,selected_package = f"{selected_package.dep} to {selected_package.des}",payment = False)
        selected.save()
        return render(request,'agency/payment.html',{'selected_package':selected_package})
    return HttpResponse('Invalid request')






