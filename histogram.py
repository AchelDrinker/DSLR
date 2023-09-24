import csv
import matplotlib.pyplot as plt
import argparse

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


parser = argparse.ArgumentParser(description="Plot histograms based on a CSV file.")
parser.add_argument("file_path", type=str, help="Path to the CSV dataset file.")
args = parser.parse_args()


houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
courses = ["Arithmancy", "Astronomy", "Herbology", "Defense Against the Dark Arts", "Divination", "Muggle Studies", "Ancient Runes", "History of Magic", "Transfiguration", "Potions", "Care of Magical Creatures", "Charms", "Flying"]
data = {house: {course: [] for course in courses} for house in houses}


with open(args.file_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        house = row['Hogwarts House']
        if house in houses:
            for course in courses:
                if is_float(row[course]):
                    data[house][course].append(float(row[course]))


for course in courses:
    plt.figure(figsize=(10, 6))
    for house in houses:
        if data[house][course]:
            plt.hist(data[house][course], alpha=0.5, label=house)
    plt.title(f"{course} Distribution by House")
    plt.xlabel("Scores")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()
