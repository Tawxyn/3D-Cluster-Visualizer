import random
import csv
import pandas as pd

user_input = int(input("Enter amount of data points you would like generated " + 
                    "into the csv file: "))
def generate_blobs(generation_target):
    data_set = []

    try:
        lower_limit = int(input("Enter lower limit of cluster (whole number): "))
        upper_limit = int(input("Enter upper limit of cluster (whole number): "))
    except ValueError:
        print("Please enter a valid whole number for the lower / upper limits.")

    for i in range(1, generation_target):
        i =+ 1

        x = random.randint(int(lower_limit), int(upper_limit))
        y = random.randint(int(lower_limit), int(upper_limit))
        z = random.randint(int(lower_limit), int(upper_limit))
        sub_data = [x, y, z]
        data_set.append(sub_data)

    df = pd.DataFrame(data_set)
    print(df)

generate_blobs(user_input)