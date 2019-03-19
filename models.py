from flask import request 

""" Module for new events
"""
class Entries():
    """
        class defining all methods
    """
    # userlist = []
    def __init__(self):
        self.diaries = []
        

    def add_entry(self,event_id, title,  description):
        """
           Method to post events
        """
        event_list = [event_entry for event_entry in self.diaries]

        id = len(event_list) + 1
        entry = {
            'title': title, 'id':id,'description': description
             
        }
        self.diaries.append(entry)
        return {'New entry': [
            entry for entry in self.diaries]}

    def get_all_entries(self):
        """
           Method to get all events
        """
        if not self.diaries:
            return True
        return self.diaries
        
    def get_one_entry(self, event_id):
        """
           Method to get a single event
        """
        available_entry_id = [
            entry for entry in self.diaries
            if entry ['id'] == event_id]
        if not available_entry_id:
            return {event_id:"entry_id doesnot exist"}
        return available_entry_id

  
    def update(self,event_id):
        """
           method for modifying an entry
           
        """
        for entry in self.diaries:
            if event_id == entry['id']:
                entry_json = request.get_json()
                title = entry_json['title']
                entry['title'] = title
                return {event_id:'Event has been updated'}

    def exit_entry(self, title):
        for entry in self.diaries:
            if title == entry['title']:
                return True
        return False