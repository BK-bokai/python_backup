
Sub Main
	'Declare the variable that will reference the application
	Dim SurferApp As Object
	Set SurferApp = CreateObject("Surfer.Application")
	SurferApp.Visible = False
	strCurDirectory = CurDir


Set inpath="D:\bokai\python\python-code\calmet\20191216ㄒ糤代紇臫畖\家览挡狦\uv\"
Set infile="20191216_1910uv.txt"

Set outpath="D:\bokai\python\python-code\calmet\20191216ㄒ糤代紇臫畖\家览挡狦\avg\"
Set Ufile ="20191216_1910_u_avg.txt"
Set Vfile ="20191216_1910_v_avg.txt"

'----U GRID
SurferApp.GridData(DataFile:=inpath+infile,xCol:=1, yCol:=2, zCol:=3, NumRows:=40, NumCols:=40, Algorithm:=srfKriging, OutGrid:=outpath+Ufile, OutFmt:=srfGridFmtS7)
'----V GRID
SurferApp.GridData(DataFile:=inpath+infile,xCol:=1, yCol:=2, zCol:=4, NumRows:=40, NumCols:=40, Algorithm:=srfKriging, OutGrid:=outpath+Vfile, OutFmt:=srfGridFmtS7)

End Sub
