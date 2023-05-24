# Image Watermark GUI

Welcome to my Image Watermark-GUI project, a Python-based GUI application for watermarking images. The application was developed by [DanielVenette](https://github.com/DanielVenette) and allows you to select an image, enter a watermark text, adjust its opacity and rotation, and finally save the watermarked image in PNG format.

## Features

1. Intuitive GUI for selecting and watermarking images.
2. Customizable watermark text with adjustable opacity and rotation.
3. Watermarked images saved in PNG format.

## Dependencies

This application requires the following Python libraries:
- tkinter
- PIL (Pillow)

## How to Use

1. Clone this repository or download the source code.
2. Run `main.py` to start the GUI application.
3. Click 'Browse' to select an image to watermark.
4. Enter your desired watermark text in the 'Watermark text:' field.
5. Choose the font size for your watermark text from the dropdown menu.
6. Adjust the opacity of your watermark by clicking the '⬆' or '⬇' buttons.
7. Adjust the rotation of your watermark by clicking the '↺' or '↻' buttons.
8. Click 'Create Watermark' to watermark the image. The watermarked image will be saved in the same directory as the original image, with '_watermarked' appended to the original file name.

## Important

This project was built and tested on Python 3.x and tkinter 8.x. Ensure you are using these versions to avoid any issues.

Also, to ensure the GUI functions properly, `main.py` and `watermarker.py` should be in the same directory.

## Contributions

Contributions to Day-84-Watermark-GUI are always welcome! Whether it's feature improvements, bug fixes, or simply spreading the word, all contributions help improve this project.

Feel free to open issues or submit pull requests.

## License

MIT License
