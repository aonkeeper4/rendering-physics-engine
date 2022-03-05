from math import sqrt, pi, sin, cos
from random import random

def get_specular_reflection_from_normal(v, n):
    return v - n*(v.dot(n))*2

def get_diffuse_reflection_from_normal(v, n):
    # return v - n*(v.dot(n))*2
    theta = random(2*pi)
    return v*cos(theta) + k.cross(v)*sin(theta) + k*k.dot(v)*(1-cos(theta))

def sphere_line_intersection(o, u, c, r):
        nabla = (u.dot(o-c))**2 - ((o-c).length**2-r**2)
        if nabla < 0: return tuple() # oh god my eyes
        d0 = -(u.dot(o-c)) + sqrt(nabla)
        d1 = -(u.dot(o-c)) - sqrt(nabla)
        v0 = o + u*d0 if d0 > 0 else None
        v1 = o + u*d1 if d1 > 0 else None
        if nabla == 0: result = (v0)
        else: result = (v0, v1)
        return tuple(v for v in result if v is not None)