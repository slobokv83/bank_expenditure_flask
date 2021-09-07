from utils.constants import apiKey

configAuth = {
		"Authorization": f'Basic {apiKey}',
		'Content-Type': 'application/x-www-form-urlencoded',
		'basiq-version': '2.0'
}

configCreate = {
		"Authorization": 'Bearer',
		"Accept": 'application/json',
		'Content-Type': 'application/json'
}

configTrans = {
		"Authorization": 'Bearer',
		"Accept": 'application/json',
}