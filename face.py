import threading
import random
import time
import tkinter as tk


class Face(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.speaking = False
        self.started = False
        self._lock = threading.Lock()
        self._ready = threading.Event()
        self.start()
        self._ready.wait(timeout=3)

    def set_speaking(self, val: bool):
        with self._lock:
            self.speaking = bool(val)

    def run(self):
        try:
            self.root = tk.Tk()
            self.root.title("Max")
            self.root.configure(bg="black")
            self.root.geometry("420x260")
            self.root.resizable(False, False)
            self.canvas = tk.Canvas(self.root, width=420, height=260, bg="black", highlightthickness=0)
            self.canvas.pack()
            self.left_eye = self.canvas.create_oval(90, 70, 170, 130, fill="#00ffaa", outline="")
            self.right_eye = self.canvas.create_oval(250, 70, 330, 130, fill="#00ffaa", outline="")
            self.mouth = self.canvas.create_rectangle(140, 170, 280, 175, fill="#00ffaa", outline="")
            self.next_blink = time.time() + random.uniform(2.5, 4.5)
            self._ready.set()
            self.animate()
            self.root.mainloop()
        except Exception:
            self._ready.set()
            return

    def animate(self):
        try:
            with self._lock:
                speaking = self.speaking
            if speaking:
                amp = random.randint(4, 22)
                y1 = 172 - amp // 2
                y2 = 172 + amp // 2
                self.canvas.coords(self.mouth, 140, y1, 280, y2)
                self.canvas.itemconfig(self.mouth, fill="#00ffaa")
            else:
                self.canvas.coords(self.mouth, 160, 172, 260, 176)
                self.canvas.itemconfig(self.mouth, fill="#008877")
            t = time.time()
            if t >= self.next_blink:
                self.canvas.itemconfig(self.left_eye, fill="black")
                self.canvas.itemconfig(self.right_eye, fill="black")
                self.root.after(120, self._open_eyes)
                self.next_blink = t + random.uniform(2.5, 4.5)
            self.root.after(60, self.animate)
        except Exception:
            return

    def _open_eyes(self):
        try:
            self.canvas.itemconfig(self.left_eye, fill="#00ffaa")
            self.canvas.itemconfig(self.right_eye, fill="#00ffaa")
        except Exception:
            pass


try:
    face = Face()
except Exception:
    face = None


def set_speaking(val: bool):
    if face:
        face.set_speaking(val)
