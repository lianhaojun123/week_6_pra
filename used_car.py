"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("my car", 180)
    my_car.drive(30)
    print(my_car)

    limo = Car("limo", 100)
    limo.add_fuel(20)
    limo.drive(115)
    print(limo)


main()
