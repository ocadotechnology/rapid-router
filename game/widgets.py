from django import forms
class DropDownMenuSelectMultiple(forms.SelectMultiple):
    """
    A SelectMultiple wich will use checkboxes to select individual items
    """
class Media:
    css = {
        'all': ('game/css/pqselect.dev.css',)
    }
js = (
    'game/js/pqselect.dev.js',
)
def render(self, name, value, attrs, choices=()):
    html = super(DropDownMenuSelectMultiple, self).render(name, value, attrs, choices)
    return html

def value_from_datadict(self, data, files, name):
    if isinstance(data, (MultiValueDict, MergeDict)):
        return data.getlist(name)
    return data.get(name, None)