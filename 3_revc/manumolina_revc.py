'''
/*
 * @name: revc.py
 * @author: Manu Molina
 * @version: 1.0
 * @description: 
 	Given: A DNA string ss of length at most 1000 bp.
	Return: The reverse complement scsc of ss.
 * @date: 30/11/2017 
 * @python version: 3.6.3 Anaconda
*/
'''
dict = {
'A':'T',
'C':'G',
'G':'C',
'T':'A'
}

str = "AAAACCCGGT"
for key in dict:
	str = str.replace(key, dict[key])

print(str)

'''with open("Output.txt", "w") as text_file:
    print(str, file=text_file)'''
