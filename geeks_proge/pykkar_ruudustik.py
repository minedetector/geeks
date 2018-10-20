from pykkar import *
create_world("""
########
#>     #
#      #
#      #
#      #
#      #
########
""")
set_speed(10)
# Defineerin vasakulepöörde
def left():
    right()
    right()
    right()
# Defineerin täispöörde
def pööre():
    right()
    right()
# Määran i väärtuse
i = 0
while True:
    # Kontrollin, kas i on paarisarv, kui on siis värvin
    if i % 2 == 0 :
        paint()
    # Kontrollin , kas ees on sein, kui ei siis astun
    if not is_wall():
        step()
        i = i+1
    # Kui tuleb ette sein, siis kontrollin suunda, kui suund on ida siis teen pöörde  paremale
    elif is_wall():
        if get_direction() == "E":
            right()
            if is_wall():
                break
            i=i+1
            step()
            right()
        # Kui suund on läände siis pöören vasakule
        else:
            left()
            if is_wall():
                break
            i=i+1
            step()
            left()
