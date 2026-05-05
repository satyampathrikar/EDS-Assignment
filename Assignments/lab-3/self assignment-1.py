import numpy as np
import matplotlib.pyplot as plt

# Create dummy image (random pixels)
img = np.random.randint(0, 255, (5, 5, 3))

print("Image Array:\n", img)

# Show image
plt.imshow(img)
plt.title("Random Image")
plt.show()