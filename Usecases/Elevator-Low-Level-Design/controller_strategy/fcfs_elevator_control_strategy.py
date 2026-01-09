from controller_strategy.elevator_control_strategy import ElevatorControlStrategy


class FirstComeFirstServerElevatorControlStrategy(ElevatorControlStrategy):
    def determine_next_stop(self, floor_num) -> int:
        print(f"Applying First Come First Serve Algorithm and Moving elevator to floor {floor_num}")
        return 1