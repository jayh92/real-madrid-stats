Project: Real Madrid Stats

1. Data Source: api.football-data.org/index
2. Consume RESTful API: python project
	* Use 'requests':
		* http://docs.python-requests.org/en/latest/index.html
	* Code:
		import http.client
		import json

		connection = http.client.HTTPConnection('api.football-data.org')
		headers = { 'X-Auth-Token': 'cf310facc79747d7a896173e62b04b4d' }
		connection.request('GET', '/alpha/soccerseasons', None, headers )
		response = json.loads(connection.getresponse().read().decode())

		print (response)

3. Parse JSON: python project
4. UI: HTML5 & CSS

5. Running realmadrid
    * Open Applications > Terminal: $ python get.py