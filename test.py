import imageio
import os
import image_slicer
image_slicer.slice('huge_test_image.png', 14)

reader = imageio.get_reader('test.mp4')

for frame_number, im in enumerate(reader):
    for tile_number, p in enumerate(tiles):
        try:
            imageio.imwrite(f'test_split/frame_{frame_number}_{tile_number}.jpg', im)
        except FileNotFoundError:
            os.mkdir('test_split')
            imageio.imwrite(f'test_split/frame_{frame_number}_{tile_number}.jpg', im)

