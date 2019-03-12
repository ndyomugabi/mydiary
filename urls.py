"""
Module decorates views to urls
"""
from views import AllDairyEntries

class GetUrls:
    """
    Method that views with urls
    """
    @staticmethod
    def fetch_urls(event):
        """
        Method that views with urls
        """
        event.add_url_rule('/api/v1/entries/',
                              view_func=AllDairyEntries.as_view('getallentries'), defaults={'event_id': None},
                              methods=['GET',])
        event.add_url_rule('/api/v1/entries/<int:event_id>/',
                              view_func=AllDairyEntries.as_view('getoneentry'),
                              methods=['GET',])
        event.add_url_rule('/api/v1/entries/',view_func=AllDairyEntries.as_view('postentry'), methods=['POST',])
        event.add_url_rule('/api/v1/entries/<int:event_id>/', view_func= AllDairyEntries.as_view('modifyanentry'), methods=['PUT',])
