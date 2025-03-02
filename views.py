from django.shortcuts import render
from django.views import View
from datetime import datetime
from zoneinfo import ZoneInfo

class IndexView(View):
    def get(self, request):
        now_time = datetime.now(
            ZoneInfo("Asia/Tokyo")
        ).strftime("%Y年%m月%d日 %H:%M:%S")
        return render(
            request, "diary/index.htm", {"now_time": now_time})  # 修正: コンテキストを辞書に変更

index = IndexView.as_view()