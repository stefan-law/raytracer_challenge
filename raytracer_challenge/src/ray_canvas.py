"""Implements a canvas for storing pixels"""
from __future__ import annotations

import sys
sys.path.append('raytracer_challenge')

import src.ray_functions as rf

class Canvas:
    """Implements a canvas"""

    def __init__(self, width, height, max_color_value=255) -> None:
        self.width = width
        self.height = height
        self.max_color_value = max_color_value
        self.canvas = [[rf.color(0,0,0) for y in range(self.height)] for x in range(self.width)]

    def canvas_to_ppm(self):
        """Prints canvas to a PPM file"""
        print("Enter filename: ")
        filename = input() + ".ppm"
        with open(filename, 'w', encoding="utf-8") as f:

            # Print PPM Header
            f.write(f"P3\n{self.width} {self.height}\n{self.max_color_value}\n")
            # Print pixels (with separate RGB values)
            for y in range(self.height):
                count = 0
                for x in range(self.width):
                    pixel = self.canvas[x][y]
                    pixel_buffer = [pixel.red, pixel.green, pixel.blue]
                    
                    for color in pixel_buffer:
                        #Clamp colors
                        if color > 1:
                            color = 1
                        elif color < 0:
                            color = 0

                        #Determine if new line needed and print scaled color value
                        if count + len(str(round(color *255))) > 70:
                            count = 0
                            f.write('\n' + str(round(color * 255)) + ' ')
                        else:
                            count += (len(str(color)) + 1)
                            f.write(str(round(color * 255)) + ' ')
                f.write('\n')
                
            
