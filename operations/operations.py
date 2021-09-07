from utils.constants import url, tokenEndPoint, userEndPoint,\
                            connectEndPoint, jobEndPoint
from utils.body import dataAuth, dataUser, dataLogin
from utils.header import configAuth, configCreate, configTrans

import requests
import json

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
	return json.loads(response.text)