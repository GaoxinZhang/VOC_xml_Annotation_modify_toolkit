import matplotlib.pyplot as plt
import numpy as np


# draw the picture
def draw(Curve_one):
    plt.figure()
    plot1, = plt.plot(Curve_one[0], Curve_one[1], 'co-', linewidth=2.0, markersize=10.0)
    # set X axis
    plt.xlim([0.5, 1.05])
    plt.xticks(np.linspace(0.5, 1.0, 6))
    plt.xlabel("Precision", fontsize="x-large")
    # set Y axis
    plt.ylim([0.1, 1.05])
    plt.yticks(np.linspace(0.1, 1.0, 10))
    plt.ylabel("Recall", fontsize="x-large")
    # set figure information
    plt.title("Precision --- Recall", fontsize="x-large")
    plt.legend([plot1], ("Curve_one"), loc="lower left",
               numpoints=1)
    plt.grid(True)
    # draw the chart
    plt.show()


# main function
def main():

    # Curve
    Curve = [
        (0.999200, 0.998067, 0.995260, 0.989679, 0.976811, 0.937295, 0.849400, 0.751620, 0.667903, 0.599113, 0.542607),
        (0.107668, 0.262707, 0.436613, 0.607831, 0.771336, 0.904606, 0.968826, 0.989191, 0.996214, 0.998741, 0.999759)]

    # Call the draw function
    draw(Curve)


# function entrance
if __name__ == "__main__":
    main()