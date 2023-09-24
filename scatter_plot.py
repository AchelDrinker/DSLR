import csv
import matplotlib.pyplot as plt
import argparse 

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

parser = argparse.ArgumentParser(description="Generate scatter plot from dataset.")
parser.add_argument("file_path", type=str, help="Path to the CSV dataset file.")
parser.add_argument("--features", type=str, nargs='+', help="List of features to plot.", default=["Feature1", "Feature2"])

args = parser.parse_args()

features = args.features


if len(features) != 2:
    print("Please provide exactly two features for scatter plot.")
    exit(1)

data = {feature: [] for feature in features}

with open(args.file_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        valid_row = all(feature in row and is_float(row[feature]) for feature in features)
        if valid_row:
            for feature in features:
                data[feature].append(float(row[feature]))

plt.scatter(data[features[0]], data[features[1]])
plt.title(f"Scatter Plot of {features[0]} vs {features[1]}")
plt.xlabel(features[0])
plt.ylabel(features[1])
plt.show()
