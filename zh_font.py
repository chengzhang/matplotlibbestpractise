# coding = utf8
from mplfonts import use_font
import matplotlib.pyplot as plt

use_font('Noto Serif CJK SC')

xs = ['一', '二', '三']
ys = [1, 2, 3]
idx = range(len(xs))
plt.bar(idx, ys)
plt.xticks(idx, xs)
plt.show()
