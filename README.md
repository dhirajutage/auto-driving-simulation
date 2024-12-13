# Automatic Car Simulation

## Overview

**Automatic Car Simulation** is a project designed to simulate the behavior of an autonomous vehicle.

## Getting Started

These instructions will help you set up and run the project locally.

### Steps to Use the Simulation

1. Clone the repository:

   ```bash
   git clone https://gitlab.com/sph8610935/automatic-car-simulation.git
   cd automatic-car-simulation

   ```
2. Running Application :
   
   ```
   python main.py

   ```
3. Sample Input/Output :
   
   ```

    -- SCENARIO 1 ---
    
   Please choose from the following options:
   [1] Start over
   [2] Exit
   1
   Please enter the width and height of the simulation field in x y format:
   10 10 
   You have created a field of 10 x 10.

   Please choose from the following options:
   [1] Add a car to field
   [2] Run simulation
   1
   Please enter the name of the car:
   A
   Please enter initial position of car A in x y Direction format:
   1 2 N
   Please enter the commands for car A:
   FFRFFFFRRL
   Your current list of cars are:
   - A, (1,2) N, FFRFFFFRRL
   Please choose from the following options:
   [1] Add a car to field
   [2] Run simulation
   1
   Please enter the name of the car:
   B 
   Please enter initial position of car B  in x y Direction format:
   7 8 N
   Please enter the commands for car B :
   FFLFFFFFFF
   Your current list of cars are:
   - A, (1,2) N, FFRFFFFRRL
   - B , (7,8) N, FFLFFFFFFF
   Please choose from the following options:
   [1] Add a car to field
   [2] Run simulation
   2
   Your current list of cars are:
   - A, (1,2) N, FFRFFFFRRL
   - B , (7,8) N, FFLFFFFFFF
   Running simulation...
   After simulation, the result is:
   - A, (5,4) S
   - B , (0,9) W
   No collisions occurred.

   -- SCENARIO 2 ---

   Please choose from the following options:
   [1] Start over
   [2] Exit
   1
   Please enter the width and height of the simulation field in x y format:
   10 10 
   You have created a field of 10 x 10.

   Please choose from the following options:
   [1] Add a car to field
   [2] Run simulation
   1
   Please enter the name of the car:
   A
   Please enter initial position of car A in x y Direction format:
   1 2 N
   Please enter the commands for car A:
   FFRFFFFRRL
   Your current list of cars are:
   - A, (1,2) N, FFRFFFFRRL
   Please choose from the following options:
   [1] Add a car to field
   [2] Run simulation
   1
   Please enter the name of the car:
   B
   Please enter initial position of car B in x y Direction format:
   7 8 W
   Please enter the commands for car B:
   FFLFFFFFFF
   Your current list of cars are:
   - A, (1,2) N, FFRFFFFRRL
   - B, (7,8) W, FFLFFFFFFF
   Please choose from the following options:
   [1] Add a car to field
   [2] Run simulation
   2
   Your current list of cars are:
   - A, (1,2) N, FFRFFFFRRL
   - B, (7,8) W, FFLFFFFFFF
   Running simulation...
   After simulation, the result is:
   - A, collides with A at (5,4) at step 7
   - B, collides with B at (5,4) at step 7

   Please choose from the following options:
   [1] Start over
   [2] Exit


   ```

3. Running Test Cases
   ```
   python -m unittest ./tests/test_car.py 
   
   sample Output:
         Launching unittests with arguments python -m unittest /Users/dhirajkumarutage/PycharmProjects/auto-driving-simulation/tests/test_car.py 
      Testing started at 8:42 pm ...

      Ran 3 tests in 0.001s
      OK
      Process finished with exit code 0

   ```
      
