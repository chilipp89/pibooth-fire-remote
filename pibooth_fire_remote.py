import threading

from evdev import InputDevice, categorize, ecodes
import pygame

import pibooth
from pibooth.utils import LOGGER


__version__ = "0.1.4"

try:
    #creates object 'fire tv remote' to store the data
    dev = InputDevice('/dev/input/event2')
except FileNotFoundError:
    LOGGER.warning("Bluetooth device not Found.")
    dev = None

BUTTONDOWN = pygame.USEREVENT + 1

SECTION = "FIRE-Remote"

@pibooth.hookimpl
def pibooth_configure(cfg):
    #button code variables (change to suit your device)
    cfg.add_option(SECTION, 'enterBtn', 96,
                       "Enter Button Code")
    cfg.add_option(SECTION, 'backBtn', 158,
                   "Back Button Code")
    cfg.add_option(SECTION, 'settingsBtn', 139,
                   "Setting Button Code")
    cfg.add_option(SECTION, 'homeBtn', 172,
                   "Home Button Code")
    cfg.add_option(SECTION, 'up', 103,
                   "Up Button Code")
    cfg.add_option(SECTION, 'down', 108,
                   "Down Button Code")
    cfg.add_option(SECTION, 'left', 105,
                   "Left Button Code")
    cfg.add_option(SECTION, 'right', 106,
                   "Right Button Code")
    cfg.add_option(SECTION, 'playpause', 164,
                   "Play Button Code")
    cfg.add_option(SECTION, 'forward', 208,
                   "Forward Button Code")
    cfg.add_option(SECTION, 'backward', 168,
                   "Backward Button Code")


@pibooth.hookimpl
def pibooth_startup(cfg, app):
    if dev is not None:
        th = threading.Thread(target=run_event_monitor, args=(cfg, app))
        th.daemon = True
        th.start()

def run_event_monitor(cfg, app):
    #loop and filter by event code and print the mapped label
    if dev is not None:

        enterBtn = int(cfg.get(SECTION, 'enterBtn'))
        backBtn = int(cfg.get(SECTION, 'backBtn'))
        settingsBtn = int(cfg.get(SECTION, 'settingsBtn'))
        homeBtn = int(cfg.get(SECTION, 'homeBtn'))
        up = int(cfg.get(SECTION, 'up'))
        down = int(cfg.get(SECTION, 'down'))
        left = int(cfg.get(SECTION, 'left'))
        right = int(cfg.get(SECTION, 'right'))
        playpause = int(cfg.get(SECTION, 'playpause'))
        forward = int(cfg.get(SECTION, 'forward'))
        backward = int(cfg.get(SECTION, 'backward'))

        for event in dev.read_loop():

            if event.type == ecodes.EV_KEY and hasattr(event, "code"):
                if event.value == 1:
                    if event.code == enterBtn:
                        pygame.event.post(pygame.event.Event(BUTTONDOWN, capture=1, printer=0,
                                                   button=app.buttons.capture))

                        LOGGER.info("enterBtn")
                    elif event.code == settingsBtn:
                        pygame.event.post(pygame.event.Event(BUTTONDOWN, capture=1, printer=1,
                                                             button=app.buttons))
                        LOGGER.info("settingsBtn")
                    if event.code == homeBtn:
                        LOGGER.info("homeBtn")
                    elif event.code == backBtn:
                        LOGGER.info("backBtn")
                    elif event.code == playpause:
                        LOGGER.info("Play/Pause")
                    elif event.code == up:
                        LOGGER.info("up")
                    elif event.code == down:
                        LOGGER.info("down")
                    elif event.code == left:
                        LOGGER.info("left")
                    elif event.code == right:
                        LOGGER.info("right")
                    elif event.code == forward:
                        pygame.event.post(pygame.event.Event(BUTTONDOWN, capture=0, printer=1,
                                                             button=app.buttons.printer))
                        LOGGER.info("forward")
                    elif event.code == backward:
                        LOGGER.info("backward")
