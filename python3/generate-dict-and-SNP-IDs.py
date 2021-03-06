#!/usr/bin/env python3

##usage: define input and output path and run with python3

import os
dictionary = {}

#define input/output
output_path = '../23andmefiles_with_ids'
input_path = '../23andmefiles/'
dictionaryfilename= 'sssss.txt'
files = os.listdir(input_path)
#completeName = os.path.join(output_path, file_name)
#print(completeName)


#define the ID generation
IDprefix= "A.t.1001-random-"
iterator = 0


#print(files)

#testing on a subset of files 
#myfiles = ['6101.23.txt', '9856.23.txt']


#print(files)
#print(myfiles)

##build a dictionary with Chromosome, position and Genotype as Key
for filename in files:
    ##tesing for subset of files 
    #if (filename in myfiles):
        with open(os.path.join(input_path,filename)) as f:
            for line in f:
                ##Split each line.
                line = line.strip().split("\t")
                ##store chromosome, position, and genotype as key in the hash
                next_key=('\t'.join([line[i] for i in [1, 2, 3]]))
                ##and the value in the hash is the ID 
                next_value=line[0]
                ##generate numbered IDs
                iterator = iterator + 1 
                ##overwrite existing key in hash with new ID 
                next_value=IDprefix + str(iterator)
                dictionary[next_key] = next_value

#print(dictionary)

##write the dictionary to a file (=produce the 'common SNP' file)
with open(dictionaryfilename, 'w') as f: 
    for key, value in dictionary.items(): 
        f.write('%s\t%s\n' % (value, key))
    
    
#print("\nImportant output starts here!")
#lookupvalue='1-711-CC'
#print("the value for key "+ lookupvalue +" is %s" % dictionary[lookupvalue])

##add the SNP ID to every variant in every file (generate a new file for each)
for filename in files:
    ##tesing for subset of files 
    #if (filename in myfiles):
        new_outfile_name=os.path.join(output_path, os.path.splitext(filename)[0]+"-with-ID"+".txt")
        print("##")
        print(filename)
        print(new_outfile_name)
        new_outfile = open(new_outfile_name, 'w')
        with open(os.path.join(input_path,filename)) as f:
            for line in f:
                #Split each line.
                line = line.strip().split("\t")
                this_key=('\t'.join([line[i] for i in [1, 2, 3]]))
                new_outfile.write("%s" % dictionary[this_key] + "\t" + this_key + "\n") 
        new_outfile.close()
        
