guess = input("Guess a letter: ").upper()
guessed_letters + = guess
secret_word = "PYTHON"
spins_left = 6
print(f"Sorry,'{guess}' is not in the puzzle")
print("========================================")
display += letter +""
while spins_left > 0:
    print(f"Spins remaining: {spins_left}")
elif guess in guessed_letters:



if spins_left == 0:
    print(f"\nGAME OVER! The secret word was: {secret_word}")