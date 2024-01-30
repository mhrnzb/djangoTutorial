from django.shortcuts import render
from django.http import HttpResponse ,  HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string 

# Create your views here.

days = {
    'saturday': 'this is satureday in disctionary',
    'sunday': 'this is sunday in disctionary',
    'monday': 'this is monday in disctionary',
    'tuesday': 'this is tuesday in disctionary',
    'wednesday': 'this is wednesday in disctionary',
    'thursday': 'this is thursday in disctionary',
    'friday': None,
}

def dynamic_days(request, day):
    day_data = days.get(day)
    #DTL django template language
    #Django Template Filters
    #https://docs.djangoproject.com/en/5.0/ref/templates/builtins/
    #https://docs.djangoproject.com/en/5.0/ref/templates/language/


    #if day_data is not None:

    context = {
            "data": day_data,
            "day": f'selected day is {day}'

        }
    return render( request , 'challenges/challenge.html' , context )
        #response_data = f' <h1 style="color: red" >day is : {day} and data is : {day_data}</h1> '
        #response_data = render_to_string('challenges/challenge.html')
        #return HttpResponse(response_data)
    
    #return HttpResponseNotFound('day does not exists')







def days_list(request):

    days_list = list(days.keys())
    context ={
        'days':days_list
    }
    return render(request, 'challenges/index.html', context)



def dynamic_days_by_number(request , day ):
    days_names = list(days.keys())
    if day > len(days_names):
        return HttpResponseNotFound('days does not exist')
    redirect_day = days_names[day - 1]
    redirect_url = reverse('days-of-week' , args=[redirect_day])
    return HttpResponseRedirect(redirect_url)
    #return HttpResponse(day)

