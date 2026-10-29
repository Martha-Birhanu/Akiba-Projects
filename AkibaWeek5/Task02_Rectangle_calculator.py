class Rectangle:
    def __init__ (self,length,width):
        self.length=length
        self.width=width

    def area(self):
        area=(self.length)*(self.width)

        return f"Area: {area}"


    def perimeter(self):
        perimeter=2*(self.length + self.width)

        return f"Perimeter: {perimeter}"


r1=Rectangle(6,8)
r2=Rectangle(8,10)
Area_unit="m\u00b2"

print(f"Rectangle_1\n{r1.area()}{Area_unit} \n{r2.perimeter()}m")
print(f"Rectangle_2\n{r1.area()}{Area_unit} \n{r2.perimeter()}m")


    