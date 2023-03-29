from django.urls import path

from pet_app import views, adminviews, userviews, officeviews

urlpatterns = [
    path('', views.home, name='home'),
    path('login_view', views.login_view, name='login_view'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('customer_register', views.customer_register, name='customer_register'),

    path('admin_home', adminviews.admin_home, name='admin_home'),
    path('officer_add', adminviews.officer_register, name='officer_add'),
    path('officer_view', adminviews.officer_view, name='officer_view'),
    path('customer_view', adminviews.customer_view, name='customer_view'),
    path('officer_edit/<int:id>/', adminviews.officer_edit, name='officer_edit'),
    path('officer_delete/<int:id>/', adminviews.officer_delete, name='officer_delete'),
    path('accept_customer/<int:id>/', adminviews.accept_customer, name='accept_customer'),
    path('reject_customer/<int:id>/', adminviews.reject_customer, name='reject_customer'),
    path('pet_register_vi', adminviews.pet_register_vi, name='pet_register_vi'),
    path('pet_register_del/<int:id>/', adminviews.pet_register_del, name='pet_register_del'),
    path('reply_complaint/<int:id>/', adminviews.reply_complaint, name='reply_complaint'),
    path('complaint_admin', adminviews.complaint_admin, name='complaint_admin'),
    path('approve_pet/<int:id>/', adminviews.approve_pet, name='approve_pet'),
    path('reject_pet/<int:id>/', adminviews.reject_pet, name='reject_pet'),

    path('user_home', userviews.user_home, name='user_home'),
    path('officer_view_user', userviews.officer_view, name='officer_view_user'),
    path('view_schedule_customer', userviews.view_schedule_customer, name='view_schedule_customer'),
    path('take_appointment/<int:id>', userviews.take_appointment, name='take_appointment'),
    path('appointment_view', userviews.appointment_view, name='appointment_view'),
    path('pet_register', userviews.pet_register, name='pet_register'),
    path('pet_register_view', userviews.pet_register_view, name='pet_register_view'),
    path('complaint_add_user', userviews.complaint_add_user, name='complaint_add_user'),
    path('complaint_user', userviews.complaint_user, name='complaint_user'),

    path('officer_home', officeviews.officer_home, name='officer_home'),
    path('pet_register_vie', officeviews.pet_register_vie, name='pet_register_vie'),
    path('pet_register_officer', officeviews.pet_register_officer, name='pet_register_officer'),
    path('pet_update/<int:id>/', officeviews.pet_update, name='pet_update'),
    path('pet_delete/<int:id>/', officeviews.pet_delete, name='pet_delete'),
    path('schedule_add', officeviews.schedule_add, name='schedule_add'),
    path('schedule_view', officeviews.schedule_view, name='schedule_view'),
    path('schedule_update/<int:id>/', officeviews.schedule_update, name='schedule_update'),
    path('schedule_delete/<int:id>/', officeviews.schedule_delete, name='schedule_delete'),
    path('appointment_view_doctor', officeviews.appointment_view_doctor, name='appointment_view_doctor'),
    path('approve_appointment/<int:id>', officeviews.approve_appointment, name='approve_appointment'),
    path('reject_appointment/<int:id>', officeviews.reject_appointment, name='reject_appointment'),
]
