class Vec:
    def __init__(self, *args):
        if len(args)==1:
            x = args[0][0]
            y = args[0][1]
        else:
            x = args[0]
            y = args[1]

        self.x = x
        self.y = y

        self.a = x
        self.b = y

        self.w = x
        self.h = y
    
    def sep(self):
        return self.x, self.y