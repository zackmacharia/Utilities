# Utilities

## Fix_CSV  
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