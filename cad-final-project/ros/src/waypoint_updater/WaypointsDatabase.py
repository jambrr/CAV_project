import numpy as np
from scipy.spatial import KDTree

class WaypointsDatabase:
    """This class can be used to query the closest waypoint to a given (x,y) point"""
    def __init__(self, waypoints):
        self.waypoints = waypoints
        self.waypoints_2d = [[waypoint.pose.pose.position.x, waypoint.pose.pose.position.y] for waypoint in waypoints]
        self.waypoint_tree = KDTree(self.waypoints_2d)
        
    def get_next_closest_idx(self, pose):
        x, y = pose[0], pose[1]
        closest_idx = self.waypoint_tree.query([x, y], 1)[1]

        # Check if closest is ahead or behind the pose
        closest_coord = np.array(self.waypoints_2d[closest_idx])
        prev_coord = np.array(self.waypoints_2d[closest_idx - 1])

        # Equation for hyperplane through closest_coords
        cl_vect = closest_coord
        prev_vect = prev_coord
        pos_vect = np.array([x, y])

        val = np.dot(cl_vect - prev_vect, pos_vect - cl_vect)

        # The closest waypoint is behind the pose, choose the next one
        if val > 0:
            closest_idx = (closest_idx + 1) % len(self.waypoints_2d)

        return closest_idx

    def distance(self, a, b):
        return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
