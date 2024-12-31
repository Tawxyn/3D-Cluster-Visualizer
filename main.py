import random
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    
    # Save data frame to csv file
    df.to_csv("output.csv", index=False)
    
    return df

# Centroid creation
def random_centroids(data, user_input):
    centroids = []
    for i in range(user_input):
        # Grab a sample row of values and turn into float value from list of data from data frame 
        centroid = data.apply(lambda x: float(x.sample().iloc[0]))
        centroids.append(centroid)
    return pd.concat(centroids, axis=1)

# Distance formula / cluster assignment 
def get_labels(data, centroids):
    distances = centroids.apply(lambda x: np.sqrt(((data - x) ** 2).sum(axis=1)))
    return distances.idxmin(axis=1)

# Create new centroids by group
def new_centroids(data, labels):
    return data.groupby(labels).mean().T

# Plot clusters
def plot_clusters_3d(fig, ax, data, labels, centroids, iteration): 
    
    # Clear the axes to redraw the plot
    ax.clear() 
    ax.set_title(f'Iteration {iteration}')
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_zlabel('Z', fontsize=12)

    # Plot data points
    scatter = ax.scatter(
        data.iloc[:, 0], # x-cords
        data.iloc[:, 1], # y-cords
        data.iloc[:, 2], # z-cords
        c = labels,
        cmap = 'viridis',
        s = 8,
        alpha = 0.5
    )
    # Plot centroids
    ax.scatter(
        centroids.iloc[0, :], # x-cords
        centroids.iloc[1, :], # y-cords
        centroids.iloc[2, :], # z-cords
        c = 'red',
        s = 25,
        alpha = 1
    )

    # Add grid for better visibility
    ax.grid(True, linestyle='--', alpha=0.7)
            
    plt.draw()
    plt.pause(0.5)  



# Main function to execute clustering
def main():
    user_input = int(input("Enter the number of clusters: "))
    data = generate_blobs(user_input)
    if data is None:
        return

    # Remove cluster label for K-Means algorithm
    data = data.drop('cluster', axis=1)
    
    # Set max iter, and centroid data frame
    max_iterations = 1000
    centroids = random_centroids(data, user_input)
    old_centroids = pd.DataFrame()
    iteration = 1

    # Create figure for plot and add 3D subplot
    fig = plt.figure(figsize=(11, 8))
    ax = fig.add_subplot(111, projection='3d')

    while iteration < max_iterations:
        # Save previous centroids
        old_centroids = centroids
        # Assign labels
        labels = get_labels(data, centroids)
        # Calculate new centroids
        centroids = new_centroids(data, labels)
        # Plot clusters
        plot_clusters_3d(fig, ax, data, labels, centroids, iteration)
         # Check if centroids have converged
        if centroids.equals(old_centroids):
            print(f"K-Means converged in {iteration} iterations.")
            break  

        iteration += 1

    if iteration == max_iterations:
        print(f"K-Means reached the maximum iterations ({max_iterations}).") 

    plt.show()

# Run the main function
if __name__ == '__main__':
    main()

