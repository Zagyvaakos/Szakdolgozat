import pyautogui
import win32gui
import numpy as np
from mss import mss

def take_screenshot(window_title=None):
     
     window = {"left": 0, "top":0, "width": 1280, "height":720}
     capture = mss()
     if window_title:
         hwnd = win32gui.FindWindow(None, window_title)
         if hwnd:
             
             #win32gui.SetForegroundWindow(hwnd)
             x, y, x1, y1 = win32gui.GetClientRect(hwnd)
             x, y = win32gui.ClientToScreen(hwnd, (x, y))
             x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
             region=(x, y, x1, y1)
             frame = np.array(capture.grab(region))
             return frame
         else:
             print('Window not found!')
     else:
          frame = np.array(capture.grab(window))
          return frame

