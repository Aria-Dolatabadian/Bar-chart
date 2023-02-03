import matplotlib.pyplot as plt
Production = [8e6, 6e6, 5e6, 3.5e6]
def millions(x, pos):
    """The two args are the value and tick position."""
    return '${:1.1f}M'.format(x*1e-6)
fig, ax = plt.subplots()
# Use automatic FuncFormatter creation
ax.yaxis.set_major_formatter(millions)
ax.bar(['Canola', 'Rice', 'Wheat', 'Corn'], Production)
ax.set_ylabel('Production')
ax.set_title('Crops production')
plt.show()
