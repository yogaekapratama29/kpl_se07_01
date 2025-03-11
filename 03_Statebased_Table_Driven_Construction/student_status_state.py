from enum import Enum

class StudentStatus(Enum):
    TERDAFTAR ="Terdaftar"
    LULUS = "Lulus"
    CUTI = "Cuti"
    AKTIF = "Aktif"

class TriggerInputState(Enum):
    CETAK_KSM = "Cetak KSM"
    MENYELESAIKAN_CUTI = "Menyelesaikan Cuti"
    LULUS = "Lulus"
    MENGAJUKAN_CUTI = "Mengajukan Cuti"

state_transitions = {
    StudentStatus.TERDAFTAR : {
        TriggerInputState.CETAK_KSM : StudentStatus.AKTIF,
        TriggerInputState.MENGAJUKAN_CUTI : StudentStatus.CUTI
    },
    StudentStatus.AKTIF : {
        TriggerInputState.LULUS : StudentStatus.LULUS,
        TriggerInputState.MENGAJUKAN_CUTI : StudentStatus.CUTI
    },
    StudentStatus.CUTI : {
        TriggerInputState.MENYELESAIKAN_CUTI : StudentStatus.AKTIF
    }
}

def change_state(current_state, trigger):
    cond_1 = current_state in state_transitions
    cond_2 = trigger in state_transitions[current_state]
    if cond_1 and cond_2:
        return state_transitions[current_state][trigger]
    else:
        return "Transaksi Tidak Valid"
    
current_state = StudentStatus.TERDAFTAR
trigger_input = TriggerInputState.CETAK_KSM
next = change_state(current_state, trigger_input)
print(next)