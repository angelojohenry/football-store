from django.urls import path
from main.views import show_main, add_object, show_object, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_product, delete_product, add_product_entry_ajax, edit_product_ajax, login_user_ajax, register_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-object/', add_object, name='add_object'),
    path('product/<str:id>/', show_object, name='show_object'),
    path('xml/', show_xml, name= 'show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('register/ajax/', register_ajax, name='register_ajax'),
    path('login/', login_user, name='login'),
    path('login/ajax/', login_user_ajax, name='login_ajax'),
    path('logout/', logout_user, name='logout'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    path('create-product-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('edit-product/<uuid:id>/', edit_product_ajax, name='edit_product_ajax'),
]