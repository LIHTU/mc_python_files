# read in a 1-bpp BMP file and build it inside minecraft
#
# (c) 2013 Thinking Binaries Ltd
# Written by David Whale @whaleygeek

import mcpi.minecraft as minecraft
from mcpi.block import *


import sys

class BMP():
  def __init__(self, f):
    self.file = f
    
  def read(self, n):
    return self.file.read(n)
    
  def readU8(self):
    data = self.file.read(1)
    return ord(data[0])
  
  def readU16(self):
    data = self.file.read(2)
    return ord(data[0]) + (ord(data[1])<<8)
  
  def readU32(self):
    data = self.file.read(4)
    return ord(data[0]) + (ord(data[1])<<8) + (ord(data[2])<<16) + (ord(data[3])<<24)

  def dumpHeader(self):
    print "bmp.signature:", self.bmp_signature
    print "bmp.size:",      self.bmp_size
    print "bmp.start:",     self.bmp_start

    print "dib.size:",    self.dib_size
    print "dib.width:",   self.dib_width
    print "dib.height:",  self.dib_height
    print "dib.planes:",  self.dib_planes
    print "dib.bpp:",     self.dib_bpp
    print "dib.comp:",    self.dib_comp
    print "dib.imgsize:", self.dib_imgsize
    print "dib.hres:",    self.dib_hres
    print "dib.vres:",    self.dib_vres
    print "dib.palsize:", self.dib_palsize
    print "dib.impcol",   self.dib_impcol    
    
  def readHeader(self):
    self.file.seek(0)
    
    # BMP Header
      # 0x0000 U16 Signature ("BM")
      # 0x0002 U32 file size (bytes)
      # 0x0006 U16 reserved
      # 0x0008 U16 reserved
      # 0x000A U32 start offset of pixel data

    self.bmp_signature = self.read(2)
    self.bmp_size      = self.readU32()
    self.bmp_resv1     = self.readU16()
    self.bmp_resv2     = self.readU16()
    self.bmp_start     = self.readU32()
  
    # DIB Header
      # 0x000E U32 header size (bytes)
      # 0x0012 S32 width (pixels)
      # 0x0016 S32 height (pixels)
      # 0x001A U16 colour planes (1)
      # 0x001C U16 bits per pixel (1,4,8,16,24,32)
      # 0x001E U32 compression method
      # 0x0022 U32 raw image size
      # 0x0026 U32 horizontal resolution
      # 0x002A U32 vertical resolution
      # 0x002E U32 colours in palette (0=>2^n)
      # 0x0032 U32 number of important colours (ignored)
  
    self.dib_size    = self.readU32()
    self.dib_width   = self.readU32()
    self.dib_height  = self.readU32()
    self.dib_planes  = self.readU16()
    self.dib_bpp     = self.readU16()
    self.dib_comp    = self.readU32()
    self.dib_imgsize = self.readU32()
    self.dib_hres    = self.readU32()
    self.dib_vres    = self.readU32()
    self.dib_palsize = self.readU32()
    self.dib_impcol  = self.readU32()
  
  def dumpPalette(self):
    self.file.seek(54)

    if self.dib_bpp == 1:
      palsize = 2
    elif self.dib_bpp == 4:
      palsize = 16 
    elif self.dib_bpp == 8:
      palsize = 256
    elif self.dib_bpp == 24:
      palsize = 0
    
    for i in range(palsize):
      red    = self.read(1)
      green  = self.read(1)
      blue   = self.read(1)
      unused = self.read(1)
      R = ord(red[0])
      G = ord(green[0])
      B = ord(blue[0])
      print "pal", i, R, G, B
      
  def drawPixels(self, mc):
    
    rowsize = (((self.dib_bpp * self.dib_width) + 31) / 32 ) * 4
    rows = self.dib_imgsize / rowsize
    
    self.file.seek(self.bmp_start)
    
    # pixel data scans from the bottom upwards
    # make sure we don't overrun bits in the final byte if not used
    
    x = 0.5
    y = 0.5
    z = 0.5

    for rowno in range(rows):
      #self.file.seek(self.bmp_start + (self.dib_height - rowno-1)*rowsize)
      self.file.seek(self.bmp_start + rowno*rowsize)
      rowstr = ""
      row = self.read(rowsize)
      bitcount = 1
      y = 0.5 + rowno
      x = 0.5
      
      for byteno in range(rowsize):
        if bitcount >= self.dib_width:
          break
        byte = ord(row[byteno])
        mask = 0x80
        
        for bit in range(8):
          if (byte & mask) != 0:
            rowstr += " "
            mc.setBlock(x, y, z, AIR)
          else:
            rowstr += "x"
            mc.setBlock(x, y, z, GLOWING_OBSIDIAN)
          mask >>= 1
          bitcount = bitcount + 1
          x = x + 1
          if bitcount >= self.dib_width:
            break
          
      print rowstr


if __name__ == '__main__':
  name = sys.argv[1]
  print "dumping file:", name
  
  f = open(name, "rb")
  mc = minecraft.Minecraft.create("localhost")

  bmp = BMP(f)
  bmp.readHeader()
  
  if bmp.dib_bpp != 1:
    print "ERROR: More than 1 BPP"
  else:
    #bmp.dumpHeader()
    #bmp.dumpPalette()
    #bmp.dumpPixels()
    bmp.drawPixels(mc)

  f.close()
  
  
