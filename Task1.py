
# Objective:
# The aim of this assignment is to deepen your understanding and application of Python sets in various 
# scenarios, ranging from basic operations to advanced manipulations and best practices. 
# You will correct given codes, use sets in everyday contexts, and tackle challenges that require 
# creative thinking and problem-solving.

# Task 1: Flight Route Comparison
# Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. 
# You have two sets of flight destinations, one for each airline. Write a Python program to find out:

# Destinations that both airlines fly to.
# Destinations unique to your airline.
# Whether there are any destinations that neither airline shares.
# Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

same_destinations = our_routes.intersection(competitor_routes)
our_unique_destinations = our_routes.difference(competitor_routes)
no_shared_destinations = our_routes.symmetric_difference(competitor_routes)

print("Destinations that both airlines fly to:", same_destinations)
print("Destinations unique to our airline:", our_unique_destinations)
print("Destinations that neither airline shares:", no_shared_destinations)