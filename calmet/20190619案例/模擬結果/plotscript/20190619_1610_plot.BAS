Sub Main
	'Declare the variable that will reference the application
	Dim SurferApp As Object
	Set SurferApp = CreateObject("Surfer.Application")
	SurferApp.Visible = False


'Open base SRF file
Set Plot = SurferApp.Documents.Open("D:\bokai\�B�ճ�_����\107112\calmet\20190619�n��ר�\�������G\�n��v2.srf")

Set Title = Plot.Shapes.Item(index:="Title")
Title.Text = "2019_M06_D19_1610(UTC+0800)_AVG"

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



obs.DataFile = "D:\bokai\�B�ճ�_����\107112\calmet\20190619�n��ר�\�������G\obs\2019_M06_D19_1610(UTC+0800)_OBS_1HR.vec"
sim.SetInputGrids("D:\bokai\�B�ճ�_����\107112\calmet\20190619�n��ר�\�������G\avg\20190619_1610_u_avg.txt","D:\bokai\�B�ճ�_����\107112\calmet\20190619�n��ר�\�������G\avg\20190619_1610_v_avg.txt")


Plot.Export("D:\bokai\�B�ճ�_����\107112\calmet\20190619�n��ר�\�������G\imgs\201906191610.jpg",Options:="Width=654, Height=650")

'Plot.Export("D:\bokai\�B�ճ�_����\107112\calmet\20190619�n��ר�\�������G\imgs\201906191610.jpg")

End Sub
