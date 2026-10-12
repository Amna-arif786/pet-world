def get_liked_pet_ids(request):
    raw = request.session.get('liked_pets', [])
    return {int(pk) for pk in raw}


def set_liked_pet_ids(request, liked_ids):
    request.session['liked_pets'] = sorted(liked_ids)
    request.session.modified = True


def liked_pets(request):
    return {'liked_pet_ids': get_liked_pet_ids(request)}
