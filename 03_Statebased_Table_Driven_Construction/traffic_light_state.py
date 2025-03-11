from enum import Enum
import time

class TrafficLight(Enum):
    MERAH = "Merah"
    HIJAU = "Hijau"
    KUNING = "Kuning"

state_transitions = {
    TrafficLight.MERAH : TrafficLight.HIJAU,
    TrafficLight.HIJAU : TrafficLight.KUNING,
    TrafficLight.KUNING : TrafficLight.MERAH
}

state_durations = {
    TrafficLight.MERAH : 6,
    TrafficLight.HIJAU : 4,
    TrafficLight.KUNING : 1
}

current_state = TrafficLight.MERAH

while True:
    print(f"State: {current_state.value}")
    time.sleep(state_durations[current_state])
    current_state = state_transitions[current_state]


current_state = TrafficLight.MERAH
next_state = state_transitions[current_state]
print(next_state)