import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import numpy as np
x = [0.3,0.8,1.4,2.1,2.9]
y = [5.28,6.83,4.35,3.26,2.35]
spl = UnivariateSpline(x, y)
xs = np.linspace(0, 2.9, 1000)
plt.plot(xs, spl(xs), 'g')
plt.show()