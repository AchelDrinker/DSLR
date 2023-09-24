import csv
import matplotlib.pyplot as plt
import argparse

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

parser = argparse.ArgumentParser(description="Plot pairwise relationships in a dataset.")
parser.add_argument("file_path", type=str, help="Path to the CSV dataset file.")
parser.add_argument("--features", type=str, nargs='+', help="List of features to plot.", default=["Feature1", "Feature2", "Feature3"])

args = parser.parse_args()

features = args.features
data = {feature: [] for feature in features}

with open(args.file_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        valid_row = all(feature in row and is_float(row[feature]) for feature in features)
        if valid_row:
            for feature in features:
                data[feature].append(float(row[feature]))

n = len(features)
fig, axes = plt.subplots(n, n, figsize=(15, 15))

for i, feature_i in enumerate(features):
    for j, feature_j in enumerate(features):
        ax = axes[i, j]
        if i == j:
            ax.hist(data[feature_i], bins=20, alpha=0.5)
        else:
            ax.scatter(data[feature_j], data[feature_i], alpha=0.5)
        if i == n - 1:
            ax.set_xlabel(feature_j)
        if j == 0:
            ax.set_ylabel(feature_i)

plt.show()
