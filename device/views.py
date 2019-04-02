from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import data

def index(request):
    return render(request, "index.html", {})


def data_extract(request):
    data_list = data.objects.all()
    c = 0
    all_data = {}
    for x in data_list:
        temp = {
                "distance": x.distance,
                "speed": x.speed,
                "acceleration": x.acceleration,
                "direction": x.direction,
                "date" : x.date
            }
        all_data[c] = temp
        c += 1
    return JsonResponse(all_data)



def data_save(request):
    # if request.method=="GET":
        # url = xyz.com/data_save/?latitude=12345.45&longitude=924.3244&altitude=235.43&temperature=23.12&humidity=234.23&time=21.23.22&date=12.23.23
    username = "shivam"
    distance = request.GET.get("distance")
    speed = request.GET.get("speed")
    acceleration = request.GET.get("acceleration")
    direction = request.GET.get("direction")
    date = request.GET.get("date")
    query = data(username = username, distance = distance, speed = speed, acceleration = acceleration, direction = direction, date = date)
    query.save()
    return HttpResponse("Your Data has been saved")
