# Views file of news
# list of table we have in database[profile,category,User,News_content,comments_data,message_user,feedback]
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from admin1.models import News_content
from django.http import HttpResponse
from django.contrib import auth
from .models import User
from admin1.models import profile, category 
from user.models import comments_data, message_user ,feedback
from django.http import HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
Url_Current_location = "/news"
# Create your views here.
def master1(request):
	if request.user.is_authenticated:
		check_status = profile.objects.filter(is_login='News').filter(user_id=request.user)
		if len(check_status) == 1:
			chk_cnt = News_content.objects.all().count()
			if chk_cnt == 0:
				repoter_detail = profile.objects.filter(user_id=request.user)
				return render(request,'news/index.html', {'repoter_detail':repoter_detail})
			else:
				tottal_news = News_content.objects.filter(user_id=request.user).count()			
				Approved = News_content.objects.filter(status="Approved").filter(user_id=request.user).count()
				Pending = News_content.objects.filter(status="Pending").filter(user_id=request.user).count()
				tottal_comments = comments_data.objects.all().count()
				latest_news = News_content.objects.filter(status="Approved").latest('id')
				latest = News_content.objects.get(News_title=latest_news).news_category		
				repoter_detail = profile.objects.filter(user_id=request.user)
				return render(request, 'news/index.html', {'tottal_news':tottal_news, 'Approved':Approved, 'Pending':Pending, 'tottal_comments':tottal_comments, 'latest':latest, 'repoter_detail':repoter_detail})
		else:
			auth.logout(request)
			return render(request, 'news/Login.html', {"error":"Login fail! You are not a reporter."})			
	else:
		return render(request, 'news/Login.html')

def index(request):
	if request.user.is_authenticated:		
		check_status = profile.objects.filter(is_login='News').filter(user_id=request.user)
		if len(check_status) == 1:			
			repoter_detail = profile.objects.filter(user_id=request.user)
			return render(request,'news/index.html', {'repoter_detail':repoter_detail})
		else:		
			auth.logout(request)		
			return render(request, 'news/Login.html', {"error":"Login fail! You are not a reporter."})
	else:
		return render(request, 'news/Login.html')
	
def user_profile(request):
	if request.user.is_authenticated:		
		check_status = profile.objects.filter(is_login='News').filter(user_id=request.user)
		if len(check_status) == 1:
			all_profile = profile.objects.filter(user_id=request.user)			
			al = profile.objects.get(user_id=request.user).facebook
			user = User.objects.all()
			print("your facebook is")
			print(al)
			return render(request,'news/Profile.html', {'all_profile':all_profile,'edit_profile':edit_profile})
		else:		
			auth.logout(request)		
			return render(request, 'news/Login.html', {"error":"Login fail! You are not a reporter."})
	else:
		return render(request, 'news/Login.html')
def edit_profile(request):
	if request.method == "POST":
		edit_profile = profile.objects.filter(user_id=request.user)
		phn = request.POST['phone_no']
		addrs = request.POST['address']
		prof = request.POST['proffession']
		fb = request.POST['facebook_profile']
		insta = request.POST['instagram_profile']
		twit = request.POST['twitter_profile']
		fld = request.POST['Field_location']
		fnm = request.POST['fname']
		lst = request.POST['lname']
		email = request.POST['email']
		data_id = request.POST['id']
		chk = profile.objects.get(user_id=request.user).image
		try:			
			filepath = request.FILES['image1']
		except MultiValueDictKeyError:
			filepath = False

		if filepath == False:
			name_img = chk
		else:			
			fs1 = FileSystemStorage()
			filename = fs1.save(filepath.name, filepath)
			name_img = fs1.url(filename)	
		ext = profile(id=data_id, phone_no=phn, Address=addrs, proffession=prof, facebook=fb, instagram=insta, twitter=twit, Field_location=fld, user_id=request.user, image=name_img, is_login='News')
		ext.save()
		return redirect('/news/user_profile')
	else:			
		edit_profile = profile.objects.filter(user_id=request.user)		
		return render(request,'news/Profile.html', {'edit_profile':edit_profile})	

def Addnews(request):
	if request.user.is_authenticated:
		check_status = profile.objects.filter(is_login='News').filter(user_id=request.user)
		if len(check_status) == 1:
			if request.method == 'POST':
				n_title = request.POST['NewsTitle']
				content = request.POST['COntent']
				vdo = request.POST['video']
				News_category = request.POST['News_Type']
				image1 = request.FILES['image1']
				fs1 = FileSystemStorage()
				filename = fs1.save(image1.name, image1)
				url1 = fs1.url(filename)			
				data_stored = News_content(News_title=n_title, content=content, video=vdo, news_category=News_category, image=url1, user_id=request.user)
				data_stored.save()
				return redirect('/news/status')
			else:			
				category_data = category.objects.all()
				return render(request, 'news/Addnews.html', {'category_data':category_data})
		else:		
			auth.logout(request)		
			return render(request, 'news/Login.html', {"error":"Login fail! You are not a reporter."})
	else:		
		return render(request, 'news/Login.html', {"error":"Invalid user"})

def Status(request):
	if request.user.is_authenticated:	
		check_status = profile.objects.filter(is_login='News').filter(user_id=request.user)
		if len(check_status) == 1:
			spec_data = News_content.objects.filter(user_id=request.user)
			Url_Current_location = "news/Status.html"
			return render(request, Url_Current_location, {'data1':spec_data})
		else:		
			auth.logout(request)		
			return render(request, 'news/Login.html', {"error":"Login fail! You are not a reporter."})
	else:
		return render(request, 'news/Login.html')

def login(request):
	if request.user.is_authenticated:
		auth.login(request, request.user)
		return redirect('/news')
	else:
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = auth.authenticate(username=username,password=password)
			check_status = profile.objects.filter(is_login='News').filter(user_id=user)
			if len(check_status) == 1:
				if user is not None:
					auth.login(request, user)
					return redirect('/news')
				else:
					return render(request, 'news/Login.html', {"error":"Login fail! Invalid credential"})
		else:				
			return render(request, 'news/Login.html', {"error":"Login fail! You are not a reporter."})

def logout(request):
	auth.logout(request)
	return render(request, 'news/Login.html')

def edit_data(request,id):
	spec_data_edit = News_content.objects.filter(id=id)
	show_category_data = category.objects.all()
	return render(request,'news/Status.html',{'edit_data':spec_data_edit, 'show_category_data':show_category_data})

def show_data(request, id):
	show_data = News_content.objects.filter(id=id)
	return render(request, 'news/Status.html', {'show_data':show_data})
	
def edit_data_stored(request, id):
	n_title = request.POST['news_title']
	content = request.POST['content']
	vdo = request.POST['video']
	news_image = News_content.objects.get(id=id).image
	try:			
		image1 = request.FILES['image1']
		fs1 = FileSystemStorage()
		filename = fs1.save(image1.name, image1)
		url1 = fs1.url(filename)			
	except MultiValueDictKeyError:
		url1 = news_image
	News_category = request.POST['News_Type']
	Status = "Pending"
	data_stored = News_content(id=id, News_title=n_title, content=content, image=url1, video=vdo, news_category=News_category, status=Status, user_id=request.user)
	data_stored.save()	
	return redirect('/news/status')

def data_delete(request, id):
	delete_data = News_content.objects.filter(id=id)
	delete_data.delete()
	return redirect('/news/status')	

def show_comment(request,id):
	comment = comments_data.objects.filter(news_id=id)	
	print(comment)
	return render(request, 'news/Status.html', {'comment':comment})

def comment_data(request, id):
	if comments_data.objects.filter(id=id):
		print("DELETE_QUERY IS FIRED NOW")
		comment_delete = comments_data.objects.filter(id=id)
		comment_news = comments_data.objects.get(id=id).news_id	
		news_get_id =  News_content.objects.get(News_title=comment_news).id	
		news = News_content.objects.filter(id=news_get_id)
		comment = comments_data.objects.filter(news_id=comment_news)	
		comment_delete.delete()
		return render(request, 'news/Status.html', {'comment':comment, 'news':news})
	else:
		Url_Current_location = '/news/status'
		return HttpResponseRedirect(Url_Current_location)

def total_News(request):
	if request.user.is_authenticated:
		check_status = profile.objects.filter(is_login='News').filter(user_id=request.user)
		if len(check_status) == 1:
			tottal_news = News_content.objects.filter(user_id=request.user).count()
			latest_tottal_news = News_content.objects.filter(user_id=request.user)
			Approved = News_content.objects.filter(status="Approved").count()
			Pending = News_content.objects.filter(status="Pending").count()
			tottal_comments = comments_data.objects.all().count()
			latest_news = News_content.objects.filter(status="Approved").latest('id')
			latest = News_content.objects.get(News_title=latest_news).news_category		
			return render(request, 'news/index.html', {'tottal_news':tottal_news, 'Approved':Approved, 'Pending':Pending, 'tottal_comments':tottal_comments, 'latest':latest, 'latest_tottal_news':latest_tottal_news})
		else:
			auth.logout(request)
			return render(request, 'news/Login.html', {"error":"Login fail! You are not a reporter."})			
	else:
		return render(request, 'news/Login.html')

def Approved_News(request):
	if request.user.is_authenticated:
		check_status = profile.objects.filter(is_login='News').filter(user_id=request.user)
		if len(check_status) == 1:
			tottal_news = News_content.objects.filter(user_id=request.user).filter(user_id=request.user).count()
			data_Approved_news = News_content.objects.filter(status="Approved").filter(user_id=request.user)
			Approved = News_content.objects.filter(status="Approved").filter(user_id=request.user).count()
			Pending = News_content.objects.filter(status="Pending").filter(user_id=request.user).count()
			tottal_comments = comments_data.objects.all().count()
			latest_news = News_content.objects.filter(status="Approved").latest('id')
			latest = News_content.objects.get(News_title=latest_news).news_category		
			return render(request, 'news/index.html', {'tottal_news':tottal_news, 'Approved':Approved, 'Pending':Pending, 'tottal_comments':tottal_comments, 'latest':latest, 'data_Approved_news':data_Approved_news})
		else:
			auth.logout(request)
			return render(request, 'news/Login.html', {"error":"Login fail! You are not a reporter."})
	else:
		return render(request, 'news/Login.html')

def pending(request):
	if request.user.is_authenticated:
		check_status = profile.objects.filter(is_login='News').filter(user_id=request.user)
		if len(check_status) == 1:
			tottal_news = News_content.objects.filter(user_id=request.user).filter(user_id=request.user).count()
			data_pending_news = News_content.objects.filter(status="Pending").filter(user_id=request.user).filter(user_id=request.user)
			Approved = News_content.objects.filter(status="Approved").filter(user_id=request.user).count()
			Pending = News_content.objects.filter(status="Pending").filter(user_id=request.user).count()
			tottal_comments = comments_data.objects.all().count()
			latest_news = News_content.objects.filter(status="Approved").latest('id')
			latest = News_content.objects.get(News_title=latest_news).news_category		
			return render(request, 'news/index.html', {'tottal_news':tottal_news, 'Approved':Approved, 'Pending':Pending, 'tottal_comments':tottal_comments, 'latest':latest, 'data_pending_news':data_pending_news})
		else:
			auth.logout(request)
			return render(request, 'news/Login.html', {"error":"Login fail! You are not a reporter."})
	else:
		return render(request, 'news/Login.html')

def data_comments(request):
	if request.user.is_authenticated:
		check_status = profile.objects.filter(is_login='News').filter(user_id=request.user)
		if len(check_status) == 1:
			tottal_news = News_content.objects.filter(user_id=request.user).count()
			data_comments = comments_data.objects.all()
			Approved = News_content.objects.filter(status="Approved").filter(user_id=request.user).count()
			Pending = News_content.objects.filter(status="Pending").filter(user_id=request.user).count()
			tottal_comments = comments_data.objects.all().count()
			latest_news = News_content.objects.filter(status="Approved").latest('id')
			latest = News_content.objects.get(News_title=latest_news).news_category		
			return render(request, 'news/index.html', {'tottal_news':tottal_news, 'Approved':Approved, 'Pending':Pending, 'tottal_comments':tottal_comments, 'latest':latest, 'data_comments':data_comments})
		else:
			auth.logout(request)
			return render(request, 'news/Login.html', {"error":"Login fail! You are not a reporter."})
	else:
		return render(request, 'news/Login.html')

def delete_all(request):
	delete_profile =  profile.objects.all()
	delete_profile.delete()
	delete_category = category.objects.all()
	delete_category.delete()
	delete_User = User.objects.all()
	delete_User.delete()
	delete_News_content = News_content.objects.all()
	delete_News_content.delete()
	delete_comments_data = comments_data.objects.all()
	delete_comments_data.delete()
	delete_message_user = message_user.objects.all()
	delete_message_user.delete()
	delete_feedback =  feedback.objects.all()
	delete_feedback.delete()
	return redirect('/news')
