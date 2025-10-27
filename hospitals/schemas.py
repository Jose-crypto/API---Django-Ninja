from ninja import Schema, ModelSchema
from .models import Hospital

# Schema class of pydantics used to validate data reques (validar datos de entrada), and format data of response(validar datos de salida )


class HospitalSchema(ModelSchema):
    class Config:
        model = Hospital
        model_fields = ['facility_bed', 'district',
                        'hospital_name', 'website', 'city_town']


