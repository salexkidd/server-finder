"""
host admin module
"""
#django modules
from django.contrib import admin

#host modules
import host.models as host_models


admin.site.register(host_models.Host)
