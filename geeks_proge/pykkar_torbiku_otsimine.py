from pykkar import *
create_world("""
################
# >            #
#              #
#        1     #
#              #
#              #
################
""")
set_speed(8)
# Defineerin vasakule pöörde
def left() :
    right()
    right()
    right()
# Defineerin 180 kraadise pöörde
def pööre() :
    right()
    right()
# Panen pykkari otsima torbikut
while True :
    if is_cone() :
        break
    elif is_wall():
        if get_direction() == "E" :
            right()
            if is_cone() :
                continue
            step()
            right()
        else :
            left()
            if is_cone():
                continue
            step()
            left()
    else:
        step()
take()
while not get_direction() == "E" :
    right()
while not is_wall():
    step()
right()
while not is_wall() :
    step()
pööre()
step()
pööre()
put()