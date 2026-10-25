import numpy as np

class vec3:

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.e = np.array([x, y, z], dtype=np.float32)

    @property
    def x(self):
        return self.e[0]

    @property
    def y(self):
        return self.e[1]

    @property
    def z(self):
        return self.e[2]

    def __neg__(self):
        return vec3(-self.e[0], -self.e[1], -self.e[2])

    def __getitem__(self, index):
        return self.e[index]

    def __iadd__(self, other):
        self.e[0] += other.e[0]
        self.e[1] += other.e[1]
        self.e[2] += other.e[2]
        return self

    def __imul__(self, other):
        self.e[0] *= other
        self.e[1] *= other
        self.e[2] *= other
        return self

    def __itruediv__(self, other):
        self.e[0] /= other
        self.e[1] /= other
        self.e[2] /= other
        return self

    def __add__(self, other):
        return vec3(self.e[0] + other.e[0], self.e[1] + other.e[1], self.e[2] + other.e[2])

    def __mul__(self, other):
        if isinstance(other, vec3):
            return vec3(self.e[0] * other.e[0], self.e[1] * other.e[1], self.e[2] * other.e[2])
        return vec3(self.e[0] * other, self.e[1] * other, self.e[2] * other)

    __rmul__ = __mul__

    def __truediv__(self, other):
        return vec3(self.e[0] / other, self.e[1] / other, self.e[2] / other)

    def length_squared(self):
        return self.e[0] ** 2 + self.e[1] ** 2 + self.e[2] ** 2

    def length(self):
        return np.sqrt(self.length_squared())

    def __str__(self):
        return f"{self.e[0]} {self.e[1]} {self.e[2]}"

    def __sub__(self, other):
        return vec3(self.e[0] - other.e[0], self.e[1] - other.e[1], self.e[2] - other.e[2])

    def cross(self, other):
        return vec3(self.e[1] * other.e[2] - self.e[2] * other.e[1], self.e[2] * other.e[0] - self.e[0] * other.e[2], self.e[0] * other.e[1] - self.e[1] * other.e[0])

    def dot(self, other):
        return self.e[0] * other.e[0] + self.e[1] * other.e[1] + self.e[2] * other.e[2]

    def unit_vector(self):
        return self / self.length()


point3 = vec3