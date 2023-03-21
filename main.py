from tkinter import *
from tkinter import filedialog as fd
import tkinter.font as font
from tkinter.messagebox import showinfo
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageTk
from watermarker import WaterMarker

BG_BUTTON = '#FEFBE9'
BG = '#E1EEDD'
TEXT_COLOR = '#183A1D'

font_size_choices = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72]
global wm_opacity
global text_rotation
wm_opacity = 50
text_rotation = 0


# select the file to be watermarked
def select_file():
    # available file types
    filetypes = (
        ('PNG Files', '*.png*'),
        ('JPEG Files', '*.jpg'),
        ('TIF Files', '*.tif'),
        ('Bitmap Files', '*.bit'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes,
    )
    # delete anything in the image_path Entry and insert the file path the user chooses
    image_path.delete(0, END)
    image_path.insert(0, filename)

    # update canvas with image to be watermarked (used pillow because tkinter wouldn't handle jpg files).
    # resize image to fiz on canvas if image is bigger than canvas.
    # Open image first using PIL, resize, then convert to PhotoImage:
    image_to_wm = Image.open(image_path.get())  # PIL solution
    image_width = image_to_wm.width
    image_height = image_to_wm.height
    if image_width > canvas.winfo_width() or image_height > canvas.winfo_height():
        ratio = min(canvas.winfo_width() / image_width, canvas.winfo_height() / image_height)
        new_width = int(image_width * ratio)
        new_height = int(image_height * ratio)
        image_to_wm = ImageTk.PhotoImage(image_to_wm.resize((new_width, new_height)))
    else:
        image_to_wm = ImageTk.PhotoImage(Image.open(image_path.get()))  # PIL solution
    # make image a canvas attribute so it doesn't get garbage-collected
    canvas.img = image_to_wm
    canvas.itemconfig(image_id, image=image_to_wm)


# function to wrap the select_file function in a try block in case the file is not found
def safe_select_file():
    try:
        select_file()
    except TclError:
        showinfo("No usable files found",
                 message=f'No usable file found at:\n {image_path.get()}')


# watermark image in file path and then update canvas
def watermark_image():
    # this line calls on the "watermark_generator" method inside the WaterMarker class to create
    # and save the watermarked image
    WaterMarker().watermark_generator(image_path.get(),
                                      clicked.get(),
                                      message=entry_wm_text.get(),
                                      opacity=wm_opacity,
                                      rotation=text_rotation,
                                      canvas_width=canvas.winfo_width(),
                                      canvas_height=canvas.winfo_height(),
                                      )
    # the code below creates a PhotoImage with the watermarked image and updates the canvas with it
    wi_path = image_path.get().split(".")[0] + \
              "_watermarked.png"
    wi = ImageTk.PhotoImage(Image.open(wi_path))  # PIL solution
    canvas.img = wi
    canvas.itemconfig(image_id, image=wi)
    return wi_path


def click_create_watermark():
    wi_path = watermark_image()
    showinfo(title="Image Saved",
             message=f'Watermarked imaged save to:'
                     f'\n {wi_path}'
             )


def change_font_size(font_size):
    watermark_image()


# increase opacity and re-watermark image
def increase_opacity():
    global wm_opacity
    if wm_opacity <= 245:
        wm_opacity += 10
    watermark_image()


# decrease opacity and re-watermark image
def decrease_opacity():
    global wm_opacity
    if wm_opacity >= 10:
        wm_opacity -= 10
    watermark_image()


# rotate 20 degrees counter-clockwise:
def rotate_counter():
    global text_rotation
    text_rotation += 20
    watermark_image()


# rotate 20 degrees clockwise:
def rotate_clockwise():
    global text_rotation
    text_rotation -= 20
    watermark_image()


# create program window
window = Tk()
window.title("Watermark Generator")
window.config(bg=BG)
window.minsize(width=500, height=500)

# show grid outline
# window.grid_rowconfigure(0, weight=1)
# window.grid_columnconfigure(0, weight=1)
# window.grid_propagate(False)
# window.grid_configure(borderwidth=1, highlightthickness=1)


# label that instructs user how to use program
instruction_label = Label(text="Click 'Browse' to find an image to add a watermark to",
                          font=("Arial", 12, "bold")
                          )

# create a canvas for the image, and include a welcome image
canvas = Canvas()
canvas.config(width=500,
              height=500,
              bg=BG,
              highlightthickness=0,
              )

canvas.grid(column=0, row=0, rowspan=7, padx=15, pady=15)
welcome_image = PhotoImage(file="owl_watermarked.png")
image_id = canvas.create_image(250, 250, image=welcome_image)

# create a label asking user to choose an image to watermark
label_1 = Label(text="Please choose an image to watermark:",
                bg=BG,
                foreground=TEXT_COLOR)
label_1.grid(column=1, row=0,
             # sticky="S",
             )

image_path = Entry(width=30)
image_path.grid(column=1, row=1,
                sticky="N"
                )
browse_button = Button(text="Browse",
                       command=select_file,
                       bg=BG_BUTTON,
                       foreground=TEXT_COLOR,
                       padx=5,
                       width=18,
                       )
browse_button.grid(column=2, row=1,
                   sticky="N",
                   padx=20,
                   columnspan=2,
                   )

# create an Entry for the watermark text
label_wm_text = Label(text="Watermark text:",
                      bg=BG,
                      foreground=TEXT_COLOR)
label_wm_text.grid(column=1, row=2)
entry_wm_text = Entry(width=30)
entry_wm_text.grid(column=1, row=3,
                   sticky="N")

# watermark image button
watermark_button = Button(text="Create Watermark",
                          command=click_create_watermark,
                          bg=BG_BUTTON,
                          padx=5,
                          width=18,
                          )
watermark_button.grid(column=2, row=3, columnspan=2,
                      sticky="N")

# Font size picker
label_font_size = Label(text="Font Size:",
                        bg=BG,
                        foreground=TEXT_COLOR,
                        )
label_font_size.grid(column=1, row=4)
clicked = IntVar()
clicked.set(12)
font_size_om = OptionMenu(window, clicked, *font_size_choices, command=change_font_size)
font_size_om.config(bg=BG_BUTTON,
                    padx=5,
                    width=18,
                    )
font_size_om.grid(column=2, row=4, columnspan=2)

# choose opacity
myFont = font.Font(size=12)
label_opacity = Label(text="Opacity:",
                      bg=BG,
                      foreground=TEXT_COLOR,
                      )
label_opacity.grid(column=1, row=5)
button_opacity_up = Button(text="⬆",
                           bg=BG_BUTTON,
                           foreground=TEXT_COLOR,
                           command=increase_opacity,
                           width=3
                           )
button_opacity_up['font'] = myFont
button_opacity_up.grid(column=2, row=5)
button_opacity_down = Button(text="⬇",
                             bg=BG_BUTTON,
                             foreground=TEXT_COLOR,
                             command=decrease_opacity,
                             width=3,
                             )
button_opacity_down['font'] = myFont
button_opacity_down.grid(column=3, row=5)

# change watermark rotation
label_rotation = Label(text="Rotation:",
                       bg=BG,
                       foreground=TEXT_COLOR,
                       )
label_rotation.grid(column=1, row=6)
button_counter_rotation = Button(text='↺',
                                 bg=BG_BUTTON,
                                 foreground=TEXT_COLOR,
                                 command=rotate_counter,
                                 width=3,
                                 )
button_counter_rotation.grid(column=3, row=6)
button_clockwise_rotation = Button(text='↻',
                                   bg=BG_BUTTON,
                                   foreground=TEXT_COLOR,
                                   command=rotate_clockwise,
                                   width=3,
                                   )
button_clockwise_rotation.grid(column=2, row=6)

mainloop()
