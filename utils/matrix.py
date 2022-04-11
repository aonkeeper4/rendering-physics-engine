from math import sin, cos, sqrt
import random

def cascade(val, func, n):
    for i in range(n):
        val = func(val)
    return val

class Matrix:
    def __init__(self, data):
        self.data = data

    @property
    def T(self):
        return self.transpose()

    @property
    def height(self):
        return len(self.data)

    @property
    def width(self):
        return len(self.data[0])

    def __str__(self):
        return '\n'.join(['\t'.join([str(x) for x in row]) for row in self.data])

    def __matmul__(self, other):
        if isinstance(other, Matrix) and self.width == other.height and self.height == other.width:
            return Matrix([[sum(a*b for a, b in zip(row, col)) for col in zip(*other.data)] for row in self.data])
        elif isinstance(other, Vector) and self.width == other.dimension:
            return Vector([sum(a*b for a, b in zip(row, other.data)) for row in self.data])
        else:
            raise TypeError('Matrix can only be matrix multiplied by a Matrix of transposed dimensions or Vector with same dimension as matrix height')

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[x*other for x in row] for row in self.data])
        else:
            raise TypeError('Matrix can only be multiplied by a scalar')

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[x/other for x in row] for row in self.data])
        else:
            raise TypeError('Matrix can only be divided by a scalar')

    def __add__(self, other):
        if isinstance(other, Matrix) and self.height == other.height and self.width == other.width:
            return Matrix([[a+b for a, b in zip(row, col)] for row, col in zip(self.data, other.data)])
        else:
            raise TypeError('Matrix can only be added to a Matrix of same dimensions')

    def __sub__(self, other):
        if isinstance(other, Matrix) and self.height == other.height and self.width == other.width:
            return Matrix([[a-b for a, b in zip(row, col)] for row, col in zip(self.data, other.data)])
        else:
            raise TypeError('Matrix4x4 can only be subtracted from a Matrix of same dimensions')

    def __pow__(self, other):
        if isinstance(other, int):
            return cascade(self, lambda x: self@x, other-1)
        else:
            raise TypeError('Matrix can only be raised to an integer power')

    def to_list(self):
        return self.data

    def minor(self, i, j):
        # Minor of a matrix is the matrix with the row and column removed
        return Matrix([[self.data[y][x] for x in range(self.width) if x != j] for y in range(self.height) if y != i])

    def cofactor(self, i, j):
        # Cofactor of a matrix is the determinant of the minor matrix
        return (-1)**(i+j) * (self.minor(i, j)).determinant()

    def adjoint(self):
        # Adjoint of a matrix is the transpose of the cofactor matrix
        return Matrix([[self.cofactor(j, i) for j in range(self.width)] for i in range(self.height)])

    def inverse(self):
        if self.determinant() == 0:
            raise ValueError('Matrix is not invertible')
        else:
            # Inverse of a matrix is the adjoint matrix divided by the determinant
            return Matrix(self.adjoint().data) / self.determinant()

    def transpose(self):
        # Transpose of a matrix is the matrix with rows and columns swapped
        return Matrix([[x for x in row] for row in zip(*self.data)])

    def determinant(self):
        # Determinant of a matrix is the product of the diagonal elements
        if self.height == 2 and self.width == 2:
            return self.data[0][0]*self.data[1][1] - self.data[0][1]*self.data[1][0]
        elif self.width == self.height:
            return sum(self.data[0][i]*self.cofactor(0, i) for i in range(self.width))
        else:
            raise ValueError('Matrix is not square')

    def __eq__(self, other):
        if isinstance(other, Matrix) and self.height == other.height and self.width == other.width:
            return all(self.data[i][j] == other.data[i][j] for i in range(self.height) for j in range(self.width))
        else:
            raise TypeError('Matrix can only be compared to another Matrix of same dimensions')
    
    def __ne__(self, other):
        return not self.__eq__(other)

    @staticmethod
    def identity(n):
        return Matrix([[1 if i == j else 0 for i in range(n)] for j in range(n)])

    @staticmethod
    def det(mat):
        if isinstance(mat, Matrix):
            return mat.determinant()
        else:
            raise TypeError('Determinant can only be calculated on a Matrix')

    @staticmethod
    def adj(mat):
        if isinstance(mat, Matrix):
            return mat.adjoint()
        else:
            raise TypeError('Adjoint can only be calculated on a Matrix')

    @staticmethod
    def inv(mat):
        if isinstance(mat, Matrix):
            return mat.inverse()
        else:
            raise TypeError('Inverse can only be calculated on a Matrix')

    @staticmethod
    def rotate(angle, axis):
        if axis == 'x':
            return Matrix([[1, 0, 0],
                           [0, cos(angle), -sin(angle)],
                           [0, sin(angle), cos(angle)]])
        elif axis == 'y':
            return Matrix([[cos(angle), 0, sin(angle)],
                           [0, 1, 0],
                           [-sin(angle), 0, cos(angle)]])
        elif axis == 'z':
            return Matrix([[cos(angle), -sin(angle), 0],
                           [sin(angle), cos(angle), 0],
                           [0, 0, 1]])
        else:
            raise ValueError('Axis must be x, y, or z')
class Vector:
    def __init__(self, *data):
        self.data = data

    @property
    def dimension(self):
        return len(self.data)

    @property
    def x(self):
        return self.data.get(0)

    @property
    def y(self):
        return self.data.get(1)

    @property
    def z(self):
        return self.data.get(2)

    @property
    def length(self):
        return sqrt(sum(x**2 for x in self.data))

    def __str__(self):
        return '\n'.join(map(str, self.data))

    def __matmul__(self, other):
        if isinstance(other, Matrix) and self.dimension == other.width:
            return Vector([sum(a*b for a, b in zip(row, self.data)) for row in other.data])
        else:
            raise TypeError('Vector can only be matrix multiplied by a Matrix of same width')

    def __add__(self, other):
        if isinstance(other, Vector) and self.dimension == other.dimension:
            return Vector([a+b for a, b in zip(self.data, other.data)])
        else:
            raise TypeError('Vector can only be added to a Vector of same dimension')

    def __sub__(self, other):
        if isinstance(other, Vector) and self.dimension == other.dimension:
            return Vector([a-b for a, b in zip(self.data, other.data)])
        else:
            raise TypeError('Vector can only be subtracted from a Vector of same dimension')

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector([x*other for x in self.data])
        else:
            raise TypeError('Vector can only be multiplied by a scalar')

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector([x/other for x in self.data])
        else:
            raise TypeError('Vector can only be divided by a scalar')

    def dot(self, other):
        return sum(a*b for a, b in zip(self.data, other.data))

    def cross(self, other):
        if self.dimension == 3 and other.dimension == 3:
            return Vector([self.data[1]*other.data[2] - self.data[2]*other.data[1],
                           self.data[2]*other.data[0] - self.data[0]*other.data[2],
                           self.data[0]*other.data[1] - self.data[1]*other.data[0]])
        else:
            raise TypeError('Cross product can only be calculated for 3D vectors')

    def __eq__(self, other):
        if isinstance(other, Vector) and self.dimension == other.dimension:
            return all(a == b for a, b in zip(self.data, other.data))
        else:
            raise TypeError('Vector can only be compared to a Vector of same dimension')
    
    def __ne__(self, other):
        return not self.__eq__(other)

    def normalized(self):
        return self / self.length

    @staticmethod
    def normalize(vector):
        return vector / vector.length

    @staticmethod
    def unit_random(length):
        return Vector([random.random() for _ in range(length)]).normalized()

    @staticmethod
    def from_angle(angle, axis):
        if axis == 'x':
            return Vector([cos(angle), sin(angle), 0])
        elif axis == 'y':
            return Vector([cos(angle), 0, sin(angle)])
        elif axis == 'z':
            return Vector([cos(angle), 0, sin(angle)])
        else:
            raise ValueError('Axis must be x, y, or z')