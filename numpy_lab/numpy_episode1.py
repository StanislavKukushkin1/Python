import os
import numpy as np
from PIL import Image

folder = os.path.dirname(__file__)
source = os.path.join(folder, 'lunar_images')
result = os.path.join(folder, 'results', 'episode1')
os.makedirs(result, exist_ok=True)

for name in sorted(os.listdir(source)):
    if not name.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue

    image = np.array(Image.open(os.path.join(source, name)).convert('L'), dtype=float)
    minimum = image.min()
    maximum = image.max()

    improved = (image - minimum) * 255 / (maximum - minimum)
    improved = improved.astype(np.uint8)

    filename = os.path.splitext(name)[0] + '.png'
    Image.fromarray(improved).save(os.path.join(result, filename))
