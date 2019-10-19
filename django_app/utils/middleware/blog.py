from blog.models import Post

class BlogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self,request, response):
        '''
            Add top five posts in response when user views "blog" 
        '''
        if 'blog' in request.path.split('/'):
            response.context_data['top_posts'] = Post.objects.top_posts()
        return response