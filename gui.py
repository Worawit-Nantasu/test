import tkinter as tk

# สร้างหน้าต่างหลัก
window = tk.Tk()

# เพิ่ม Label
label = tk.Label(window, text="Hello, world!")
label.pack()

# เพิ่ม Entry
entry = tk.Entry(window)
entry.pack()

# เพิ่ม Button
button = tk.Button(window, text="Click me!")
button.bind("<Button-1>", lambda event: print("You clicked me!"))
button.pack()

# แสดงหน้าต่าง
window.mainloop()
