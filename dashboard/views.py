from functools import cached_property
from msilib.schema import Error
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from User.forms import  UpdateUserForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Pharmacy, Medicine


@login_required
def dashboard(request):
    print(request.user)
    print(request.user.id)
    info = Pharmacy.objects.all()
    
    context = { 'info':info}
    return render(request, 'dashboard/home_content.html', context)

@login_required
def Profile(request):
    if Pharmacy.objects.filter(user_id = request.user.id).exists() == False:
        return redirect('create_profile')
    
    return redirect(f"update_profile/{Pharmacy.objects.get(user_id=request.user.id).id}")

@login_required
def add_item(request):
    if Pharmacy.objects.filter(user_id = request.user.id).exists() == False:
        return redirect('create_profile')
   
    return redirect('add_item')


class MedicineListView(LoginRequiredMixin, ListView):
    
    model = Medicine
    template_name = 'dashboard/item_list.html'
    context_object_name = 'info'


class MedicineCreateView(LoginRequiredMixin, CreateView):
    model = Medicine
    template_name = 'dashboard/MedicineForm.html'
    fields = ['medicine_name', 'comapny']
    
    def test_func(self):
                print('test')
                item = self.get_object()
                if self.request.user == item.owner.user:
                    return True
                return False
    def form_valid(self, form):
                
                form.instance.owner = self.request.user.pharmacy
                return super().form_valid(form)
                                                        
    

    

class MedicineUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Medicine
    template_name = 'dashboard/MedicineForm.html'
    fields = ['medicine_name', 'comapny']
    def form_valid(self, form):
        form.instance.owner = self.request.user.pharmacy
        return super().form_valid(form)

    def test_func(self):
        item = self.get_object()
        print(self.request.user == item.owner.user)
        
        if self.request.user == item.owner.user:
            return True
        return False


class MedicineDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    DeleteView.model = Medicine

    DeleteView.success_url =  reverse_lazy('item_list')
    def test_func(self):
        item = self.get_object()
        if self.request.user == item.owner.user:
            return True
        return False
    
    
class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Pharmacy
    template_name = 'dashboard/create_profile.html'
    fields = ['pharmacy_name',"phone_number","location","google_map_link"]
    
    def test_func(self):
                print('test')
                item = self.get_object()
                
                if self.request.user == item.user:
                    return True
                return False
    def form_valid(self, form):
                
                form.instance.user = self.request.user
                return super().form_valid(form)
                                                        
class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pharmacy
    template_name = 'dashboard/update_profile.html'
    fields = ['pharmacy_name',"phone_number","location","google_map_link"]
    def test_func(self):
                print('test')
                item = self.get_object()
                
                if self.request.user == item.user:
                    return True
                return False
    def form_valid(self, form):
                
                form.instance.user = self.request.user
                return super().form_valid(form)  


@login_required
def update_admin_profile(request):
    
    if request.method == 'POST':
        info_form = UpdateUserForm(request.POST,instance=request.user)
        if info_form.is_valid():
            info_form.save()
            messages.success(request, f'\a تم تحديث حسابك بنجاح')

            return redirect('dashboard')
    else:
        info_form = UpdateUserForm(instance=request.user)

    context = {
        'info_form' : info_form,
    }
    return render(request, 'dashboard/update_admin_profile.html', context)



