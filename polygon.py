class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, width):
        self.__width = width

    @height.setter
    def height(self, height):
        self.__height = height

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        matrix_list = [['*' for column in range(0, self.width)] for row in range(0, self.height)]
        matrix_list = [''.join(row) for row in matrix_list]

        output_string = '\n'.join(matrix_list)

        return output_string + ('\n')

    def get_amount_inside(self, other):
        times_height = self.height // other.height
        times_width = self.width // other.width

        return times_height * times_width


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width=side, height=side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f'Square(side={self.width})'

    @Rectangle.width.setter
    def width(self, side):
        self._Rectangle__width = side
        self._Rectangle__height = side

    @Rectangle.height.setter
    def height(self, side):
        self._Rectangle__width = side
        self._Rectangle__height = side
