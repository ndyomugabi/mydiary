"""end points for the questions"""
from flask import jsonify
from flask import request, Request
from flask.views import MethodView

class AllDairyEntries(MethodView):
    """class for getting questions"""
    dairies = []

    def get(self, event_id):
        """
        method for all get requests"
        """
        if event_id == None:
            return jsonify({'entries':[entry for entry in self.dairies]})  #checks entries in ourlist diaries
        
        entry = [entry for entry in self.dairies if entry['event_id'] == event_id] #checks the events in ourlist and returns the specific event with corresponding event_id
        return jsonify({'entry' : entry}) #return entry in position zero

    def post(self):
        """method for all post requests"""
        if not request.json:
            return jsonify({'error':"not a json request"}), 400
        else:
            entry = {'title':request.json['title'], 'description' : request.json['description'],
                        'event_id':request.json['event_id']}
            self.dairies.append(entry)
            return jsonify({'entries' : self.dairies}),201

    def update(self, event_id):
        for entry in self.dairies: 
            if event_id == entry['event_id']:
                event_json= request.get_json()
                entry['title']= title
                return {event_id:"placed"}

    def put(self, event_id):
        return jsonify ({"entries":AllDairyEntries.update(self,event_id)}),200


