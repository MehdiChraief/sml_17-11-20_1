from microbit import *
number = 0
basic.show_number(number)
def on_button_pressed_a():
    if number < 9:   
        global number
        number +=1
        basic.show_number(number)
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_b():
    if number > 0:
        global number
        number -=1
        basic.show_number(number)
input.on_button_pressed(Button.B, on_button_pressed_b)