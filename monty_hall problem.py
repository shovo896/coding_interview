import random

def monty_hall_simulate(switch: bool, trials: int = 10000) -> float:
    wins = 0
    for _ in range(trials):
        doors = [0, 0, 1]  # 1 = car, 0 = goat
        random.shuffle(doors)
        
        choice = random.randint(0, 2)
        
        # Host reveals a goat door that's not the chosen one
        remaining = [i for i in range(3) if i != choice and doors[i] == 0]
        reveal = random.choice(remaining)
        
        # Switch choice if strategy says so
        if switch:
            final_choice = next(i for i in range(3) if i != choice and i != reveal)
        else:
            final_choice = choice

        if doors[final_choice] == 1:
            wins += 1

    return wins / trials
