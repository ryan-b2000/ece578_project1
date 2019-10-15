# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 256

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False,
                           pixel_order=ORDER)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)


while True:
    # Comment this line out if you have RGBW/GRBW NeoPixels
  
    
    
    #Row 1 left-> Right
    pixels[57] = wheel(1 & 255) 
    pixels[56] = wheel(1 & 255) 
    pixels[55] = wheel(1 & 255) #wheel(color & color#) 
    pixels[70] = wheel(1 & 255) 
    pixels[72] = wheel(1 & 255) #wheel(cnolor & color#) 
    pixels[121] = wheel(1 & 255) 
    pixels[132] = wheel(1 & 255) #wheel(color & color#) 
    pixels[133] = wheel(1 & 255) 
    pixels[134] = wheel(1 & 255) #wheel(color & color#) 
    pixels[187] = wheel(1 & 255) 
    pixels[186] = wheel(1 & 255) #wheel(color & color#) 
    pixels[185] = wheel(1 & 255) 
    pixels[196] = wheel(1 & 255) #Top Left pixel 
    pixels[197] = wheel(1 & 255) 
    pixels[198] = wheel(1 & 255) #wheel(color & color#) 
    
    
    pixels[139] = wheel(1 & 255) 
    pixels[140] = wheel(1 & 255) #w heel(color & color#) 
    pixels[141] = wheel(1 & 255) 
    pixels[180] = wheel(1 & 255) #wheel(color & color#) 
    pixels[179] = wheel(1 & 255) 
    pixels[178] = wheel(1 & 255) #wheel(color & color#) 
    pixels[203] = wheel(1 & 255) 
    pixels[204] = wheel(1 & 255) #wheel(color & color#) 
    pixels[205] = wheel(1 & 255) 
    pixels[114] = wheel(1 & 255) 
    pixels[77] = wheel(1 & 255) #wheel(color & color#) 
    pixels[50] = wheel(1 & 255) 
    pixels[49] = wheel(1 & 255) #wheel(color & color#) 
    pixels[48] = wheel(1 & 255) 
    pixels[47] = wheel(1 & 255) #wheel(color & color#) 
    pixels[46] = wheel(1 & 255) 
    pixels[45] = wheel(1 & 255)
    pixels[44] = wheel(1 & 255) 
    pixels[43] = wheel(1 & 255) #w heel(color & color#) 
    pixels[84] = wheel(1 & 255) 
    pixels[107] = wheel(1 & 255) #wheel(color & color#) 
    pixels[146] = wheel(1 & 255) 
    pixels[147] = wheel(1 & 255) #wheel(color & color#) 
    pixels[148] = wheel(1 & 255) 
    pixels[173] = wheel(1 & 255) #wheel(color & color#) 
    pixels[172] = wheel(1 & 255) 
    pixels[171] = wheel(1 & 255) 
    pixels[210] = wheel(1 & 255) #wheel(color & color#) 
    pixels[211] = wheel(1 & 255) 
    pixels[212] = wheel(1 & 255) #wheel(color & color#) 
    
    
    pixels[37] = wheel(1 & 255) 
    pixels[90] = wheel(1 & 255) #wheel(color & color#) 
    pixels[101] = wheel(1 & 255) 
    pixels[152] = wheel(1 & 255)
    pixels[153] = wheel(1 & 255) 
    pixels[154] = wheel(1 & 255) #wheel(color & color#) 
    pixels[167] = wheel(1 & 255) 
    pixels[166] = wheel(1 & 255)
    pixels[165] = wheel(1 & 255) #wheel(color & color#) 
    pixels[216] = wheel(1 & 255)
    pixels[217] = wheel(1 & 255)
    pixels[218] = wheel(1 & 255) 
    pixels.show()
    time.sleep(40)
    pixels.fill((0, 0, 0))
    pixels.show()
       

    #rainbow_cycle(0.001)    # rainbow cycle with 1ms delay per step
