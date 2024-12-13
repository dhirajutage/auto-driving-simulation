class Car:
    def __init__(self, name, x, y, direction, commands):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = commands
        self.executed_commands = 0
        self.is_collided = False

    def move(self, width, height):
        """Move the car according to its direction while staying within boundaries."""
        if self.direction == "N":
            if self.y < height - 1:
                self.y += 1
        elif self.direction == "S":
            if self.y > 0:
                self.y -= 1
        elif self.direction == "E":
            if self.x < width - 1:
                self.x += 1
        elif self.direction == "W":
            if self.x > 0:
                self.x -= 1

    def turn_left(self):
        """Turn the car 90 degrees to the left."""
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "N"

    def turn_right(self):
        """Turn the car 90 degrees to the right."""
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "N"

    def execute_command(self, command, width, height):
        """Execute a single command (F, L, or R)."""
        if command == "F":
            self.move(width, height)
        elif command == "L":
            self.turn_left()
        elif command == "R":
            self.turn_right()

    def position(self):
        """Return the current position of the car."""
        return (self.x, self.y)
