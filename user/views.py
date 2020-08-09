from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from user.models import comments_data
from news.models import News_content
from admin1.models import profile, category
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
from user.models import message_user, feedback
Url_Current_location = "/user"
# Create your views here.
def index(request):	
	if request.user.is_authenticated:	
		msg = message_user.objects.filter(reciver_id=request.user)
		user_data = profile.objects.filter(user_id=request.user)	
		news_show_data = News_content.objects.filter(status="Approved").order_by('-id')[:1]
		news_data = News_content.objects.filter(status="Approved").order_by('-id')[:5]
		category_list = category.objects.all()
		latest_news_two = News_content.objects.filter(status="Approved").order_by('-id')[:2]
		latest_news_three = News_content.objects.filter(status="Approved").order_by('-id')[:3]
		sports_video = News_content.objects.filter(status="Approved").filter(news_category="Sports")
		bussiness_video = News_content.objects.filter(status="Approved").filter(news_category="Business")
		news = News_content.objects.filter(status="Approved").order_by('id')[:2]
		return render(request, 'user/index.html', {'news_show_data':news_show_data, 'news_data':news_data,'category_list':category_list, 'latest_news_two':latest_news_two, 'latest_news_three':latest_news_three, 'sports_video':sports_video, 'bussiness_video':bussiness_video, 'news':news, 'user_data':user_data,'msg':msg})
	else:
		news_show_data = News_content.objects.filter(status="Approved").order_by('-id')[:1]
		news_data = News_content.objects.filter(status="Approved").order_by('-id')[:5]
		category_list = category.objects.all()
		latest_news_two = News_content.objects.filter(status="Approved").order_by('-id')[:2]
		latest_news_three = News_content.objects.filter(status="Approved").order_by('-id')[:3]
		sports_video = News_content.objects.filter(status="Approved").filter(news_category="Sports")
		bussiness_video = News_content.objects.filter(status="Approved").filter(news_category="Business")
		news = News_content.objects.filter(status="Approved").order_by('id')[:2]
		return render(request, 'user/index.html', {'news_show_data':news_show_data, 'news_data':news_data,'category_list':category_list, 'latest_news_two':latest_news_two, 'latest_news_three':latest_news_three, 'sports_video':sports_video, 'bussiness_video':bussiness_video, 'news':news})

def about(request):
	return render(request, 'user/About.html')

def login(request):
	if request.user.is_authenticated:
		return render(request, 'user/index.html')
	else:
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = auth.authenticate(username=username,password=password)
			check_status = profile.objects.filter(is_login='User').filter(user_id=user)
			if len(check_status) == 1:
				if user is not None:
					auth.login(request, user)
					return redirect('/user')
				else:
					return render(request, '/user', {"error":"Invalid credential"})
			else:
				return render(request, '/user', {'error_login':'pls check your credentials'})
		else:
			return render(request, '/user')
def register(request):
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
				extend = profile(user_id=user, phone_no=request.POST['phone_no'], Address=request.POST['address'], image=url1, is_login='User')
				extend.save()
				auth.login(request, user)
				return redirect('/user')
			else:
				return render(request, 'register.html', {'error':'password doesnot match'})
		else:
			return render(request, 'register.html')

def logout(request):
	auth.logout(request)
	return redirect('/user')

def news_video(request, id):	
	if request.user.is_authenticated:	
		msg = message_user.objects.filter(reciver_id=request.user)
		user_data = profile.objects.filter(user_id=request.user)	
		news_show_data = News_content.objects.filter(status="Approved").order_by('-id')[:1]
		category_list = category.objects.all()
		latest_news_three = News_content.objects.filter(status="Approved").order_by('-id')[:3]
		sports_video = News_content.objects.filter(status="Approved").filter(news_category="Sports")
		bussiness_video = News_content.objects.filter(status="Approved").filter(news_category="Business")
		news_data = News_content.objects.filter(status="Approved").order_by('-id')[:5]
		latest_news_two = News_content.objects.filter(status="Approved").order_by('-id')[:2]
		news = News_content.objects.filter(status="Approved").order_by('id')[:2]
		return render(request, 'user/index.html', {'news_show_data':news_show_data, 'news_data':news_data,'category_list':category_list, 'latest_news_two':latest_news_two, 'latest_news_three':latest_news_three, 'sports_video':sports_video, 'bussiness_video':bussiness_video, 'news':news, 'user_data':user_data,'msg':msg})
	else:
		news_show_data = News_content.objects.filter(status="Approved").order_by('-id')[:1]
		news_data = News_content.objects.filter(status="Approved").order_by('-id')[:5]
		category_list = category.objects.all()
		latest_news_two = News_content.objects.filter(status="Approved").order_by('-id')[:2]
		latest_news_three = News_content.objects.filter(status="Approved").order_by('-id')[:3]
		sports_video = News_content.objects.filter(status="Approved").filter(news_category="Sports")
		bussiness_video = News_content.objects.filter(status="Approved").filter(news_category="Business")
		news = News_content.objects.filter(status="Approved").order_by('id')[:2]
		return render(request, 'user/index.html', {'news_show_data':news_show_data, 'news_data':news_data,'category_list':category_list, 'latest_news_two':latest_news_two, 'latest_news_three':latest_news_three, 'sports_video':sports_video, 'bussiness_video':bussiness_video})

def latest_news(request,id):
	g_id = News_content.objects.latest('id')
	get_id = g_id.id
	print(get_id)
	current = id	
	pre_id = id
	after_id = id
	x = 0
	y = 0
	while x == 0:
		pre = pre_id - 1
		if News_content.objects.filter(id=pre,status="Approved"):
			pre_show_data = News_content.objects.filter(id=pre,status="Approved")
			x = 1
		elif News_content.objects.filter(id=pre,status="Pending"):			
			pre_id = pre_id - 1
			x = 0
		elif pre == 0:
			pre_show_data = News_content.objects.filter(status="Approved").order_by('-id')[:1]
			x = 1
		else :
			pre_id = pre_id - 1
			x = 0
	if News_content.objects.filter(status="Approved").latest('id'):
		aft_show_data = News_content.objects.filter(status="Approved").order_by('id')[:1]
	while y == 0:
		after = after_id + 1
		if News_content.objects.filter(id=after,status="Approved"):
			aft_show_data = News_content.objects.filter(id=after,status="Approved")
			# print("Id approver:"+ str(after))
			y = 1
		elif News_content.objects.filter(id=after,status="Pending"):
			after_id = after_id + 1
			# print("Id Pending:"+ str(after))
			y = 0
		elif after >= get_id:
			# print("Got latest id:"+ str(after))
			aft_show_data = News_content.objects.filter(status="Approved").order_by('id')[:1]					
			y = 1
		else :
			# print("Id Missing:"+ str(after))
			after_id = after_id + 1
			y = 0		
	cur_show_data = News_content.objects.filter(id=current,status="Approved")
	b = News_content.objects.get(id=current)
	reporter_detail = profile.objects.filter(user_id=b.user_id)	
	d = profile.objects.all()
	comment = comments_data.objects.filter(news_id=id).order_by('-id')	
	category_list = category.objects.all()	
	if request.user.is_authenticated:
		msg = message_user.objects.filter(reciver_id=request.user)	
		news_data = News_content.objects.filter(status="Approved").order_by('-id')[:5]
		latest_news_two = News_content.objects.filter(status="Approved").order_by('-id')[:2]
		news = News_content.objects.filter(status="Approved").order_by('id')[:2]
		return render(request, 'user/Latest_news.html', {'pre_show_data':pre_show_data,'cur_show_data':cur_show_data,'aft_show_data':aft_show_data, 'reporter_detail':reporter_detail, 'comment':comment, 'd':d,'msg':msg, 'category_list':category_list, 'news_data':news_data, 'latest_news_two':latest_news_two, 'news':news})
	else:
		news_data = News_content.objects.filter(status="Approved").order_by('-id')[:5]
		latest_news_two = News_content.objects.filter(status="Approved").order_by('-id')[:2]
		news = News_content.objects.filter(status="Approved").order_by('id')[:2]
		return render(request, 'user/Latest_news.html', {'pre_show_data':pre_show_data,'cur_show_data':cur_show_data,'aft_show_data':aft_show_data, 'reporter_detail':reporter_detail, 'comment':comment, 'd':d, 'category_list':category_list, 'news_data':news_data, 'latest_news_two':latest_news_two, 'news':news})

def comments(request, id):
	if request.user.is_authenticated:
		check_status = profile.objects.filter(is_blocked="Unblock").filter(user_id=request.user)
		if len(check_status) == 1:			
			if request.method == 'POST':
				comm = request.POST['commentss']
				print(comm)
				news = News_content.objects.get(id=id)				
				news.save()
				print(news)						
				comments_store = comments_data(data=comm, user_id=request.user,news_id=news)
				comments_store.save()
				Url_Current_location = "/user/latest_news/%s" %id
				return HttpResponseRedirect(Url_Current_location)
			else:
				print("It's get method")
				edit_data = comments_data.objects.filter(id=id)
				Url_Current_location = "/user/latest_news/%s" %id
				return render(request, 'Url_Current_location', {'edit_data':edit_data})
		else:
			Ur = request.user			
			print("User is blocked")
			print(Ur)
			return redirect('/user')
	else:
		return redirect('/user')

def edit_comment_data(request,id):
	if request.method == "POST":
		print("POST request")
		comment = comments_data.objects.get(id=id).news_id
		print(comment)
		n_id = News_content.objects.get(News_title=comment).id
		print(n_id)
		edit = request.POST['edit_comment']
		news = comment
		edit_comment = comments_data(id=id,data=edit,user_id=request.user,news_id=news)
		edit_comment.save()
		id = n_id
		Url_Current_location = "/user/latest_news/%s" %id
		return HttpResponseRedirect(Url_Current_location)
	else:
		print("get method")
		comments_da = comments_data.objects.get(id=id).news_id		
		comment = comments_data.objects.filter(news_id=comments_da)
		single_comments = comments_data.objects.filter(id=id)
		cur_show_data = News_content.objects.filter(News_title=comments_da,status="Approved")		
		Url_Current_location = "/user/latest_news/%s" %3		
		reporter_detail = profile.objects.filter(user_id=comments_da.user_id)	
		d = profile.objects.all()
		return render(request, 'user/Latest_news.html', {'comment':comment, 'cur_show_data':cur_show_data, 'reporter_detail':reporter_detail, 'd':d,'single_comments':single_comments})

def delete_comment(request, id ):
	if request.user.is_authenticated:		
		comment = comments_data.objects.filter(id=id)	
		re_comment = comments_data.objects.get(id=id).news_id
		n_id = News_content.objects.get(News_title=re_comment).id
		id = n_id
		comment.delete()
		print("comment deleted successfully")
		Url_Current_location = "/user/latest_news/%s" %id
		return HttpResponseRedirect(Url_Current_location)
	else:
		comment = comments_data.objects.filter(id=id)	
		re_comment = comments_data.objects.get(id=id).news_id
		n_id = News_content.objects.get(News_title=re_comment).id
		id = n_id		
		print("User is Blocked")
		Url_Current_location = "/user/latest_news/%s" %id
		return HttpResponseRedirect(Url_Current_location)

def user_profile(request):
	if request.user.is_authenticated:	
		usr = profile.objects.filter(user_id=request.user).filter(is_login="User")
		if usr == 1:
			user_detail = profile.objects.filter(user_id=request.user)
			s_profile = User.objects.filter(username=request.user)
			u_profile = User.objects.get(username=request.user).last_name
			print(u_profile)
			return render(request, 'user/profile.html', {'user_detail':user_detail,'profile':s_profile})
		else:		
			user_detail = profile.objects.filter(user_id=request.user)
			s_profile = User.objects.filter(username=request.user)
			u_profile = User.objects.get(username=request.user).last_name
			print(u_profile)
			return render(request, 'user/profile.html', {'user_detail':user_detail,'profile':s_profile, 'not_user':'It looks like you are Admin or Reporter'})
	else:
		print("Profile")
		return redirect('/user')

def edit_profile(request):
	if request.user.is_authenticated:
		usr = profile.objects.filter(user_id=request.user).filter(is_login="User")
		if usr == 1:			
			if request.method == "POST":
				fnm = request.POST['fname']
				lst = request.POST['lname']
				phn = request.POST['phone_no']
				addrs = request.POST['address']
				email = request.POST['email']
				fb = request.POST['facebook']
				insta = request.POST['instagram']
				twit = request.POST['twitter']
				edit_profile = profile.objects.filter(user_id=request.user)			
				data_id = profile.objects.get(user_id=request.user).id
				chk = profile.objects.get(user_id=request.user).image
				try:			
					filepath = request.FILES['image1']
				except MultiValueDictKeyError:
					filepath = False

				if filepath == False:
					filepath = chk
				ext = profile(id=data_id, phone_no=phn, Address=addrs, facebook=fb, instagram=insta, twitter=twit, user_id=request.user, image=filepath, is_login='User')
				ext.save()
				return redirect('/user/profile')
			else:
				edit_user = profile.objects.filter(user_id=request.user)
				edit_profile = User.objects.filter(username=request.user)
				return render(request, 'user/profile.html', {'edit_user':edit_user,'edit_profile':edit_profile})
		else:		
			return redirect('/user')
	else:
		print("Profile")
		return redirect('/user')

def message(request,id):
	msg = request.POST['message']
	print(msg)
	send = request.user	
	print(send)
	get_reciver = comments_data.objects.get(id=id).user_id
	reciver = get_reciver
	print(reciver)
	re_comment = comments_data.objects.get(id=id).news_id
	n_id = News_content.objects.get(News_title=re_comment).id
	id = n_id		
	print(id)
	print("message Send")
	Url_Current_location = "/user/latest_news/%s" %id
	store_msg = message_user(data=msg, sender_id=send, reciver_id=reciver)
	store_msg.save()
	return HttpResponseRedirect(Url_Current_location)

def category_grid(request, category):
	category_news = News_content.objects.filter(news_category=category).filter(status="Approved")
	category_single_news = News_content.objects.filter(news_category=category)[:1]
	sin = News_content.objects.get(id=1).image
	print(sin)		
	return render(request,'user/category_grid.html', {'category_news':category_news, 'category_single_news':category_single_news})

def contact(request):
	if request.user.is_authenticated:
		news_data = News_content.objects.filter(status="Approved").order_by('-id')[:5]
		latest_news_two = News_content.objects.filter(status="Approved").order_by('-id')[:2]
		news = News_content.objects.filter(status="Approved").order_by('id')[:2]
		user_detail = User.objects.filter(username=request.user)
		ex_user_detail = profile.objects.filter(user_id=request.user)
		category_list = category.objects.all()
		return render(request, 'user/contact.html', {'ex_user_detail':ex_user_detail,'user_detail':user_detail, 'news_data':news_data, 'latest_news_two':latest_news_two, 'news':news, 'category_list':category_list})
	else:
		news_data = News_content.objects.filter(status="Approved").order_by('-id')[:5]
		latest_news_two = News_content.objects.filter(status="Approved").order_by('-id')[:2]
		news = News_content.objects.filter(status="Approved").order_by('id')[:2]
		category_list = category.objects.all()
		return render(request, 'user/contact.html', {'news_data':news_data, 'latest_news_two':latest_news_two, 'news':news, 'category_list':category_list})

def contact_detail(request):
	if request.method == "POST":
		news_data = News_content.objects.filter(status="Approved").order_by('-id')[:5]
		latest_news_two = News_content.objects.filter(status="Approved").order_by('-id')[:2]
		news = News_content.objects.filter(status="Approved").order_by('id')[:2]
		name = request.POST['name']
		email = request.POST['email']
		feedback_data = request.POST['feedback_data']
		store_feedback = feedback(name=name, email=email, feed_back=feedback_data)
		store_feedback.save()
		category_list = category.objects.all()
		return render(request, 'user/contact.html', {'Done':'Your feedback is saved', 'news_data':news_data, 'latest_news_two':latest_news_two, 'news':news, 'category_list':category_list})
	else:
		news_data = News_content.objects.filter(status="Approved").order_by('-id')[:5]
		latest_news_two = News_content.objects.filter(status="Approved").order_by('-id')[:2]
		news = News_content.objects.filter(status="Approved").order_by('id')[:2]
		category_list = category.objects.all()
		return render(request, 'user/contact.html', {'news_data':news_data, 'latest_news_two':latest_news_two, 'news':news, 'category_list':category_list})