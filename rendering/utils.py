from math import sqrt

def get_vector_reflection_from_normal(v, n):
    return v - n*(v.dot(n))*2

def sphere_line_intersection(o, u, c, r):
        nabla = (u.dot(o-c))**2 - ((o-c).length**2-r**2)
        if nabla < 0: return tuple() # oh god my eyes
        d0 = -(u.dot(o-c)) + sqrt(nabla)
        d1 = -(u.dot(o-c)) - sqrt(nabla)
        v0 = o + u*d0
        v1 = o + u*d1
        if nabla == 0: return (v0)
        else: return (v0, v1)