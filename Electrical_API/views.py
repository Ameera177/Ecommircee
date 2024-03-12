from django.shortcuts import render
from django.http import JsonResponse
from phone.models import Items,ItemDetails
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET'])
def getallitems_list(request):
    Electrical=Items.objects.all()
    Electricallist=list(Electrical.values())
    return JsonResponse({
        'Electrical':Electricallist
    })
@api_view(['GET'])
def list_item_details(request):
    Electrical=ItemDetails.objects.select_related('itemsid').all()
    list1=[]
    for item in Electrical:
        getitems=({
            'id':item.id,
            'name':item.itemsid.name,
            'color':item.color,
            'price':item.price,
            'qty':item.qty,
            'tax':item.tax,
            'total':item.total,
        })
        list1.append(getitems)
        
    
    return JsonResponse({
        'Electrical':list1
    })

def list_item_detailsbyid(request,id):
    Electrical=ItemDetails.objects.select_related('itemsid').filter(id=id)
    list1=[]
    for item in Electrical:
        getitems=({
            'id':item.id,
            'name':item.itemsid.name,
            'color':item.color,
            'price':item.price,
            'qty':item.qty,
            'tax':item.tax,
            'total':item.total
        })
        list1.append(getitems)
        
    
    return JsonResponse({
        'Electrical':list1
    })
