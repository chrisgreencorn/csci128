## CSCI 128 Lab, Week 4
#### Chris Greencorn

#### Lab 4.1: Vacation Planning

```
# Cost of hotel room for specified number of nights

def hotel_cost(nights):
 total_hotel_cost = 140 * nights
 return total_hotel_cost

# Flight Prices
## Toronto = 183
## Ottawa = 220
## Edmonton = 222
## Vancouver = 475

# Cost of return airfare for cities

def plane_ride_cost(city):
  # Return price for city
  if city == Toronto:
    return 183
  elif city == Ottawa:
    return 220
  elif city == Edmonton:
    return 222
  elif city == Vancouver:
    return 475
  else:
   print 'You can fly to Toronto, Ottawa, Edmonton, or Vancouver'
  plane_ride_cost = city
  return total_flights_return

# Cost of rental car, with $50 discount after 7 days and $20 discount between

def rental_car_cost(days):
  rental_car_cost = 40 * int(days)
  week_plus_discount = rental_car_cost - 50
  three_days_plus_discount = rental_car_cost - 20
  if days >= 3 and days < 7:
   return three_days_plus_discount
  elif days >= 7:
   return week_plus_discount
  else:
   return base_car_rental

def trip_cost(city,days):
  total_trip_cost = hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days)
  return total_trip_cost
  print total_trip_cost
```

## Lab 4.2: Reverse String Duplicator

```
def ReverseDuplicator(string):
  pile = ""
  for letter in string:
    pile = letter + letter + pile
  return pile
```
