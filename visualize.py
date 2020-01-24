import csv
import sys
import numpy as np
import matplotlib.pyplot as plt

with open(sys.argv[1]) as f:
    reader = csv.reader(f)
    raw_data = list(reader);

actual_x = [float(i[0]) for i in raw_data]
actual_y = [float(i[1]) for i in raw_data]
predicted_x = [float(i[2]) for i in raw_data]
predicted_y = [float(i[3]) for i in raw_data]

plt.plot(actual_x, actual_y, 'b-');
plt.plot(predicted_x, predicted_y, 'r-');
plt.legend(['actual', 'predicted'])
plt.show()
