
Sub Main
	'Declare the variable that will reference the application
	Dim SurferApp As Object
	Set SurferApp = CreateObject("Surfer.Application")
	SurferApp.Visible = False
	strCurDirectory = CurDir


Set inpath="D:\bokai\python\python-code\calmet\20191216案例10min風場平均與增加影響半徑\模擬結果\uv\"
Set infile="timeuv.txt"

Set outpath="D:\bokai\python\python-code\calmet\20191216案例10min風場平均與增加影響半徑\模擬結果\avg\"
Set Ufile ="time_u_avg.txt"
Set Vfile ="time_v_avg.txt"

'----U GRID
SurferApp.GridData(DataFile:=inpath+infile,xCol:=1, yCol:=2, zCol:=3, NumRows:=40, NumCols:=40, Algorithm:=srfKriging, OutGrid:=outpath+Ufile, OutFmt:=srfGridFmtS7)
'----V GRID
SurferApp.GridData(DataFile:=inpath+infile,xCol:=1, yCol:=2, zCol:=4, NumRows:=40, NumCols:=40, Algorithm:=srfKriging, OutGrid:=outpath+Vfile, OutFmt:=srfGridFmtS7)

End Sub
