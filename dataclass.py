from dataclasses import dataclass

@dataclass

# defined a class that will compare the event based on string
class Message:
    event: str

# stored messages in their corresponding variables
wipers = Message("Windshield wipers turned on")
hazardLights = Message("Hazard lights turned on")

# checks their value by comparing
print(wipers < hazardLights)