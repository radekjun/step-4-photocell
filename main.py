def on_button_pressed_a():
    global Icon
    Icon = IconNames.HAPPY
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Icon
    Icon = IconNames.SAD
input.on_button_pressed(Button.B, on_button_pressed_b)

PhoVal = 0
CalVal = pins.analog_read_pin(AnalogPin.P0)
Icon = IconNames.SKULL

def on_forever():
    global PhoVal
    PhoVal = pins.analog_read_pin(AnalogPin.P0)
    # basic.show_number(0)
    if PhoVal < CalVal - 2:
        basic.show_icon(Icon)
    else:
        basic.clear_screen()
basic.forever(on_forever)
