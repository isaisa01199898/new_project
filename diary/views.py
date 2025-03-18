from django.shortcuts import render
from django.views import View
from datetime import datetime
from zoneinfo import ZoneInfo
ser_data=78
data=78,68.75.85,92,120
class IndexView(View):
    def get(self, request):
        now_time = datetime.now(
            ZoneInfo("Asia/Tokyo")
        ).strftime("%Y年%m月%d日 %H:%M:%S")
        return render(
            request, "diary/index.html", {"now_time": now_time , "ser_data":ser_data})  # 修正: コンテキストを辞書に変更
 

index = IndexView.as_view()
