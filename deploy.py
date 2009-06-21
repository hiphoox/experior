
class HttpsRedirect(object):
    """
    Handles conditional HTTPS operations. If the request has https, the Location header in the redirect is replaced by an Https.
    """
    def process_response(self, request, response):
      if request.is_secure() and request.method == 'POST':
        print response['Location']
        location = 'https://' + request.META.get('SERVER_NAME') + response['Location']
        response['Location'] = location
      
      return response
