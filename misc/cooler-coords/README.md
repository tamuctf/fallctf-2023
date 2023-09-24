# Cooler Coords

We found Link's notebook on his latest journey to find Princess Zelda. The last page of his notebook contains what seems to be a coordinate of his next shrine to tackle (-3291, -2512, 0038). Can you find out where Link went? 

flag format:
gigem{Name_Shrine}

Author: Emmie

## Solution

Due to the description of the challenge I figured it was asking for the shrine location at the (x, y, z) coordinates in the game of Zelda.

I put in google this search term:

Zelda coordinates shrine ("-3291, -2512, 0038")

The second website that showed up was this one: https://www.gamertw.com/en/zelda/totk/shrine

On line 43 of this page were these coordinates: -3291, -2512, 0050. This was very similar to the provided coordinates as only the third value is 12 off. By the corresponding shrine being "Mayatat Shrine" the flag is gigem{Mayatat_Shrine}.

flag:
`gigem{Mayatat_Shrine}`
