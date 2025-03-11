from enum import Enum

class jenisKelamin(Enum):
    PRIA = 1
    WANITA = 2

patients = []

def add_patient(name : str,gender : jenisKelamin):
    if not isinstance(gender, jenisKelamin):
        raise ValueError("Jenis Kelamin harusnya pria atau wanita")
    patients
    patients.append({"name" : name, "gender" : gender.name})

add_patient("Andi", jenisKelamin.PRIA)
add_patient("Caca", jenisKelamin.WANITA)

for patient in patients:
    print(f"Nama: {patient['name']}, Jenis Kelamin: {patient['gender']}")