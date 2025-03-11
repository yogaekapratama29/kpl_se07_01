from enum import Enum

class JenisKelamin(Enum):
    LAKI_LAKI = 1
    PEREMPUAN = 2

print(JenisKelamin.LAKI_LAKI)
print(JenisKelamin.LAKI_LAKI.value)
print(JenisKelamin.LAKI_LAKI.name)
