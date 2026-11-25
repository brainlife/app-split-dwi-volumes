[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-brainlife.app.575-blue.svg)](https://doi.org/10.25663/brainlife.app.575)

# Extract DWI volumes of choice

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

**Extracts selected volumes from a DWI image, with matching bvals and bvecs, using MRtrix3 mrconvert.**

Runs mrconvert -coord 3 with the requested (0-indexed) volume list and exports the corresponding gradient table as FSL bvals/bvecs. Use it to drop or keep specific volumes or shells before further processing.

Run it on brainlife.io: [https://doi.org/10.25663/brainlife.app.575](https://doi.org/10.25663/brainlife.app.575)

| Input | Datatype | Required | Description |
|---|---|---|---|
| `dwi` | `neuro/dwi` | yes | DWI image with bvals and bvecs. |

| Output | Datatype | Description |
|---|---|---|
| `output` | `neuro/dwi` | DWI containing only the selected volumes, with matching bvals and bvecs. |

| Parameter | Type | Default | Description |
|---|---|---|---|
| `vols` | string |  | This field is intended to specify the volumes of interest. IMPORTANT: this uses 0 indexing. So the first volume is 0, and the remaining volumes are N-1. If a selection of non-consecutive volumes are desired, list the volume numbers and include commas between them (ex. 0,2,4,24,99) If a series of volumes is desired, use a start:step:end format, where "start" is the starting volume, "step" is the number of steps before the next volume selected, and "end" is the ending volume. For example, if you want every volume from the first volume to the 40th volume, do 0:1:39 You can also use the keyword "end" to specify that you want all volumes from a starting volume to the end of the nifti (ex. 24:1:end would be the 25th volume and then all the remaining volumes). This should also follow the start:step:end format. These can be combined. For example, if a user wants the 2nd, 4th, 40th-60th, and 70th to end, you would specify this field as '1,3,39:1:59,69:1:end" |

Runtime: container `brainlife/mrtrix3:3.0.2`; 4 CPUs; 32 GB memory; 1 h walltime.

<!-- brainlife-app:end -->

This app will extract volumes from a diffusion MRI volume based on user input using MRTrix3.

### Authors

- Brad Caron (bacaron@utexas.edu)

### Contributors

- Soichi Hayashi (shayashi@iu.edu)

### Funding Acknowledgement

brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

### Citations

We kindly ask that you cite the following articles when publishing papers and code using this code.

1. Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). https://doi.org/10.1038/s41597-019-0073-y

2. Tournier JD, Smith R, Raffelt D, Tabbara R, Dhollander T, Pietsch M, Christiaens D, Jeurissen B, Yeh CH, Connelly A. MRtrix3: A fast, flexible and open software framework for medical image processing and visualisation. Neuroimage. 2019 Nov 15;202:116137. doi: 10.1016/j.neuroimage.2019.116137. Epub 2019 Aug 29. PMID: 31473352.

#### MIT Copyright (c) 2020 brainlife.io The University of Texas at Austin and Indiana University

## Running the App

### On Brainlife.io

You can submit this App online at [https://doi.org/10.25663/brainlife.app.575](https://doi.org/10.25663/brainlife.app.575) via the 'Execute' tab.

### Running Locally (on your machine)

1. git clone this repo

2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files.

```json
{
    "dwi": "/input/dwi/dwi.nii.gz",
    "bvecs": "/input/dwi/bvecs.nii.gz",
    "bvals": "/input/dwi/bvals.nii.gz",
    "vols": "0 1 2 3 40 41 50:64"
}
```

### Sample Datasets

You can download sample datasets from Brainlife using [Brainlife CLI](https://github.com/brain-life/cli).

```
npm install -g brainlife
bl login
mkdir input
bl dataset download
```

3. Launch the App by executing 'main'

```bash
./main
```

## Output

The main output of this App is a dwi datatype

#### Product.json

The secondary output of this app is `product.json`. This file allows web interfaces, DB and API calls on the results of the processing.

### Dependencies

This App only requires [singularity](https://www.sylabs.io/singularity/) to run. If you don't have singularity, you will need to install following dependencies.   

- MRTrix3: https://www.mrtrix.org/

#### MIT Copyright (c) 2020 brainlife.io The University of Texas at Austin and Indiana University
