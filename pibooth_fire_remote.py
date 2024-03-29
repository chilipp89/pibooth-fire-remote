import threading

from evdev import InputDevice, categorize, ecodes
import pygame

from pynput.keyboard import Key, Controller

keyboard = Controller()

import pibooth
from pibooth.utils import LOGGER


__version__ = "0.2.2"



BUTTONDOWN = pygame.USEREVENT + 1

SECTION = "FIRE-Remote"


def get_device(cfg_in):
    try:
        # creates object 'fire tv remote' to store the data
        device_name = str(cfg_in.get(SECTION, 'device'))
        dev = InputDevice(device_name)
    except FileNotFoundError:
        LOGGER.warning("Bluetooth device not Found.")
        dev = None

    except PermissionError:
        LOGGER.warning("Bluetooth device busy")
        dev = None

    return dev
@pibooth.hookimpl
def pibooth_configure(cfg):
    #button code variables (change to suit your device)
    cfg.add_option(SECTION, 'device', '/dev/input/event2',
                   "Device Path")
    cfg.add_option(SECTION, 'pictureBtn', 96,
                       "pictureBtn Button Code")
    # cfg.add_option(SECTION, 'backBtn', 158,
    #                "Back Button Code")
    cfg.add_option(SECTION, 'settingsBtn', 139,
                   "Setting Button Code")
    # cfg.add_option(SECTION, 'homeBtn', 172,
    #                "Home Button Code")
    # cfg.add_option(SECTION, 'up', 103,
    #                "Up Button Code")
    # cfg.add_option(SECTION, 'down', 108,
    #                "Down Button Code")
    cfg.add_option(SECTION, 'left', 105,
                   "Left Button Code")
    cfg.add_option(SECTION, 'right', 106,
                   "Right Button Code")
    # cfg.add_option(SECTION, 'playpause', 164,
    #                "Play Button Code")
    cfg.add_option(SECTION, 'printBtn', 208,
                   "printBtn Button Code")
    # cfg.add_option(SECTION, 'backward', 168,
    #                "Backward Button Code")


@pibooth.hookimpl
def pibooth_startup(cfg, app):
    th = threading.Thread(target=run_event_monitor, args=(cfg, app))
    th.daemon = True
    th.start()

def run_event_monitor(cfg, app):
    #loop and filter by event code and print the mapped label
    while True:

        dev = get_device(cfg)
        if dev is not None:

            pictureBtn = int(cfg.get(SECTION, 'pictureBtn'))
            # backBtn = int(cfg.get(SECTION, 'backBtn'))
            settingsBtn = int(cfg.get(SECTION, 'settingsBtn'))
            # homeBtn = int(cfg.get(SECTION, 'homeBtn'))
            # up = int(cfg.get(SECTION, 'up'))
            # down = int(cfg.get(SECTION, 'down'))
            left = int(cfg.get(SECTION, 'left'))
            right = int(cfg.get(SECTION, 'right'))
            # playpause = int(cfg.get(SECTION, 'playpause'))
            printBtn = int(cfg.get(SECTION, 'printBtn'))
            # backward = int(cfg.get(SECTION, 'backward'))
            try:
                for event in dev.read_loop():

                    if event.type == ecodes.EV_KEY and hasattr(event, "code"):
                        if event.value == 1:
                            if event.code == pictureBtn:
                                pygame.event.post(pygame.event.Event(BUTTONDOWN, capture=1, printer=0,
                                                           button=app.buttons.capture))

                                LOGGER.info("pictureBtn")
                            elif event.code == settingsBtn:
                                pygame.event.post(pygame.event.Event(BUTTONDOWN, capture=1, printer=1,
                                                                     button=app.buttons))
                                LOGGER.info("settingsBtn")
                            # if event.code == homeBtn:
                            #     LOGGER.info("homeBtn")
                            # elif event.code == backBtn:
                            #     LOGGER.info("backBtn")
                            # elif event.code == playpause:
                            #     LOGGER.info("Play/Pause")
                            # elif event.code == up:
                            #     keyboard.press(Key.up)
                            #     keyboard.release(Key.up)
                            #     LOGGER.info("up")
                            # elif event.code == down:
                            #     keyboard.press(Key.up)
                            #     keyboard.release(Key.up)
                            #     LOGGER.info("down")
                            elif event.code == left:
                                keyboard.press(Key.left)
                                keyboard.release(Key.left)
                                LOGGER.info("left")
                            elif event.code == right:
                                keyboard.press(Key.right)
                                keyboard.release(Key.right)
                                LOGGER.info("right")
                            elif event.code == printBtn:
                                pygame.event.post(pygame.event.Event(BUTTONDOWN, capture=0, printer=1,
                                                                     button=app.buttons.printer))
                                LOGGER.info("printBtn")
                            # elif event.code == backward:
                            #     LOGGER.info("backward")
            except OSError:
                pass
