import math


# ***************************************************************************************************************************
# ***************************************************************************************************************************

# metrics to be collected for each run - will need more operation on these metrics to get metrics across ALL runs
# likely can pass the output list (metrics[]) into another list, and perform operations through a similar process as done here

# ***************************************************************************************************************************
# ***************************************************************************************************************************

steps = []
steps_example = [[0, 0, 20, 1], [0, 1, 22, 1], [1, 1, 24, 0], [1, 2, 30, 0], [1, 3, 40, 1]]


# steps legend:
# [0] = x coordinate
# [1] = y coordinate
# [2] = elevation
# [3] = on-trail indicator (1 -> on-trail, 0 -> off-trail)


def calc_run_metrics(steps):
    metrics = [0, 0, -1, 0, 0, 0]
    # NOTE: a step is only considered when moving from one space to the next, the start position is not a step by itself
    # remove the (-1)s in the metrics[] to count the start position as a step

    # metrics legend (metrics per run):
    # [0] = number of moves
    # [1] = net elevation
    # [2] = count of 2m steps
    # [3] = count of 5m steps
    # [4] = count of 10m steps
    # [5] = count of on-trail steps

    metrics[0] = len(
        steps) - 1  # dropping by one since a 'step' is considered a move from one spot to the next, start position is not a step

    # iterate through all the values of the steps[] list
    for i in range(metrics[0]):

        # Net Elevation
        metrics[1] = metrics[1] + abs(steps[i][2] - steps[i + 1][2])

        # Count of 2m, 5m, 10m steps
        if (steps[i][2] - steps[i - 1][2]) <= 2:
            metrics[2] = metrics[2] + 1

        elif (steps[i][2] - steps[i - 1][2]) <= 5:
            metrics[3] = metrics[3] + 1

        else:
            metrics[4] = metrics[4] + 1

        # Count of on-trail steps
        if steps[i][3] == 1:
            metrics[5] = metrics[5] + 1

    # testing
    # print("move: "+str(i))
    # print("net elevation: "+str(metrics[1]))
    # print("2m: "+ str(metrics[2]) + " - 5m: "+ str(metrics[3])+ " - 10m: "+ str(metrics[4]))
    # print("on-trail steps: "+str(metrics[5])+"\n")

    return metrics


# **********************
# **********************

# old code

# **********************
# **********************


# List of required functions
# Pythagorean distance #
# trail steepness #
# trail length
# distance to goal (straight line distance)
# net elevation change of trail #
# max continuous elevation change #
#   check continuity of elevation change fnc #


# input parameters ==========================================================================
# grid_square_size = 5 #5m in our presentation

# start_elevation = 0 #this should be passed in from the map
# goal_elevation = 100 #this should be passed in from the map

# # start_x =
# # start_y =

# # end input parameters =======================================================================

# # variable initialization ********************************
# incline_polarity = 1 # -1 = , 1 = same direction as before
# old_incline_polarity = 1

# trail_net_elevation_start = start_elevation
# trail_net_elevation_end = goal_elevation

# continuous_elevation_segment_start = start_elevation #not sure if we need these yet
# continuous_elevation_segment_end = start_elevation
# longest_continuous_elevation_segment = 0 #def need to initialize this one


# end variable initialization ****************************

# Note: the following few variables USUALLY (not always) refer to the current move/step being made, in some cases I just use them as placeholders and will specify
# x1 = start array position
# x2 = end array position
# y1 = start height
# y2 = end height


# this function takes two input numbers (the x and y values from an array) and outputs a number (distance)
# def pythagorean_distance(x1, x2, y1, y2):
#     return math.sqrt((((x2 - x1)*grid_square_size)**2) + ((y2 - y1)**2) )


# # function takes two heights at and outputs the angle relative to the horizon
# def trail_steepness(x1, x2, y1, y2):
#     return math.atan( (y2 - y1) / ((x2 - x1)*grid_square_size) )

# takes the current move and verifies if this move is in the same up/down direction as the previous move
# if it is in the same direction, it takes the difference between the 'height resulting by moving', and the 'start of this continuous run'
# this should likely be called at each step/move

# can use a list for calculating this as well
# def max_continuous_elevation_change(y1, y2):
#     continuous_elevation_segment_end = y2

#     if not check_incline_continuity(y1, y2):
#         continuous_elevation_segment_start = y1

#     curr_continuous_elevation_change = abs(continuous_elevation_segment_end - continuous_elevation_segment_start) #note: abs gives only net change, not sure about pos vs neg changes

#     if curr_continuous_elevation_change > longest_continuous_elevation_segment:
#         longest_continuous_elevation_segment = curr_continuous_elevation_change

#     return longest_continuous_elevation_segment


# helper function to max_continuous_elevation_change()
# checks that the move is still in the same vertical direction as the previous move
# def check_incline_continuity(y1, y2):
#     incline_continuity = False
#     old_incline_polarity = incline_polarity

#     #checks elevation change of step (if y2 < y1, elevation decreased)
#     if y2 < y1:
#         incline_polarity = -1
#     else:
#         incline_polarity = 1

#     #check if the previous elevation change was the same as the current
#     if old_incline_polarity == incline_polarity:
#         incline_continuity = True
#     else:
#         incline_continuity = False

#     return incline_continuity


# reward structure attempt
# def calc_reward(x1, x2, y1, y2, penal_angle, reward_size):
#     reward = 0
#     if trail_steepness(x1, x2, y1, y2) > penal_angle:
#         reward = reward - reward_size
#     else:
#         reward = reward + reward_size
#     return reward





