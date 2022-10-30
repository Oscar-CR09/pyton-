class Color:
    def __init__(self,color):
        self._color=color

    @property   #get
    def color(self):
        return self._color

    @color.setter #set
    def color(self,color):
        self._color=color

    def __str__(self):
        return f'{self.color} '