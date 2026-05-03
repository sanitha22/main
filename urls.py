from django.urls import path
from .import views, meme_views, story_views

urlpatterns= [
    path('',views.index,name='index'),
    path('registration/',views.registration,name='registration'),
    path('login/',views.login,name='login'),
    path('userhome/',views.userhome,name='userhome'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('profile/',views.profile,name='profile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('admin_view_user/<int:id>',views.admin_view_user,name='admin_view_user'),
    path('login_history',views.login_history,name='login_history'),
    path('admin_user/<int:id>/delete/', views.admin_delete_user, name='admin_delete_user'),
    path('feedback/', views.feedback, name='feedback'),
    path('feedback-dashboard/', views.feedback_dashboard, name="feedback_dashboard"),
    path('delete_message/<int:id>/', views.delete_message, name='delete_message'),
    path('logout/',views.logout,name='logout'),
    path("user_management/", views.user_management, name="user_management"),
    path("caption/", views.caption_generator, name="caption"),
    path("results/", views.caption_results, name="results"),
    path("delete-caption/<int:id>/", views.delete_caption, name="delete_caption"),


    path('meme/', meme_views.meme_generator, name='meme_generator'),
    path('meme/results/', meme_views.meme_results, name='meme_results'),
    path('meme/delete/<int:id>/', meme_views.delete_meme, name='delete_meme'),

    path('story/', story_views.story_generator, name='story_generator'),
    path('story/download/', story_views.download_story_pdf, name='download_story_pdf'),
    
    path('editor/', views.editor_page, name='editor'),
    path('collage/', views.collage, name='collage'),
    path('style-converter/', views.style_converter, name='style_converter'),
    path('video-result/', views.video_result, name='video_result'),
    path('video-upload/', views.video_upload, name='video_upload'),

]