import serial
import win32api
import win32con
import win32gui

# Constants for Windows API
WM_APPCOMMAND = 0x0319
APPCOMMAND_VOLUME_UP = 0x0a
APPCOMMAND_VOLUME_DOWN = 0x09

# Open serial port
ser = serial.Serial('COM3', 9600)  # Change COM3 to your Arduino's COM port

def set_volume(current_volume, target_volume):
    if current_volume < target_volume:
        for _ in range(target_volume - current_volume):
            win32api.SendMessage(win32gui.GetForegroundWindow(), WM_APPCOMMAND, 0, APPCOMMAND_VOLUME_UP * 0x10000)
    elif current_volume > target_volume:
        for _ in range(current_volume - target_volume):
            win32api.SendMessage(win32gui.GetForegroundWindow(), WM_APPCOMMAND, 0, APPCOMMAND_VOLUME_DOWN * 0x10000)

def get_volume_level():
    return 50

current_volume = get_volume_level()

while True:
    if ser.in_waiting > 0:
        pot_value = int(ser.readline().strip())
        target_volume = pot_value * 100 // 700
        if target_volume != current_volume:
            set_volume(current_volume, target_volume)
            current_volume = target_volume
