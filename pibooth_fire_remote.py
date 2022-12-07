from evdev import InputDevice, categorize, ecodes
import pygame

import asyncio
import pibooth
from pibooth.utils import LOGGER

LOGGER.info("Fire Remote Gen 1 - mapping")

#creates object 'gamepad' to store the data
dev = InputDevice('/dev/input/event2')

BUTTONDOWN = pygame.USEREVENT + 1

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

async def helper(dev):
    async for ev in dev.async_read_loop():
        print(repr(ev))

@pibooth.hookimpl
def pibooth_startup(app):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(helper(dev))
    # #loop and filter by event code and print the mapped label
    # for event in gamepad.read_loop():
    #
    #     if event.type == ecodes.EV_KEY:
    #         if event.value == 1:
    #             if event.code == enterBtn:
    #                 event = pygame.event.Event(BUTTONDOWN, capture=1, printer=0,
    #                                            button=app.buttons.capture)
    #
    #                 LOGGER.info("enterBtn")
    #             elif event.code == settingsBtn:
    #                 LOGGER.info("settingsBtn")
    #             if event.code == homeBtn:
    #                 LOGGER.info("homeBtn")
    #             elif event.code == backBtn:
    #                 LOGGER.info("backBtn")
    #             elif event.code == playpause:
    #                 LOGGER.info("Play/Pause")
    #             elif event.code == up:
    #                 LOGGER.info("up")
    #             elif event.code == down:
    #                 LOGGER.info("down")
    #             elif event.code == left:
    #                 LOGGER.info("left")
    #             elif event.code == right:
    #                 LOGGER.info("right")
    #             elif event.code == forward:
    #                 LOGGER.info("forward")
    #             elif event.code == backward:
    #                 LOGGER.info("backward")