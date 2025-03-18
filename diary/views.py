from django.shortcuts import render
from django.views import View
from datetime import datetime
from zoneinfo import ZoneInfo
ser_data=78
data1=78
data2=78
data3=78
data4=78
data5=78
data6=88
data7=68

class IndexView(View):
    def get(self, request):
        now_time = datetime.now(
            ZoneInfo("Asia/Tokyo")
        ).strftime("%Y年%m月%d日 %H:%M:%S")
        return render(
            request, "diary/index.html", {"now_time": now_time , "ser_data":ser_data , "data1":data1 ,
"data2":data2,
"data3":data3,
"data4":data4,
"data5":data5,
"data6":data6,
"data7":data7
})  
 

index = IndexView.as_view()
