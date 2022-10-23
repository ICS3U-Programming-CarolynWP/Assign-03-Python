#!/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/10/16
# Asks the user to enter two coordinate points
# And displays the quadrant and how far away both
# Points are from each other.


def main():

    # Title of the coordinate program
    print("Coordinates and their Quadrants\n")

    # User input explanation
    print("The first coordinate will be labeled (x1,y1)")
    print("The second coordinate will be labeled (x2,y2)\n")

    # Input for the two coordinates x1y1 and x2y2
    # First coordinate user input
    print("Enter your first coordinate:\n")

    # x1 user input
    x_coord_1 = input("Enter x1: ")

    # y1 user input
    y_coord_1 = input("Enter y1: ")

    # Line break
    print("\n")

    # Second coordinate user input
    print("Enter your second coordinate:\n")

    # x2 user input
    x_coord_2 = input("Enter x2: ")

    # y2 user input
    y_coord_2 = input("Enter y2: ")

    # Line break
    print("\n")

    # Try Catch statement to make sure the inputs are
    # Integers
    try:
        x_coord_1_integer = int(x_coord_1)
        x_coord_2_integer = int(x_coord_2)
        y_coord_1_integer = int(y_coord_1)
        y_coord_2_integer = int(y_coord_2)

    except Exception:
        print("That is not an integer.")

    else:
        # If...ElseIf...Else statement for the quadrants (1st coordinate pair):
        # 1st Quadrant (If x and y are positive)
        if x_coord_1_integer > 0 and y_coord_1_integer > 0:
            print(
                "Your first coordinate (",
                x_coord_1_integer,
                ",",
                y_coord_1_integer,
                ") is in Quadrant 1\n",
            )

        # 2nd Quadrant (If x is negative and y is positive)
        elif x_coord_1_integer < 0 and y_coord_1_integer > 0:
            print(
                "Your first coordinate (",
                x_coord_1,
                ",",
                y_coord_1,
                ") is in Quadrant 2\n",
            )

        # 3rd Quadrant (If x is negative and y is negative)
        elif x_coord_1_integer < 0 and y_coord_1_integer < 0:
            print(
                "Your first coordinate (",
                x_coord_1_integer,
                ",",
                y_coord_1_integer,
                ") is in Quadrant 3\n",
            )

        # 4th Quadrant(If x is positive and y is negative)
        elif x_coord_1_integer > 0 and y_coord_1_integer < 0:
            print(
                "Your first coordinate (",
                x_coord_1_integer,
                ",",
                y_coord_1_integer,
                ") is in Quadrant 4\n",
            )
        else:
             print(
                "Your first coordinate (",
                x_coord_1_integer,
                ",",
                y_coord_1_integer,
                ") is not in any quadrant\n",
            )
            
        # If...ElseIf...Else statement for the quadrants (2nd coordinate pair):
        # 1st Quadrant (If x and y are positive)
        if x_coord_2_integer > 0 and y_coord_2_integer > 0:
            print(
                "Your second coordinate (",
                x_coord_2_integer,
                ",",
                y_coord_2_integer,
                ") is in Quadrant 1\n",
            )

        # 2nd Quadrant (If x is negative and y is positive)
        elif x_coord_2_integer < 0 and y_coord_2_integer > 0:
            print(
                "Your second coordinate (",
                x_coord_2_integer,
                ",",
                y_coord_2_integer,
                ") is in Quadrant 2\n",
            )

        # 3rd Quadrant (If x is negative and y is negative)
        elif x_coord_2_integer < 0 and y_coord_2_integer < 0:
            print(
                "Your second coordinate (",
                x_coord_2_integer,
                ",",
                y_coord_2_integer,
                ") is in Quadrant 3\n",
            )

        # 4th Quadrant (If x is positive and y is negative)
        elif x_coord_2_integer > 0 and y_coord_2_integer < 0:
            print(
                "Your second coordinate (",
                x_coord_2_integer,
                ",",
                y_coord_2_integer,
                ") is in Quadrant 4\n",
            )
        else:
             print(
                "Your second coordinate (",
                x_coord_2_integer,
                ",",
                y_coord_2_integer,
                ") is not in any quadrant\n",
            )

        # Function to determine how far away x1y1 is from x2y2
        distance_from_x = x_coord_1_integer - x_coord_2_integer
        distance_from_y = y_coord_1_integer - y_coord_2_integer

        # Display the distance from the first coordinate to the second coordinate
        print(
            "Your first coordinate is ",
            distance_from_x,
            "unit(s) away and",
            distance_from_y,
            "unit(s) away from your second coordinate!",
        )


if __name__ == "__main__":
    main()
