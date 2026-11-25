<h1 align="center">Extract DWI volumes of choice</h1>

<p align="center">
  A diffusion-weighted image containing only the volumes you select, with matching bvals and bvecs, using MRtrix3.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.575"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.575-blue.svg" alt="Run on brainlife.io"></a>
  <a href="https://github.com/brainlife/app-split-dwi-volumes/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" alt="MIT license"></a>
</p>

> **This branch, `mrtrix3-v1.0`, is the brainlife.io App Extract DWI volumes of choice** ([doi:10.25663/brainlife.app.575](https://doi.org/10.25663/brainlife.app.575)). The other Apps in this repository are listed under **Versions on brainlife.io** below.

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Extracts selected volumes from a DWI image, with matching bvals and bvecs, using MRtrix3 mrconvert.**

Runs mrconvert -coord 3 with the requested (0-indexed) volume list and exports the corresponding gradient table as FSL bvals/bvecs. Use it to drop or keep specific volumes or shells before further processing.

| | |
|---|---|
| **Inputs** | `neuro/dwi` |
| **Outputs** | `neuro/dwi` |
| **Container** | `brainlife/mrtrix3:3.0.2` |
| **Resources** | 4 CPUs · 32 GB memory · 1 h walltime |
| **Run it** | [doi.org/10.25663/brainlife.app.575](https://doi.org/10.25663/brainlife.app.575) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `dwi` | `neuro/dwi` | yes | DWI image with bvals and bvecs. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `output` | `neuro/dwi` | DWI containing only the selected volumes, with matching bvals and bvecs. |

<details>
<summary><b>Parameters</b> (1)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `vols` | string |  | This field is intended to specify the volumes of interest. IMPORTANT: this uses 0 indexing. So the first volume is 0, and the remaining volumes are N-1. If a selection of non-consecutive volumes are desired, list the volume numbers and include commas between them (ex. 0,2,4,24,99) If a series of volumes is desired, use a start:step:end format, where "start" is the starting volume, "step" is the number of steps before the next volume selected, and "end" is the ending volume. For example, if you want every volume from the first volume to the 40th volume, do 0:1:39 You can also use the keyword "end" to specify that you want all volumes from a starting volume to the end of the nifti (ex. 24:1:end would be the 25th volume and then all the remaining volumes). This should also follow the start:step:end format. These can be combined. For example, if a user wants the 2nd, 4th, 40th-60th, and 70th to end, you would specify this field as '1,3,39:1:59,69:1:end" |

</details>

<!-- brainlife-app:end -->

## Versions on brainlife.io

Each version is a separate App on brainlife.io, built from its own branch of this repository.

| Version | Tool | Branch | Run it | Status |
|---|---|---|---|---|
| **Extract DWI volumes of choice** (this branch) | MRtrix3 3.0.2 | [`mrtrix3-v1.0`](https://github.com/brainlife/app-split-dwi-volumes/tree/mrtrix3-v1.0) | [doi:10.25663/brainlife.app.575](https://doi.org/10.25663/brainlife.app.575) | current |
| Extract DWI volumes of choice - Deprecated | DIPY (start and end volume) | [`v1.0`](https://github.com/brainlife/app-split-dwi-volumes/tree/v1.0) | [doi:10.25663/brainlife.app.371](https://doi.org/10.25663/brainlife.app.371) | deprecated |

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.575](https://doi.org/10.25663/brainlife.app.575), choose a `neuro/dwi` dataset from your project, list the volumes you want in `vols`, and press **Execute**. The App writes a `neuro/dwi` dataset with only those volumes to your project. Use it to drop or keep specific volumes or shells before further processing.

#### `vols`

The volumes to keep, passed to `mrconvert -coord 3`. **Indexing starts at 0**: the first volume is 0 and the last is N-1.

- Non-consecutive volumes: list them separated by commas, for example `0,2,4,24,99`.
- A series of volumes: use `start:step:end`. For example, every volume from the first to the 40th is `0:1:39`.
- The keyword `end` means the last volume, for example `24:1:end` keeps the 25th volume and all the remaining ones.
- The forms can be combined. For the 2nd, 4th, 40th–60th and 70th-to-last volumes, use `1,3,39:1:59,69:1:end`.

The deprecated version (`v1.0`) instead took a `start_volume` and an `end_volume` (counting from 1) and extracted that range with DIPY.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) and [`jq`](https://jqlang.github.io/jq/). The App runs in the `brainlife/mrtrix3:3.0.2` container.

1. Clone this repository and check out the current version (`git checkout mrtrix3-v1.0`).
2. Create `config.json` with the paths to your inputs and the volumes to keep:

   ```json
   {
       "dwi": "/input/dwi/dwi.nii.gz",
       "bvecs": "/input/dwi/dwi.bvecs",
       "bvals": "/input/dwi/dwi.bvals",
       "vols": "0,1,2,3,40,41,50:1:64"
   }
   ```

3. Run the App:

   ```bash
   ./main
   ```

## Outputs

```text
output/
├── dwi.nii.gz   the selected volumes
├── dwi.bvecs    matching gradient directions (FSL format)
└── dwi.bvals    matching b-values (FSL format)
```

## Troubleshooting

- **`failed`**: `output/dwi.bvecs` was not written. Check that `vols` uses commas and `start:step:end` ranges (not spaces), that the indices start at 0 and are within the number of volumes, and that the bvals and bvecs match the DWI.

## Citing

> [!TIP]
> If you use this App in your work, please cite the App, the software it builds on and brainlife.io (below). GitHub's **Cite this repository** button gives the App citation in APA and BibTeX.

- Tournier J-D, Smith R, Raffelt D, Tabbara R, Dhollander T, Pietsch M, Christiaens D, Jeurissen B, Yeh C-H, Connelly A. MRtrix3: A fast, flexible and open software framework for medical image processing and visualisation. *NeuroImage* 202:116137 (2019). [doi:10.1016/j.neuroimage.2019.116137](https://doi.org/10.1016/j.neuroimage.2019.116137)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)
- Extract DWI volumes of choice. brainlife.io App. [doi:10.25663/brainlife.app.575](https://doi.org/10.25663/brainlife.app.575)
- Jenkinson et al. FSL. *NeuroImage* 62:782-790 (2012). [doi:10.1016/j.neuroimage.2011.09.015](https://doi.org/10.1016/j.neuroimage.2011.09.015)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)

## Authors

- Brad Caron

**Contributors:** Soichi Hayashi

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io is publicly funded, and acknowledging that support helps keep it running. This App was developed with support from Wellcome, the U.S. National Institutes of Health (including the BRAIN Initiative BRAIN CONNECTS program: The Axonal Projectome EXchange, U24NS140384, and the Center for Mesoscale Connectomics, UM1NS132207) and the U.S. National Science Foundation.</sub>

## License

MIT. MRtrix3 is distributed under the [Mozilla Public License 2.0](https://www.mrtrix.org/).
