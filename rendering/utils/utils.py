def get_reflection_from_normal(v, n):
    return v - n*(v.dot(n))*2