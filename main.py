from class_wiggle import  Wiggle


# set to 'True' if you want to save an output file

write_file = True

# Enter the full path to the wiggle file that you want to normalise

filename ='C:\\Users\\hpatterton\\Documents\\Students\\Jessica Reid\\NGS\\Galaxy543-[K16_6d_(Bedgraph_Treatment)]_normalized_by_1.28688747_3.wig'
wiggle = Wiggle()

# The normalization factor to use.  Each data point is multiplied by this factor.

factor = 1

wiggle_array,total,number_of_values = wiggle.NormalizeWiggleFile(filename, factor)
dot = filename.rfind('.')
outfile = filename[:dot]+'_normalized_by_'+str(factor)+'_4.wig'
if(write_file):
	handle = open(outfile,'w')
	max = len(wiggle_array)
	for index in range(0,max):
		handle.write(wiggle_array[index])
	handle.close()
	print('Written to '+outfile)
	print(str(number_of_values)+' data values written')
print('Total value = '+str(total))



number_of_data_points_in_chromosome,total_counts_in_chromosome,chromosome_name = wiggle.CountsPerChromosome(filename)
number_of_chromosomes = len(chromosome_name)
for i in range(0,number_of_chromosomes):
	print(chromosome_name[i],'\t',number_of_data_points_in_chromosome[i],'\t',total_counts_in_chromosome[i])


