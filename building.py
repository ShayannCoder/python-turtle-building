import turtle 

t = turtle.Turtle() # Create the turtle object
screen = turtle.Screen() # Create a screen object so that we can manipulate the dimentions of the screen

# Changes the size of the window to max
screen.screensize()
screen.setup(width = 1.0, height = 1.0)

t.speed(0) # Set turtle speed to max
screen.tracer(0) # Turn turtle animation off 


# Set the world coordinates so that the turtle starts from the bottom-left
screen.setworldcoordinates(0, 0, screen.window_width(), screen.window_height())

BUILDING_WIDTH = 500
BUILDING_HEIGHT = 650
BUILDING_COLOR = "#6c655e"
WINDOW_COLOR = "#303b44"
WINDOW_LENGTH = 50
WINDOW_WIDTH = 30
COLOR_TOGGLE = True

# Creating an origin point(bottom-left of the building) to make drawing easier
ORIGIN_X, ORIGIN_Y = 450, screen.window_height() // 8

# Creating (x,y) poin to identify the starting place of the windows
WINDOWS_STARTING_X, WINDOWS_STARTING_Y = ORIGIN_X + 20, ORIGIN_Y + 120

window_positions = [] # A list to store the position of the windows so that we can redraw over them later to make the effect of animation


# Depending on the length and the width passed to the function it draws either a rectangle or a square
def draw_rectangle_square(length, width): 
    for _ in range(2):
        t.fd(length)
        t.left(90)
        t.fd(width)
        t.left(90)


# This function will only be used for creating the windows needed for the patterns, initial windows and other shapes will be made by the above function
def draw_windows(length, width, color):
    
    t.color(BUILDING_COLOR, color)
    t.begin_fill()
    for _ in range(2):
        t.fd(length)
        t.left(90)
        t.fd(width)
        t.left(90)
    t.end_fill()


# This function creates a cloud
def draw_cloud(x, y, size=30):
    t.up()
    t.goto(x, y)
    t.down()
    t.color("white")
    t.begin_fill()
    t.circle(size)
    t.end_fill()

    t.up()
    t.goto(x + size, y)
    t.down()
    t.begin_fill()
    t.circle(size * 1.2) # Slightly larger circle to give a fluffy look
    t.end_fill()

    t.up()
    t.goto(x + size * 2, y)
    t.down()
    t.begin_fill()
    t.circle(size)
    t.end_fill()


# Creates the clouds when called
def draw_clouds():
    cloud_positions = [
        (50, 500),
        (300, 600),
        (700, 800),
        (1050, 450),
        (1300, 650)
    ]
    
    for pos in cloud_positions:
        draw_cloud(pos[0], pos[1])


# Creating the environment 
def environment():
    screen.bgcolor("skyblue")
    t.color("green")

    t.up()
    t.goto(-10, -20)
    t.down()

    #making the green ground
    t.begin_fill()
    t.goto(screen.window_width(), -20)
    t.goto(screen.window_width(), ORIGIN_Y)
    t.goto(-10, ORIGIN_Y)
    t.goto(-10,-20)
    t.end_fill()

    # Draw the grey road
    road_y_start = ORIGIN_Y - 10    # Starting point of the road
    road_y_end = ORIGIN_Y - 110    # End point of the road

    t.up()
    t.color("grey")
    t.goto(-10, road_y_start)
    t.down()

    # Draw the road from left to right
    t.begin_fill()
    t.goto(screen.window_width(), road_y_start)
    t.goto(screen.window_width(), road_y_end)
    t.goto(-10, road_y_end)
    t.goto(-10, road_y_start)
    t.end_fill()

    # Draw white stripes in the center of the road
    stripe_length = 30
    stripe_spacing = 50
    t.color("white")
    t.width(5)  # Thickness of the stripe

    t.up()
    y_stripe = (road_y_start + road_y_end) / 2  # Center line of the road

    # Draw stripes along the road width
    for x in range(0, screen.window_width(), stripe_length + stripe_spacing):
        t.goto(x, y_stripe)
        t.down()
        t.forward(stripe_length)
        t.up()

    draw_clouds()


def outline_of_building():

    t.width(2)
    
    t.color(BUILDING_COLOR)
    t.up()
    # Go to the starting position of the building 
    t.goto(ORIGIN_X, ORIGIN_Y)
    t.down()

    draw_rectangle_square(BUILDING_WIDTH, BUILDING_HEIGHT) # Draws the outline of the building
    draw_rectangle_square(BUILDING_WIDTH, 100) # Draws the outline of the bottom part of the building


# Draws the windows of the bottom part of the building
def draw_bottom_windows(): 
    bottom_windows_length = 100
    bottom_windows_width = 100
    for i in range(5):
        t.fillcolor(WINDOW_COLOR)
        t.begin_fill()

        if i == 4: # For the last part where the door is located
            t.fillcolor(BUILDING_COLOR)

        draw_rectangle_square(bottom_windows_length, bottom_windows_width)
        t.fd(100)
        t.end_fill()


# Creating the door in the bottom right
def draw_door():
    door_x_position = ORIGIN_X + 420

    t.goto(door_x_position, ORIGIN_Y)
    t.color("black")
    t.begin_fill()
    draw_rectangle_square(60, 80)
    t.end_fill()


# Function to create the thick frame of the building
def thick_frame():
    # Returning to the origin cordinates
    t.up()
    t.color(BUILDING_COLOR)
    t.goto(ORIGIN_X, ORIGIN_Y)
    t.down()

    # Creating the thick frame of the building (left-side)
    t.begin_fill()
    draw_rectangle_square(20, BUILDING_HEIGHT)
    t.end_fill()

    t.goto(ORIGIN_X, ORIGIN_Y + 630) # Goes to the top-left of the building, and builds the (top-side)
    t.begin_fill()
    draw_rectangle_square(BUILDING_WIDTH, 20)
    t.end_fill()

    t.goto(ORIGIN_X + 480, ORIGIN_Y + BUILDING_HEIGHT) # Goes to top-right of the building, and builds the (right-side)
    t.right(90)
    t.begin_fill()
    draw_rectangle_square(BUILDING_HEIGHT, 20)
    t.end_fill()

    # Creating the thicker portion of the building above the bottom windows
    t.up()
    t.goto(ORIGIN_X, ORIGIN_Y + 100)
    t.down()
    t.begin_fill()
    t.left(90)
    draw_rectangle_square(BUILDING_WIDTH, 20)
    t.end_fill()


# This function is used to draw the initial upper windows of the building before the patterns and designs between them
def draw_upper_windows():
    rows = 16
    colums = 10
    index = 0 # Index for the position of each (x, y) pair in the windows_positions list
    
    t.color(BUILDING_COLOR, WINDOW_COLOR) # Second argument will be used for the fill color
    t.goto(WINDOWS_STARTING_X, WINDOWS_STARTING_Y) # Going to the start of creating the windows
    
    for row in range(rows):
        for colum in range(colums):
            
            window_positions.append(t.pos()) # Save the position of each window in a list to create the light patterns later
            window_positions[index] = list(window_positions[index]) # Changing the given (x, y) coordinates from a tuple to a list

            # Rounding the numbers to be precise
            window_positions[index][0] = float(round(window_positions[index][0], 2))
            window_positions[index][1] = float(round(window_positions[index][1], 2))
            index += 1 # Increment the index by one after each iteration to access the next element(x, y) in the list

            # Beginning to draw the windows
            t.begin_fill()
            if colum == colums - 1: # Special case for the last windows on the right
                draw_rectangle_square(10, WINDOW_WIDTH)
            else:
                draw_rectangle_square(WINDOW_LENGTH, WINDOW_WIDTH)
                t.fd(WINDOW_LENGTH)
            t.end_fill()
            
        t.up()
        t.goto(WINDOWS_STARTING_X, WINDOWS_STARTING_Y + (row + 1) * WINDOW_WIDTH) # Moving to the next row
        t.down()


# This function removes the windows that the three rectangular designs are drawn over in the building so that when we add light patterns the three rectangular designs are not altered
def remove_window_at_position(pos):
    global window_positions # Making windows_positions global so that we can make changes to it inside the function

    x, y = pos # Stores x value in x, and y value in y

    # Rounding up the two vlaues so that we can get an exact match to the values stored in the list
    x = round(x, 2)
    y = round(y, 2)
    
    if [x, y] in window_positions:
            window_positions.remove([x, y])
           

# Creates the rectangle between the windows based on the rows and colums and the design passed to the function
def create_design_between_windows(rows, columns, design):
    
    for row in range(rows):
        for column in range(columns):
            remove_window_at_position(t.pos())
                
            t.begin_fill()
            t.fillcolor(BUILDING_COLOR)
            draw_rectangle_square(WINDOW_LENGTH, WINDOW_WIDTH)
            t.end_fill()
            t.fd(WINDOW_LENGTH)

        # Depending on the design the turtle moves to the next designated row, the leftmost rectange is the first and so on
        if design == 1:
            t.goto(WINDOWS_STARTING_X + 50, (WINDOWS_STARTING_Y + 60) + (row + 1)  * WINDOW_WIDTH)
        elif design == 2:
            t.goto(WINDOWS_STARTING_X + 200, (WINDOWS_STARTING_Y + 120) + (row + 1)  * WINDOW_WIDTH)
        else:
            t.goto(WINDOWS_STARTING_X + 300, (WINDOWS_STARTING_Y + 120) + (row + 1)  * WINDOW_WIDTH)


def apply_design_between_windows():

    # Creating the left-most design
    t.up()
    t.goto(WINDOWS_STARTING_X + 50, WINDOWS_STARTING_Y + 60) 
    t.down()
    create_design_between_windows(12, 2, 1)

    # Creating the middle design
    t.up()
    t.goto(WINDOWS_STARTING_X + 200, (WINDOWS_STARTING_Y + 120))
    t.down()
    create_design_between_windows(10, 1, 2)

    # Creating the right-most design
    t.up()
    t.goto(WINDOWS_STARTING_X + 300, (WINDOWS_STARTING_Y + 120))
    t.down()
    create_design_between_windows(12, 2, 3)
    

# Gets the pattern, the color theme and the pattern number which changes the animation from the user
def get_pattern():
    title_1 = "Column or Row Based Pattern?"
    message_1 = "1 for column based pattern and 2 for row based pattern"

    # This first loop gets the column or row based pattern from the user
    while True:
        try:
            user_choice = turtle.textinput(title_1, message_1).lower()
            if (user_choice != "1") and (user_choice != "2"):
                continue
            break
        except AttributeError:
            continue

    title_2 = "Chose the color theme!"
    message_2 = "Write two colors and seperate them with a space"

    # This loop gets the two colors from the user
    while True:
        try:
            user_color = turtle.textinput(title_2, message_2).lower()
            first_color, second_color = user_color.split(" ")
            color_theme = [first_color, second_color]
            break
        except ValueError:
            message_2 = "Make sure to type two colors and seperate them with a space"
            continue
        except AttributeError:
            continue
        
    title_3 = "Choose a number 1 through 5"
    message_3 = "Depending on the the number you provide the pattern will be different!"

    # This loop gets the number 1-5 from the user that is later used in the patterns to give us different pattern animations
    while True:
        try:
            user_number = int(turtle.textinput(title_3, message_3))
            if (user_number > 5) or (user_number < 1):
                message_3 = "Please choose a number 1 through 5"
                continue
            break
        except AttributeError:
            continue
    try:
        return user_choice, color_theme, user_number
    except UnboundLocalError:
        pass

       
# Creates a pattern based on columns
def pattern_1(color_theme, pattern_number):
    global COLOR_TOGGLE
    
    for position in window_positions:
        x, y = position[0], position[1] # Stores the x and y values of each window in x and y respectively

        column_number = (x - ORIGIN_X) // WINDOW_LENGTH # This equation gives us the column number depending on the x coordinate

        """COLOR_TOGGLE is used to toggle the colors for each time the animation repeats, initially it's value is set to true 
        but later in the animate function we reverse its value each time so it gives us the pattern but in opposite coloring each iteration"""

        if COLOR_TOGGLE:
            # The pattern number is given by the user and this is what allows us to have multiple types of animations within the column and row bassed pattern
            if column_number  % pattern_number == 0: 
                color = color_theme[0]
            else:
                color = color_theme[1]
        else:
            if column_number % pattern_number == 0:
                color = color_theme[1]
            else:
                color = color_theme[0]
        t.up()
        t.goto(x, y)
        t.down()

        if x == (ORIGIN_X + 470): # Special case of the last window in each row
            draw_windows(10, WINDOW_WIDTH, color)
        else:
            draw_windows(WINDOW_LENGTH, WINDOW_WIDTH, color)


# Creates a pattern based on rows
def pattern_2(color_theme, pattern_number):
    global COLOR_TOGGLE

    for position in window_positions:
        x, y = position[0], position[1]
        
        # Calculate the row number based on the y coordinate
        row_number = int((y - WINDOWS_STARTING_Y) / WINDOW_WIDTH)
        
        # Alternate colors based on row_number % pattern_number
        if COLOR_TOGGLE:
            if row_number % pattern_number == 0:
                color = color_theme[0]
            else:
                color = color_theme[1]
        else:
            if row_number % pattern_number == 0:
                color = color_theme[1]
            else:
                color = color_theme[0]

        # Move to position and draw the window with the selected color
        t.up()
        t.goto(x, y)
        t.down()
        
        if x == (ORIGIN_X + 470): # Special case of the last window in each row
            draw_windows(10, WINDOW_WIDTH, color)
        else:
            draw_windows(WINDOW_LENGTH, WINDOW_WIDTH, color)



def animate(pattern, color_theme, pattern_number):
    # toggle is used to toggle the animation and its value is reversed every time it repeates so we get different coloring in the pattern
    toggle = True

    def animation_step():
        global COLOR_TOGGLE
        nonlocal toggle

        if  pattern == "1":
            if toggle:
                pattern_1(color_theme, pattern_number)
                # The value of COLOR_TOGGLE is reversed so we get opposite coloring in the next iteration
                COLOR_TOGGLE = not COLOR_TOGGLE
            else:
                pattern_1(color_theme, pattern_number)
        else:
            if toggle:
                pattern_2(color_theme, pattern_number)
                COLOR_TOGGLE = not COLOR_TOGGLE
            else:
                pattern_2(color_theme, pattern_number)
        
        toggle = not toggle
        screen.update() # Refreshes the screen after the code is executed
        screen.ontimer(animation_step, 50) # Repeates the animation_step function every 200ms
        
    animation_step()


def main():
    t.hideturtle() # Hides the turtle
    environment() # Creates the initial environment
    outline_of_building() # Creates the initial thin frame of the building
    draw_bottom_windows() # Creates the bottom windows plus the place where the door is placed
    draw_door() # Creates the door
    thick_frame() # Creates the thick frame of the building
    draw_upper_windows() # Creates the remaining windows in the upper portion of the building
    apply_design_between_windows() # Creates the three rectangles between the windows of the building
    pattern, color_theme, pattern_number = get_pattern() # Gets the pattern and color theme from the user
    animate(pattern, color_theme, pattern_number) # Animates the colors
    
    screen.mainloop()
    

if __name__ == "__main__":
    main()


