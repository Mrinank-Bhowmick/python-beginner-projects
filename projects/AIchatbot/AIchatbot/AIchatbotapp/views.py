from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth
from django.contrib.auth.models import User
import openai
from .models import Chat
from django.utils import timezone

# Create your views here.

openai_api_key = 'Enter_your_api_key'
openai.api_key = openai_api_key

def ask_openai(message):
	response = openai.ChatCompletion.create(
		# model  = "text-davinci-003",
		# prompt = message,
		# max_tokens = 150,
		# n=1,
		# stop = None,
		# temperature = 0.7,
		model = "gpt-3.5-turbo",
		# model = "gpt-4",
		messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ]
        #we can change to any newer models. see openai dcumentation.
    )
    
    
	# print(response)
	answer = response.choices[0].message.content.strip()
	return answer



def AIchatbot(request):
	#get all previous chats of the specific user
	prevChats = Chat.objects.filter(user = request.user)



	if request.method == 'POST':
		message = request.POST.get('message')
		# response = 'Gotcha your message. I will respond when API gets connected.'
		response = ask_openai(message)

		#save message in db
		chat = Chat(user=request.user, message = message, response = response, created_at = timezone.now())
		chat.save()
		return JsonResponse({'message': message, 'response':response})
	return render(request, 'AIchatbot.html', {'prevChats':prevChats})


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(request, username = username, password = password)
		if user is not None:
			auth.login(request, user)
			return redirect('AIchatbot')
		else:
			err_msg = "Invalid username or password"
			return render(request, 'login.html', {'error_message': err_msg})
	else:
		return render(request, 'login.html')

def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if password1==password2:
			try: 
				user = User.objects.create_user(username, email,password1)
				user.save()
				auth.login(request,user)
				return redirect('AIchatbot')
			except: 
				error_msg = "Error creating account"
			return render(request, 'register.html',{'error_message':error_msg})

		else:
			error_msg = "Password don't match."
			return render(request, 'register.html',{'error_message':error_msg})

	return render(request, 'register.html')

def logout(request):
	auth.logout(request)
	return redirect('login')

