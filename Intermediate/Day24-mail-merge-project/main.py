PLACEHOLDER = "[name]"

# Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as example_letter:
    letter = example_letter.read()

with open("./Input/Names/invited_names.txt") as name_file:
    lines = name_file.readlines()
    # for each name in invited_names.txt
    # Replace the [name] placeholder with the actual name.
    for line in lines:
        name = line.strip()
        output_letter = letter.replace(PLACEHOLDER, name)
        # Save the letters in the folder "ReadyToSend".
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as output_file:
            output_file.write(output_letter)

