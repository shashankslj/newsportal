from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import category, profile
from news.models import News_content
from .models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from user.models import comments_data
from django.utils.datastructures import MultiValueDictKeyError
from user.models import feedback
import feedparser
# Create your views here.
def master1(request):
	if request.user.is_authenticated:
		check_status = profile.objects.filter(is_login='Admin').filter(user_id=request.user)
		if len(check_status) == 1:			
			tottal_news = News_content.objects.all().count()			
			Approved = News_content.objects.filter(status="Approved").all().count()
			Pending = News_content.objects.filter(status="Pending").all().count()
			tottal_category = category.objects.all().count()
			tottal_comments = comments_data.objects.all().count()
			block_user = profile.objects.filter(is_blocked="block").count()
			tottal_reporter = profile.objects.filter(is_login="News").count()
			admin_detail = profile.objects.filter(user_id=request.user)			
			unblock_user = profile.objects.filter(is_blocked="Unblock").filter(is_login="User").count()
			return render(request, 'admin1/index.html', {'admin_detail':admin_detail, 'tottal_news':tottal_news, 'Approved':Approved, 'Pending':Pending, 'tottal_comments':tottal_comments, 'tottal_category':tottal_category, 'block_user':block_user, 'unblock_user':unblock_user, 'tottal_reporter':tottal_reporter})
		else:		
			auth.logout(request)		
			return render(request, 'admin1/Login.html', {"error":"Login fail! You are not a Administrator."})
	else:
		return render(request, 'admin1/Login.html')
		
def index(request):
	if request.user.is_authenticated:
		check_status = profile.objects.filter(is_login='Admin').filter(user_id=request.user)
		if len(check_status) == 1:
			admin_detail = profile.objects.filter(user_id=request.user)
			return render(request,'admin1/index.html', {'admin_detail':admin_detail})
		else:		
			auth.logout(request)		
			return render(request, 'admin1/Login.html', {"error":"Login fail! You are not a Administrator."})	
	else:
		return render(request, 'admin1/Login.html')

def user_profile(request):
	if request.user.is_authenticated:		
		check_status = profile.objects.filter(is_login='Admin').filter(user_id=request.user)
		if len(check_status) == 1:
			all_profile = profile.objects.filter(user_id=request.user)			
			al = profile.objects.get(user_id=request.user).facebook
			user = User.objects.all()
			admin_detail = profile.objects.filter(user_id=request.user)
			return render(request, 'admin1/profile.html', {'all_profile':all_profile, 'admin_detail':admin_detail})
		else:		
			auth.logout(request)		
			return render(request, 'admin1/Login.html', {"error":"Login fail! You are not a Administrator."})
	else:
		return render(request, 'admin1/Login.html')

def Content_category(request):
	if request.user.is_authenticated:
		check_status = profile.objects.filter(is_login='Admin').filter(user_id=request.user)
		if len(check_status) == 1:
			if request.method == 'POST':
				a_category = request.POST['category_name']
				cat = category( category_name=a_category)
				cat.save()			
				return redirect('/admin1/contentCategory')
			else:
				category_data = category.objects.all()
				admin_detail = profile.objects.filter(user_id=request.user)
				return render(request, 'admin1/Content Category.html',{'data_cat':category_data, 'admin_detail':admin_detail})
		else:		
			auth.logout(request)		
			return render(request, 'admin1/Login.html', {"error":"Login fail! You are not a Administrator."})
	else:
		return render(request, 'admin1/Login.html')

def media_repoter_information(request):
	if request.user.is_authenticated:
		check_status = profile.objects.filter(is_login='Admin').filter(user_id=request.user)
		if len(check_status) == 1:
			media = User.objects.all()
			media_reporter = profile.objects.filter(is_login='News')
			admin_detail = profile.objects.filter(user_id=request.user)
			return render(request,'admin1/Media Repoter Information.html', {'media_reporter':media_reporter, 'admin_detail':admin_detail})
		else:		
			auth.logout(request)		
			return render(request, 'admin1/Login.html', {"error":"Login fail! You are not a Administrator."})
	else:
		return render(request, 'admin1/Login.html')

def News_update(request):
	if request.user.is_authenticated:
		check_status = profile.objects.filter(is_login='Admin').filter(user_id=request.user)
		if len(check_status) == 1:
			news = News_content.objects.all()
			admin_detail = profile.objects.filter(user_id=request.user)
			return render(request,'admin1/News Update.html', {'news':news, 'admin_detail':admin_detail})
		else:		
			auth.logout(request)		
			return render(request, 'admin1/Login.html', {"error":"Login fail! You are not a Administrator."})
	else:
		return render(request, 'admin1/Login.html' )

def User_detail(request):
	if request.user.is_authenticated:		
		check_status = profile.objects.filter(is_login='Admin').filter(user_id=request.user)
		if len(check_status) == 1:
			user_details = profile.objects.filter(is_login='User')
			admin_detail = profile.objects.filter(user_id=request.user)
			return render(request,'admin1/UserDetail.html', {'user':user_details, 'admin_detail':admin_detail})
		else:		
			auth.logout(request)		
			return render(request, 'admin1/Login.html', {"error":"Login fail! You are not a Administrator."})
	else:
		return render(request, 'admin1/Login.html')

def login(request):
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				auth.login(request, user)
				return redirect('/admin1')
			else:
				return render(request, 'admin1/login.html', {'error':'Login fail! Invalid credential'})
		else:
			return render(request, 'admin1/login.html')
def register(request):
	if request.method == 'POST':
		if request.POST['password'] == request.POST['cpassword']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'register.html', {'error':'Username has already taken'})
			except User.DoesNotExist:
				user = User.objects.create_user(username=request.POST['username'], first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'], password=request.POST['password'])				
				image1 = request.FILES['image1']		
				fs1 = FileSystemStorage()
				filename = fs1.save(image1.name, image1)
				url1 = fs1.url(filename)
				extend = profile(phone_no=request.POST['phone_no'], Address=request.POST['address'], user_id=user, facebook=request.POST['facebook'], instagram=request.POST['Instagram'], twitter=request.POST['twitter'], proffession=request.POST['proffesion'], Field_location=request.POST['field_location'], is_login="News", image=url1)
				extend.save()
				return redirect('/admin1/mediaRepoterInformation')
			else:
				return render(request, 'admin1/login.html', {'error':'password doesnot match'})
		else:
			return render(request, 'admin1/login.html')

def logout(request):
	auth.logout(request)
	return redirect('/admin1')

def show_data(request,id):
	spec_data_edit = category.objects.filter(id=id)
	admin_detail = profile.objects.filter(user_id=request.user)
	return render(request,'/admin1/contentCategory.html',{'spec_data':spec_data, 'admin_detail':admin_detail})

def delete_data(request, id):
	delete_data = category.objects.filter(id=id)
	delete_data.delete()
	return redirect('/admin1/contentCategory')

def edit_data(request, id):	
	admin_detail = profile.objects.filter(user_id=request.user)
	edit_data = category.objects.filter(id=id)
	return render(request, 'admin1/Content Category.html',{'edit_data':edit_data, 'admin_detail':admin_detail})

def edit_data_stored(request, id):
	content_name = request.POST['category_name_edit']
	data_stored = category(id=id, category_name=content_name)
	data_stored.save()
	return redirect('/admin1/contentCategory')

def show_content_data(request, id):
	edit_data = News_content.objects.filter(id=id)
	show_category_data = category.objects.all()
	admin_detail = profile.objects.filter(user_id=request.user)
	return render(request, 'admin1/News Update.html',{'edit_news_data': edit_data, 'show_category_data':show_category_data, 'admin_detail':admin_detail})

def delete_content_data(request, id):
	delete_data = News_content.objects.filter(id=id)
	delete_data.delete()
	return render(request, 'admin1/News Update.html')


def news_update(request, id):
	Status = "Approved"
	news = News_content.objects.get(id=id)
	news_staus = News_content.objects.get(id=id).status
	if news_staus == "Approved":
		staus_update = "Pending"
		print("Status is Approved")
	else:
		staus_update = "Approved"	
		print("Status is Pending")
	news.status = staus_update	
	news.save()
	print("Updated")
	return redirect('/admin1/newsUpdate')

def show_data(request):
	return render(request, 'admin1/News Update.html')

def delete_media_data(request, id):
	delete_data = profile.objects.filter(id=id)
	user = " "
	for x in delete_data:
		user = x.user_id
	print(user)
	data_media_reporter = User.objects.get(username = user)
	print(data_media_reporter)
	delete_data.delete()
	data_media_reporter.delete()
	return redirect('/admin1/mediaRepoterInformation')

def delete_user_data(request, id):
	delete_data = profile.objects.filter(id=id)
	user = " "
	for x in delete_data:
		user = x.user_id
	print(user)
	delete_user_data = User.objects.get(username=user)
	delete_data = profile.objects.filter(id=id)
	delete_data.delete()
	delete_user_data.delete()	
	return redirect('/admin1/userDetail')

def edit_profile(request):
	if request.user.is_authenticated:		
		if request.method == "POST":			
			user = User.objects.get(username=request.user)
			phn = request.POST['phone_no']
			addrs = request.POST['address']
			prof = request.POST['proffession']
			fb = request.POST['facebook_profile']
			insta = request.POST['instagram_profile']
			twit = request.POST['twitter_profile']
			fld = request.POST['Field_location']
			chk = profile.objects.get(user_id=request.user).image
			chk_id = profile.objects.get(user_id=request.user).id
			try:			
				filepath = request.FILES['image1']
				image1 = request.FILES['image1']
				fs1 = FileSystemStorage()
				filename = fs1.save(image1.name, image1)
				url1 = fs1.url(filename)	
			except MultiValueDictKeyError:
				filepath = False
			if filepath == False:
				url1 = chk
			fnm = request.POST['fname']
			lst = request.POST['lname']
			email = request.POST['email']
			ext = profile(id=chk_id, phone_no=phn, Address=addrs, proffession=prof, facebook=fb, instagram=insta, twitter=twit, image=url1, Field_location=fld, user_id=user, is_login="Admin")
			ext.save()			
			return redirect('/admin1/user_profile')	
		else:			
			edit_profile = profile.objects.filter(user_id=request.user)
			admin_detail = profile.objects.filter(user_id=request.user)	
			return render(request, 'admin1/Profile.html', {'edit_profile':edit_profile, 'admin_detail':admin_detail})
	else:
		return render(request, 'admin1/Login.html')

def block_user(request, id):
	if request.user.is_authenticated:		
		user_details = profile.objects.get(id=id)
		block = profile.objects.get(id=id).is_blocked
		if block == "Unblock":
			User_blocked = "block"
			print("*********User is block*********")
		else:
			User_blocked = "Unblock"
			print("*********User is Unblock*********")
		user_details.is_blocked = User_blocked
		user_details.save()
		print(block)
		return redirect('/admin1/userDetail')
	else:
		return render(request, 'admin1/Login.html')


def total_News(request):
	if request.user.is_authenticated:
		check_status = profile.objects.filter(is_login='Admin').filter(user_id=request.user)
		if len(check_status) == 1:
			tottal_news = News_content.objects.all().count()
			latest_tottal_news = News_content.objects.all()
			Approved = News_content.objects.filter(status="Approved").count()
			Pending = News_content.objects.filter(status="Pending").count()
			tottal_comments = comments_data.objects.all().count()
			latest_news = News_content.objects.filter(status="Approved").latest('id')
			latest = News_content.objects.get(News_title=latest_news).news_category	
			tottal_category = category.objects.all().count()	
			block_user = profile.objects.filter(is_blocked="block").count()
			tottal_reporter = profile.objects.filter(is_login="News").count()
			admin_detail = profile.objects.filter(user_id=request.user)
			unblock_user = profile.objects.filter(is_blocked="Unblock").filter(is_login="User").count()	
			return render(request, 'admin1/index.html', {'admin_detail':admin_detail,'tottal_news':tottal_news, 'Approved':Approved, 'Pending':Pending, 'tottal_comments':tottal_comments, 'latest':latest, 'latest_tottal_news':latest_tottal_news, 'tottal_category':tottal_category, 'block_user':block_user, 'unblock_user':unblock_user, 'tottal_reporter':tottal_reporter})
		else:
			auth.logout(request)
			return render(request, 'admin1/login.html', {"error":"Login fail! You are not a Admin."})			
	else:
		return render(request, 'admin1/login.html')

def Approved_News(request):
	if request.user.is_authenticated:
		check_status = profile.objects.filter(is_login='Admin').filter(user_id=request.user)
		if len(check_status) == 1:
			tottal_news = News_content.objects.all().count()
			data_Approved_news = News_content.objects.filter(status="Approved")
			Approved = News_content.objects.filter(status="Approved").count()
			Pending = News_content.objects.filter(status="Pending").count()
			tottal_comments = comments_data.objects.all().count()
			latest_news = News_content.objects.filter(status="Approved").latest('id')
			latest = News_content.objects.get(News_title=latest_news).news_category		
			tottal_category = category.objects.all().count()
			block_user = profile.objects.filter(is_blocked="block").count()
			tottal_reporter = profile.objects.filter(is_login="News").count()
			admin_detail = profile.objects.filter(user_id=request.user)
			unblock_user = profile.objects.filter(is_blocked="Unblock").filter(is_login="User").count()
			return render(request, 'admin1/index.html', {'admin_detail':admin_detail, 'tottal_news':tottal_news, 'Approved':Approved, 'Pending':Pending, 'tottal_comments':tottal_comments, 'latest':latest, 'data_Approved_news':data_Approved_news,'tottal_category':tottal_category, 'block_user':block_user, 'unblock_user':unblock_user, 'tottal_reporter':tottal_reporter})
		else:
			auth.logout(request)
			return render(request, 'admin1/login.html', {"error":"Login fail! You are not a Admin."})
	else:
		return render(request, 'admin1/login.html')

def pending(request):
	if request.user.is_authenticated:
		check_status = profile.objects.filter(is_login='Admin').filter(user_id=request.user)
		if len(check_status) == 1:
			tottal_news = News_content.objects.all().count()
			data_Approved_news = News_content.objects.filter(status="Pending")
			Approved = News_content.objects.filter(status="Approved").count()
			Pending = News_content.objects.filter(status="Pending").count()
			tottal_comments = comments_data.objects.all().count()
			latest_news = News_content.objects.filter(status="Approved").latest('id')
			latest = News_content.objects.get(News_title=latest_news).news_category	
			tottal_category = category.objects.all().count()	
			admin_detail = profile.objects.filter(user_id=request.user)
			block_user = profile.objects.filter(is_blocked="block").count()
			tottal_reporter = profile.objects.filter(is_login="News").count()
			unblock_user = profile.objects.filter(is_blocked="Unblock").filter(is_login="User").count()
			return render(request, 'admin1/index.html', {'admin_detail':admin_detail,'tottal_news':tottal_news, 'Approved':Approved, 'Pending':Pending, 'tottal_comments':tottal_comments, 'latest':latest, 'data_Approved_news':data_Approved_news,'tottal_category':tottal_category, 'block_user':block_user, 'unblock_user':unblock_user, 'tottal_reporter':tottal_reporter})
		else:
			auth.logout(request)
			return render(request, 'admin1/login.html', {"error":"Login fail! You are not a Admin."})
	else:
		return render(request, 'admin1/login.html')

def data_comments(request):
	if request.user.is_authenticated:
		check_status = profile.objects.filter(is_login='Admin').filter(user_id=request.user)
		if len(check_status) == 1:
			tottal_news = News_content.objects.all().count()
			data_comments = comments_data.objects.all()
			Approved = News_content.objects.filter(status="Approved").count()
			Pending = News_content.objects.filter(status="Pending").count()
			tottal_comments = comments_data.objects.all().count()
			latest_news = News_content.objects.filter(status="Approved").latest('id')
			latest = News_content.objects.get(News_title=latest_news).news_category	
			tottal_category = category.objects.all().count()
			block_user = profile.objects.filter(is_blocked="block").count()
			tottal_reporter = profile.objects.filter(is_login="News").count()
			admin_detail = profile.objects.filter(user_id=request.user)
			unblock_user = profile.objects.filter(is_blocked="Unblock").filter(is_login="User").count()	
			return render(request, 'admin1/index.html', {'admin_detail':admin_detail, 'tottal_news':tottal_news, 'Approved':Approved, 'Pending':Pending, 'tottal_comments':tottal_comments, 'latest':latest, 'data_comments':data_comments, 'tottal_category':tottal_category, 'block_user':block_user, 'unblock_user':unblock_user, 'tottal_reporter':tottal_reporter})
		else:
			auth.logout(request)
			return render(request, 'admin1/login.html', {"error":"Login fail! You are not a Admin."})
	else:
		return render(request, 'admin1/login.html')

def categorie(request):
	if request.user.is_authenticated:
		check_status = profile.objects.filter(is_login='Admin').filter(user_id=request.user)
		if len(check_status) == 1:
			tottal_news = News_content.objects.all().count()
			data_comments = comments_data.objects.all()
			tottal_category = category.objects.all().count()
			Approved = News_content.objects.filter(status="Approved").count()
			Pending = News_content.objects.filter(status="Pending").count()
			tottal_comments = comments_data.objects.all().count()
			latest_news = News_content.objects.filter(status="Approved").latest('id')
			latest = News_content.objects.get(News_title=latest_news).news_category		
			tottal_category = category.objects.all().count()	
			single_category = category.objects.all()
			block_user = profile.objects.filter(is_blocked="block").count()
			tottal_reporter = profile.objects.filter(is_login="News").count()
			admin_detail = profile.objects.filter(user_id=request.user)
			unblock_user = profile.objects.filter(is_blocked="Unblock").filter(is_login="User").count()
			return render(request, 'admin1/index.html', {'admin_detail':admin_detail, 'tottal_news':tottal_news, 'Approved':Approved, 'Pending':Pending, 'tottal_comments':tottal_comments, 'latest':latest, 'tottal_category':tottal_category, 'single_category':single_category, 'block_user':block_user, 'unblock_user':unblock_user, 'tottal_reporter':tottal_reporter})
		else:
			auth.logout(request)
			return render(request, 'admin1/login.html', {"error":"Login fail! You are not a Admin."})
	else:
		return render(request, 'admin1/login.html')

def show_block(request):
	if request.user.is_authenticated:
		check_status = profile.objects.filter(is_login='Admin').filter(user_id=request.user)
		if len(check_status) == 1:
			tottal_news = News_content.objects.all().count()
			data_comments = comments_data.objects.all()
			tottal_category = category.objects.all().count()
			Approved = News_content.objects.filter(status="Approved").count()
			Pending = News_content.objects.filter(status="Pending").count()
			tottal_comments = comments_data.objects.all().count()
			latest_news = News_content.objects.filter(status="Approved").latest('id')
			latest = News_content.objects.get(News_title=latest_news).news_category		
			tottal_category = category.objects.all().count()	
			show_block_user = profile.objects.filter(is_blocked="block")
			block_user = profile.objects.filter(is_blocked="block").count()
			tottal_reporter = profile.objects.filter(is_login="News").count()
			admin_detail = profile.objects.filter(user_id=request.user)
			unblock_user = profile.objects.filter(is_blocked="Unblock").filter(is_login="User").count()
			return render(request, 'admin1/index.html', {'admin_detail':admin_detail,'tottal_news':tottal_news, 'Approved':Approved, 'Pending':Pending, 'tottal_comments':tottal_comments, 'latest':latest, 'tottal_category':tottal_category, 'block_user':block_user, 'unblock_user':unblock_user, 'tottal_reporter':tottal_reporter, 'show_block_user':show_block_user})
		else:
			auth.logout(request)
			return render(request, 'admin1/login.html', {"error":"Login fail! You are not a Admin."})
	else:
		return render(request, 'admin1/login.html')

def unshow_block(request):
	if request.user.is_authenticated:
		check_status = profile.objects.filter(is_login='Admin').filter(user_id=request.user)
		if len(check_status) == 1:
			tottal_news = News_content.objects.all().count()
			data_comments = comments_data.objects.all()
			tottal_category = category.objects.all().count()
			Approved = News_content.objects.filter(status="Approved").count()
			Pending = News_content.objects.filter(status="Pending").count()
			tottal_comments = comments_data.objects.all().count()
			latest_news = News_content.objects.filter(status="Approved").latest('id')
			latest = News_content.objects.get(News_title=latest_news).news_category		
			tottal_category = category.objects.all().count()	
			unshow_block_user = profile.objects.filter(is_blocked="Unblock").filter(is_login="User")
			block_user = profile.objects.filter(is_blocked="block").count()
			tottal_reporter = profile.objects.filter(is_login="News").count()
			admin_detail = profile.objects.filter(user_id=request.user)
			unblock_user = profile.objects.filter(is_blocked="Unblock").filter(is_login="User").count()
			return render(request, 'admin1/index.html', {'admin_detail':admin_detail,'tottal_news':tottal_news, 'Approved':Approved, 'Pending':Pending, 'tottal_comments':tottal_comments, 'latest':latest, 'tottal_category':tottal_category, 'block_user':block_user, 'unblock_user':unblock_user, 'tottal_reporter':tottal_reporter, 'unshow_block_user':unshow_block_user})
		else:
			auth.logout(request)
			return render(request, 'admin1/login.html', {"error":"Login fail! You are not a Admin."})
	else:
		return render(request, 'admin1/login.html')

def show_reporter(request):
	if request.user.is_authenticated:
		check_status = profile.objects.filter(is_login='Admin').filter(user_id=request.user)
		if len(check_status) == 1:
			tottal_news = News_content.objects.all().count()
			data_comments = comments_data.objects.all()
			tottal_category = category.objects.all().count()
			Approved = News_content.objects.filter(status="Approved").count()
			Pending = News_content.objects.filter(status="Pending").count()
			tottal_comments = comments_data.objects.all().count()
			latest_news = News_content.objects.filter(status="Approved").latest('id')
			latest = News_content.objects.get(News_title=latest_news).news_category		
			tottal_category = category.objects.all().count()	
			unshow_reporter = profile.objects.filter(is_login="News")
			block_user = profile.objects.filter(is_blocked="block").count()
			tottal_reporter = profile.objects.filter(is_login="News").count()
			admin_detail = profile.objects.filter(user_id=request.user)
			unblock_user = profile.objects.filter(is_blocked="Unblock").filter(is_login="User").count()
			return render(request, 'admin1/index.html', {'admin_detail':admin_detail,'tottal_news':tottal_news, 'Approved':Approved, 'Pending':Pending, 'tottal_comments':tottal_comments, 'latest':latest, 'tottal_category':tottal_category, 'block_user':block_user, 'unblock_user':unblock_user, 'tottal_reporter':tottal_reporter, 'unshow_reporter':unshow_reporter})
		else:
			auth.logout(request)
			return render(request, 'admin1/login.html', {"error":"Login fail! You are not a Admin."})
	else:
		return render(request, 'admin1/login.html')


def admin_feedback(request):
	if request.user.is_authenticated:
		check_status = profile.objects.filter(is_login='Admin').filter(user_id=request.user)
		if len(check_status) == 1:
			admin_detail = profile.objects.filter(user_id=request.user)
			feed_back = feedback.objects.all()
			return render(request, 'admin1/feedback.html', {'feedback':feed_back, 'admin_detail':admin_detail})
		else:
			auth.logout(request)
			return render(request, 'admin1/login.html', {"error":"Login fail! You are not a Admin."})
	else:
		return render(request, 'admin1/login.html')

def del_admin_feedback(request,id):
	feed_back = feedback.objects.filter(id=id)
	feed_back.delete()
	return redirect('admin1/admin_feedback')

def register_admin(request):
	if request.method == 'POST':
		if request.POST['password'] == request.POST['cpassword']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'register.html', {'error':'Username has already taken'})
			except User.DoesNotExist:
				user = User.objects.create_user(username=request.POST['username'], first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'], password=request.POST['password'])
				image = request.FILES['image']		
				fs1 = FileSystemStorage()
				filename = fs1.save(image.name, image)
				url1 = fs1.url(filename)
				extend = profile(user_id=user, phone_no=request.POST['phone_no'], Address=request.POST['address'], image=url1, is_login='Admin')
				extend.save()
				auth.login(request, user)
				return redirect('/admin1/login')
			else:
				return render(request, 'admin1/login.html', {'error':'password doesnot match'})
	else:
		return render(request, 'admin1/login.html', {'error':'password doesnot match'})