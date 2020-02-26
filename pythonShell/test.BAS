Sub Main
	'Declare the variable that will reference the application
	Dim SurferApp As Object
	Set SurferApp = CreateObject("Surfer.Application")
	SurferApp.Visible = False


'Open base SRF file
Set Plot = SurferApp.Documents.Open("D:\bokai\劉博凱_景丰\calmet\20190619南科案例\模擬結果\南科.srf")

Set Title = Plot.Shapes.Item(index:="Title")
Title.Text = "2019_M06_D19_1620(UTC+0800)"

Set Vector = Plot.Shapes.Item(index:="Vector")
Set obs = Vector.Overlays(2)
Set sim = Vector.Overlays(1)

obs.DataFile = "D:\bokai\劉博凱_景丰\calmet\20190619南科案例\模擬結果\obs\2019_M06_D19_1620(UTC+0800)_OBS_1HR.vec"
sim.SetInputGrids("D:\bokai\劉博凱_景丰\calmet\20190619南科案例\模擬結果\avg\20190619_1620_u_avg.txt","D:\bokai\劉博凱_景丰\calmet\20190619南科案例\模擬結果\avg\20190619_1620_v_avg.txt")


Plot.Export("D:\bokai\劉博凱_景丰\calmet\20190619南科案例\模擬結果\imgs\test.gif",Options:="Width=1024, Height=1024")


End Sub
