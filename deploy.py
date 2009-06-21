
class HttpsRedirect(object):
    """
    Handles conditional HTTPS operations. If the request has https, the Location header in the redirect is replaced by an Https.
    """
    def process_response(self, request, response):
      #response.__setitem__('Basura' , 'norberto')
      if self.is_deploymentserver(request) and request.method == 'POST':
        location = 'https://' + request.META.get('SERVER_NAME') + response['Location']
        response['Location'] = location
      return response

    def is_deploymentserver(self, request):
       if request.META.get('SERVER_NAME').find('webfactional') >= 0:
         return True
       return False
