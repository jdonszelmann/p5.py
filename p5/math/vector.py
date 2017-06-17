class Vector:
    DECIMAL_PRECISION = 6

    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def checktype(obj):
        return isinstance(obj, Vector)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __getitem__(self, key: int):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        elif key == 2:
            return self.z
        else:
            raise AttributeError("Only x, y and z-axis are supported")

    def __setitem__(self, key: int, value):
        if key == 0:
            self.x = value
        elif key == 1:
            self.y = value
        elif key == 2:
            self.z = value
        else:
            raise AttributeError("Only x, y and z-axis are supported")

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __sub__(self, other):
        return self.__class__(self.x - other.x, self.y - other.y, self.z - other.z)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __mul__(self, val):
        return self.__class__(self.x * val, self.y * val, self.z * val)

    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y
        self.z *= other.z
        return self

    def __truediv__(self, val):
        return self.__class__(self.x / val, self.y / val, self.z / val)

    def __itruediv__(self, other):
        self.x /= other.x
        self.y /= other.y
        self.z /= other.z
        return self

    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5

    def __matmul__(self, other):
        return self.dist(other)

    def inproduct(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def crossproduct(self, other):
        return self.__class__(self.y * other.z - other.y * self.z, self.z * other.x - self.x * other.z,
                              self.x * other.y - other.x * self.y)

    def isperpendicular(self, other):
        return self.inproduct(other) == 0

    def dot(self, matrix):
        """
        Matrix must be ordered in the following way:
        Each element in main list is a row
        [[0,0,0], [0,0,0], [0,0,0]]
        """
        new_vector = self.__class__()
        for indexrow, row in enumerate(matrix):
            intermediary = 0
            for indexcolumn, elem in enumerate(row):
                intermediary += elem * self[indexcolumn]
            new_vector[indexrow] = intermediary
        return new_vector

    def add(self, other):
        return self.__class__(self.x + val, self.y + val,self.z + val)

    def sub(self, other):
        return self.__class__(self.x - val, self.y - val,self.z - val)

    def mult(self, val):
        return self.__class__(self.x * val, self.y * val,self.z * val)

    def rotate(self, axis='x', by=0):
        new_vector = Vector()
        if axis == 'x':
            X_AXIS = [[1, 0, 0],
                      [0, math.cos(by), -math.sin(by)],
                      [0, math.sin(by), math.cos(by)]]
            new_vector += self.dot(X_AXIS)
        elif axis == 'y':
            Y_AXIS = [[math.cos(by), 0, math.sin(by)],
                      [0, 1, 0],
                      [-math.sin(by), 0, math.cos(by)]]
            new_vector += self.dot(Y_AXIS)
        elif axis == 'z':
            Z_AXIS = [[math.cos(by), -math.sin(by), 0],
                      [math.sin(by), math.cos(by), 0],
                      [0, 0, 1]]
            new_vector += self.dot(Z_AXIS)
        elif axis is str:
            raise ValueError("Axis not supported, only x-, y- and z-axis")
        else:
            raise TypeError("Axis not supported, only x-, y- and z-axis")
        for i in range(len(self)):
            self[i] = new_vector[i]

    @property
    def magnitude(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def limit(self, limit):
        if self.magnitude > limit:
            self.setmag(limit)

    def setmag(self, val):
        m = self.magnitude
        self.x = (self.x / m) * val
        self.y = (self.y / m) * val
        self.z = (self.z / m) * val

    def normalize(self):
        m = self.magnitude
        self.x = self.x / m
        self.y = self.y / m
        self.z = self.z / m

    def copy(self):
        return self.__class__(self.x, self.y, self.z)

    def __repr__(self):
        return 'Vector: [x={}, y={}, z={}]'.format(self.x, self.y, self.z)

    def __str__(self):
        return 'Vector: [x={}, y={}, z={}]'.format(self.x, self.y, self.z)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y) ^ hash(self.z)

    def round_values(self):
        self.x = round(self.x, self.DECIMAL_PRECISION)
        self.y = round(self.y, self.DECIMAL_PRECISION)
        self.z = round(self.z, self.DECIMAL_PRECISION)

    def angle(self, other):
        return math.acos(self.inproduct(other) / (self.magnitude * other.magnitude))

    def __len__(self):
        return 3

    def to_vertice(self):
        return self.x, self.y, self.z



def CreateVector(*args, **kwargs):
    return Vector(*args, **kwargs)