"""
   Module for defining views
"""

from flask import jsonify, request
from flask.views import MethodView
from models import Entries


event_entries = Entries()


class AllDairyEntries(MethodView):
    """
       class for defining views
    """

    def post(self):
        """
           method to post all events
        """
      
        keys = ("title",  "description")
        
        if not set(keys).issubset(set(request.json)):
            return jsonify({'Alert':'fill all fields'}) 
            
        
        if event_entries.exit_entry(request.json['title']):
                return jsonify({'Alert':'your entry has already been input'})
    
        post_data = request.get_json()
        title = request.json['title']
        description = request.json['description'] 
        id = 'id' 

        
        event_entries.add_entry(id, title, description)

        response_object =  event_entries.__dict__
        
        return jsonify(response_object), 201


    def get(self, event_id=None):
        """
           method for all get requests and single request
        """
        if event_id is None:
            if event_entries.get_all_entries() is True:
                return jsonify({'events':'No new entry,Please enter an event'})
            return jsonify({'events': event_entries.get_all_entries()}), 200
        return jsonify({'events': event_entries.get_one_entry(event_id)}), 200
    def put(self,event_id):
        """
            method for puts/cancels events
           param: route /api/events/<int:event_id>/cancel
           response: json data
        """
        post_data = request.get_json()

        key= 'title'
        if key not in post_data:
            return jsonify({'alert':'input feilds'})
        
        return jsonify({'new title':event_entries.update(event_id)}),200