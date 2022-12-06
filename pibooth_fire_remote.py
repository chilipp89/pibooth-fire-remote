from evdev import InputDevice, categorize, ecodes

print("ACGAM R1 - pad mapping")

#creates object 'gamepad' to store the data
gamepad = InputDevice('/dev/input/event0')

print(gamepad)

#button code variables (change to suit your device)
enterBtn = 304
MicroBtn = 305
up = 115
down = 114
left = 165
right = 163
playpause = 164
forward = 166
backward = 167

#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    print(categorize(event))

    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == enterBtn:
                print("enterBtn")
            elif event.code == MicroBtn:
                print("MicroBtn")
            elif event.code == playpause:
                print("Play/Pause")
            elif event.code == up:
                print("up")
            elif event.code == down:
                print("down")
            elif event.code == left:
                print("left")
            elif event.code == right:
                print("right")
            elif event.code == forward:
                print("forward")
            elif event.code == backward:
                print("backward")