from sklearn.neighbors import KNeighborsClassifier
import numpy as np


class myknclf:
    def __init__(self):
        x_data = np.array([
        # O
        [0, 255, 255, 255, 0,
        255, 0, 0, 0, 255,
        255, 0, 0, 0, 255,
        255, 0, 0, 0, 255,
        0, 255, 255, 255, 0],
        [0, 255, 255, 255, 0,
        255, 255, 0, 0, 255,
        255, 0, 0, 0, 255,
        255, 0, 0, 0, 255,
        0, 255, 255, 255, 0],
        [0, 255, 255, 255, 0,
        255, 0, 0, 255, 255,
        255, 0, 0, 0, 255,
        255, 0, 0, 0, 255,
        0, 255, 255, 255, 0],
        # X
        [255, 0, 0, 0, 255,
        0, 255, 0, 255, 0,
        0, 0, 255, 0, 0,
        0, 255, 0, 255, 0,
        255, 0, 0, 0, 255],
        [255, 255, 0, 0, 255,
        0, 255, 0, 255, 0,
        0, 0, 255, 0, 0,
        0, 255, 0, 255, 0,
        255, 0, 0, 0, 255],
        [255, 0, 0, 255, 255,
        0, 255, 0, 255, 0,
        0, 0, 255, 0, 0,
        0, 255, 0, 255, 0,
        255, 0, 0, 0, 255]
        ])
        y_data = ['O']*3+['X']*3
        self.model = KNeighborsClassifier(n_neighbors=1)
        self.model.fit(x_data, y_data)


        