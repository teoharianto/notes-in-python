import tkinter as tk
import tkinter.messagebox as box

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        frm1 = tk.Frame(self)
        frm1.pack(fill=tk.BOTH)
        self.judul = tk.Label(frm1, text="  Judul", width=4)
        self.judul.pack(side=tk.LEFT,padx=5, pady=5)
        self.jEntry = tk.Entry(frm1)
        self.jEntry.pack(fill=tk.BOTH,padx=5, pady=3, expand=True)
        
        frm2 = tk.Frame(self)
        frm2.pack(fill=tk.BOTH, expand=True)
        self.iJudul = tk.Label(frm2, text="Isi", width=2)
        self.iJudul.pack(side=tk.LEFT,padx=12, pady=5)
        self.iEntry = tk.Entry(frm2)
        self.iEntry.pack(fill=tk.BOTH, anchor=tk.N, padx=5, pady=5, expand=True, orient=tk.VERTICAL)

        self.simpan = tk.Button(self, text="Simpan", width=10, command = self.berhasil)
        self.simpan.pack(side=tk.RIGHT, anchor=tk.N,padx=5, pady=7)

    def berhasil(self):
        box.showinfo("Sukses","Catatan berhasil disimpan!")