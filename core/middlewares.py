from django.shortcuts import render,redirect

def auth(view_function):
    def wrapped_view(request,*args,**kwargs):
        if request.user.is_authenticated == False:
            return redirect('login')
        return view_function(request,*args,**kwargs)
    return wrapped_view
