from django.shortcuts import render, redirect, get_object_or_404
from main.forms import StoreForm
from main.models import Store
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    store_list = Store.objects.all()

    context = {
        'appname' : 'Football Store',
        'name': 'Angelo Johenry Apituley',
        'class': 'PBP B',
        'store_list': store_list
    }

    return render(request, "main.html", context)

def add_object(request):
    form = StoreForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "add_object.html", context)

def show_object(request, id):
    store = get_object_or_404(Store, pk=id)

    context = {
        'store': store
    }

    return render(request, "object_detail.html", context)

def show_xml(request):
    store_list = Store.objects.all()
    xml_data = serializers.serialize("xml", store_list)
    return HttpResponse(xml_data, content_type= "application/xml")

def show_json(request):
    store_list = Store.objects.all()
    json_data = serializers.serialize("json", store_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, store_id):
    try:
        store_item = Store.objects.filter(pk=store_id)
        xml_data = serializers.serialize("xml", store_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Store.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, store_id):
    try:
        store_item = Store.objects.filter(pk=store_id)
        json_data = serializers.serialize("json", [store_item])
        return HttpResponse(json_data, content_type="application/json")
    except Store.DoesNotExist:
        return HttpResponse(status= 404)