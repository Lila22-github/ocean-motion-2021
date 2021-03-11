import sys

date = sys.argv[1]

vectorq_practicefile = open("vectorq.exec","w")

vectorq_practicefile.write("#!/bin/csh\n")

vectorq_practicefile.write("set dir = ./test/")
vectorq_practicefile.write("set dhdir = /Users/brownscholar/desktop/Internship/atlantic_data/dh/\n")
vectorq_practicefile.write("set dendir = /Users/brownscholar/desktop/Internship/atlantic_data/density/\n")
vectorq_practicefile.write("set auxdir = /Users/brownscholar/desktop/Internship/atlantic_data/aux/\n")
vectorq_practicefile.write("set outdir = /Users/brownscholar/desktop/Internship/atlantic_data/omega/\n")
vectorq_practicefile.write("set fileinfo = {$dir}info_pr.dat\n")
vectorq_practicefile.write("set filedh =  {$dhdir}/dh_" +date+ ".txt\n")
vectorq_practicefile.write("set filest =  {$dendir}/density_"+date+ ".txt\n")
vectorq_practicefile.write("set filestm = {$auxdir}/st0/"+date+ "_st0.dat\n")
vectorq_practicefile.write("set filequ =  {$outdir}/u/"+date+ "_qu.gr\n")
vectorq_practicefile.write("set fileqv =  {$outdir}/v/"+date+ "_qv.gr\n")
vectorq_practicefile.write("set fileqdi = {$auxdir}/qdi/"+date+ "_qdi.gr\n")
vectorq_practicefile.write("\n")
vectorq_practicefile.write("./vectorq.exe << !\n")
vectorq_practicefile.write("'$fileinfo'	#>>>>>Escribe info file info.dat:\n")
vectorq_practicefile.write("'$filedh'	#>>>>>Escribe fichero de altura Dinamica:\n")
vectorq_practicefile.write("'$filest'	#>>>>>Escribe fichero de densidad:")
vectorq_practicefile.write("'$filestm'	#>>>>>Escribe fichero de densidad promedio:\n")
vectorq_practicefile.write("'$filequ'	#>>>>>Escribe fichero Qu:\n")
vectorq_practicefile.write("'$fileqv'	#>>>>>Escribe fichero Qv:\n")
vectorq_practicefile.write("'$fileqdi'	#>>>>>Escribe fichero Qdi:\n")

vectorq_practicefile.close()