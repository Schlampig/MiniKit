# -*- coding:utf-8 -*-
import textwrap
from PIL import Image, ImageFont, ImageDraw
FONT = ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB W6.ttc", 18)


def simple_justify(s, width=50):
    """
    Use python build-in liburary "textwrap" to set width of s.
    :param s: string, input text
    :param width: int, number of characters in each line
    :return: lst, a list = [line_1, line_2, ...]
    """
    wrp = textwrap.TextWrapper(width=width, break_on_hyphens=False)
    lst = wrp.wrap(s)
    return lst


def complex_justify(s, width=50):
    """
    Set width of s in a delicated way :)
    :param s: string, input text
    :param width: int, number of characters in each line
    :return: lst, a list = [line_1, line_2, ...]
    """
    def left_justify(words, width):
        """
        Given an iterable of words, return a string consisting of the words
        left-justified in a line of the given width.
        >>> left_justify(["hello", "world"], 16)
        'hello world     '
        :param words: list = [char_1, char_2, ...]
        :param width: int
        :return: string
        """
        return ' '.join(words).ljust(width)  # ljust is a build-in function

    def justify(words, width):
        """
        Divide words (an iterable of strings) into lines of the given
        width, and generate them. The lines are fully justified, except
        for the last line, and lines with a single word, which are
        left-justified.
        >>> words = "This is an example of text justification.".split()
        >>> list(justify(words, 16))
        ['This    is    an', 'example  of text', 'justification.  ']
        :param words: list = [char_1, char_2, ...]
        :param width: int
        :return: lst, a list = [line_1, line_2, ...]
        """
        line = []  # List of words in current line.
        col = 0  # Starting column of next word added to line.
        for word in words:
            if line and col + len(word) > width:
                if len(line) == 1:
                    yield left_justify(line, width)
                else:
                    # After n + 1 spaces are placed between each pair of
                    # words, there are r spaces left over; these result in
                    # wider spaces at the left.
                    n, r = divmod(width - col + 1, len(line) - 1)
                    narrow = ' ' * (n + 1)
                    if r == 0:
                        yield narrow.join(line)
                    else:
                        wide = ' ' * (n + 2)
                        yield wide.join(line[:r] + [narrow.join(line[r:])])
                line, col = [], 0
            line.append(word)
            col += len(word) + 1
        if line:
            yield left_justify(line, width)
    s = s.split()
    lst = list(justify(s, width=width))
    return lst


def txt2img(s, save_path, s_max=800):
    """
    Input a text and save it to an image with .jpg format.
    :param s: string, input text
    :param save_path: string, saved image path
    :param s_max: int, image size
    :return: None (a image is saved)
    """
    global FONT
    # clean the text
    lst = complex_justify(s)
    # draw the image
    bias_x, bias_y = 10, 10
    h_line = FONT.getsize(s)[1]  # set the line height
    h_img = h_line * (len(lst) + 1)  # set the image height
    img = Image.new("RGB", (s_max+bias_y, h_img+bias_x), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    for line in lst:
        draw.text((bias_x, bias_y), line, font=FONT, fill="#000000")
        bias_y += h_line
    # save the image
    if save_path.endswith(".jpg"):
        img.save(save_path)
        return True
    else:
        raise ValueError("[ERROR] Format of image is wrong [.jpg is required].")


if __name__ == "__main__":
    text = """ 
    Understanding videos such as TV series and movies requires analyzing who the 
    characters are and what they are doing. We address the challenging problem of 
    clustering face tracks based on their identity. Different from previous work 
    in this area, we choose to operate in a realistic and difficult setting where: 
    (i) the number of characters is not known a priori; and (ii) face tracks 
    belonging to minor or background characters are not discarded. To this end, we 
    propose Ball Cluster Learning (BCL), a supervised approach to carve the embedding 
    space into balls of equal size, one for each cluster. The learned ball radius is 
    easily translated to a stopping criterion for iterative merging algorithms. This 
    gives BCL the ability to estimate the number of clusters as well as their assignment, 
    achieving promising results on commonly used datasets. We also present a thorough 
    discussion of how existing metric learning literature can be adapted for this task.
    """
    txt2img(text, save_path="new_img.jpg")
 
