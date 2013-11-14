from django.db.models import fields

from south.modelsinspector import add_introspection_rules

from common.helper import md5_hash


class RandomHashField(fields.CharField):
    """
    Store a random hash for a certain model field.
    
    @param update_on_save optional field whether to update this hash or not, everytime the model instance is saved
    """
    def __init__(self, update_on_save=False, *args, **kwargs):
        #TODO: args & kwargs serve no purpose but to make django evolution to work
        self.update_on_save = update_on_save
        super(fields.CharField, self).__init__(max_length=128, unique=True, blank=False, null=False, db_index=True,
            default=md5_hash())
    
    def pre_save(self, model_instance, add):
        if not add and not self.update_on_save:
            return getattr(model_instance, self.name)
        
        random_hash = md5_hash()
        setattr(model_instance, self.name, random_hash)
        return random_hash

add_introspection_rules([
    (
        [RandomHashField], # Class(es) these apply to
        [],         # Positional arguments (not used)
        {           # Keyword argument
            "update_on_save": ["update_on_save", {"default": False}],
        },
    ),
], ["^common\.db_fields\.RandomHashField"])
