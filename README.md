<h2>Backend/Python Coding round</h2>

<h3>Assignment 1:</h3> 
Write a python program to scrape the list of links available in this Github repository (https://github.com/vinta/awesome-python) and search them by exact name from the console. Search result should return the github url of the result repository. 

Expected output: 
```
$ python search_repos.py
> Query? graphene 
> Output: https://github.com/graphql-python/graphene/
```

The list should be scraped and kept in a runtime variable as soon as the program is initialized.. Handle the error with a suitable error message in case the exact name is not matched from the list. 



<h3>Assignment 2:</h3> 
Write a python class that is able to return the meaning of an English language word provided to it in the terminal. (Use https://dictionaryapi.dev/) 

Expected output:
```
$ python dictionary_search.py
> Word? <user inputs the word “House”>
> Output: House. Noun. A building for human habitation, especially one that is lived in by a family or small group of people.
```  


<h3>Assignment 3:</h3> 
Write a python class that is able to return the flight distance between two cities given their latitude and longitude coordinates. 

Expected output: 
```
$ python city_distance.py
> City 1: 51.5074 N, 0.1278 W
> City 2: 48.8566 N, 2.3522 E
> Output: City 1 and City 2 are 342.87 km apart
```

<h3>Assignment 4:</h3> 
Write a python class that is able to find three available WiFi networks with the strongest signal and connect to the one where the password is provided. 

Expected output:
```
$ python wifi.py
> Your available wifi networks are: 
> [1] Wifi_network 1
> [2] Wifi_network 2
> [3] Wifi_network 3
> Your choice? 3
> Password: *******
> connected!
``` 


<h3>Assignment 5:</h3> 
A building has 20 floors and 5 lifts. Each floor of the building has a lift lobby. A user can be on any of the 20 floors and can request a lift. The positions of the lifts are denoted by a 5-length array of random numbers representing the current floor position (and direction of) of each lift. If no direction is given, it means that the lift is sitting idle on that floor. Example:

lift_position = [0, 1D, 12, 4U, 19D]

Write a python program to allot to most efficiently lift to a user who requests it from any floor with intention of going up or down. On running the program the lift position should be randomly initialized. 

A user can request for a lift in the following format: <lift position> <going up or down>
Such as 5U or 10D. 

Expected output:
```
$ python lifts.py
> Enter a request? 5U
> Lift #4 will be coming up to receive you.
```