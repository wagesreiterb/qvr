import tkinter as tk
import uuid
from tkinter import ttk
import subprocess


def get_uuid4():
    return str(uuid.uuid4())[:8]


vlc_handle = 0


def start_vlc():
    global vlc_handle
    vlc_handle = subprocess.Popen(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe'], shell=True)



def stop_vlc():
    vlc_handle.terminate()


def get_recordings_list():
    entry_one_list = (get_uuid4(), 'Buccaneers_at_Bears', '2314', '2023-10-07 02:00 AM EDT', '2023-10-07 05:00 AM EDT')
    entry_two_list = (get_uuid4(), '49ers_at_Dolphins', '2314', '2023-10-07 02:00 AM EDT', '2023-10-07 05:00 AM EDT')
    recordings_list = (entry_one_list, entry_two_list)

    return recordings_list

padx = '5'
pady = '5'

window = tk.Tk()
window.geometry("660x480")
window.title("Que's Video Recorder")
# window.resizable(0, 0)
window.columnconfigure(0, weight=1)

text1 = tk.StringVar()
text1.set('text')


def add_recording_frame():
    frame_recording = tk.LabelFrame(window, text="recording")
    frame_recording.columnconfigure(0, weight=1)
    frame_recording.columnconfigure(1, weight=3)
    frame_recording.columnconfigure(2, weight=1)
    frame_recording.columnconfigure(3, weight=3)
    frame_recording.columnconfigure(4, weight=1)
    frame_recording.columnconfigure(5, weight=1)
    frame_recording.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
    # frame_recording.grid_propagate(0)
    label_title = tk.Label(frame_recording, text='title', justify="right")
    label_title.grid(row=0, column=0)
    entry_title  = tk.Entry(frame_recording, textvariable=text1, font=('calibre', 10, 'normal'))
    entry_title .grid(row=0, column=1, padx='10', pady='10')
    label_channel = tk.Label(frame_recording, text='channel', justify="right")
    label_channel.grid(row=0, column=3)
    entry_channel = tk.Entry(frame_recording, textvariable=text1, font=('calibre', 10, 'normal'))
    entry_channel.grid(row=0, column=4, padx='10', pady='10')
    label_start = tk.Label(frame_recording, text='start', justify="right")
    label_start.grid(row=1, column=0)
    entry_start = tk.Entry(frame_recording, textvariable=text1, font=('calibre', 10, 'normal'))
    entry_start.grid(row=1, column=1, padx='10', pady='10')
    label_end = tk.Label(frame_recording, text='end', anchor="e", justify="right")
    label_end.grid(row=1, column=3)
    entry_end = tk.Entry(frame_recording, textvariable=text1, font=('calibre', 10, 'normal'))
    entry_end.grid(row=1, column=4, padx='10', pady='10')

    button_width = 10
    pad_x = 5
    pad_y = 5
    btn_rec = tk.Button(frame_recording, text="rec", command=start_vlc, width=button_width)
    btn_rec.grid(row=0, column=5, sticky='ew', padx=pad_x, pady=pad_y)
    btn_stop = tk.Button(frame_recording, text="stop", width=button_width, padx=pad_x, pady=pad_y)
    btn_stop.grid(row=0, column=6, sticky='ew', padx=pad_x, pady=pad_y)
    btn_schedule = tk.Button(frame_recording, text="schedule", width=button_width, padx=pad_x, pady=pad_y)
    btn_schedule.grid(row=1, column=5, sticky='ew', padx=pad_x, pady=pad_y)
    btn_schedule = tk.Button(frame_recording, text="delete", width=button_width, padx=pad_x, pady=pad_y)
    btn_schedule.grid(row=1, column=6, sticky='ew', padx=pad_x, pady=pad_y)


def add_scheduled_frame():
    frame_scheduled = tk.LabelFrame(window, text="scheduled")
    frame_scheduled.grid(row=1, column=0, padx=20, pady=0, sticky="ew")

    s = ttk.Style()
    s.theme_use('clam')
    tree = ttk.Treeview(frame_scheduled, column=("c1", "c2", "c3", "c4", "c5"), show='headings', height=5)

    #tree.column("# 1", anchor=CENTER, width=100)
    tree.column("# 1", width=60)
    tree.heading("# 1", text="uuid")
    tree.heading("# 2", text="title")
    tree.heading("# 3", text="channel")
    tree.column("# 3", width=60)
    tree.heading("# 4", text="start_time")
    tree.heading("# 5", text="end_time")


    # tree.insert('', 'end', text="1", values=entry_one_list)
    # tree.insert('', 'end', text="1", values=entry_two_list)
    for entry_list in get_recordings_list():
        tree.insert('', 'end', text="1", values=entry_list)

    scrollbar = ttk.Scrollbar(frame_scheduled, orient='vertical', command=tree.yview)
    scrollbar.grid(row=0, column=1, sticky=tk.NS)
    tree['yscrollcommand'] = scrollbar.set

    tree.grid(row=0, column=0, padx=0, pady=0, sticky="ew")


add_recording_frame()
add_scheduled_frame()
window.mainloop()
