import requests

response = requests.get("http://randomfox.ca/floof")
print('status_code', response.status_code)
print('\n')
print('json', response.json())
print('\n')
print('headers', response.headers)
print('\n')
print('content', response.content)
print('\n')
print('raw', response.raw.msg)
print('raw', response.raw.read())
print('raw', response.raw.headers)
print('raw', response.raw.flush())

print('\n')
print('reason', response.reason)
print('\n')
print('request body', response.request.body)
print('request headers', response.request.headers)
print('request method', response.request.method)
print('request url', response.request.url)
print('request hooks', response.request.hooks)

print('\n')
print('text', response.text)
print('\n')
print('url', response.url)
