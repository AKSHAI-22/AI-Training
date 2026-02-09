visits = [
    {"patient_id": "P1", "doctor": "Dr.A", "visit_count": 3},
    {"patient_id": "P2", "doctor": "Dr.B", "visit_count": 5},
    {"patient_id": "P3", "doctor": "Dr.A", "visit_count": 2},
    {"patient_id": "P4", "doctor": "Dr.C", "visit_count": 4},
    {"patient_id": "P5", "doctor": "Dr.B", "visit_count": 1}
]

doctor_total={}
for r in visits:
    doc=r["doctor"]
    cnt=r["visit_count"]
    if doc in doctor_total:
        doctor_total[doc]+=cnt
    else:
        doctor_total[doc]=cnt
print(doctor_total)

max_visit=visits[0]["visit_count"]
top_patient=visits[0]["patient_id"]
for r in visits:
    if r["visit_count"] > max_visit:
        max_visit = r["visit_count"]
        top_patient = r["patient_id"]
print(top_patient)
print(max_visit)
