from flask import Flask
from operations.operations import authenticate, configUpdate, createUser,\
                                  createConn, getJobStatus
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bank_expenditure():
  token = authenticate()
  configUpdate(token)
  userId = createUser()
  jobId = createConn(userId)
  jobStatus = getJobStatus(jobId)

  return {'token': token,
          'userId': userId,
          'jobId': jobId,
          'jobStatus': jobStatus}
