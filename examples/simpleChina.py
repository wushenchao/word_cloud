#!/usr/bin/env python
"""
Minimal Example
===============

Generating a square wordcloud from the US constitution using default arguments.
"""

from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)

font = path.join(d, "DroidSansFallbackFull.ttf")

# Read the whole text.
text = open(path.join(d, 'constitutionChina.txt')).read()

# Generate a word cloud image
wordcloud = WordCloud(font_path=font).generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(font_path=font, max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()
