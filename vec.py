class Vec:
    def __init__(self, x, y=None):
        if y == None:
            y = x[1]
            x = x[0]
        self.x = x
        self.y = y

        self.a = x
        self.b = y

        self.w = x
        self.h = y
    
    def sep(self):
        return self.x, self.y