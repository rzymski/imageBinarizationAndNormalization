import tkinter as tk
from imageRefactorApp import ImageRefactorApp
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageRefactorApp(root)
    root.mainloop()


# import numpy as np
#
# tab = np.zeros(256, dtype=np.uint8)
#
# arr = np.array([1, 10, 20, 255, 10, 50, 0, 1, 10, 255], dtype=np.uint8)
#
# uniqueValues, counts = np.unique(arr, return_counts=True)
# for value, count in zip(uniqueValues, counts):
#     print(f"{value} occurs {count} times")
#
# print(counts)


# tab[arr] = tab[arr] + 1
# print(tab)

# x = np.arange(256)
# x[arr] += 999
# print(x)
#
# print(x[arr])