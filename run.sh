#!/bin/bash

dwi=`jq -r '.dwi' config.json`
bvecs=`jq -r '.bvecs' config.json`
bvals=`jq -r '.bvals' config.json`
vols=`jq -r '.vols' config.json`

# make output dirs
outdir="output"
[ ! -d ${outdir} ] && mkdir -p ${outdir}

# extract volumes
[ ! -f ${outdir}/dwi.nii.gz ] && mrconvert -fslgrad ${bvecs} ${bvals} -export_grad_fsl ${outdir}/dwi.bvecs ${outdir}/dwi.bvals -coord 3 ${vols} ${dwi} ${outdir}/dwi.nii.gz -force -nthreads 4
