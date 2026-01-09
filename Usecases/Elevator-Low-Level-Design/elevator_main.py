from elevator_system import ElevatorSystem
from selection_strategy.odd_even_elevator_sel_strategy import OddEvenElevatorSelStrategy
from elevator_direction import ElevatorDirection

def main():
    elevatorSystem = ElevatorSystem.get_elevator_system()
    elevatorSystem.initialize_elevator_system(12, 4)

    elevatorSystem.set_elevator_selectionStrategy(OddEvenElevatorSelStrategy())
    print("------------------------------------------------------------------")
    
    elevatorSystem.send_external_request(ElevatorDirection.DOWN, 10)

    print("------------------------------------------------------------------")


    elevatorSystem.send_internal_request(7, 4)

    print("------------------------------------------------------------------")

if __name__ == "__main__":
    main()