TRUNCATE_LENGTH = 20

def truncate_feature_name(feature, max_length=20):
    if len(feature) > max_length:
        return feature[:max_length - 4] + "... "
    else:
        return feature.ljust(max_length, ' ')
    
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

import csv
import argparse
import math

def describe(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = {h: [] for h in header}
        contains_numeric = {h: False for h in header}

        stats = ["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]

        for row in reader:
            for h, value in zip(header, row):
                if is_float(value):  # Remplacement ici
                    data[h].append(float(value))
                    contains_numeric[h] = True

        features_stats = {}

        for feature in header:
            if not contains_numeric[feature]:
                continue
            nums = data[feature]
            if not nums:
                continue

            n = len(nums)
            mean = sum(nums) / n
            std = math.sqrt(sum((x - mean) ** 2 for x in nums) / n)
            nums.sort()
            min_val = nums[0]
            q25 = nums[int(n * 0.25)]
            median = nums[int(n * 0.5)]
            q75 = nums[int(n * 0.75)]
            max_val = nums[-1]

            features_stats[feature] = [n, mean, std, min_val, q25, median, q75, max_val]

        print(f"{'':<{TRUNCATE_LENGTH}}", end='')
        for feature in header:
            if contains_numeric[feature]:
                truncated_feature = truncate_feature_name(feature, TRUNCATE_LENGTH)
                print(f"{truncated_feature:<{TRUNCATE_LENGTH}}", end='')
        print()

        for i, stat in enumerate(stats):
            print(f"{stat:<{TRUNCATE_LENGTH}}", end='')
            for feature in header:
                if feature in features_stats:
                    val = features_stats[feature][i]
                    print(f"{val:<{TRUNCATE_LENGTH}.2f}", end='')
            print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Describe dataset.")
    parser.add_argument("file_path", type=str, help="Path to the CSV dataset file.")
    args = parser.parse_args()

    describe(args.file_path)
