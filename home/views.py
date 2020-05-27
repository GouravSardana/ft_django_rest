from rest_framework import viewsets
from home.models import FtUser
from home.serializers import FtUserSerializer


class FtUserViewSet(viewsets.ModelViewSet):
    serializer_class = FtUserSerializer
    queryset = FtUser.objects.all()

    def list(self, request, *args, **kwargs):
        response = super(FtUserViewSet, self).list(request, *args, **kwargs)
        if response is not None:
            response.data = {"ok": True, "members": response.data}
        else:
            response.data = {"ok": False, "members": None}
        return response

