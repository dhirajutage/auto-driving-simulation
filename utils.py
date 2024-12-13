from car import Car

def add_car(cars):
    """
    Adding the car elements

    :param cars:
    :return:
    """
    car_name = input("Please enter the name of the car:\n")

    # No Dups
    if any(car.name == car_name for car in cars):
        print(f"A car with the name {car_name} already exists. Please choose a different name.")
        return None

    x, y, direction = input(f"Please enter initial position of car {car_name} in x y Direction format:\n").split()
    x, y = int(x), int(y)


    if direction not in ['N', 'S', 'E', 'W']:
        print("Invalid direction. Please use one of N, S, E, W.")
        return None
    commands = input(f"Please enter the commands for car {car_name}:\n")

    new_car = Car(car_name, x, y, direction, commands)


    return new_car


def display_car_list(cars):
    """

    Display the Cars name and co-ordinates
    :param cars:
    :return:
    """
    print("Your current list of cars are:")
    for car in cars:
        print(f"- {car.name}, ({car.x},{car.y}) {car.direction}, {car.commands}")
