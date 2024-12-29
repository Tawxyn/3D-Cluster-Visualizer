import random
import csv
import pandas as pd
import numpy as np

user_input = int(input("Enter the amount of clusters you would like to simulate the generation and k-means algorithm: "))

def generate_blobs(cluster_amount):
    cluster_center = []
    cluster_center_mean = []

    # Try exception to get upper and lower limit from user
    try:    
        total_data_points = int(input("Enter the number of data points you want for each cluster: "))
        lower_limit = float(input("Enter lower limit of cluster center from eachother (whole number): "))
        upper_limit = float(input("Enter upper limit of cluster center from eachother (whole number): "))
    except ValueError:
        print("Please enter a valid whole number for the lower / upper limits.")

    # For loop to generate random variables from lower and upper limit
    for i in range(0, cluster_amount):

        x = random.uniform(float(lower_limit), float(upper_limit))
        y = random.uniform(float(lower_limit), float(upper_limit))
        z = random.uniform(float(lower_limit), float(upper_limit))
        standard_deviation = random.uniform(0.5, 3)
        sub_data = [round(x, 2), round(y, 2), round(z, 2)]
        sub_data_mean = [round(standard_deviation, 2)]
        cluster_center.append(sub_data)
        cluster_center_mean.append(sub_data_mean)

    gaussian_distribution = []

    # Loop through cluster and normalize points based on gaussian dist.
    for i in range(len(cluster_center)):

        # Set cluster location, scale baed on std. dev., and dimensions which is hardcoded as 3D
        points = np.random.normal(loc=cluster_center[i], 
                                  scale=cluster_center_mean[i], 
                                  size=(total_data_points, 3)
        )

        #Append cluster index to each point
        labeled_points = np.hstack([points, np.full((total_data_points, 1), i)])
        gaussian_distribution.append(labeled_points)
    
    # Flatten the list of arrays into one signle 2D Array
    flat_data = np.vstack(gaussian_distribution)

    # Set new 2d array into data frame with correct column headers
    df = pd.DataFrame(flat_data, columns=['x', 'y', 'z', 'cluster'])
    print(df)
    
    # Save data frame to csv file
    df.to_csv("output.csv", index=False)


# Run function
generate_blobs(user_input)

