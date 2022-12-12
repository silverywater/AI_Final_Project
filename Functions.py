import math

# List of required functions
# Pythagorean distance #
# trail steepness #
# trail length
# distance to goal (straight line distance)
# net elevation change of trail #
# max continuous elevation change #
#   check continuity of elevation change fnc #


# input parameters ==========================================================================
grid_square_size = 5 #5m in our presentation

start_elevation = 0 #this should be passed in from the map
goal_elevation = 100 #this should be passed in from the map

# start_x = 
# start_y = 

# end input parameters =======================================================================

# variable initialization ********************************
incline_polarity = 1 # -1 = , 1 = same direction as before
old_incline_polarity = 1

trail_net_elevation_start = start_elevation
trail_net_elevation_end = goal_elevation

continuous_elevation_segment_start = start_elevation #not sure if we need these yet
continuous_elevation_segment_end = start_elevation
longest_continuous_elevation_segment = 0 #def need to initialize this one


# end variable initialization ****************************

# Note: the following few variables USUALLY (not always) refer to the current move/step being made, in some cases I just use them as placeholders and will specify
# x1 = start array position
# x2 = end array position
# y1 = start height
# y2 = end height


# this function takes two input numbers (the x and y values from an array) and outputs a number (distance)
def pythagorean_distance(x1, x2, y1, y2):
    return math.sqrt((((x2 - x1)*grid_square_size)**2) + ((y2 - y1)**2) )


# function takes two heights at and outputs the angle relative to the horizon
def trail_steepness(x1, x2, y1, y2):
    return math.atan( (y2 - y1) / ((x2 - x1)*grid_square_size) )


# making the assumption that the pythagorean distance is used for trail length, not just the motion in the x/y directions
# consider doing both (passed as an input)
def trail_length():
    temp = 0

def sld_to_goal():
    temp1 = 0


# one assumption about this is that we always want to start low and finish at high elevation
# useful for determining if you dip below the trail's starting elevation or reach higher than the trail's goal elevation
# this should be called at each step/move - y1 and y2 refer to the current steps

# can use a list of all the steps taken to get to goal, then just take min/max of that list
def trail_net_elevation_change(y1, y2):
    if y1 < trail_net_elevation_start:
        trail_net_elevation_start = y1

    if y2 > trail_net_elevation_end:
        trail_net_elevation_end = y2

    return trail_net_elevation_end - trail_net_elevation_start


# takes the current move and verifies if this move is in the same up/down direction as the previous move
# if it is in the same direction, it takes the difference between the 'height resulting by moving', and the 'start of this continuous run'
# this should likely be called at each step/move

# can use a list for calculating this as well
def max_continuous_elevation_change(y1, y2):
    continuous_elevation_segment_end = y2

    if not check_incline_continuity(y1, y2):
        continuous_elevation_segment_start = y1
    
    curr_continuous_elevation_change = abs(continuous_elevation_segment_end - continuous_elevation_segment_start) #note: abs gives only net change, not sure about pos vs neg changes

    if curr_continuous_elevation_change > longest_continuous_elevation_segment:
        longest_continuous_elevation_segment = curr_continuous_elevation_change

    return longest_continuous_elevation_segment


# helper function to max_continuous_elevation_change()
# checks that the move is still in the same vertical direction as the previous move
def check_incline_continuity(y1, y2):
    incline_continuity = False
    old_incline_polarity = incline_polarity

    #checks elevation change of step (if y2 < y1, elevation decreased)
    if y2 < y1:
        incline_polarity = -1
    else: 
        incline_polarity = 1
    
    #check if the previous elevation change was the same as the current
    if old_incline_polarity == incline_polarity:
        incline_continuity = True
    else:
        incline_continuity = False

    return incline_continuity






# reward structure attempt
def calc_reward(x1, x2, y1, y2, penal_angle, reward_size):
    reward = 0
    if trail_steepness(x1, x2, y1, y2) > penal_angle:
        reward = reward - reward_size
    else:
        reward = reward + reward_size
    return reward


def main():
    print(pythagorean_distance(5,22,40))
    print(trail_steepness(2,4,10,50))

# Using the special variable 
# __name__
if __name__=="__main__":
    main()
