'''
This script tried to fix a problem with the https redirects in the deployment server.
The problem was that when the server sent a 302 status code to the browser it sent only a relative path without the https protocol.
It had the consequence that the client tried to do the GET operation using http.
We don't need it anymore because it was solved modifying the django.wsgi module, but I have left it as a reference.
'''
 
class HttpsRedirect(object):
    """
    Handles conditional HTTPS operations. If the request has https, the Location header in the redirect is replaced by an Https.
    """
    def process_response(self, request, response):
      #response.__setitem__('Informacion' , response['Location'])
      if self.is_deploymentserver(request) and request.method == 'POST':
        if self.has_relative_reference(response):
          location = self.create_url_with_relative(request, response)
        else:
          location = self.create_url(request, response)
          
        response['Location'] = location
      return response

    def is_deploymentserver(self, request):
       if request.META.get('SERVER_NAME').find('webfactional') >= 0:
         return True
       return False

    def has_relative_reference(self, response):
        if response['Location'].find('../') >= 0:
          return True
        return False

    def create_url(self, request, response):
        path = request.META.get('HTTP_REFERER').replace('https://experior.webfactional.com','')
        url = 'https://' + request.META.get('SERVER_NAME') + path
        return url
   
    def create_url_with_relative(self, request, response):
        path = request.META.get('HTTP_REFERER').replace('https://experior.webfactional.com','')
        elements = path.strip('/').split('/')
        path = '/'.join(elements[:-1])
        relative = response['Location']
        commands = relative.strip('/').split('/')
        commands = '/'.join(commands[1:]) + '/'
        url = 'https://' + request.META.get('SERVER_NAME') + '/' + path + '/'
        if commands != '/':
           url = url + commands
        return url
