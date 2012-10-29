import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from hyperion.model import ModelOutput
from hyperion.util.constants import pc

# Open the model - we specify the name without the .rtout extension
m = ModelOutput('output.rtout')

# Create the plot
fig = plt.figure(dpi=100)
ax = fig.add_subplot(1, 1, 1)

# Extract the SED for the smallest inclination and largest aperture, and
# scale to 300pc. In Python, negative indices can be used for lists and
# arrays, and indicate the position from the end. So to get the SED in the
# largest aperture, we set aperture=-1.

f = np.linspace(0, 255, 10)
print f
j = [0,1,2,3,4,5,6,7,8,9]
for k in range(len(j)):
    print 'color number', f[k]
    print 'integer', int(f[k])
    g = plt.cm.gist_heat(int(f[k]))
    print 'color vector', g
    i = j[k]
    print 'incination', i
    
    wav, nufnu = m.get_sed(inclination=i, aperture=-1, distance=300 * pc)
    # Plot the SED. The loglog command is similar to plot, but automatically
    # sets the x and y axes to be on a log scale.
    lines = ax.loglog(wav,nufnu.transpose())
    
    ax.loglog(wav, nufnu,color=g)

#colorbar    
image = wav,nufnu.transpose()
lines = ax.imshow(image,cmap=plt.cm.gist_heat)    
fig.colorbar(lines)

# Add some axis labels (we are using LaTeX here)
ax.set_xlabel(r'$\lambda$ [$\mu$m]')
ax.set_ylabel(r'$\lambda F_\lambda$ [ergs/s/cm$^2$]')

# Set view limits
ax.set_xlim(0.1, 2000.)
ax.set_ylim(1.e-15, 2.e-09)

# Write out the plot
fig.savefig('sedall.png')