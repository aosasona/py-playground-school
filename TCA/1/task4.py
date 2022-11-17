import random

"""
we will pick door number 3 as our winning door

function run_simulation_without_switching runs an instance of the simulation by following these steps:
1. create a random choice for the winning door
2. create a random choice for the door the player chooses
3. return True if both choices are the same, otherwise return False

function run_simulation_with_switching runs an instance of the simulation by following these steps:
1. create a random choice for the winning door
2. create a random choice for the door the player chooses
3. create a another variable that holds the door that the player did not choose and is not the winning door 
(this is the door that will be opened)
4. create a new player choice that is the door that the player did not choose and is not the door that was opened
"""

WINNING_DOOR = 3


def run_simulation_without_switching() -> bool:
    player_choice = random.randint(1, 3)
    return player_choice == WINNING_DOOR


def run_simulation_with_switching() -> bool:
    player_choice = random.randint(1, 3)
    opened_door = 1 if player_choice == 2 else 2
    player_choice = [num for num in range(1, 4) if num not in (player_choice, opened_door)][0]
    return player_choice == WINNING_DOOR


def calculate_percentage(part: int, whole: int) -> float:
    return (part / whole) * 100


def main():
    number_of_simulations = int(input("Enter the number of simulations to run: "))
    score_without_switching, score_with_switching = 0, 0
    for _ in range(number_of_simulations):
        score_without_switching += int(run_simulation_without_switching())
        score_with_switching += int(run_simulation_with_switching())
    winning_percentage = calculate_percentage((score_with_switching + score_without_switching),
                                              (number_of_simulations * 2))
    print(f"\n==================  Without switching   ==================\n"
          f"    Total score -> {score_without_switching}\n"
          f"    Winning percentage -> {calculate_percentage(score_without_switching, number_of_simulations):.2f}%")
    print(f"==================  With switching  ==================\n"
          f"    Total score -> {score_with_switching}\n"
          f"    Winning percentage -> {calculate_percentage(score_with_switching, number_of_simulations):.2f}%")
    print(f"==================  Total Average  ==================\n"
          f"    Winning percentage -> {winning_percentage:.2f}%\n")




if __name__ == "__main__":
    main()
