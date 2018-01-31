from django.shortcuts import render, reverse, HttpResponseRedirect
from django.views.generic import ListView
from .models import Rentapp
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import RentAppForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


def rentlist(request):

    rent_list = Rentapp.objects.all()
    query = request.GET.get("q")
    if query:
        rent_list = rent_list.filter(
            Q(location__icontains=query)|
            Q(rooms_available__icontains=query)
            # Q(user__username__icontains=query)

            ).distinct()    
    paginator = Paginator(rent_list, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    
    

    context = {
    "object_list":queryset,
    "title":"List",
    "page_request_var":page_request_var,
    "rent_list": rent_list,
    
    }

    return render(request, 'rentapp/rent_list.html', context)

@login_required
def rentform(request):
    if request.method == "POST":
        form = RentAppForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('rentapp:rent-list'))
    else:
        form = RentAppForm()
    context = {
    'form':form
    }
            
    return render(request, 'rentapp/rent_form.html', context)




def buyrent(request, rentapp_id):
    rent_detail = get_object_or_404(Rentapp, pk=rentapp_id)
    context = {
        'rent_detail':'rent_detail'
    }
    return render(request, 'rentapp/rent_detail', context)
    

        
            




        


  


