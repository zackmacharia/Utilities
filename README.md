# Utilities

## COMPACT
This generator function removes duplicate subsequent values in a sequence.
### Example: Working with a sequence of integers
#### Command: python compact.py

Input Sequence: [1, 1, 2, 2, 3, 2]

## CSV_PARSER    
This utility takes a csv file and updates the delimiter per users specification.  
### Example: Changing delimeter from a pipe to comma
#### Command: python fix_csv.py <src_file> <new_file> ,  

Input File:  
Reading|Make|Model|Type|Value  
Reading 0|Toyota|Previa|distance|19.83942  
Reading 1|Dodge|Intrepid|distance|31.28257  

Output File  
Reading,Make,Model,Type,Value  
Reading 0,Toyota,Previa,distance,19.83942  
Reading 1,Dodge,Intrepid,distance,31.28257   

## DEV_ENV_SETUP
This utility automates the workflow for building a development environment.
Automated Tasks Details:
* Clones remote GitHub reposistory
* Creates a new python3 virtualenvironment


## TAIL  
This utility takes a sequence or an iterator and returns the last items specified by an integer passed as input
### Example: Working with a sequence
#### Command: python tail.py(seq, num)

Input Sequence and Integer passed to function:
seq = [1, 1, 2, 2, 3, 2]; num = 3

Output Sequence: [2, 3, 2] --> returns the last 3 items specified by num
