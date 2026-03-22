PLACEHOLDER = "[name]"

with open("Project\\Input\\names\\Names.txt") as names_file:
        names = names_file.readlines()
        print(names)


with open("Project\\Input\\Letters\\starting_letters.txt") as letter_file:
        letter_contents = letter_file.read()
        for name in names:
                name = name.strip()
                new_letter = letter_contents.replace(PLACEHOLDER, name)
                with open(f"Project\\Output\\ReadyToSend\\letter_for_{name}.txt", mode="w") as completed_letter:
                        completed_letter.write(new_letter)
