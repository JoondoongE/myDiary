from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

def home(request):
    return render(request, 'main.html')

#메인페이지
def blog(request):
    items = Item.objects.filter().order_by('-pk')
    return render(request, 'blog/blog.html', {'items':items})

def post(request, pk):
    items = Item.objects.get(pk=pk)
    return render(request, 'blog/single_post.html',{'items':items})

# def itemRegist(request):
#     return render(request,'itemRegist.html')

# def itemCreate(request):
#     if request.method=='POST' or request.method =='FILES':
#         items = Item()
#         items.image=request.FILES['image']
#         items.location=request.POST['location']
#         items.body=request.POST['body']
#         items.save()
#     return redirect('main')

#추억등록 위한 페이지
def write(request):
    if request.method == 'GET':
        form = ItemForm()
        return render(request, 'blog/post_write.html', {'form': form})

    elif request.method == 'POST':
        form = ItemForm(request.POST,request.FILES) #작성한 폼을 가져와 form에 저장
        if form.is_valid(): #작성한 폼의 값이 유효하다면
            items = Item() #새로운 Post 객체를 생성해주고 
            items.image = form.cleaned_data['image']
            items.location = form.cleaned_data['location'] #post 객체의 title에 폼에 작성한 title을 저장
            items.body = form.cleaned_data['body'] #post 객체의 content에 폼에 작성한 content를 저장
            items.save() #post를 저장(데이터베이스에 저장한다)
            return redirect('blog') #저장을 하였으면 url name이 'home'인 곳으로 리다이렉트
        return redirect('write') #폼이 유효하지 않았다면 url name이 'write'인 곳으로 리다이렉트
    
def edit(request, pk):
    items = Item.objects.get(pk=pk)
    if request.method =='GET':
        form = ItemForm(instance=items)
        return render(request, 'blog/post_write.html', {'form':form})
    
    else:
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            items.image = form.cleaned_data['image']
            items.location = form.cleaned_data['location'] #post 객체의 title에 폼에 작성한 title을 저장
            items.body = form.cleaned_data['body'] #post 객체의 content에 폼에 작성한 content를 저장
            items.save() #post를 저장(데이터베이스에 저장한다)
            return redirect('home')
        return redirect('blog')


def delete(request, pk):
    items = Item.objects.get(pk=pk)
    items.delete()
    return redirect('blog')

