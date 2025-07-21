try:
    with open("sample.txt", "r") as file:
        sample = file.read()
        print(sample)
except FileNotFoundError:
    print("Error: The File 'sample.txt' was not found.")