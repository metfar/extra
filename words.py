#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cod.py
#  
#  Copyright 2024 William Martinez Bas <metfar@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import chardet;#This library will be used to detect the charset later

def undump(inp:str)->str:
	"""
		Convert an hexadecimal dump into a bytes array
	"""
	out=b'';						#create an empty array of bytes
	
	arr:str="".join(inp.split());	#delete spaces from the input string
									#and put it into string arr

	for f in range(0,len(arr),2):	#loop thru the arr string, step 2
		sec=arr[f:f+2];				#take two characters
		dec=int(sec,16);			#convert the hexadecimal characters to an int
		out+=bytes([dec]);			#add the decimal as a byte to out array of bytes
	return(out);
	
def undumptxt(inp:str)->str:
	"""
		Convert an hexadecimal dump with/without spaces
		into a string containing one row for each byte 
		with the whole info of each.
	"""
	out:str="";
	#clean it
	arr:str="".join(inp.split());
	for f in range(0,len(arr),2):
		sec=arr[f:f+2];
		dec=int(sec,16);
		charac=chr( 32 if dec==10 else dec);
		if dec==170:
			out+=" === EOF === ";
		else:
			out+="%02d"%(f/2);					#byte number
			out+=": "+sec;						#hexadecimal
			out+="=>"+("%03d"%dec);				#to decimal value
			out+="--->"+charac;					#corresponding to character
		out+="\n";								#line feed
	return(out);

def main(args):
	"""
	Create a file containing the French word épistèmê (because it has acute, grave and circumflex accents )
	
	Meaning: Common name. (Philosophy) All scientific knowledge, the knowledge of an era and its presuppositions.
			"Nom commun. (Philosophie) Ensemble des connaissances scientifiques, du savoir d'une époque et ses présupposés. "(Wikimedia Foundation, Inc, 2023)
	"""
	
	f=open("word","wb"); 				#create a file pointer to write a binary information
	f.write("épistèmê".encode());		#convert the string with the word into bytes, and write it to the file
	f.close();							#close the file
	
	strdump= 'a9c3 6970 7473 a8c3 c36d 0d 0aaa';		#output of linux: hexdump word (Kerrisk, 2023)
			# ···  i p  t s  ···  ··m  \n \r\eof		This is a Most Significant Byte of Word First (HiLow; BigEndian)
			
	strdump2='c3a9 7069 7374 c3a8 6dc3 aa 0d 0a';		#the same string but using Less Significant Byte of Word First
			# ···  p i  s t  ···  ··m  \n \r\eof		(Lower-Higher order) (LittleEndian)  
	
	f=open("word","rb");# read the file "word" (created above) and get the data
	data=f.read();
	f.close();
	print(data);		#print the bytes of the file: b'\xc3\xa9pist\xc3\xa8m\xc3\xaa'
						#which is the input of strdump2, showing that the data was write in the file
						#in Little Endian format, and not in Big Endian like hexdump displayed before
	
	print(undumptxt(strdump));		#prints bytes info of hexdump
	print(undumptxt(strdump2));		#prints bytes info of the file "word"
	
	undumpped=undump(strdump2);		#convert the strdump2 string into an array of bytes
	charset=chardet.detect(undumpped)['encoding'];#detect the encoding (most of the times) of the undumpped variable
	print(undump(strdump2).decode(charset));	#prints it decoded
	return(0);

if __name__ == '__main__':
	import sys;
	sys.exit(main(sys.argv));

# ex: sts=4 sw=4 et filetype=python
