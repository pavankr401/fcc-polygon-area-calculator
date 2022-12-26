class Rectangle:
    #constructor
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def __repr__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)
    
    def set_width(self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height
        
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)
    
    def get_picture(self):
        if(self.width > 50 or self.height > 50):
            return "Too big for picture."
        
        # draw rectangle
        result = ""
        for i in range(self.height):
            for j in range(self.width):
                result += "*"
            result += '\n'
        
        return result
    
    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        Rectangle.__init__(self, side, side)
        
    def __repr__(self):
        return "Square(side={})".format(self.side)
    
    def set_side(self, side):
        self.side = side
        Rectangle.__init__(self, side, side)
        
    def set_width(self, side):
        self.side = side
        Rectangle.__init__(self, side, side)
        
    def set_height(self, side):
        self.side = side
        Rectangle.__init__(self, side, side)


# rect = Rectangle(10, 3)
# sq = Square(2)
# print(sq)


# sq.set_width(4)
# print(rect.get_amount_inside(sq))
# print(sq)