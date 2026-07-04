## 1. What does this program do?
This program processes raw data from a robot's distance sensor,
filters out invalid readings (negative numbers or wrong types), and decides the robot's action based on obstacles.(`STOP`, `SLOW`, or `MOVE FAST`).

## 2. How does the Robot class work?
The `Robot` class serves as the main controller. It stores the robot's state (name and battery)
and provides the logic (`analyze_sensor`) to process distance data and make movement decisions.

## 3. What does each method do?
* `__init__`: Sets up the robot's name and battery level when created.
* `analyze_sensor`: Checks each distance reading to filter out errors, then assigns an action
* (`STOP`, `SLOW`, or `MOVE FAST`) depending on how close the obstacle is.

## 4. How do I run the code?
In the terminal down below, write `python3` followed by the file name:
python3 robot.py
## 5. What did you learn from using AI?
* How to structure clean methods like analyze_sensor.
* It helped me structure the logical flow in my mind.
* Writing clear, organized comments.
* Best practices for checking errors and handling edge cases safely.
