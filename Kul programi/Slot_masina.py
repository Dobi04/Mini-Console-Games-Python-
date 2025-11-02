#┌───────────┐     \ | /
#|   |   |   |      \|/
#└───────────┘     ─────
#🍒 - Cherries
#🍋 - Lemon
#🍉 - Watermelon
#🍊 - Orange
#🍇 - Grapes
#🍓 - Strawberry

import time
import random

lever_frames = {
    1:  ("┌────────────────┐         \\   ",
         "| 🍒 | 🍉 | 🍇 |            \\  ",
         "└────────────────┘         ─────"),
    2:  ("┌────────────────┐          \\   ",
         "| 🍋 | 🍊 | 🍓 |             \\  ",
         "└────────────────┘         ─────"),
    3:  ("┌────────────────┐           |  ",
         "| 🍒 | 🍋 | 🍉 |             |  ",
         "└────────────────┘         ─────"),
    4:  ("┌────────────────┐            / ",
         "| 🍊 | 🍒 | 🍇 |             /  ",
         "└────────────────┘         ─────"),
    5:  ("┌────────────────┐           /",
         "| 🍋 | 🍉 | 🍓 |            / ",
         "└────────────────┘         ─────"),
    6:  ("┌────────────────┐            / ",
         "| 🍊 | 🍓 | 🍇 |             /  ",
         "└────────────────┘         ─────"),
    7:  ("┌────────────────┐           |  ",
         "| 🍇 | 🍒 | 🍋 |             |  ",
         "└────────────────┘         ─────"),
    8:  ("┌────────────────┐         \\   ",
         "| 🍉 | 🍓 | 🍊 |             \\  ",
         "└────────────────┘         ─────"),
    9:  ("┌────────────────┐         \\    ",
         "| 🍒 | 🍋 | 🍇 |            \\   ",
         "└────────────────┘         ─────")

}


def lever_animation():
    for frame in range(1,10):
        for line in lever_frames.get(frame):
            print(line)
        time.sleep(0.1)

def decoding(slot):
    match slot:
        case 1:
            return "🍒"
        case 2:
            return "🍋"
        case 3:
            return "🍉"
        case 4:
            return "🍊"
        case 5:
            return "🍇"
        case 6:
            return "🍓"

def print_result(fruit1, fruit2, fruit3, slot1, slot2, slot3, score):
    print("**************RESULT**************")
    print("┌────────────────┐         \\    ")
    print(f"| {fruit1} | {fruit2} | {fruit3} |            \\   ")
    print("└────────────────┘         ─────")

    score_this_round = Win_or_lost(slot1, slot2, slot3)
    score += Win_or_lost(slot1, slot2, slot3)

    print("**********************************")
    print(f"Score in this round: {score_this_round}")
    print(f"Curent score: {score}")
    print("**********************************")
    return score

def Win_or_lost(slot1, slot2, slot3):
    score = 0
    if(slot1 == slot2 == slot3):
        print("WICTORIII!!!!")
        score += 10
    elif((slot1 == slot2 or slot1 == slot3 or slot2 == slot3) and (slot1 != slot2 or slot1 != slot3 or slot2 != slot3)):
        print("Good job!")
        score += 2
    else:
        print("You lose!")
        print("Beeter luck next time")
    return score

def slot_mecanic(score):
    slot1 = random.randint(1,6)
    slot2 = random.randint(1,6)
    slot3 = random.randint(1,6)
    
    fruit1 = decoding(slot1)
    fruit2 = decoding(slot2)
    fruit3 = decoding(slot3)

    return print_result(fruit1, fruit2, fruit3, slot1, slot2, slot3, score)


is_going = True

print("*************SLOT MACHINE*************")
input("Preace enter to roll the slot machine")
score = 0
while is_going:
    lever_animation()
    score = slot_mecanic(score)

    end = input("Roll again? (q to quit): ").lower()
    if end == 'q':
        is_going = False
    
