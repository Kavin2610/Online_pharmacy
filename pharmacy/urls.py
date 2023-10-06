from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from payment.views import CreateCheckoutSessionView

urlpatterns = [
    path('', include('core.urls')),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

