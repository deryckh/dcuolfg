# Copyright 2012-2013 Deryck Hodge.  This software is licensed under the
# GNU Lesser General Public License version 3 (see the file LICENSE).

"""
Forms for handling characters.
"""

from django.forms import ModelForm

from dcuolfg.characters.models import Character


class AddCharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = (
            'name',
            'server',
            'role',
            'powerset',
            'description',
            'level',
            'combat_rating',
            'skill_points',
#            'image',
        )
