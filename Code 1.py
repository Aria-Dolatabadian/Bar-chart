import matplotlib.pyplot as plt
Production = [115, 220, 330, 540]
def f(x, pos):
    """The two args are the value and tick position."""
    return '{:1.1f}'.format(x*1)
fig, ax = plt.subplots()
# Use automatic FuncFormatter creation
ax.yaxis.set_major_formatter(f)
ax.bar(['Canola', 'Rice', 'Wheat', 'Corn'], Production)
ax.set_ylabel('Production')
ax.set_title('Crops production')
plt.show()

