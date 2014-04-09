from django.views.generic import ListView
from django.db.models import Q

class SearchableListView(ListView):
    '''
    Render a list of objects that's searchable.
    '''
    # pylint: disable=R0901
    # pylint: disable=E1101
    #: The fields the search will be performed on, using ``queryset.filter``.
    search_fields = ()

    def get_context_data(self, **kwargs):
        context = super(SearchableListView, self).get_context_data(**kwargs)
        if self.search_fields:
            context['search'] = True
            query = self.request.GET.get('q')
            if query:
                context['search_query'] = query
        return context

    def get_queryset(self):
        queryset = super(SearchableListView, self).get_queryset()
        if self.search_fields:
            query = self.request.GET.get('q')
            if query is None:
                return queryset
            queryset = self.search_queryset(queryset, query)
        return queryset

    def search_queryset(self, queryset, search_term):
        query = Q()
        for field in self.search_fields:
            lookup = 'icontains'
            if not isinstance(field, basestring):
                field, lookup = field
            query = query | Q(**{'%s__%s' % (field, lookup): search_term})
        return queryset.filter(query)
