players = []

prompts = []
promptsPerPerson = int(input("How many prompts should each player enter? "))
for player in players:
    for i in range(promptsPerPerson):
        prompt = input("Enter a prompt for the game: ")
        prompts.append(prompt)
