# (11 - 1) % 21 + 1 = 11
from os import path
import math
import numpy as np
from PIL import Image, ImageFont, ImageDraw
from fontTools.ttLib import TTFont
from binarization import static_binarization
from lab5.lab5 import calculate_profile, cut_white
from itertools import product

greek_letters = list('AΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ')
sharp_letters = 'AΔΛ'
hang_letters = 'ΓΡ'
symm_hang_letters = 'ΤΥΨ'
bi_grams = [hang + sharp for hang, sharp in product(hang_letters, sharp_letters)] + \
           [hang + sharp for hang, sharp in product(symm_hang_letters, sharp_letters)] + \
           [sharp + hang for hang, sharp in product(symm_hang_letters, sharp_letters)] # + \
           # ['´' + letter for letter in greek_letters] + \
           # [letter + '´' for letter in greek_letters]
symbol_set = greek_letters + bi_grams + ['´']
font_path = path.join('fonts', 'Times New Roman Greek Regular.ttf')
font_size = 52


def filename(n):
    return f"generated/letter_{str(n + 1).zfill(2)}.png"


class FontDrawer:
    def __init__(self):
        self.font = TTFont(font_path)
        self.img_font = ImageFont.truetype(font_path, font_size)
        self.cmap = self.font['cmap']
        self.t = self.cmap.getcmap(3, 1).cmap
        self.s = self.font.getGlyphSet()
        self.units_per_em = self.font['head'].unitsPerEm

    def render_text(self, text):
        img = Image.new(mode="RGB",
                        size=(math.ceil(self.get_text_width(text, font_size)), font_size),
                        color="white")
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), text, (0, 0, 0), font=self.img_font)
        return img

    def render_binarized(self, text, level=100):
        img = self.render_text(text)
        return 255 - static_binarization(np.array(img), level)

    def get_char_width(self, c, point_size):
        assert len(c) == 1
        if ord(c) in self.t and self.t[ord(c)] in self.s:
            pts = self.s[self.t[ord(c)]].width
        else:
            pts = self.s['.notdef'].width
        return pts * float(point_size) / self.units_per_em

    def get_text_width(self, text, point_size):
        total = 0
        for c in text:
            total += self.get_char_width(c, point_size)
        return total


def save_arr_as_img(arr, file_name):
    binarized_letter = Image.fromarray(255 - arr, 'L')
    binarized_letter = binarized_letter.convert('1')
    binarized_letter.save(file_name)


if __name__ == '__main__':
    font_drawer = FontDrawer()
    # letters that can merge
    for i, letter in enumerate(symbol_set[:-1]):
        binarized_arr = font_drawer.render_binarized(letter)
        # Delete white around letter
        for axis in (0, 1):
            letter_profile = calculate_profile(binarized_arr, axis)
            binarized_arr, _ = cut_white(binarized_arr, letter_profile, axis)
        save_arr_as_img(binarized_arr, filename(i))

    # Psili
    binarized_arr = font_drawer.render_binarized('´')
    # Delete white around letter
    binarized_arr = binarized_arr[10:46, 5:12]
    save_arr_as_img(binarized_arr, filename(len(symbol_set) - 1))


