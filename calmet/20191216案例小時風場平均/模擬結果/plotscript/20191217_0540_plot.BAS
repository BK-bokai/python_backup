Sub Main
	'Declare the variable that will reference the application
	Dim SurferApp As Object
	Set SurferApp = CreateObject("Surfer.Application")
	SurferApp.Visible = False


'Open base SRF file
Set Plot = SurferApp.Documents.Open("D:\bokai\python\python-code\calmet\20191216案例10min風場平均\模擬結果\南科v2.srf")

Set Title = Plot.Shapes.Item(index:="Title")
Title.Text = "2019_M12_D17_0540(UTC+0800)_AVG"

Set Vector = Plot.Shapes.Item(index:="Vector")
Set obs = Vector.Overlays(2)
Set sim = Vector.Overlays(1)

Vector.SetLimits(xMin:=165.4, xMax:=185.4, yMin:=2545.8, yMax:=2565.8)
Vector.xMapPerPU = 2.857142857
Vector.yMapPerPU = 2.857142857

Set lineMap = Plot.Shapes.Item(index:="lineMap")
lineMap.SetLimits(xMin:=165000, xMax:=186000, yMin:=2545000, yMax:=2566000)
lineMap.xMapPerPU = 1909.090909
lineMap.yMapPerPU = 1909.090909



obs.DataFile = "D:\bokai\python\python-code\calmet\20191216案例10min風場平均\模擬結果\obs\2019_M12_D17_0540(UTC+0800)_OBS_1HR.vec"

sim.SetInputGrids("D:\bokai\python\python-code\calmet\20191216案例10min風場平均\模擬結果\avg\20191217_0540_u_avg.txt","D:\bokai\python\python-code\calmet\20191216案例10min風場平均\模擬結果\avg\20191217_0540_v_avg.txt")


Plot.Export("D:\bokai\python\python-code\calmet\20191216案例10min風場平均\模擬結果\imgs\201912170540.jpg",Options:="Width=654, Height=650")

'Plot.Export("D:\bokai\劉博凱_景丰\107112\calmet\20190619南科案例\模擬結果\imgs\201912170540.jpg")

End Sub
