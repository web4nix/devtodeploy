from django.shortcuts import render, redirect
from django.contrib import messages, auth
# import User model to check if user exists in the database
from django.contrib.auth.models import User
# import the login method is attribute of auth
from contacts.models import Contact

# Create your views here.

def register(request):
    if request.method == 'POST':
        #print('submit post request')  test for post
        #return redirect('register') test fot post
        # test message (always error here)
        # messages.error(request, 'testing error messages')

        # get formfield input values from the url
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #validations
        # check passwords match
        if password == password2:
            # check username exists (in database)
            # objects retrieves from database
            # filter on username, checking username database on the input username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email is already being used')
                    return redirect('register')
                else:
                    #return
                    # on success create variable holding all input values
                    # create_user()  
                    # objects to update the database
                    user = User.objects.create_user(username=username, password=password, email=email,
                                    first_name=first_name, last_name=last_name)
                    user.save()
                    # auto login, after registration
                    #auth.login(request, user)
                    #return redirect('index')
                    #messages.success(request, 'You are now logged in as {}'.format(user.username))
                    
                    # or login manually
                    messages.success(request, 'You are successful registrated and can log in')
                    return redirect('login')

        else:
            messages.error(request, 'Passwords do not match')
            #return render(request, 'accounts/register.html')
            return redirect('register')


    else:
        return render(request, 'accounts/register.html')



def login(request):
    if request.method == 'POST':
        # retrieve inlog credentials from the POST request
        username = request.POST['username']
        password = request.POST['password']
        # authentication against the database:
        user = auth.authenticate(username=username, password=password)

        # login user
        if user is not None:   # means it is found
            auth.login(request, user)
            #messages.success(request, 'you are logged in')
            messages.success(request, 'Welcome {}'.format(user.username))
            return redirect('dashboard')
        else:
            messages.error(request, 'you are not a registered user')
            return redirect('login')
        
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You are logged out')
    return redirect('index')


def dashboard(request):
    # retrieve the id of the logged in user and the date of inquiry
    # bring in the Contacts model order on date
    # filter where loggedin user (request.user.id is same as user_id of database)
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = { 'contacts': user_contacts }
    return render(request, 'accounts/dashboard.html', context)


