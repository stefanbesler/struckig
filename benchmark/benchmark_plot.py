from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ticks = ('1 DoF', '3 DoF', '6 DoF', '7 DoF')
struckig_average_mean = [3, 18, 42, 58]
struckig_average_err = [1, 3, 5, 6]

y_pos = np.arange(len(ticks))
height = 0.35

plt.figure(figsize=(9.0, 4.0), dpi=120)

# Average
plt.subplot(1, 1, 1)
plt.suptitle('Benchmark of x degree-of-freedom, time-synchronized trajectory\nVM with TwinCAT 3.1.4024.17; AMD Ryzen 3600X (1 Isolated Core)\n Single task with 1ms cycletime (lower is better)', fontsize=10)

ax = plt.gca()

ax.grid(True, linestyle='--', color='grey', alpha=.25)
ax.barh(y_pos, struckig_average_mean, height=height, xerr=struckig_average_err, label='Struckig')
ax.set_yticks(y_pos)
ax.set_yticklabels(ticks)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Mean Calculation Duration [µs]')
ax.legend()

plt.savefig(Path(__file__).parent.parent / 'benchmark.png')
