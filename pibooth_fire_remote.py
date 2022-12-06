from evdev import InputDevice, categorize, ecodes

print("ACGAM R1 - pad mapping")

#creates object 'gamepad' to store the data
gamepad = InputDevice('/dev/input/event2')

print(gamepad)

#button code variables (change to suit your device)
enterBtn = 96
backBtn = 158
settingsBtn = 139
homeBtn = 172
up = 103
down = 108
left = 105
right = 106
playpause = 164
forward = 208
backward = 168

#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    print(categorize(event))

    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == enterBtn:
                print("enterBtn")
            elif event.code == settingsBtn:
                print("settingsBtn")
            if event.code == homeBtn:
                print("homeBtn")
            elif event.code == backBtn:
                print("backBtn")
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