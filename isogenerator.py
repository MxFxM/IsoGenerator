import pandas as pd
import matplotlib.pyplot as plt

#
# SETTINGS AND OPTIONS
#
INPUT_FILENAME = "testfile"
OPTION_PRINT_DATA_INPUT = False
OPTION_PLOT_INPUT_DIAGRAM = False
OPTION_PLOT_3D_INPUT_DIAGRAM = True

#
# CODE
#

# read input file
input_data = pd.read_csv(f"./input_data/{INPUT_FILENAME}.csv", header=0, sep=';')
if OPTION_PRINT_DATA_INPUT:
    print(input_data.head())

# plot input data
if OPTION_PLOT_INPUT_DIAGRAM:
    plt.plot(input_data["black_x"], 150-input_data["black_y"], color="black", label="black")
    plt.plot(input_data["blue_x"], 150-input_data["blue_y"], color="blue", label="blue")
    plt.plot(input_data["grey_x"], 150-input_data["grey_y"], color="grey", label="grey")
    plt.plot(input_data["red_x"], 150-input_data["red_y"], color="red", label="red")
    plt.plot(input_data["green_x"], 150-input_data["green_y"], color="green", label="green")
    plt.plot(input_data["pink_x"], 150-input_data["pink_y"], color="pink", label="pink")
    plt.legend(loc="best")
    plt.show()

# plot input data on a 3d scatter plot
if OPTION_PLOT_3D_INPUT_DIAGRAM:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(input_data["black_x"], 150-input_data["black_y"], input_data["black_z"], color="black", marker='o')
    ax.scatter(input_data["blue_x"], 150-input_data["blue_y"], input_data["blue_z"], color="blue", marker='o')
    ax.scatter(input_data["grey_x"], 150-input_data["grey_y"], input_data["grey_z"], color="grey", marker='o')
    ax.scatter(input_data["red_x"], 150-input_data["red_y"], input_data["red_z"], color="red", marker='o')
    ax.scatter(input_data["green_x"], 150-input_data["green_y"], input_data["green_z"], color="green", marker='o')
    ax.scatter(input_data["pink_x"], 150-input_data["pink_y"], input_data["pink_z"], color="pink", marker='o')
    ax.set_xlabel("X-Axis")
    ax.set_ylabel("Y-Axis")
    ax.set_zlabel("Height")
    plt.show()
