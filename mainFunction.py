import tkinter as tk
import tkinter.messagebox as box

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.judul = tk.Label(self, text="Judul Catatan")
        self.judul.pack(side=tk.LEFT)
        self.jEntry = tk.Entry(self, bd=3)
        self.jEntry.pack(side=tk.RIGHT)
        self.iJudul = tk.Label(self, text="Isi Catatan")
        self.iJudul.pack(side=tk.LEFT)
        self.iEntry = tk.Entry(self, bd=3)
        self.iEntry.pack(side=tk.RIGHT)
        self.simpan = tk.Button(self, text="Simpan", command = self.berhasil)
        self.simpan.pack(side=tk.RIGHT)

    def berhasil(self):
        box.showinfo("Sukses","Catatan berhasil disimpan!")