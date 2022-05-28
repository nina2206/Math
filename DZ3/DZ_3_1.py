# Сложение векторов
import numpy as np
vect1_cordinates = [10, 10, 10]
vect2_cordinates = [0, 0, -10]
vect1 = np.array(vect1_cordinates)
vect2 = np.array(vect2_cordinates)

print(f"Summ of two vectors {vect1_cordinates} & {vect2_cordinates}:\n\033[36m{vect1 + vect2}")