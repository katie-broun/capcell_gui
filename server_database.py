from pymodm import MongoModel, fields


class Patient(MongoModel):
    room_no = fields.IntegerField(primary_key=True)
    name = fields.CharField()
    patient_mrn = fields.IntegerField()
    cpap_pressure = fields.IntegerField()
    cpap_metrics = fields.DictField()
