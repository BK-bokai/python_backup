import report
from report import get_description
from report import get_description as des
description = report.get_description()
description2 = get_description()
description3 = des()
print("Yesterday's weather", description3)
print("Today's weather:", description)
print("tomorrow's weather:", description2)

# python解釋器會將 *.py 腳本文件進行編譯，並將編譯結果保存到__pycache__目錄中。
#下次再執行工程時，若解釋器發現這個 *.py 腳本沒有修改過，就會跳過編譯這一步，直接運行以前生成的保存在 __pycache__文件夾裡的 *.pyc 文件。
#這樣工程較大時就可以大大縮短項目運行前的準備時間；如果你只需執行一個小工程，沒關係 忽略這個文件夾就行。