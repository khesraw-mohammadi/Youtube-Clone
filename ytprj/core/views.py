from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from core.models import Video, Comment
from django.views.decorators.csrf import csrf_exempt




def index(request):
    video = Video.objects.filter(visibility="public")    
    context = {
        "video":video
    }

    return render(request, "index.html", context)


def videoDetail(request, pk):
    video = Video.objects.get(id=pk)
    
    video.views = video.views + 1
    video.save()

    # comments section
    comments = Comment.objects.filter(active=True, video=video).order_by("-date")

    context = {
        "video":video,
        "comments" : comments
    }

    return render(request, "video-detail.html", context)


def ajax_save_comment(request):
    
    if request.method == "POST":
        pk = request.POST.get("id")
        comment = request.POST.get("comment")
        video = Video.objects.get(id=pk)
        user = request.user

        new_comment = Comment.objects.create(comment = comment, user = user, video = video)
        responst = "Comment Posted"
        return HttpResponse(responst)
    


@csrf_exempt
def ajax_delete_comment(request):
    if request.method == "POST":
        id = request.POST.get("cid")
        comment = Comment.objects.get(id=id)
        comment.delete()
        return JsonResponse({"status":1})
    else:
        return JsonResponse({"status":2})

