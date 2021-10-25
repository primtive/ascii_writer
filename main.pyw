from PIL import Image
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfile
import pyperclip

root = tk.Tk()
root.configure(background='#333333')
root.title('ASCII Writer')
root.geometry("900x700+200+200")
root.resizable(False, False)

filename = ''


def convert(resolution: int):
    global filename, chars_t

    img = Image.open(filename)

    width, height = img.size
    aspect_ratio = height / width
    new_width = int(resolution)
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))

    img = img.convert('L')

    pixels = img.getdata()

    chars_l = list(chars_t.get("1.0", "end"))

    new_pixels = [chars_l[pixel // len(chars_l)] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)

    if width > height: highest = width/height
    else: highest = height/width

    converted_text.delete(1.0, "end")
    converted_text.insert(1.0, ascii_image)


def file_picker():
    global filename
    filename = askopenfilename(initialdir="/",
                               title="Select file",
                               filetypes=(("Все файлы", "*.*"),
                                          (".jpg", "*.jpg"),
                                          (".jpeg", "*.jpeg"),
                                          (".png", "*.png"),
                                          (".ico", "*.ico"),))
    convert(scale.get())


def save():
    ascii_image = converted_text.get("1.0", "end")
    if len(ascii_image) > 0:
        f = asksaveasfile(mode='w', defaultextension=".txt", filetypes=[("Текстовый документ", "*.txt")])
        if f is None:
            return
        f.write(ascii_image)
        f.close()


def copy():
    string = converted_text.get("1.0", "end")
    pyperclip.copy(string)


def font(fontsize: int):
    converted_text.config(font='Courier ' + str(fontsize))


converted_text = tk.Text(root,
                         borderwidth=0,
                         background='#262626',
                         fg='white',
                         insertbackground='white')

select_button = tk.Button(root,
                          text='Выбрать файл',
                          command=file_picker,
                          background='#393939',
                          borderwidth=0,
                          relief='solid',
                          fg='white')

save_button = tk.Button(root,
                        text='Сохранить как текст',
                        command=save,
                        background='#393939',
                        borderwidth=0,
                        relief='solid',
                        fg='white')

copy_button = tk.Button(root,
                        text='Скопировать как текст',
                        command=copy,
                        background='#393939',
                        borderwidth=0,
                        relief='solid',
                        fg='white')

scale = tk.Scale(root, orient=tk.HORIZONTAL,
                 length=200,
                 from_=0,
                 to=1000,
                 tickinterval=10,
                 command=convert,
                 bg='#393939',
                 highlightbackground='#393939',
                 highlightcolor='#393939',
                 troughcolor='#262626',
                 fg='#393939',
                 borderwidth=0,
                 relief='solid',
                 showvalue=0)

scale_text = tk.Label(root,
                      text='Разрешение изображения',
                      bg='#393939',
                      fg='white')

font_scale = tk.Scale(root, orient=tk.HORIZONTAL,
                      length=200,
                      from_=1,
                      to=100,
                      tickinterval=10,
                      command=font,
                      bg='#393939',
                      highlightbackground='#393939',
                      highlightcolor='#393939',
                      troughcolor='#262626',
                      fg='#393939',
                      borderwidth=0,
                      relief='solid',
                      showvalue=0)

font_text = tk.Label(root,
                     text='Размер шрифта',
                     bg='#393939',
                     fg='white')

chars_t = tk.Text(root,
                borderwidth=0,
                background='#262626',
                fg='white',
                insertbackground='white')

chars_text = tk.Label(root,
                      text='Символы:',
                      bg='#393939',
                      fg='white')

#

converted_text.place(x=0, y=0,
                     width=700, height=700)

select_button.place(x=700, y=0,
                    width=200, height=30)

scale.place(x=700, y=40,
            width=200, height=40)
scale_text.place(x=700, y=60,
                 width=200, height=20)

font_scale.place(x=700, y=100,
                 width=200, height=40)
font_text.place(x=700, y=120,
                width=200, height=20)

copy_button.place(x=700, y=630,
                  width=200, height=30)

save_button.place(x=700, y=670,
                  width=200, height=30)

chars_text.place(x=700, y=500,
                 width=200, height=30)
chars_t.place(x=700, y=530,
            width=200, height=100)
chars_t.insert(1.0, ".,'*\"-:/+!2P%#")

root.mainloop()