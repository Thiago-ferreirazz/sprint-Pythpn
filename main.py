import os
import random

# ASCII art representing the logo
logo = """
_______                      ________    ___      _________   
|\  ___ \                    |\   __  \  |\  \    |\___   ___\ 
\ \   __/|     ____________  \ \  \|\  \ \ \  \   \|___ \  \_| 
 \ \  \_|/__  |\____________\ \ \   ____\ \ \  \       \ \  \  
  \ \  \_|\ \ \|____________|  \ \  \___|  \ \  \       \ \  \ 
   \ \_______\                  \ \__\      \ \__\       \ \__
    \|_______|                   \|__|       \|__|        \|__|
"""

# List of available pilots
pilots = [
    "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10",
    "P11", "P12", "P13", "P14", "P15", "P16", "P17", "P18", "P19", "P20"
]

    # Points assigned based on ranking
ranking_points = {
    1: 500, 2: 400, 3: 350, 4: 300, 5: 250, 6: 200, 7: 180, 8: 160,
    9: 140, 10: 120, 11: 100, 12: 90, 13: 80, 14: 70, 15: 60, 16: 50,
    17: 40, 18: 30, 19: 20, 20: 10
}

# Achievements and their respective points
achievements = {"VR": 200, "PD": 175, "MB": 100, "MU": 150, "VL": -100}

# Função para debugar o código
def debugger():
    print("Starting debug mode...\n")

    # Explicação e execução da função select_pilots
    print("1. A função `select_pilots` permite que o usuário selecione 5 pilotos.\n")
    selected_pilots = select_pilots()
    print(f"Pilotos selecionados: {selected_pilots}\n")

    # Explicação e execução da função verify_choice
    print(
        "2. A função `verify_choice` verifica se o piloto escolhido está na lista de pilotos disponíveis. Se não estiver, solicita outro input.\n")
    test_pilot = "P1"
    verified_pilot = verify_choice(test_pilot)
    print(f"Piloto verificado: {verified_pilot}\n")

    # Explicação e execução da função generate_ranking
    print("3. A função `generate_ranking` gera uma classificação aleatória de pilotos.\n")
    race_results = generate_ranking()
    enumerate_ranking(race_results)
    print("Classificação gerada acima.\n")

    # Explicação e execução da função point_checker
    print(
        "4. A função `point_checker` calcula os pontos que os pilotos selecionados ganham com base na posição final na corrida.\n")
    captain = selected_pilots[0]
    points = point_checker(selected_pilots, race_results, captain)
    print(f"Total de pontos calculados: {points}\n")

    # Explicação e execução da função achivments_simu
    print("5. A função `achivments_simu` gera aleatoriamente quais pilotos ganharam conquistas durante a corrida.\n")
    achievements_results = achivments_simu()
    for key in achievements_results:
        print(f"{key} recebeu {achievements_results[key]} pontos de conquista.")
    print()

    # Explicação e execução da função achivments_points
    print("6. A função `achivments_points` soma os pontos ganhos pelos pilotos selecionados nas conquistas.\n")
    achievements_points_total = achivments_points(achievements_results, selected_pilots)
    print(f"Total de pontos de conquistas: {achievements_points_total}\n")

    # Explicação e execução da função determine_rank
    print("7. A função `determine_rank` determina o ranking do jogador com base nos pontos totais acumulados.\n")
    global_points = 6500
    rank, point_deduction = determine_rank(global_points)
    print(f"Com {global_points} pontos você estaria no {rank} e perderia {point_deduction} antes de entrar em qualquer partida")

# Function to clear the console screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to verify if the selected pilot is valid
def verify_choice(selected_pilot):
    while selected_pilot not in pilots:
        selected_pilot = input("Enter a pilot from the list: ").upper()
    return selected_pilot

# Function to generate a randomized ranking
def generate_ranking():
    simulation = []
    while len(simulation) < 20:
        pilot = random.choice(pilots)
        if pilot not in simulation:
            simulation.append(pilot)
    return simulation

# Function to print the ranking with enumeration
def enumerate_ranking(pilot_list):
    for index, pilot in enumerate(pilot_list):
        print(f"{index + 1}: {pilot}\n")

# Function to select pilots by the user
def select_pilots():
    print(f"\nThese are the available pilots:\n{pilots}\n")
    selected_pilots = []
    for i in range(5):
        pilot = verify_choice(input(f"Select your {i + 1}º pilot: ").upper())
        while pilot in selected_pilots:
            pilot = verify_choice(input("Choose a different pilot: ").upper())
        selected_pilots.append(pilot)
    return selected_pilots

# Function to calculate the points earned by each pilot in a race
def point_checker(selected_pilots, race_results, captain):
    total_points = 0
    for pilot in selected_pilots:
        position = race_results.index(pilot) + 1
        points = ranking_points[position]
        if pilot == captain:
            points = int(points * 1.5)
        total_points += points
        print(f"{pilot} scored {points}")
    return total_points

# Function to simulate achievements for each race
def achivments_simu():
    round_achievements = {}
    for key in achievements:
        new_key = random.choice(pilots)
        round_achievements[new_key] = achievements[key]
    return round_achievements

# Function to calculate the total points earned through achievements
def achivments_points(results, selected_pilots):
    total = 0
    for pilot in range(len(selected_pilots)):
        for key in results:
            if selected_pilots[pilot] == key:
                total += results[key]
    return total

# Function to determine the ranking based on total points earned
def determine_rank(points):
    if points >= 9000:
        return "Diamond", 300
    elif points >= 6000:
        return "Platinum", 250
    elif points >= 4000:
        return "Gold", 200
    elif points >= 2000:
        return "Silver", 100
    else:
        return "Bronze", 0

# Main game function
def game():
    global_points = 0
    print(logo)
    print("Welcome to the E-pit simulation")
    way = input("Press any key to start a simulation or type debugger: ")
    if way =="debugger":
        debugger()
        input("Press any key to start a simulation: ")
        clear()

    while True:
        rank, point_deduction = determine_rank(global_points)
        print(f"\nYour current score is {global_points}")
        print(f"You are in {rank} rank, you will lose {point_deduction} points for playing this round\n")

        selected_pilots = select_pilots()
        print(f"\nThese are your pilots: {selected_pilots}\n")

        captain = input("Select a captain among them, who will score 50% more: ").upper()
        while captain not in selected_pilots:
            captain = input("Choose one of the pilots selected by you: ").upper()

        race_results = generate_ranking()
        print("\nThis is the result:\n")
        enumerate_ranking(race_results)

        round_points = point_checker(selected_pilots, race_results, captain)

        print("\nRound achievements: \n")
        achievements_results = achivments_simu()
        
        for key in achievements_results:
            if achievements_results[key] == 200:
                print(f"{key} Set the fastest lap")
            elif achievements_results[key] == 175:
                print(f"{key} Was the standout pilot")
            elif achievements_results[key] == 150:
                print(f"{key} Made the most overtakes")
            elif achievements_results[key] == 100:
                print(f"{key} Received the most boosts")
            else:
                print(f"{key} Set the slowest lap")
        
        points_gained = achivments_points(achievements_results, selected_pilots)
        
        print(f"\nYou received {points_gained} through the achievements\n")

        global_points += round_points - point_deduction + points_gained
        print(f"\nThis is your score for this round: {round_points} For your placements + {points_gained} for your achievements - {point_deduction} ranking cost = {round_points - point_deduction + points_gained}")

        keep_simulating = input('Type "stop" to end the simulation or any other key to keep playing: ').lower()
        if keep_simulating == "stop":
            clear()
            print(logo)
            print(f"\n Your final rank was {rank}\n")
            print("We appreciate your time")
            break
        else:

            clear()
            print(logo)

game()