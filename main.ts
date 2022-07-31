input.onButtonPressed(Button.A, function () {
    Icon = IconNames.Happy
})
input.onButtonPressed(Button.B, function () {
    Icon = IconNames.Sad
})
let PhoVal = 0
let CalVal = pins.analogReadPin(AnalogPin.P0)
let Icon = IconNames.Skull
basic.forever(function () {
    PhoVal = pins.analogReadPin(AnalogPin.P0)
    // basic.show_number(0)
    if (PhoVal < CalVal - 2) {
        basic.showIcon(Icon)
    } else {
        basic.clearScreen()
    }
})
