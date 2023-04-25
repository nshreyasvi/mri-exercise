## MRI Analysis Coding Exercise

### Objective 
Carry out an analysis of 40 brain imaging study subjects of cortical thickness, comparing chronic schizophrenia cases to age and sex-matched controls by estimating Cohen's D value.

## FreeSurfer Installation on WSL 2 Ubuntu 20.04
- `wget https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/dev/freesurfer_ubuntu20-7-dev_amd64.deb`
- `sudo apt-get install ./freesurfer_ubuntu20-7-dev_amd64.deb`
- `echo "export XDG_RUNTIME_DIR=$HOME/.xdg" >> $HOME/.bashrc`
- `echo "export DISPLAY=:0" >> $HOME/.bashrc`
- `echo "export FREESURFER_HOME=/usr/local/freesurfer/7-dev" >> $HOME/.bashrc`
- Use the form [provided here](https://surfer.nmr.mgh.harvard.edu/registration.html) to generate the `license.txt` file and copy it to the home directory.
- `echo "export FS_LICENSE=$HOME/license.txt" >> $HOME/.bashrc`
- `echo "source /usr/local/freesurfer/7-dev/SetUpFreeSurfer.sh" >> $HOME/.bashrc`
- Logout and log back into the WSL 2 Ubuntu session.
- Use `freeview` command in terminal to see if the installation was successful.

## Analysis Steps
- In this exercise, I extracted 40 subjects from the Northwestern University Schizophrenia Data and Software Tool (NUSDAST) which were balanced for age, gender and ethnicity. The dataset consisted of 20 schizophrenia subjects and 20 control subjects. Details for each of the subjects used in this analysis can be seen in `dataset_subjects.csv` file.
- Once the dataset was finalized, it was downloaded from the [XNAT web-instance](https://central.xnat.org/data/projects/NUDataSharing/) by using the [XNAT Desktop Client](https://www.xnat.org/download/desktop-client/).
- In order to perform the next stages of analysis, [FreeSurfer](https://surfer.nmr.mgh.harvard.edu/) was installed on the Windows machine using WSL 2 (Ubuntu 20.04).
- The installation was carried out in a manner [described here](https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/dev/). Please see the section **Freesurfer Installation** for detailed information for the case of WSL 2 Ubuntu 20.04.
- As the next step, to carry out cortical reconstruction process and extraction of information corresponding to different brain regions run the command `recon-all <subject 1> <subject 2> ...`.
- The process usually taken 2-3 hours to finish depending on the computer specifications. In order to save time, I extracted the outputs from `recon-all` command through the NUSDAST XNAT web instance to further carry out analysis.
- In order to extract the thickness of different brain regions in tabular format run 
`aparcstats2table --subjects <subject 1> <subject 2> --hemi rh --meas thickness --tablefile thickness_rh.csv` and
`aparcstats2table --subjects <subject 1> <subject 2> --hemi lh --meas thickness --tablefile thickness_lh.csv`. (*Optional:If volume of of different regions is required it can be done so using `asegstats2table --subjects <subject 1> <subject 2> --meas volume --tablefile aseg_stats.csv`*.)
- This will generate the `thickness_lh.csv` and `thickness_rh.csv` files similar to the ones that are present in the [repository](https://github.com/nshreyasvi/mri-exercise) repository. These CSV files contain the thickness of 35 brain regions on left hemisphere and 35 brain regions on the right hemisphere.
- Once we obtain the thickness information, we extract the Cohen's D value.
- For this we first need to install pandas using `pip install pandas` followed by running the Cohen's D value extraction script `python cohend.py > cohens_d.csv` which is also available in [this link](https://github.com/nshreyasvi/mri-exercise/blob/main/cohend.py).
- This will generate the `cohens_d.csv` file containing Cohen's D value obtained for the 70 brain regions in the left and right hemisphere.
- In order to generate the colormap corresponding to the Cohen's D value, run `python color_make.py` python script available at [this link](https://github.com/nshreyasvi/mri-exercise/blob/main/color_make.py).
- This will generate `color_gen.txt` where the Cohen's D values are normalized to fit onto a color scale (0-255 for RGB). The magnitude of the Cohen's D value is represented by the `Red` color and the positive and negative value is represented using `Green` color. Furthermore, the `color_gen_class.txt` represents if the value is positive (Red) or negative (Green).

## Visualization: 

Visualization for the study was carried out for the subject number CC1960_0 wherein the following command was used to illustrate different brain regions as well as their segmented regions obtained through freesurfer:
```
freeview subjects_nu/CC1960_0/FreeSurfer_v5-3-0/mri/T1.mgz subjects_nu/CC1960_0/FreeSurfer_v5-3-0/mri/aseg.mgz:colormap=lut subjects_nu/CC1960_0/FreeSurfer_v5-3-0/mri/brainmask.mgz subjects_nu/CC1960_0/FreeSurfer_v5-3-0/mri/aparc+aseg.mgz subjects_nu/CC1960_0/FreeSurfer_v5-3-0/mri/wm.mgz:visible=0 -f subjects_nu/CC1960_0/FreeSurfer_v5-3-0/surf/lh.white:edgecolor=blue subjects_nu/CC1960_0/FreeSurfer_v5-3-0/surf/rh.white:edgecolor=blue subjects_nu/CC1960_0/FreeSurfer_v5-3-0/surf/lh.pial:edgecolor=red subjects_nu/CC1960_0/FreeSurfer_v5-3-0/surf/rh.pial:edgecolor=red subjects_nu/CC1960_0/FreeSurfer_v5-3-0/surf/rh.inflated:overlay=rh.thickness:overlay_threshold=0.1,3::name=inflated_thickness:visible=0 subjects_nu/CC1960_0/FreeSurfer_v5-3-0/surf/lh.inflated:overlay=lh.thickness:overlay_threshold=0.1,3::name=inflated_thickness:visible=0 -viewport 3d -layout 1
```

In order to plot the colormap the following steps were followed:
- After writing the above given code in the terminal, freeview will open on your computer. Double click on `brainmask` and `aparc+aseg` ensuring both of the checkboxes are ticked.
- Click on `Color Map` and select `Lookup Table`. In `Lookup Table` select the `color_gen_class.txt` or `color_gen.txt` files to plot the color maps onto the segmented regions.

## Error with WSL 2 Ubuntu 20.04
In order to create an inflated brain with the annotations the following steps can be used:
- Only tick the checkboxes for `inflated.thickness` for right and left hemisphere while other values are unticked and double click on either of them.
- Click on `Annotations` and select `New`. Write the name as per your desire and for the color table file select `color_gen_class.txt` or `color_gen.txt` files and click on `OK`.

The visualizations should show the positive and negative Cohen's D values as follows:

**Note: Currently there seems to be a bug preventing the visualization for inflated brain with custom color table to render in WSL2 Ubuntu 20.04. [Error Video Link]()**
