import serial
import tkinter as tk
from tkinter import ttk
import pygame
import threading

def player():
    pygame.init()
    ser = serial.Serial(port="COM3", baudrate=115200)
    while True:

        for line in ser.readline():
            print(chr(line))

            if chr(line) == '0':
                filename = "notes/C" + str(combobox.get()) + ".wav"
                pygame.mixer.music.load(filename)
                pygame.mixer.music.play()

            if chr(line) == '1':
                filename = "notes/D" + str(combobox.get()) + ".wav"
                pygame.mixer.music.load(filename)
                pygame.mixer.music.play()

            if chr(line) == '2':
                filename = "notes/E" + str(combobox.get()) + ".wav"
                pygame.mixer.music.load(filename)
                pygame.mixer.music.play()
            if chr(line) == '3':
                filename = "notes/F" + str(combobox.get()) + ".wav"
                pygame.mixer.music.load(filename)
                pygame.mixer.music.play()
            if chr(line) == '4':
                filename = "notes/G" + str(combobox.get()) + ".wav"
                pygame.mixer.music.load(filename)
                pygame.mixer.music.play()

            if chr(line) == '5':
                filename = "notes/A" + str(combobox.get()) + ".wav"
                pygame.mixer.music.load(filename)
                pygame.mixer.music.play()

            if chr(line) == '6':
                filename = "notes/B" + str(combobox.get()) + ".wav"
                pygame.mixer.music.load(filename)
                pygame.mixer.music.play()


def tkint():
        while True:
            root = tk.Tk()
            root.title("Scale")
            notes = ['0', '1', '2', '3', '4', '5', '6', '7']
            global combobox
            combobox = ttk.Combobox(root, values=notes)
            combobox.pack()
            if combobox.get() != '':
                print("cb: ", combobox.get())

            root.mainloop()



if __name__ == "__main__":
    tkthread = threading.Thread(target=tkint)
    tkthread.start()
    player_thread = threading.Thread(target=player)
    player_thread.start()
