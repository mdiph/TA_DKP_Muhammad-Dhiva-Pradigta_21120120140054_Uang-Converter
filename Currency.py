#untuk menggunakan GUI dari library tkinter
import tkinter 
from tkinter import ttk
from tkinter import messagebox
from userService import userService

#untuk mengatur judul dan ukuran window GUI
root = tkinter.Tk()
root.title('Uang Converter By M.Dhiva.P')
root.geometry("600x600")

#untuk buat tab di atas
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=10)

#untuk buat 3 frame, currency, convert dan login
login_frame = tkinter.Frame(my_notebook, width=500,height=500)
currency_frame = tkinter.Frame(my_notebook, width = 500, height = 500)
conversion_frame = tkinter.Frame(my_notebook, width = 500, height = 500)

#untuk menset frame agar mengisi screen, seukuran 500px^
login_frame.pack(fill="both",expand=1)
currency_frame.pack(fill = "both",expand = 1)
conversion_frame.pack(fill = "both",expand = 1)

#untuk menambahkan tabs
my_notebook.add(login_frame,text="Login User")
my_notebook.add(currency_frame,text = "Mata Uang")
my_notebook.add(conversion_frame,text = "Convert")

#untuk matiin tab ke dua biar gak di akses duluan
my_notebook.tab(1, state='disabled')
my_notebook.tab(2,state='disabled')

#buat bagusin (memberikan warna pada frame)tkinter nya
j=0
r=200
for i in range(5):
    c=str(994422+r)
    tkinter.Frame(login_frame,width=500,height=500,bg="#"+c).place(x=j,y=0)
    tkinter.Frame(currency_frame,width=500,height=500,bg="#"+c).place(x=j,y=0)
    tkinter.Frame(conversion_frame,width=500,height=500,bg="#"+c).place(x=j,y=0)
    j=j+100
    r=r+1000
#####################
#Untuk TAB LOGIN USER
####################
#buat function login
def login():
    if len(stringEmail.get()) == 0:
        messagebox.showwarning("Email Salah!", "Harap Masukkan Email ... ")
    else:
        email = stringEmail.get()
        auth = userService(email)
        get_data = auth.login()
        if get_data:
            messagebox.showwarning(
                "SUKSES", "Email anda benar... Halo " + email)
            # buat matiin email entry biar tidak bisa di edit
            root.title('Welcome User ' + email)
            email_entry.config(state="disabled")
            # buat idupin tab kedua/ mata uang
            my_notebook.tab(1, state='normal')
            # buat matiin tab login
            my_notebook.tab(0, state="disabled")
        else:
            messagebox.showwarning("Perhatian", "Email anda salah ..")

#Buat masukin email
email = tkinter.LabelFrame(login_frame, text="Masukkan Email Anda...")
email.pack(pady=20)

#Buat Entry email
stringEmail = tkinter.StringVar()
email_entry= tkinter.Entry(email, font=("Calibri",24),textvariable=stringEmail)
email_entry.pack(pady=10,padx=10)

#frame tombol
login_frame = tkinter.Frame(login_frame)
login_frame.pack(pady=20)

#Buat Tombol Login di tab Login
login_button = tkinter.Button(login_frame, text="Login",command=login)
login_button.grid(row=0,column=0,padx=0)

#####################
#untuk TAB  Mata Uang
#####################
def lock():
    if not home_entry.get() or not conversion_entry.get() or not rate_entry.get():
        messagebox.showwarning("PERHATIAN!","Ayo Isi Semuanya!")

    else:
        #ini buat matiinn/disable entry field kalo udah di lock/kunci
        home_entry.config(state="disabled")
        conversion_entry.config(state="disabled")
        rate_entry.config(state="disabled")
        #ini buat enable atau idupin tab convert dan tab mata uang
        my_notebook.tab(2, state='normal')
        #dibawah ini buat ganti nama dari entry yang ada di tab convert
        amount_label.config(text=f'Jumlah Dari {home_entry.get()} Ke {conversion_entry.get()}...')
        converted_label.config(text=f'Jumlah Mata Uang {conversion_entry.get()}')
        convert_button.config(text=f'Convert Dari {home_entry.get()}')

def unlock():
    #ini buat enable atau buka entry box
    home_entry.config(state="normal")
    conversion_entry.config(state="normal")
    rate_entry.config(state="normal")
    #ini buat disable atau matiin tab kalau tombol buka di pencet
    my_notebook.tab(2,state='disabled')

#Buat set mata uang utama
home = tkinter.LabelFrame(currency_frame, text="Mata Uang Utama")
home.pack(pady=20)

#mata uang entry box
home_entry = tkinter.Entry(home, font=("Calibri",24))
home_entry.pack(pady=10,padx=10)

#Konversi Frame
conversion = tkinter.LabelFrame(currency_frame, text="Mata Uang Konversi")
conversion.pack(pady=20)

#label konversi 
conversion_label = tkinter.Label(conversion, text="Mata Uang Di Convert Ke...")
conversion_label.pack(pady=10)

#entry konversi
conversion_entry = tkinter.Entry(conversion, font=("Calibri",24))
conversion_entry.pack(pady=10, padx=10)

#label rate 
rate_label = tkinter.Label(conversion, text="Rate Mata Uang Sekarang...")
rate_label.pack(pady=10)

#entry rate
rate_entry = tkinter.Entry(conversion, font=("Calibri",24))
rate_entry.pack(pady=10, padx=10)

#frame tombol
button_frame = tkinter.Frame(currency_frame)
button_frame.pack(pady=20)

#Buat TOMBOL 
lock_button = tkinter.Button(button_frame, text="Kunci",command=lock)
lock_button.grid(row=0,column=0,padx=0)

unlock_button = tkinter.Button(button_frame, text="Buka",command=unlock)
unlock_button.grid(row=0,column=1,padx=0)

###################
#untuk TAB konversi 
###################
def convert():
    #buat hapus entry box nya  
    converted_entry.delete(0, tkinter.END)
    #perhitungan konversi nya
    hasilnya = float(rate_entry.get()) * float(amount_entry.get())
    #buat buletin biar desimal gak kebanyakan
    hasilnya = round(hasilnya, 2)
    #buat nambahin KOMA, biar gampang liat angka jutaan 
    hasilnya = '{:,}'.format(hasilnya)
    #buat update entry box
    converted_entry.insert(0, hasilnya)
    #disable converted entry
    converted_entry.config(state="disabled")

def clear():
    amount_entry.delete(0, tkinter.END)
    #buat enable converted entry
    converted_entry.config(state="normal")
    converted_entry.delete(0, tkinter.END)

#buat frame jumlah uang yang pengen di convert
amount_label = tkinter.LabelFrame(conversion_frame, text = "Banyaknya Uang Yang Ingin Di Konversikan...")
amount_label.pack(pady=20)

#entry box buat banyaknya uang
amount_entry = tkinter.Entry(amount_label, font=("Calibri",24))
amount_entry.pack(pady=10,padx=10)

#tombol konversi
convert_button = tkinter.Button(amount_label, text="Konversi",command =convert)
convert_button.pack(pady=20)

#frame dari converted(hasilnya)
converted_label = tkinter.LabelFrame(conversion_frame, text="Mata Uang Terkonversi")
converted_label.pack(pady=20)

#entry dari converted (hasilnya)
converted_entry = tkinter.Entry(converted_label, font=("Calibri",24), bd=0, bg="systembuttonface")
converted_entry.pack(pady=10, padx=10)

#tombol hapus
clear_button = tkinter.Button(conversion_frame, text="Clear", command=clear)
clear_button.pack(pady=20)

#buat kasih spacer, biar lebih bagus
spasi = tkinter.Label(conversion_frame, text="", width= 70)
spasi.pack()

root.mainloop()