myName = "jev"
myFriend = "localhost:12345"

class StudentList(Resource):
  def get(self)
      data = request.form.to_dict()
      
      if data.get('originator', None) == myName:
        return {"students": [{myName: {"hostname": "XXXX"}}]}, 200
      if 'originator' not in data:
        data['originator'] = myName
        
      r = get("http://{}/student/".format(myFriend), data=data)
      data = r.json()
      data["students"].append({myName: {"hostname": ""XXXX"}})
      
      return json.dumps(data), 200
      
api.add_resource(StudentList, '/student/')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=12345, threaded=True)
