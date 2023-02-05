from django.core.serializers import serialize
from django.http import JsonResponse
from django.views import View

from area.models import Area


class LoadAreaView(View):
    def get(self, request):
        # 获取请求参数
        pid = request.GET.get('pid', -1)
        pid = int(pid)

        # 根据父id查询区划信息
        areaList = Area.objects.filter(parentid=pid)

        # 进行序列化
        jareaList = serialize('json', areaList)

        return JsonResponse({'jareaList': jareaList})

