Script for the import and analysis of functional time-series MRI data 

Data extracted via fslmeants from pre-processed functional MRI data (see other scripts) using an atlas based approach
Script will import text files creating data-frames for each subject, correlate these to create a within subject functional correlation matrix,
finally these matrices will be flattened, stacked and concatenated with a variable/regressor spreadsheet (containing variables of interest
e.g. IQ/sex/weight etc. which can then be used to correlate with each ROI-ROI correlation matrix) to note, no multiple comparison correction is used
in this instance.

file setup:
1012/time_series is a folder than contains a series of text files (containing time-series data) extracted from a ROI based approach with functional fMRI data.
Each text file labelled by it's subsequent region e.g. thalamus.txt contains n values 

Variable spreadsheet contains a spreadsheet of variables per subject. Organisation; subject first column and variables of interest
in subsequent columns

list = df.columns.tolist() will output a lit of all region names in the analysis
This is useful if you wish to restric the number of regions e.g a focussed analysis on several regions rather than all provided by the atlas
To use; simply delete the ROI in the variable list that *you want to keep* and click save
Then delete the '#' for the lines 'for i in holder: i.drop(list, axis=1, inplace=True)
To check that this is done correct check the output of cor_holder (i.e. do the dimensions of the matrix make sense)




