import mne
mne.viz.set_3d_options(antialias=False)

os.environ['SUBJECTS_DIR'] = '/net/server/data/Archive/piansrann/freesurfer'
subjects_dir = '/net/server/data/Archive/piansrann/freesurfer'

subjects = ['W001','W002','W003','W004','W005','W006','W007', 'W008','W009','W010','W011','W012',
            'W013','W014','W015'] 




conductivity = [0.3] # for single layer        
        
for subj in subjects:
    print(subj)
    conductivity = [0.3] # for single layer
    model = mne.make_bem_model(subject=subj, ico=5, conductivity= conductivity, subjects_dir=subjects_dir, verbose=None)

    bem = mne.make_bem_solution(model)
    plot_bem_kwargs = dict(subject=subj,subjects_dir=subjects_dir,
    brain_surfaces="white",orientation="coronal",slices=[50, 100, 150, 200],)
    mne.viz.plot_bem(**plot_bem_kwargs)
    
    mne.write_bem_solution('/net/server/data/Archive/piansrann/data_processing/main_experiment/sources/bem/{0}_bem.h5'.format(subj), bem, overwrite=True, verbose=None)
        
