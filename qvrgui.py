import time
import tkinter # sudo apt-get install python3-tk
from tkinter import ttk
from tkinter import messagebox
import qvrRecording
import threading
import logging

videorecorder = qvrRecording.QvrRecording()


win = tkinter.Tk()
win.title("Que's Video Recorder")

#def dialog():
#    messagebox.showerror("NO NO", "Da Fiji deaf net Wixxn!")

# def start_recording():
#    videorecorder.start_recording("12345")


def start_recordingx():
    logging.info("Thread %s: starting")
    videorecorder.start_recording("12345")
    logging.info("Thread %s: finishing")


def start_recording_thread():
    x = threading.Thread(target=start_recordingx, daemon=True)
    logging.info("Main    : before running thread")
    x.start()
    # time.sleep(10)


ttk.Button(win, text='record', command=start_recording_thread).pack()

win.mainloop()