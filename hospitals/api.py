from ninja import NinjaAPI , Query, UploadedFile, File
from ninja.security import APIKeyQuery #security of endpoint
from ninja.throttling import  AnonRateThrottle # for DDos Atack , Rate Limiting
from .schemas import HospitalSchema, HospitalFilterSchema, HospitalNameSchema
from .models import Hospital
from django.shortcuts import get_object_or_404
from django.db.models import Q
from typing import Optional, Any
from django.http import HttpRequest



#init APP
app = NinjaAPI(title='Hospitals API')


# API security
class ApiKey(APIKeyQuery):
    param_name = 'api_key'
    def authenticate(self, request: HttpRequest, key:Optional[str]) -> Optional[Any]:
        valid_keys=['key1','key2','key3'] #remplazar por claves validas
        if key in valid_keys:
            return {'key':key}
        else:
            return None


api_key = ApiKey()

# Get all hospitals
@app.get('hospital/', response=list[HospitalSchema], auth=api_key ,description='Endpoint to get all hospitals', throttle=[AnonRateThrottle('5/s')])
def get_hospital(request):
    hospital = Hospital.objects.all()
    return hospital


# Get hospitals by ID
@app.get('hospitals/{hospital_id}', response=HospitalSchema, throttle=[AnonRateThrottle('1/s')] , description='Endpoint to get hospitals by ID')
def get_hospital_by_id(request, hospital_id: int):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    return hospital


# Create a new hospital
@app.post('hospitals/', response=HospitalSchema)
def create_hospital(request, payload: HospitalSchema):
    hospital = Hospital.objects.create(**payload.dict())
    return hospital


# Update a hospital
@app.put('hospitals/{hospital_id}', response=HospitalSchema)
def update_hospital(request, hospital_id: int, payload: HospitalSchema):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    for attr, value in payload.dict().items():
        setattr(hospital, attr, value)
    hospital.save()
    return {'success': True}


# Delete API Hospital
@app.delete('hospitals/{hospital_id}')
def delete_hopsital(request, hospital_id: int):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    hospital.delete()
    return {'success': True}



#busqueda search hospital  /hospital/search?query=Berlin
@app.get('hospitals/search/',response=list[HospitalSchema])
def search_hospital(request, query: str ):
    hospital =  Hospital.objects.filter(Q(hospital_name__icontains=query) | Q(city_town__icontains=query))
    return hospital



#Busqueda con filter (Case sensitive)
@app.get('hospitals/find/', response=list[HospitalSchema])
def list_hospitals(request, filters: HospitalFilterSchema = Query(...)):
    hospital= Hospital.objects.all()
    hospital = filters.filter(hospital)
    return hospital

#Search by hospital name 
@app.get('hospitals/',response=list[HospitalSchema], description='Endpoint to get all data of the hospital name')
def list_hospitals_by_name(request, filters: HospitalNameSchema = Query(...)):
    hospital= Hospital.objects.all()
    hospital = filters.filter(hospital)
    return hospital 


#endpoint para subir archivos
@app.post('upload/')
def upload(request, file: UploadedFile = File(...)):
    data = file.read()
    return {'File_name': file.name, 'data': len(data)}