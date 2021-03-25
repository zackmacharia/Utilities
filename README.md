# Utilities

## COMPACT
This generator function removes duplicate subsequent values in a sequence.
### Example: Working with a sequence of integers
#### Command: python compact.py

Input Sequence: [1, 1, 2, 2, 3, 2]

## CSV-PARSER    
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

## DEV-ENV-SETUP
This utility automates the workflow for building a development environment.
Automated Tasks Details:
* Clones remote GitHub reposistory
* Creates a new python3 virtualenvironment
### Example: Creating a new environment for user zackmacharia and repo name demo
#### Command: python envSetup.py zackmacharia demo

## TAIL  
This utility takes a sequence or an iterator and returns the last items specified by an integer passed as input
### Example: Working with a sequence
#### Command: python tail.py(seq, num)

Input Sequence and Integer passed to function:
seq = [1, 1, 2, 2, 3, 2]; num = 3

Output Sequence: [2, 3, 2] --> returns the last 3 items specified by num

## AWS-IPS    
This utility reads a JSON file containing AWS IPS and creates a new file with IP Address information only for the specified regions, in this case the US region.  
### Example: Reading contents from a URL and creating a file with US AWS IPS
#### Command: go run get_awsips_url.go  

Input Resource: Published AWS IPS URL provided by Amazon  
 
Output File: US_REGION_AWS_IPS  

15.230.39.48/31   
15.230.39.238/31    
15.230.131.48/28   