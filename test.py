import imageio
import os

reader = imageio.get_reader('test.mp4')

os.mkdir('test_split')

for frame_number, im in enumerate(reader):
    M = im.shape[0] // 1
    N = im.shape[1] // 4
    tiles = [im[x:x + M, y:y + N] for x in range(0, im.shape[0], M) for y in range(0, im.shape[1], N)]
    for tile_number, p in enumerate(tiles):
        imageio.imwrite(f'test_split/frame_{frame_number}_{tile_number}.jpg', p)
