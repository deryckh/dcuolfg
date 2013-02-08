# Copyright 2012-2013 Deryck Hodge.  This software is licensed under the
# GNU Lesser General Public License version 3 (see the file LICENSE).

"""
Site-wide views.
"""

from django.http import (
    Http404,
    HttpResponseRedirect,
)
from django.shortcuts import (
    get_object_or_404,
    render,
)
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from dcuolfg.characters.forms import AddCharacterForm
from dcuolfg.characters.models import Character

def _get_server_value_from_name(server_name):
        """Return the server value to store based on server name."""
        server_value = [
            srv[0] for srv in Character.CHARACTER_SERVER_CHOICES
            if srv[1] == server_name]
        if len(server_value) == 1:
            return server_value[0]
        return None

def index(request):
    """Main list of recently updated characters."""

    characters = Character.objects.updated()
    data = {
        'characters': characters,
        'mission_count': len(characters),
    }
    return render(request, 'characters/index.html', data)

@login_required
def add_character(request):
    """A view for a player to add a character."""

    form = None
    if request.POST:
        character = Character(player=request.user)
        form = AddCharacterForm(request.POST, instance=character)
        if form.is_valid():
            character = form.save()
            character_args = (character.get_server_display(), character.name)
            return HttpResponseRedirect(
                reverse('character_profile', args=character_args))
    else:
        form = AddCharacterForm()

    data = {
        'form': form,
    }
    return render(request, 'characters/add.html', data)

def character_profile(request, server, name):
    """Render a profile view for a character."""

    server_value = _get_server_value_from_name(server)
    if server_value is None:
        raise Http404

    character = get_object_or_404(Character, server=server_value, name=name)
    data = {
        'character': character,
    }
    return render(request, 'characters/profile.html', data)

def delete_character(request, server, name):
    """A view for a player to delete a character."""

    server_value = _get_server_value_from_name(server)
    if server_value is None:
        raise Http404

    character = get_object_or_404(Character, server=server_value, name=name)
    character.delete()
    data = {
        'msg': 'Character successfully deleted.'
    }
    return render(request, 'characters/delete.html', data)
