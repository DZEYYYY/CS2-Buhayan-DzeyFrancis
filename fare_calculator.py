# Travel Fare Calculator
FARE_RATE = 14

name = input("Enter passenger name: ")
distance = float(input("Enter distance (km): "))
passengers = int(input("Enter number of passengers: "))

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))

# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number




# Travel Fare Calculator
FARE_RATE = 14

# Validate passenger name
name = input("Enter passenger name: ")

while name.strip() == "":
    print("Invalid name. Please try again.")
    name = input("Enter passenger name: ")

# Validate distance
distance = input("Enter distance (km): ")

while not distance.replace(".", "", 1).isdigit() or float(distance) <= 0:
    print("Invalid distance. Enter a number greater than 0.")
    distance = input("Enter distance (km): ")

distance = float(distance)

# Validate number of passengers
passengers = input("Enter number of passengers: ")

while not passengers.isdigit() or int(passengers) <= 0:
    print("Invalid input. Enter a positive whole number.")
    passengers = input("Enter number of passengers: ")

passengers = int(passengers)

# Calculate total fare
total_fare = distance * FARE_RATE * passengers

# Display result
print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))
