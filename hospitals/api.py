from ninja import NinjaAPI
from .schemas import HospitalSchema
from .models import Hospital
from django.shortcuts import get_object_or_404

app = NinjaAPI(title='Hospitals API')


# Get all hospitals
@app.get('hospital/', response=list[HospitalSchema], description='Endpoint to get all hospitals')
def get_hospital(request):
    hospital = Hospital.objects.all()
    return hospital


# Get hospitals by ID
@app.get('hospital/{hospital_id}', response=HospitalSchema, description='Endpoint to get hospitals by ID')
def get_hospital_by_id(request, hospital_id: int):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    return hospital


# Create a new hospital
@app.post('hospital/', response=HospitalSchema)
def create_hospital(request, payload: HospitalSchema):
    hospital = Hospital.objects.create(**payload.dict())
    return hospital


# Update a hospital
@app.put('hospital/{hospital_id}', response=HospitalSchema)
def update_hospital(request, hospital_id: int, payload: HospitalSchema):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    for attr, value in payload.dict().items():
        setattr(hospital, attr, value)
    hospital.save()
    return {'success': True}


# Delete API Hospital
@app.delete('hospital/{hospital_id}')
def delete_hopsital(request, hospital_id: int):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    hospital.delete()
    return {'success': True}

#busque
