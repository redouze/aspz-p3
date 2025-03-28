import random
import os

file_path = 'dice_rolls.txt'

MAX_FILE_SIZE = 1024

def roll_dice():
    return random.randint(1, 6)

def write_roll_to_file(roll):
    with open(file_path, 'a') as f:
        f.write(f'{roll}\n')

def check_file_size():
    return os.path.getsize(file_path) >= MAX_FILE_SIZE

def simulate_rolls(num_rolls):
    for _ in range(num_rolls):
        
        if check_file_size():
            print(f"Ліміт розміру файлу ({MAX_FILE_SIZE} байт) перевищено. Запис зупинено.")
            break
        
        roll = roll_dice() 
        write_roll_to_file(roll)
        print(f"Кидок: {roll}")

if __name__ == '__main__':
    num_rolls = 1000
    simulate_rolls(num_rolls)
