from .models import *

def page_not_found(model, queue_number):
    return f'<h1>Error!</h1><h2/>There\'s no {model} with such queue number: {queue_number}'


def make_changes_in_model(module, current_id, next_id, previous_id):
    model = module.objects.get(id=current_id)
    model.previous_id = previous_id
    model.next_id = next_id
    module.save()