import random

vocabulary = ["mentor", "resume", "script", "object", "syntax"]
target = random.choice(vocabulary)

correct_letters = []
wrong_count = 0
max_wrong = 6

print(">>> HORIZON TECHX TASK 1: HANGMAN <<<")
print(f"Hint: Tech/Programming word with {len(target)} letters")

while wrong_count < max_wrong:
    progress = ""
    for char in target:
        if char in correct_letters:
            progress += char
        else:
            progress += "_"
    
    print(f"\nProgress: {progress}")
    print(f"Mistakes: {wrong_count}/{max_wrong}")
    
    if progress == target:
        print(f"\nSuccess! You decoded: {target}")
        print("Task 1 Completed ✅")
        break
    
    player_input = input("Type one letter: ").lower()
    
    if not player_input.isalpha() or len(player_input) != 1:
        print("Only single letters allowed!")
        continue
    
    if player_input in correct_letters:
        print("Already tried that one.")
        continue
        
    if player_input in target:
        correct_letters.append(player_input)
        print("Nice! That letter is in the word.")
    else:
        wrong_count += 1
        print(f"Nope! Wrong guesses: {wrong_count}")

else:
    print(f"\nOut of chances! Word was: {target}")
    print("Good attempt on Task 1")

print("--- End of Game ---")
