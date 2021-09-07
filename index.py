import requests
import json
import time

apiKey = 'M2E0MDgzZDUtOTc3YS00ZWZhLWI0YzAtYWQ5NmM0N2U2NWY1OjgwODgyYWNhLWJiZTg'\
	'tNDk1NS05ZjNjLWM0MDIzMDY2ZWViMA=='
url = 'https://au-api.basiq.io/'
tokenEndPoint = 'token/'
userEndPoint = 'users/'
connectEndPoint = '/connections/'
transactionEndPoint = '/transactions/'
jobEndPoint = 'jobs/'

dataAuth = {
	"grant_type": 'client_credentials',
	"scope": 'SERVER_ACCESS',
}

dataUser = {
	"email": 'slobo@gmail.com',
	"mobile": '+38163333333',
	"firstname": 'Slobodan',
	"lastname": 'Todosijevic',
}

dataLogin = {
	"loginId": 'gavinBelson',
	"password": 'hooli2016',
	"institution": {
		"id": 'AU00000',
	}
}

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

def authenticate():
	response = requests.post(
		url + tokenEndPoint,
		data=dataAuth,
		headers=configAuth)
	return json.loads(response.text)["access_token"]

def configUpdate(token) :
	configCreate["Authorization"] = f'Bearer {token}'
	configTrans["Authorization"] = f'Bearer {token}'

def createUser():
	response = requests.post(
		url + userEndPoint,
		data=dataUser,
		headers=configCreate)
	return json.loads(response.text)["correlationId"]

def createConn(userId):
	response = requests.post(
		url + userEndPoint + userId + connectEndPoint,
		data=dataLogin,
		headers=configCreate
	)
	return json.loads(response.text)["correlationId"]

def getJobStatus(jobId):
	response = requests.get(
		url + jobEndPoint + jobId,
		headers=configTrans)
	return json.loads(response.text) #response.data.steps[2].status

token = authenticate()
print('@@@token:', token)
configUpdate(token)
userId = createUser()
print('@@@userId:', userId)
jobId = createConn(userId)
print('@@@jobId:', jobId)
jobStatus = getJobStatus(jobId)
print('@@@jobStatus:', jobStatus)
