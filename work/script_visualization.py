from utils import count_figure
import os
from matplotlib import pyplot as plt

directory = "./output"

data = {}


for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    reduced_filename = filename[10:15]
    data[reduced_filename] = count_figure(file_path)

plt.bar(list(data.keys()), list(data.values()))
plt.show()