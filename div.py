#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  div.py
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



Dividend=14;
Divisor=3;
Increment=1;

for A in range(0,Dividend,Increment):
	Result=A*3;
	print(Result);
	if ( Result > Dividend ):
		Result=(A-Increment)*3;
		print ("The result of ",
				Dividend,
				"/",
				Divisor,
				"is",
				A-Increment,
				"because",
				A-Increment,"*",Divisor,"=",
				Result);
		break;

Dividend=0;
Increment=1;

for A in range(0,Dividend,Increment):
	Result=A*3;
	print(Result);
	if ( Result > Dividend ):
		Result=(A-Increment)*3;
		print ("The result of ",
				Dividend,
				"/",
				Divisor,
				"is",
				A-Increment,
				"because",
				A-Increment,"*",Divisor,"=",
				Result);
		break;

# ex: sts=4 sw=4 et filetype=python
