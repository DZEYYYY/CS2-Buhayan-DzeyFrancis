# Travel Fare Calculator

## Description
This program calculates the total travel fare based on the distance traveled and the number of passengers using a fixed rate of PHP 14 per kilometer.

## Version 1 - Original code without input validation
- Input: Accepts a passenger's name, distance traveled, and number of passengers.
- Process: Calculates the total fare by multiplying the distance, fare rate, and number of passengers.
- Output: Displays the passenger's name and total fare.
- Does not include input validation.

## Version 2 - Added input validation
- Input: Accepts a passenger's name, distance traveled, and number of passengers.
- Process: Checks if the inputs are valid before calculating the total fare.
- Output: Displays the passenger's name and total fare.
- Input Validation:
  - Passenger name must not be empty.
  - Distance must be a number greater than 0.
  - Number of passengers must be a positive whole number.
- Displays an error message when an invalid input is entered.
- Allows the user to re-enter invalid inputs until they are correct.
