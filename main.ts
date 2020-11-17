let number = 0
basic.showNumber(number)
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    if (number < 9) {
        
        number += 1
        basic.showNumber(number)
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    if (number > 0) {
        
        number -= 1
        basic.showNumber(number)
    }
    
})
