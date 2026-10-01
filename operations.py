#sub,sum,mul,div,square,cube, do operation to user input
class Calc:
    def __init__(self):
        self.a = 0
        self.b = 0

    def get_data(self):
        self.a = int(input("Enter 1st number: "))
        self.b = int(input("Enter 2nd number: "))

    def operation(self):
        print("1. Sum")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square")
        print("6. Cube")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                print("Sum =", self.a + self.b)

            case 2:
                print("Sub =", self.a - self.b)

            case 3:
                print("Mul =", self.a * self.b)

            case 4:
                print("Div =", self.a / self.b)

            case 5:
                print("Square =", self.a * self.a)

            case 6:
                print("Cube =", self.a * self.a * self.a)

            case _:
                print("Invalid choice")


c = Calc()
c.get_data()
c.operation()


      


