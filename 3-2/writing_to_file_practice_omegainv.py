import sys

date = sys.argv[1]

omegainv_practicefile = open("omegainv.exec","w")

omegainv_practicefile.write("#!/bin/csh\n")

omegainv_practicefile.write("set dir = ./test/\n")
omegainv_practicefile.write("set fileinfo = {$dir}info_pr.dat\n")
omegainv_practicefile.write("set outdir = /Users/brownscholar/desktop/BridgeUp Internship/atlantic_data/omega/\n")
omegainv_practicefile.write("set auxdir = /Users/brownscholar/desktop/BridgeUp Internship/atlantic_data/aux/\n")
omegainv_practicefile.write("set filestm = {$auxdir}/st0/"+date+"_st0.dat\n")
omegainv_practicefile.write("set fileqdi = {$auxdir}/qdi/"+date+"_qdi.gr\n")
omegainv_practicefile.write("set filew =  {$outdir}w/"+date+"_ww.gr\n")
omegainv_practicefile.write("\n")
omegainv_practicefile.write("./omegainv.exe << !\n")
omegainv_practicefile.write("'$fileinfo' 	#>>>>>Escribe info file info.dat:\n")
omegainv_practicefile.write("'$fileqdi' 	#>>>>>Escribe fichero de Div Q:\n")
omegainv_practicefile.write("''$filestm'   	#>>>>>Escribe fichero de densidad promedio:\n")
omegainv_practicefile.write("'ominput.dat'  #>>>>>Escribe fichero parametros (ominput.dat):\n")
omegainv_practicefile.write("'$filew'	#>>>>>Escribe fichero Salida W:\n")

omegainv_practicefile.close()
