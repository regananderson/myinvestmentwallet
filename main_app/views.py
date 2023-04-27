from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Asset
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

def home(request):
    assets = Asset.objects.all()
    total_amount = sum(asset.amount for asset in assets)
    total_value = sum(asset.value for asset in assets)
    context = {
        'assets': assets,
        'total_amount': total_amount,
        'total_value': total_value,
    }
    return render(request, 'home.html', context)

def assets_index(request):
    assets = Asset.objects.all()
   
    return render(request, 'assets/index.html', {'assets':assets})

def assets_detail(request):
    assets = Asset.objects.all()
    total_amount = sum(asset.amount for asset in assets)
    total_value = sum(asset.value for asset in assets)
    context = {
        'assets': assets,
        'total_amount': total_amount,
        'total_value': total_value,
    }
    return render(request, 'assets/detail.html', context)

def asset_type(request, asset_type):
    assets = Asset.objects.filter(type=asset_type)
    total_amount = sum(asset.amount for asset in assets)
    total_value = sum(asset.value for asset in assets)
    context = {
        'assets': assets,
        'total_amount': total_amount,
        'total_value': total_value,
    }
    return render(request, 'assets/list.html', context)

def investments_detail(request, asset_id):
    asset = Asset.objects.get(id=asset_id)
    return render(request, 'investments/detail.html', {'asset':asset})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('assets_detail')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm() 
    return render(request, 'registration/signup.html', {
        'form': form, 
        'error': error_message
        })

class AssetCreate(CreateView):
    model = Asset
    fields = ('type', 'name', 'amount', 'description','value')
    template_name = 'assets/main_app/asset_form.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AssetUpdate(UpdateView):
    model = Asset
    fields = '__all__'
    template_name = 'assets/main_app/asset_form.html'

class AssetDelete(DeleteView):
    model = Asset
    success_url = '/assets/'
    template_name = 'assets/main_app/asset_confirm_delete.html'
    
