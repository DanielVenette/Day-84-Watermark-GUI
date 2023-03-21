import PIL.Image
from PIL import Image, ImageDraw, ImageFont


class WaterMarker:

    def __init__(self):
        self.x = 0

    def watermark_generator(self, filepath: str,
                            font_size: int,
                            opacity: int,
                            rotation: int,
                            message: str,
                            canvas_width: int,
                            canvas_height: int,
                            ):
        with Image.open(filepath).convert("RGBA") as im:
            im_width = im.width
            im_height = im.height
            if im_width > canvas_width or im_height > canvas_height:
                ratio = min(canvas_width / im_width, canvas_height / im_height)
                new_width = int(im_width * ratio)
                new_height = int(im_height * ratio)
                im = im.resize((new_width, new_height))

            # make a blank image, the same size as the imported image, initialized to transparent text color
            txt = Image.new("RGBA", im.size, (255, 255, 255, 0))

            # get a font
            fnt = ImageFont.FreeTypeFont("C:/Windows/Fonts/FORTE.TTF", font_size)
            text_width = fnt.getsize(message)[0]
            text_height = fnt.getsize(message)[1]
            # get a drawing context
            d = ImageDraw.Draw(txt)

            # draw text, opacity/255 opacity
            d.text((int((im.size[0] - text_width) / 2),
                    int((im.size[1] - text_height) / 2)),
                   message, font=fnt, fill=(255, 255, 255, opacity))
            # rotate text by "rotation" degrees
            txt1 = txt.rotate(rotation, PIL.Image.NEAREST, expand=1)
            txt1 = txt1.resize(txt.size)
            # combine the image and text into a watermarked image
            watermarked_image = Image.alpha_composite(im, txt1)

            # save image as .png
            filepath_no_ext = filepath.split(".")[0]
            watermarked_image.save(filepath_no_ext + "_watermarked" + ".png")
