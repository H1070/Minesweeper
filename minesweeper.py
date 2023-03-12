#used medium.com for reference
#import libraries
import random
#set up the function for a grid
#for loop will run the amount of hasttags inputed
def grid_maker(i, h):
    arr = [[0 for row in range(i)] for column in range(i)] #setting the array for the grid based on the input for the height 
    for num in range(h):
        x = random.randint(0,i-1) #set at minus 1 as the array starts at zero otherwise it would be out of range. Using random to decide the plave of # on x axis
        y = random.randint(0,i-1) #Deciding places on the y axis
#the below puts the # in the grid 
        arr[y][x] = '#'
#the below code checks each spot on the grid for a #. anywhere that is not a # is a dash and this is replaced with the count 1
#the code can take a grid of any size becasue it is based on the input from the user on the height
#whne checking the grid references it will be minius 1 to make sure we don't go outside the grid


        if (x >=0 and x <= i-2) and (y >= 0 and y <= i-1):
            if arr[y][x+1] != '#':
                arr[y][x+1] += 1 # center right
        if (x >=1 and x <= i-1) and (y >= 0 and y <= i-1):
            if arr[y][x-1] != '#':
                arr[y][x-1] += 1 # center left
        if (x >= 1 and x <= i-1) and (y >= 1 and y <= i-1):
            if arr[y-1][x-1] != '#':
                arr[y-1][x-1] += 1 # top left
 
        if (x >= 0 and x <= i-2) and (y >= 1 and y <= i-1):
            if arr[y-1][x+1] != '#':
                arr[y-1][x+1] += 1 # top right
        if (x >= 0 and x <= i-1) and (y >= 1 and y <= i-1):
            if arr[y-1][x] != '#':
                arr[y-1][x] += 1 # top center
 
        if (x >=0 and x <= i-2) and (y >= 0 and y <= i-2):
            if arr[y+1][x+1] != '#':
                arr[y+1][x+1] += 1 # bottom right
        if (x >= 1 and x <= i-1) and (y >= 0 and y <= i-2):
            if arr[y+1][x-1] != '#':
                arr[y+1][x-1] += 1 # bottom left
        if (x >= 0 and x <= i-1) and (y >= 0 and y <= i-2):
            if arr[y+1][x] != '#':
                arr[y+1][x] += 1 # bottom center
    for row in arr:
        print("\t".join(str(cell) for cell in row)) #joins the numbers and # into a grid
        print("")

#ask for input from user

i=int(input("Enter height of grid: "))
h = int(input("Enter #s number: "))

#call the function grid maker
grid_maker(i, h)

