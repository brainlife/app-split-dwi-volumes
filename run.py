#!/usr/bin/env python3

import os,sys
import json
import numpy as np
import nibabel as nib
from dipy.io.image import load_nifti
from dipy.io import read_bvals_bvecs
from dipy.io.image import save_nifti

def main():

	# make output directory
	if not os.path.exists('dwi'):
		os.mkdir('dwi')

	# parse inputs
	with open('config.json') as config_f:
		config =  json.load(config_f)
		dwi_path = config["dwi"]
		bvals_path = config["bvals"]
		bvecs_path = config["bvecs"]
		startVol = config["start_volume"] - 1
		endVol = config["end_volume"] - 1

	# load dwi data
	print("loading dwi data")
	dwi,affine = load_nifti(dwi_path,return_img=False)

	# load bvals and bvecs data
	bvals, bvecs = read_bvals_bvecs(bvals_path,bvecs_path)
	print("loading dwi data complete")

	# generate output structures based on requested start and end volumes
	print("setting up output data based on requested volumes")
	out_dwi = dwi[:,:,:,startVol:endVol]

	out_bvals = bvals[startVol:endVol]

	out_bvecs = bvecs[startVol:endVol,:]
	print("setting up output data based on requested volumes complete")

	# write out data
	print("saving data")
	save_nifti(os.path.join('dwi','dwi.nii.gz'),out_dwi,affine)
	del(dwi,affine,out_dwi)

	with open(os.path.join('dwi','dwi.bvals'),'w') as bvals_to_write:
		for item in range(len(out_bvals)):
			if item != len(out_bvals[:]) - 1:
				bvals_to_write.write(str(np.int(out_bvals[item])) + ' ')
			else:
				bvals_to_write.write(str(np.int(out_bvals[item])))

	with open(os.path.join('dwi','dwi.bvecs'),'w') as bvecs_to_write:
		for dimensions in range(np.shape(out_bvecs)[1]):
			if dimensions != 2:
				for item in range(len(out_bvecs[:,dimensions])):
					if item != len(out_bvecs[:,dimensions]) - 1:
						bvecs_to_write.write(str(out_bvecs[item,dimensions]) + ' ')
					else:
						bvecs_to_write.write(str(out_bvecs[item,dimensions]))
				bvecs_to_write.write('\n')
			else:
				for item in range(len(out_bvecs[:,dimensions])):
					if item != len(out_bvecs[:,dimensions]) - 1:
						bvecs_to_write.write(str(out_bvecs[item,dimensions]) + ' ')
					else:
						bvecs_to_write.write(str(out_bvecs[item,dimensions]))
	print("saving data complete. app finished")

if __name__ == "__main__":

    main()
