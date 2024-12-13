# main.py

from car import Car
from simulation import run_simulation
from utils import display_car_list, add_car

def main():
    cars = []
    width, height = map(int, input("Please enter the width and height of the simulation field in x y format:\n").split())
    print(f"You have created a field of {width} x {height}.\n")

    while True:
        print("Please choose from the following options:")
        print("[1] Add a car to field")
        print("[2] Run simulation")

        choice = input()

        if choice == "1":
            new_car = add_car(cars)
            if new_car:
                cars.append(new_car)
                display_car_list(cars)
        elif choice == "2":
            # Display current list of cars before simulation
            display_car_list(cars)

            print("Running simulation...")
            collisions = run_simulation(cars, width, height)

            print("After simulation, the result is:")
            for car in cars:
                if car.is_collided:
                    print(f"- {car.name}, collides with {car.name} at ({car.x},{car.y}) at step {car.executed_commands}")
                else:
                    print(f"- {car.name}, ({car.x},{car.y}) {car.direction}")

            if collisions:
                for collision in collisions:
                    print(collision)
            else:
                print("No collisions occurred.")

            print("\nPlease choose from the following options:")
            print("[1] Start over")
            print("[2] Exit")
            option = input()
            if option == "1":
                main()  # Restart the simulation
                return
            elif option == "2":
                print("Thank you for running the simulation. Goodbye!")
                return


if __name__ == "__main__":
    main()
