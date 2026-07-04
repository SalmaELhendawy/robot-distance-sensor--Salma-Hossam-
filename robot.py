"""
Program Name:robot-distance-sensor-[Salma Hossam]
Description: The main purpose for this program is enabling the Robot (Jamaica) to:
             read, detect, filter obstacles' distance and make actions based on it.
"""

class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery
        # first create (Class) to group Robots' data
        # set up the initial values with (init) method

    def analyze_sensor(self, distances):
        # Customized method to analyze sensor readings and return actions

        if not isinstance(distances, (list, tuple)):
            raise TypeError("distance must be provided as list or tuple")
        """
        extra safety line code to prevent program crash if someone provide
        the program with non allowed variable type.
        """
        
        action = []
        # empty list to receive Robot(JAMAICA) decisions

        for index, distance in enumerate(distances):
            # looping through sensor's reading list using for loop and enumerate function
            # putting safety line condition code to prevent any invalid type causes crash
            # checking the negative reading value from sensor

            if not isinstance(distance, (int, float)):
                action.append(f"Error at index:{index}|Invalid type")
                continue
                
            if distance < 0:
                action.append(f"Error at index:{index}| Negative value")
                continue 
                
            # checking and filtering distances and make classification(STOP,SLOW,FAST) from sensor readings 
            if distance < 0.5:
                action.append("STOP""| Obstacle too close")
            elif 0.5 <= distance <= 1:
                action.append("SLOW""| Obstacle nearby")
            else:
                action.append("MOVE FAST""| Clear path")
                
        return action
        # Return the final list of actions for Jamaica

#_______________________ _________________  _______________________  ___________
# SYSTEM TESTING: 5+ Test Cases for Jamaica's Sensor & Error Handling                           
#_______________________ __________________  ______________________  ___________

if __name__ == "__main__":
    # 1. Create an instance of Jamaica the Robot
    jamaica = Robot(name="Jamaica", battery=100)
    print(f"Testing {jamaica.name}'s Decision Maker System \n")

    # checking 5 different test cases sorted by dictionary 
    test_cases = {
        "Case 1: Mixed valid distances": [0.2, 0.5, 1.0, 1.5, 2.5],
        "Case 2: Negative and boundary values": [-0.1, 0.0, 0.49, 0.51],
        "Case 3: Close, nearby, and clear path": [1.1, 5.0, 0.75, 0.3, 0.99],
        "Case 4: Invalid non-numeric values": ["a", 0.4, None, 1.2],
        "Case 5: Empty distance list": []
    }
    
    # Loop through test cases and display outputs
    for description, distances in test_cases.items():
        print(f"Running {description}")
        print(f"Input distances: {distances}")
        
        # Error handling for bad distance values
        try:
            results = jamaica.analyze_sensor(distances)
            print(f"Robot Decisions: {results}")
        except Exception as error:
            print(f"ERROR: {str(error)}")
        print("-") 
