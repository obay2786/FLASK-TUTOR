import openpyxl
import json
from openpyxl import load_workbook


def isiformexcel():

	#DATA
	
	# nama = "faris" # C5
	# design = "by Siberkolosis" # C6
	# company = "PT. SPI" # C7
	# date = "16-10-2021" # C9
	# timeFrom = "11:00" # C10
	# timeTo = "12:00" # E10
	# purpose = "Purpose: Service AC"; # A11
	# anggota = "[{\"Nama\":\"11810021\",\"NIK\":\"SUBIANTO\"},{\"Nama\":\"123456\",\"NIK\":\"Fadil\"}]" #h7
	

	sourcefile = r'VisitorApprovalBT.xlsx';

	wb = load_workbook(sourcefile);

	sheet = wb['Visitor Approval'];
	sheet['C5'] = nama;
	sheet['C6'] = design
	sheet['C7'] = company
	sheet['C9'] = date
	sheet['C10'] = timeFrom
	sheet['E10'] = timeTo 
	sheet['A11'] = purpose 

	wb.save(sourcefile)

	return sourcefile

isiformexcel()
