import unittest
from car import Car
from simulation import run_simulation


class TestCar(unittest.TestCase):

    def setUp(self):
        # Setup cars for testing
        self.car_a = Car(name="A", x=1, y=2, direction="N", commands="FFRFFFFRRL")
        self.car_b = Car(name="B", x=7, y=8, direction="W", commands="FFLFFFFFFF")
    def test_execute_commands(self):
        # Test executing a sequence of commands
        self.car_a.execute_command('F', 10, 10)  # Move forward
        self.assertEqual(self.car_a.x, 1)
        self.assertEqual(self.car_a.y, 3)  # Moves from (1, 2) -> (1, 3)

        self.car_a.execute_command('R', 10, 10)  # Turn right
        self.assertEqual(self.car_a.direction, "E")  # Now facing East

        self.car_a.execute_command('F', 10, 10)  # Move forward
        self.assertEqual(self.car_a.x, 2)  # Moves from (1, 3) -> (2, 3)
        self.assertEqual(self.car_a.y, 3)

        self.car_a.execute_command('L', 10, 10)  # Turn left
        self.assertEqual(self.car_a.direction, "N")  # Now facing North

    def test_collision(self):
        # Test collision detection
        cars = [self.car_a, self.car_b]

        # Move car_a and car_b to a collision point
        self.car_a.execute_command('F', 10, 10)  # Move car_a forward
        self.car_b.execute_command('F', 10, 10)  # Move car_b forward
        self.car_a.execute_command('F', 10, 10)  # Move car_a forward
        self.car_b.execute_command('F', 10, 10)  # Move car_b forward
        self.car_a.execute_command('F', 10, 10)  # Move car_a forward
        self.car_b.execute_command('F', 10, 10)  # Move car_b forward

        collisions = run_simulation(cars, 10, 10)

        # Check if a collision has been detected and that the message is correct
        self.assertGreater(len(collisions), 0, "No collision detected!")

        # Ensure that both collision messages are covered
        collision_message = collisions[0]
        self.assertTrue("A, collides with B" in collision_message or "B, collides with A" in collision_message)

    def test_no_collision(self):
        # Test when no collision occurs
        self.car_a.execute_command('F', 10, 10)
        self.car_b.execute_command('F', 10, 10)
        self.car_a.execute_command('F', 10, 10)

        collisions = run_simulation([self.car_a, self.car_b], 10, 10)
        self.assertEqual(len(collisions), 0, "Collision should not have occurred!")


if __name__ == '__main__':
    unittest.main()
