from django.shortcuts import render
from .models import *
from django.db.models import Q


def home(request):
    return render(request, 'home.html')


def index(request):
    data = modelValues.objects.all()
    return render(request, 'index.html', {'data': data})


def turkish(request):
    l = modelValues.objects.only(
        "id", "landmark", "turkish_male", "turkish_female")
    return render(request, 'filter.html', {'value': 'Turkish', 'data': l})


def caucasian(request):
    l = modelValues.objects.only(
        "id", "landmark", "caucasian_male", "caucasian_female")
    return render(request, 'filter.html', {'value': 'Caucasian', 'data': l})


def korean(request):
    l = modelValues.objects.only(
        "id", "landmark", "korean_male", "korean_female")
    return render(request, 'filter.html', {'value': 'Korean', 'data': l})


def brazil(request):
    l = modelValues.objects.only(
        "id", "landmark", "brazillian_male", "brazillian_female")
    return render(request, 'filter.html', {'value': 'Brazillian', 'data': l})


def german(request):
    l = modelValues.objects.only(
        "id", "landmark", "german_male", "german_female")
    return render(request, 'filter.html', {'value': 'German', 'data': l})


def indian(request):
    l = modelValues.objects.only(
        "id", "landmark", "indian_male", "indian_female")
    return render(request, 'filter.html', {'value': 'Indian', 'data': l})


def srilankan(request):
    l = modelValues.objects.only(
        "id", "landmark", "srilankan_male", "srilankan_female")
    return render(request, 'filter.html', {'value': 'SriLankan', 'data': l})


def taiwanese(request):
    l = modelValues.objects.only(
        "id", "landmark", "taiwanese_male", "taiwanese_female")
    return render(request, 'filter.html', {'value': 'Taiwanese', 'data': l})


def male(request):
    l = modelValues.objects.only(
        "id", "landmark", "turkish_male", "caucasian_male", "korean_male", "brazillian_male", "indian_male", "german_male", "srilankan_male", "taiwanese_male")
    return render(request, 'filtergen.html', {'value': 'Male', 'data': l})


def female(request):
    l = modelValues.objects.only(
        "id", "landmark", "turkish_female", "caucasian_female", "korean_female", "brazillian_female", "indian_female", "german_female", "srilankan_female", "taiwanese_female")
    return render(request, 'filtergen.html', {'value': 'Female', 'data': l})


def search(request):
    data = modelValues.objects.all()
    return render(request, 'searchpage.html', {'data': data})


def searchop(request):
    search = request.GET['landmark']
    value = request.GET['value']
    item_in_search = False
    item_in_search = modelValues.objects.filter(
        Q(landmark__icontains=search)).exists()
    if(item_in_search == False):
        return render(request, 'nosearch.html')
    else:
        list_total = {}
        data_total = modelValues.objects.filter(Q(landmark__icontains=search))
        print(data_total)
        for data in data_total.iterator():
            if(data.turkish_male == value):
                list_total['Turkish Male'] = value
            if(data.turkish_female == value):
                list_total['Turkish Female'] = value
            if(data.caucasian_male == value):
                list_total['Caucasian Male'] = value
            if(data.caucasian_female == value):
                list_total['Caucasian Female'] = value
            if(data.korean_male == value):
                list_total['Korean Male'] = value
            if(data.korean_female == value):
                list_total['Korean Female'] = value
            if(data.brazillian_male == value):
                list_total['Brazillian Male'] = value
            if(data.brazillian_female == value):
                list_total['Brazillian Female'] = value
            if(data.indian_male == value):
                list_total['Indian Male'] = value
            if(data.indian_female == value):
                list_total['Indian Female'] = value
            if(data.german_male == value):
                list_total['German Male'] = value
            if(data.german_female == value):
                list_total['German Female'] = value
            if(data.srilankan_male == value):
                list_total['Srilankan Male'] = value
            if(data.srilankan_female == value):
                list_total['Srilankan Female'] = value
            if(data.taiwanese_male == value):
                list_total['Taiwanese Male'] = value
            if(data.taiwanese_female == value):
                list_total['Taiwanese Female'] = value
            print(list_total)

        if not list_total:
            return render(request, 'nosearch.html')
        else:
            return render(request, 'filterval.html', {'data': search, 'd': list_total})
