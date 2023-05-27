import os, glob

for file in glob.glob(r"/home/jovyan/work/EPDE/**/*.py", recursive=True):
    try:
        with open (file, 'r') as f:
            old_data = f.read()
    except:
        continue
    new_data = old_data.replace('np.int', 'np.int_')
    new_data = new_data.replace('np.bool', 'np.bool_')
    new_data = new_data.replace('np.float', 'np.float_')
    new_data = new_data.replace('np.complex', 'np.complex_')
    new_data = new_data.replace('np.object','np.object_')
    new_data = new_data.replace('np.str','np.str_')
    new_data = new_data.replace('np.long','np.longlong',)
    new_data = new_data.replace('np.unicode','np.unicode_')
    with open (file, 'w') as f:
        f.write(new_data)
        #print(file)

for file in glob.glob(r"/home/jovyan/work/torch_DE_solver/**/*.py", recursive=True):
    try:
        with open (file, 'r') as f:
            old_data = f.read()
    except:
        continue
    new_data = old_data.replace('np.int', 'np.int_')
    new_data = new_data.replace('np.bool', 'np.bool_')
    new_data = new_data.replace('np.float', 'np.float_')
    new_data = new_data.replace('np.complex', 'np.complex_')
    new_data = new_data.replace('np.object','np.object_')
    new_data = new_data.replace('np.str','np.str_')
    new_data = new_data.replace('np.long','np.longlong',)
    new_data = new_data.replace('np.unicode','np.unicode_')
    with open (file, 'w') as f:
        f.write(new_data)
        #print(file)