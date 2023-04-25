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
- In order to extract the thickness of different brain regions in tabular format run `aparcstats2table --subjects <subject 1> <subject 2> --hemi rh --meas thickness --tablefile thickness_rh.csv` and `aparcstats2table --subjects <subject 1> <subject 2> --hemi lh --meas thickness --tablefile thickness_lh.csv`.
- This will generate the `thickness_lh.csv` and `thickness_rh.csv` files similar to the ones that are present in the [repository](https://github.com/nshreyasvi/mri-exercise) repository. These CSV files contain the thickness of 35 brain regions on left hemisphere and 35 brain regions on the right hemisphere.
- Once we obtain the thickness information, we extract the Cohen's D value for the two groups.


Visualization: CC1960_0

```
freeview subjects_nu/CC1960_0/FreeSurfer_v5-3-0/mri/T1.mgz subjects_nu/CC1960_0/FreeSurfer_v5-3-0/mri/aseg.mgz:colormap=lut subjects_nu/CC1960_0/FreeSurfer_v5-3-0/mri/brainmask.mgz subjects_nu/CC1960_0/FreeSurfer_v5-3-0/mri/aparc+aseg.mgz subjects_nu/CC1960_0/FreeSurfer_v5-3-0/mri/wm.mgz:visible=0 -f subjects_nu/CC1960_0/FreeSurfer_v5-3-0/surf/lh.white:edgecolor=blue subjects_nu/CC1960_0/FreeSurfer_v5-3-0/surf/rh.white:edgecolor=blue subjects_nu/CC1960_0/FreeSurfer_v5-3-0/surf/lh.pial:edgecolor=red subjects_nu/CC1960_0/FreeSurfer_v5-3-0/surf/rh.pial:edgecolor=red subjects_nu/CC1960_0/FreeSurfer_v5-3-0/surf/rh.inflated:overlay=rh.thickness:overlay_threshold=0.1,3::name=inflated_thickness:visible=0 subjects_nu/CC1960_0/FreeSurfer_v5-3-0/surf/lh.inflated:overlay=lh.thickness:overlay_threshold=0.1,3::name=inflated_thickness:visible=0 -viewport 3d -layout 1
```