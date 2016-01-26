from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import os
from Tutorial_Samin import settings


def UploadIMG(request):

    if request.POST:
        Getimg = request.FILES.dict()
        image = Getimg['file']
        f = ContentFile(image.read())
        path = default_storage.save('PATH_SETTING(MADIA_ROOT)\\1.png', f)
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        img = open(tmp_file.__str__(),'rb').read()
        o = Student(image=img)
        InsertDB(o)
        os.remove(path)

    return render(request,"UploadImage.html")
