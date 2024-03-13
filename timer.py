import tkinter as tk

# --- Time preset ---

countdown_preset, countdown_temp = 10, 10
timer_label: tk.Label | None = None

countdown_stop = False
countdown_restart = False


# --- Timer functionality ----


def create_time_bar():
    global timer_label
    timer_label = tk.Label(
        timer, text=f"{time_format(countdown_preset)}", font="Arial 12 bold"
    )
    timer_label.pack(side="top")


def timer_restart():
    global countdown_preset, countdown_temp
    global countdown_stop
    countdown_stop = False
    countdown_preset = countdown_temp
    timer_label.destroy()
    create_time_bar()
    timer_launcher()


def timer_stop():
    global countdown_stop, countdown_preset
    countdown_stop = True
    timer_label_config(time_format(countdown_preset))


def timer_start():
    global countdown_stop
    countdown_stop = False
    timer_countdown(countdown_preset)


def timer_launcher():
    if timer_label is None:
        create_time_bar()
    elif not countdown_stop:
        timer_start()
    elif countdown_stop:
        timer_stop()
    elif countdown_restart:
        timer_restart()


def timer_label_config(time_value: str) -> None:
    """
    Representing the current value of the timer.
    :param time_value: The current value of the timer.
    :return: None.
    """

    timer_label.config(text=time_value, fg="black")


def timer_countdown(duration) -> None:
    """
    Implementing the time countdown.
    :param duration: The starting value of the time countdown.
    :return: None.
    """
    global countdown_preset
    countdown_preset = duration

    if countdown_stop:
        timer_label_config(time_format(countdown_preset))

    elif countdown_preset and not countdown_stop:
        timer_label.after(0, timer_label_config, time_format(countdown_preset))
        timer_label.after(1000, timer_countdown, countdown_preset - 1)


def time_format(seconds) -> str:
    """
    Setting the proper timer value representation.
    :param seconds: The time value in seconds.
    :return: String.
    """
    m, s = divmod(int(seconds), 60)
    return f"Time:{m:02d}:{s:02d}"


# ---- Getting the basic tkinter widget -----
timer = tk.Tk()
timer.title("Timer")
timer.geometry("220x50")
timer.resizable(width=False, height=False)


# ---- Getting the buttons -----


tk.Button(
    timer, text="Start", font="Arial 12 bold", command=lambda: timer_start()
).pack(side="left")
tk.Button(timer, text="Stop", font="Arial 12 bold", command=lambda: timer_stop()).pack(
    side="right",
    padx=3,
    pady=3,
)
tk.Button(
    timer, text="Restart", font="Arial 12 bold", command=lambda: timer_restart()
).pack()

timer_launcher()

timer.mainloop()
