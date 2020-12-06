import numpy as np
import math

def vector(x, y, z):
    """
    Returns the vector in a 3 dimensional system.
    """
    return np.array([x, y, z])

def point(x, y, z):
    """
    Returns a point in a 3 dimensional system.
    """
    return vector(x, y, z)

def length_of_vector(v):
    """
    Returns the length of a 3 dimensional vector.
    """
    return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)

def vector_between_points(p1, p2):
    """
    Returns the vector between two points.
    """
    return p2 - p1

def vectorproduct(v1, v2):
    """
    Returns the vectorproduct 'Kreuzprodukt' of two vectors.
    """
    x = v1[1] * v2[2] - v1[2] * v2[1]
    y = v1[2] * v2[0] - v1[0] * v2[2]
    z = v1[0] * v2[1] - v1[1] * v2[0]
    return vector(x, y, z)

def intersection_between_line_and_plane(La, Lb, P0, P1, P2):
    """
    Returns the point of intersection between a lines and a plane.
    If they do not intersect, NaN will be returned.
    The first value of the return tuple is if the intersection is between the two line points.
    The second value of the return tuple is the exact point of intersection.
    """
    Lab = vector_between_points(La, Lb)
    P01 = vector_between_points(P0, P1)
    P02 = vector_between_points(P0, P2)
    det = -Lab * vectorproduct(P01, P02)
    if det.all():
        return (False, NaN)
    t = (vectorproduct(P01, P02) * (La - P0)) / det
    u = (vectorproduct(P02, -La) * (La - P0)) / det
    v = (vectorproduct(-La, P01) * (La - P0)) / det

    # return the point of intersection
    if t[0] >= 0 and t[0] <= 1:
        return (True, La + Lab * t[0])
    return (False, La + Lab * t[0])