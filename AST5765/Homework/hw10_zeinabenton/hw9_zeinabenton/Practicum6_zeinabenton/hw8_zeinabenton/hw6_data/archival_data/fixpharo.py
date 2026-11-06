#! /usr/bin/env python

# AST5765/4762 HW6 data repair
# Read, fix, and write out corrected PHARO FITS files as 2D images
# rather than 3D stacks of four images.

# Initial version 13Oct26 Joseph Harrington <jh@ucf.edu>
# Someone else must have written something like this, but omitted some
# files and didn't pass on their code to me.

# Assumes sourcedir exists and that all files in it are uncorrected
# PHARO files to be corrected. Assumes destdir exists and is writeable
# by user.

import os
import astropy.io.fits as fits
import rdpharo

datadir = '/home/jh/ast/teaching/ast5765/hw/hw6/hw6_data/'
fext    = '.fits'
extlen  = len(fext)

sourcedir = datadir + 'archival_data/'
destdir   = datadir + 'corr_data/'
fixprefix = 'rdpharocor_'

allfiles = os.listdir(sourcedir)

badfile  = []
for file in allfiles:
  if file[-extlen:] == fext:
    badfile.append(file[:-extlen])

badfile = sorted(badfile)

for i in badfile:
  (header, data) = rdpharo.rdpharo(sourcedir+i+fext)
  fits.writeto(destdir+fixprefix+i+fext, data, header, overwrite=True,
               output_verify="silentfix")
