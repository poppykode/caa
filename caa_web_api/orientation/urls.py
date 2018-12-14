from django.urls import path
from .views import (
    create_orientation_video,
    view_orientation_video,orientation_list_api_list,
    get_reg_numbers, get_student_info,video_delete,
    video_update,video_update_post,get_student_info_pass,
)
# from .students import (
#     get_reg_numbers,
# )

app_name = 'orientation'
urlpatterns = [
    path('orientation-video/',create_orientation_video, name='orientation-create'),
    path('orientation-video-create/',view_orientation_video, name='orientation-list'), 
    path('delete/<int:pk>',video_delete, name='video-delete'),
    path('edit/<int:pk>',video_update , name='video-update'),
    path('edit/video/<int:pk>',video_update_post , name='video-update-end'),
    path('api/v1/user-info-password/',get_student_info_pass),
    path('api/v1/orientation-list/',orientation_list_api_list),
    path('api/v1/reg-numbers/',get_reg_numbers), 
    path('api/v1/user-info/',get_student_info),
]