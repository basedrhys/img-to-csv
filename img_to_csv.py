from PIL import Image
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image_file', required=True)
parser.add_argument('-o', '--output_csv', required=True)
parser.add_argument('--rgb', action='store_true')
args = parser.parse_args(sys.argv[1:])

im = Image.open(args.image_file)
pix  = im.load()

width, height = im.size

with open(args.output_csv, 'w+') as f:
    for y in range(height):
        row = []
        for x in range(width):
            pixel = list(map(str, pix[x, y][:3]))
            if not args.rgb:
                pixel.reverse()
            row.append(pixel)

        f.write(','.join([item for sublist in row for item in sublist]))
        f.write('\n')
