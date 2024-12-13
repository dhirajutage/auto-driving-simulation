# simulation.py

from car import Car


def check_collisions(cars):
    """
    Check if any cars collide based on their current positions.
    :param cars:
    :return:
    """
    positions = {}
    collisions = []

    for car in cars:
        if car.is_collided:
            continue  # Skip already collided cars

        pos = car.position()

        if pos in positions:
            # Collision detected
            other_car = positions[pos]
            collision_message = f"{car.name}, collides with {other_car.name} at {pos} at step {car.executed_commands}"
            collisions.append(collision_message)
            car.is_collided = True
            other_car.is_collided = True  # Mark both cars as collided
        else:
            positions[pos] = car

    return collisions


def run_simulation(cars, width, height):
    """
    Run the simulation, move the cars and check for collisions.
    :param cars:
    :param width:
    :param height:
    :return:
    """
    step = 0
    collisions = []

    while True:
        all_done = True
        for car in cars:
            if car.executed_commands < len(car.commands) and not car.is_collided:

                car.execute_command(car.commands[car.executed_commands], width, height)
                car.executed_commands += 1
                all_done = False

        # Check for collisions after all cars have moved
        collisions = check_collisions(cars)

        if all_done or collisions:
            break

        step += 1

    return collisions
