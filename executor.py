from implementation import *

start, goal = (0, 0), (5, 7)
came_from, cost_so_far = a_star_search(diagram4, start, goal)
draw_grid(diagram4, width=3, point_to=came_from, start=start, goal=goal)
print()
#draw_grid(diagram4, width=3, number=cost_so_far, start=start, goal=goal)
#print()