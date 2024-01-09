from django.shortcuts import render
from django.views.generic import TemplateView


class UserPanelDashboardView(TemplateView):
    template_name = 'user_panel_module/user_panel_dashboard_page.html'
