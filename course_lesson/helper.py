from .models import *


def make_changes_in_model(module, current_id, next_id, previous_id):
    model = module.objects.get(id=current_id)
    model.previous_id = previous_id
    model.next_id = next_id
    module.save()