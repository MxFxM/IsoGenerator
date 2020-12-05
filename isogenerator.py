import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#
# SETTINGS AND OPTIONS
#
INPUT_FILENAME = "testfile"
X_MIN = 0
X_MAX = 250
X_COUNT = 10

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

# store the lines in a list
lines = []
lines.append([input_data["black_x"], input_data["black_y"], input_data["black_z"]])
lines.append([input_data["blue_x"], input_data["blue_y"], input_data["blue_z"]])
lines.append([input_data["grey_x"], input_data["grey_y"], input_data["grey_z"]])
lines.append([input_data["red_x"], input_data["red_y"], input_data["red_z"]])
lines.append([input_data["green_x"], input_data["green_y"], input_data["green_z"]])
lines.append([input_data["pink_x"], input_data["pink_y"], input_data["pink_z"]])
lines = np.array(lines)
print(lines)

# create the slices in x-direction as plains in y-h direction
for x in range(X_MIN, X_MAX, (X_MAX-X_MIN)//X_COUNT):
    print(f"x={x}")
    # note: for a constant x, now draw the graph in y-h directions
    # note: linearize the data between line points
    # note: show the crossing of the linearized line between two points and this plane

    # 1. get the line between every point in a line
    for n in range(len(lines[0][0])):
        pass
        # 2. is the line (between the points) crossing with the plane
        # 3. if so, store the point in a list of points
    # 4. order the list using the y-coordinate
    # 5. connect the ordered points
    # 6. plot the new line
    plt.plot()
plt.show()