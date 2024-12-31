# 3D Cluster Visualizer

A Python-based tool for generating and visualizing 3D clusters using the K-means algorithm. This tool allows you to create 3D coordinate blobs, apply the K-means clustering algorithm, and visualize the results in an interactive 3D plot with MatPlotLib. 

## Features

- Generate random 3D data points.
- Apply the K-means clustering algorithm.
- Visualize clusters in 3D.
- Save and load data from CSV files.

## Installation

Install the necessary dependencies by running the following command:

 
```bash
pip install pandas
pip install numpy
pip install matplotlib
```

## Credit:
The project scope increased, and I was inspired to add a built-from-scratch K-Means clustering algorithm, thanks to the YouTube channel Dataquest. Please check them out for an in-depth and well-explained breakdown of how the K-Means algorithm works.


## Excerpt:
This project started as an exploration of Matplotlib, with the goal of creating a simple 3D scatter plot from x, y, and z coordinates. As the project progressed, I added more features, including K-means clustering and customization options. The project grew from a basic plotter into a tool for simulating and visualizing data clusters, improving with each iteration.

# Future Improvenments:
- Load data from self submitted CSV file .
- Possible implimentation of Plotly with dash, mainly due to MatPlotLib not being as visually asthetic. 
- 2D overview to get a better idea of the K-Means algo. in action with original 3D.
- Cluster legend, and compare true cluster label to simulated clustering.