
import time
import random as rm

from sys import platform

import pyautogui as pygui

from appscript import app, k


def sleepRandom():
	time.sleep(rm.uniform(0.5, 1.5))


def type(str):
	for c in str:
		#app('System Events').keystroke(c)
		pygui.press(c)
		time.sleep(rm.uniform(.15, .2))


def moveMouse(x, y):
	pygui.moveTo(x, y, duration=rm.uniform(0.3, 0.7))


def backspace(x):
	for i in range(x):
		pygui.hotkey('backspace')
		time.sleep(rm.uniform(.05, .15))


assert (platform == 'linux' or platform == 'linux2' or platform == 'darwin' or platform == 'win32'), 'platform not found'



if platform == 'linux' or platform == 'linux2': #linux (obviously)

	def copy():
		pygui.hotkey('ctrl', 'shift', 'c')
		time.sleep(rm.uniform(.05, .15))

	def selectAll():
		pygui.hotkey('ctrl', 'shift', 'a')
		time.sleep(rm.uniform(.05, .15))
	def enter():
		pygui.hotkey('enter')
		time.sleep(rm.uniform(.05, .15))

elif platform == 'darwin': #mac os

	def copy():
		#app('System Events').keystroke('c', using=k.command_down)
		pygui.hotkey('command', 'c')
		time.sleep(rm.uniform(.05, .15))

	def selectAll():
		#app('System Events').keystroke('a', using=k.command_down)
		pygui.hotkey('command', 'a')
		time.sleep(rm.uniform(.05, .15))

	def enter():
		pygui.hotkey('return')
		time.sleep(rm.uniform(.05, .15))

elif platform == 'win32': #windows

	def copy():
		pygui.hotkey('ctrl', 'c')
		time.sleep(rm.uniform(.05, .15))

	def selectAll():
		pygui.hotkey('ctrl', 'a')
		time.sleep(rm.uniform(.05, .15))

	def enter():
		pygui.hotkey('enter')
		time.sleep(rm.uniform(.05, .15))

