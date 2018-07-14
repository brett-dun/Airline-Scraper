

from subprocess import Popen, PIPE, STDOUT

p = Popen(['open', 'https://aa.com'], stdin=PIPE, stdout=PIPE)

import pyautogui as pygui
import time

import random

from appscript import app, k

def sleepRandom():
	time.sleep(random.uniform(0.5, 1.5))

def type(str):
	for c in str:
		app('System Events').keystroke(c)
		time.sleep(random.uniform(.05, .15))

#round trip
pygui.moveTo(494, 633, duration=random.uniform(0.5, 1))
sleepRandom()
pygui.click(494, 633)
#one way
#pygui.click(584, 635)

sleepRandom()

#departing location
pygui.position(554, 749, duration=random.uniform(0.5, 1))
sleepRandom()
pygui.click(554, 749)

sleepRandom()

#app('System Events').keystroke('N', using=k.command_down)
type('\b\b\b')
type()