from django.views   import generic

class TicketListView(generic.TemplateView):
    def get_context_data(self, **kwargs):
        context = super(TicketListView, self).get_context_data(**kwargs)
        return context

    def get_template_names(self):
        return 'zeroanda/ticket/change_list.html'