# Copyright 2012 Deryck Hodge.  This software is licensed under the
# GNU Lesser General Public License version 3 (see the file LICENSE).

from django.contrib import admin

from dcuolfg.accounts.models import Profile
admin.site.register(Profile)
