import vec3

class ray:

    def __init__(self, origin, direction):
        self._origin = origin
        self._direction = direction

    def at(self, t):
        return self._origin + t * self._direction
