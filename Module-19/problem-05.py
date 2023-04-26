space_invaders = [ . . . ] # global 
player_pos = ( 200 , 25 )  # global
level = 1 max_level = 10  # global

def play ( ) : # global declared function and def is build in
     . . . 
    while ( level < max_level +1 ) : # while build in
         if len ( space_invaders ) == 0 : # len build in and if build in
            level += 1 
            continue 
. . .


local --> 