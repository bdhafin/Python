import tkinter as tk

main_window = tk.Tk()
def event_tekan():
    label2 = tk.Label(main_window, text="Ini hasil dari tekan")
    label2.pack()

#menampilkan text
label = tk.Label(main_window, text="Halo, saya adalah \n GUI sederhana dengan \n menggunakan Python")
#membuat button
tombol = tk.Button(main_window, text="Click Here", command = event_tekan)

#menyimpan di main windows
label.pack()
tombol.pack()


#mengeluarkan display
main_window.mainloop()