<h3>Assignment 5</h3> 
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

<h3>System Requirements</h3>
* python v3.8 or greater

<h3>Execution</h3>
To run, in the terminal run ```python3.8 lifts.py```
You will be prompted to enter the user floor and direction of travel.
* User floor should not exceed the total number of floors in the building
* 'U' or 'u' stands for upward direction of travel
* 'D' or 'd' stands for downward direction of travel


**Input**
```buildoutcfg
$ python3.8 lifts.py
> Following are the lift positions: ['14D', '14U', '4U', '1', '8U']
> Enter a request? 9u
```

**Output:**
```buildoutcfg
> Lift #5 will be coming to receive you.
```