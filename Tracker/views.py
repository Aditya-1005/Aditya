from django.shortcuts import render
import requests
# Create your views here.
def home(request):
    url = 'https://api.covid19india.org/data.json'
    json_obj = requests.get(url).json()

    state={}
    for item in json_obj['statewise']:
        if item['state']=='Total':
            state={
                'confirmed_cases':item['confirmed'],
                'active_cases':item['active'],
                'recovered':item['recovered'],
                'deceased':item['deaths'],
            }


    return render(request,'my_templates/home.html',{'state':state})

def state(request):
    url = 'https://api.covid19india.org/data.json'
    json_obj = requests.get(url).json()
    states=[]
    state_data={}
    for item in json_obj['statewise']:
        if item['state']!='State Unassigned' and item['state']!='Total':
            states.append(item['state'])
    response=request.POST.get('state',False)
    #print(response)
    for item in json_obj['statewise']:
        if item['state']==response:
            state_data={
                'state':item['state'],
                'confirmed_cases':item['confirmed'],
                'active_cases': item['active'],
                'recovered': item['recovered'],
                'deceased': item['deaths'],

            }

    return render(request,'my_templates/state.html',{'states':states,'state_data':state_data})

def district(request):
    url = 'https://api.covid19india.org/data.json'
    json_obj = requests.get(url).json()
    url1 = 'https://api.covid19india.org/v2/state_district_wise.json'
    district1 = requests.get(url1).json()
    states = []
    districts=[]
    for item in json_obj['statewise']:
        if item['state'] != 'State Unassigned' and item['state'] != 'Total':
            states.append(item['state'])
    response=request.POST.get('state',False)
    for dist in district1:
        if response == dist['state']:
            for item in dist['districtData']:
                dist_obj = {
                    'district': item['district'],
                    'active_cases': item['active'],
                    'confirmed_cases': item['confirmed'],
                    'recovered': item['recovered'],
                    'deaths': item['deceased'],
                }
                districts.append(dist_obj)
    return render(request,'my_templates/district.html',{'states':states,'districts':districts})