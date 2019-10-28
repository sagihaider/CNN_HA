#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 14:29:04 2019

@author: sagihaider
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 21:32:11 2019

@author: sagihaider
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:19:51 2019

@author: hr17576
"""

import glob
import shutil
import os
import itertools

#%% Define parameters for looping
people = 9  # Change the number of subjects to work on
subjects = dict(enumerate([str(s).zfill(2) for s in range(1, people+1)]))
print(subjects)

class_id = [1, 2, 3, 4]  # Class information
comb_class = [list(x) for x in itertools.combinations(class_id, 2)]  # All possible class-pairs
print(comb_class)


#%% Train Data copy into folders

for subject, band in enumerate(subjects):
    for row in comb_class:
        print(row)        
        dest_dir = "/Users/sagihaider/Features/EEG_2A/MI_Topo_Sorted/S" + str(subject+1) + "/whole_train_C" + str(row[0]) + str(row[1]) + "/class" + str(row[0])
        dest_dir_class = "/Users/sagihaider/Features/EEG_2A/MI_Topo_UnSorted/S" + str(subject+1) + "/whole_train_C" + str(row[0]) + str(row[1]) + "/*class" + str(row[0]) + ".png"
        print(dest_dir_class)
        if os.path.exists(dest_dir):
            print("True")
            shutil.rmtree(dest_dir, ignore_errors=True, onerror=None)
            print('reomved folder')
            files = glob.glob(dest_dir)
            for f in files:
                 os.remove(f)

        else:
            print("False")
            os.makedirs(dest_dir)        
            print('directory created')
            for file in glob.glob(dest_dir_class):
                 print(file)
                 shutil.copy(file, dest_dir)  
                 print('files copied')

                
            
for subject, band in enumerate(subjects):
    for row in comb_class:
        print(row)        
        dest_dir = "/Users/sagihaider/Features/EEG_2A/MI_Topo_Sorted/S" + str(subject+1) + "/whole_train_C" + str(row[0]) + str(row[1]) + "/class" + str(row[1])
        dest_dir_class = "/Users/sagihaider/Features/EEG_2A/MI_Topo_UnSorted/S" + str(subject+1) + "/whole_train_C" + str(row[0]) + str(row[1]) + "/*class" + str(row[1]) + ".png"
        print(dest_dir_class)
        if os.path.exists(dest_dir):
            shutil.rmtree(dest_dir, ignore_errors=True, onerror=None)
            print('reomved folder')
            files = glob.glob(dest_dir)
            for f in files:
                os.remove(f)
        else:
            os.makedirs(dest_dir)        
            print('directory created')
            for file in glob.glob(dest_dir_class):
                print(file)
                shutil.copy(file, dest_dir)  
                print('files copied')

#%% Test Data Copy into folders

for subject, band in enumerate(subjects):
    for row in comb_class:
        print(row)        
        dest_dir = "/Users/sagihaider/Features/EEG_2A/MI_Topo_Sorted/S" + str(subject+1) + "/whole_test_C" + str(row[0]) + str(row[1]) + "/class" + str(row[0])
        dest_dir_class = "/Users/sagihaider/Features/EEG_2A/MI_Topo_UnSorted/S" + str(subject+1) + "/whole_test_C" + str(row[0]) + str(row[1]) + "/*class" + str(row[0]) + ".png"
        print(dest_dir_class)
        if os.path.exists(dest_dir):
            shutil.rmtree(dest_dir, ignore_errors=True, onerror=None)
            print('reomved folder')
            files = glob.glob(dest_dir)
            for f in files:
                os.remove(f)
        else:
            os.makedirs(dest_dir)        
            print('directory created')
            for file in glob.glob(dest_dir_class):
                print(file)
                shutil.copy(file, dest_dir)  
                print('files copied')

for subject, band in enumerate(subjects):
    for row in comb_class:
        print(row)        
        dest_dir = "/Users/sagihaider/Features/EEG_2A/MI_Topo_Sorted/S"  + str(subject+1) + "/whole_test_C" + str(row[0]) + str(row[1]) + "/class" + str(row[1])
        dest_dir_class = "/Users/sagihaider/Features/EEG_2A/MI_Topo_UnSorted/S" + str(subject+1) + "/whole_test_C" + str(row[0]) + str(row[1]) + "/*class" + str(row[1]) + ".png"
        print(dest_dir_class)
        if os.path.exists(dest_dir):
            shutil.rmtree(dest_dir, ignore_errors=True, onerror=None)
            print('reomved folder')
            files = glob.glob(dest_dir)
            for f in files:
                os.remove(f)
        else:
            os.makedirs(dest_dir)        
            print('directory created')
            for file in glob.glob(dest_dir_class):
                print(file)
                shutil.copy(file, dest_dir)  
                print('files copied')


