
import mne
import os
import os.path as op
import numpy as np
import pandas as pd

os.environ['SUBJECTS_DIR'] = '/net/server/data/Archive/piansrann/freesurfer'
subjects_dir = '/net/server/data/Archive/piansrann/freesurfer'


subjects = ['W001','W002','W003','W004','W005','W006','W007', 'W008','W009','W010','W011','W012',
            'W013','W014','W015','W016'] 
group=['a_1','b_1','c_1','d_1','a_2','b_2','c_2','d_2']

date = ['230628','230704','230710','230711','230714','230718','230722','230724','230804',
        '230807','230809','230816','230821','230824']
        
     



for subj in subjects:
    for d in date:
        try:
            raw_er = mne.io.read_raw_fif('/net/server/data/Archive/piansrann/meg/{0}/{1}/{0}_er_raw_bads.fif'.format(subj,d),preload=True) 
            
            picks_meg = mne.pick_types(raw_er.info, meg=True, eeg=False, eog=False, stim=False, exclude=[])
            
            #raw_er.notch_filter(np.arange(50, 201, 50), filter_length='auto', phase='zero', n_jobs=-1)
            #raw_er.filter(2, 40., fir_design='firwin')
            #picks_meg = mne.pick_types(raw_er.info, meg=True, eeg=False, eog=False, stim=False, exclude=[])
            rank=mne.compute_rank(raw_er,rank='info', info=raw_er.info)
       
            cov = mne.compute_raw_covariance(raw_er,  method=('auto'), rank=rank,picks=picks_meg, n_jobs=-1)

            cov = mne.cov.regularize(cov, raw_er.info, mag=0.01, grad=0.01, rank=rank)
            
            cov.plot(raw_er.info, exclude="bads")
            
            
            cov.save('/net/server/data/Archive/piansrann/data_processing/main_experiment/sources/cov_matrix_empty_room/{0}_er-cov.fif'.format(subj))
        except (OSError):
            print('This file not exist')
