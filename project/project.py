import librosa
import soundfile as sf
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def changer(src, mode):
    audio = src
    y, sr = librosa.load(audio)
    y_ps = librosa.effects.pitch_shift(y, sr, n_steps=mode)
    sf.write(src.replace('.wav', '_change.wav'), y_ps, sr)
    messagebox.showinfo('Done', '音檔轉好囉！')

    return

def readfile():
    src_entry.delete(0, 'end')
    src = filedialog.askopenfilename(parent=root, title='請選擇wav檔', initialdir='~/Desktop/', filetypes=(('wav files','*.wav'),('all files','*.*')))
    src_entry.insert(0, src)

    global file
    file = src

    return

def choosegender(btn):
    if btn==0:
        gen_str.set('我是女生')
    else:
        gen_str.set('我是男生')

    global gen
    gen = btn

    return

def choosetype(btn):
    if btn==1:
        btn_str.set('想變超低音')
    elif btn==2:
        btn_str.set('想變低音')
    elif btn==3:
        btn_str.set('想變高音')
    else:
        btn_str.set('想變超高音')

    global pitch
    pitch = btn

    return

def go():
    try:
        if gen==1:
            if pitch==1:
                level = -5
            elif pitch==2:
                level = -3
            elif pitch==3:
                level = 10
            else:
                level = 13    
        else:
            if pitch==1:
                level = -7
            elif pitch==2:
                level = -5
            elif pitch==3:
                level = 5
            else:
                level = 8

        changer(file, level)

    except:
        messagebox.showinfo('Warning', '性別、音高、音檔都要選好！')

    return


root = tk.Tk()
f = tk.Frame()
f.grid(row=0, column=0)
root.iconbitmap('mic.ico')
root.title('簡易變聲小工具')
root.geometry('372x150')

gender_label = tk.Label(f, text='我是', width=5)
gender_label.grid(row=0, column=0)
gender_btn1 = tk.Button(f, text='女生 ♀', width=10, command=lambda: choosegender(0))
gender_btn1.grid(row=0, column=1)
gender_btn2 = tk.Button(f, text='男生 ♂', width=10, command=lambda: choosegender(1))
gender_btn2.grid(row=0, column=2) 

type_label = tk.Label(f, text='想變', width=5)
type_label.grid(row=1, column=0)
type_btn1 = tk.Button(f, text='超低音', width=10, command=lambda: choosetype(1))
type_btn1.grid(row=1, column=1)
type_btn2 = tk.Button(f, text='低音', width=10, command=lambda: choosetype(2))
type_btn2.grid(row=1, column=2)
type_btn3 = tk.Button(f, text='高音', width=10, command=lambda: choosetype(3))
type_btn3.grid(row=1, column=3)
type_btn3 = tk.Button(f, text='超高音', width=10, command=lambda: choosetype(4))
type_btn3.grid(row=1, column=4)

gen_str = tk.StringVar()
gen_label = tk.Label(f, textvariable=gen_str)
gen_label.grid(row=2, column=1, sticky='W')

btn_str = tk.StringVar()
btn_label = tk.Label(f, textvariable=btn_str)
btn_label.grid(row=2, column=2, columnspan=2, sticky='W')

src_label = tk.Label(f, text='音檔', width=5)
src_label.grid(row=3, column=0)
src_str = tk.StringVar()
src_entry = tk.Entry(f, textvariable=src_str, width=33)
src_entry.grid(row=3, column=1, columnspan=3, sticky='W')
src_entry.insert(0, ' 請選擇wav檔')
src_btn = tk.Button(f, text='選擇檔案', width=10, command= lambda: readfile())
src_btn.grid(row=3, column=4)

space = tk.Label(f).grid(row=4, column=0)

go_btn = tk.Button(f, text='GO！', width=45, background='gray', foreground='white', command= lambda: go())
go_btn.grid(row=5, column=0, columnspan=5)


f.mainloop()