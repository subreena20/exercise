class circle:
    def __init__(self, radius):
        self.radius=radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if isinstance(value,str) or (value<=0):
            raise ValueError("positive number excepted")
        self._radius=value
