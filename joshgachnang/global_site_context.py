
from website.models import Post, Category
import logging
logger = logging.getLogger('views')

def site_context(request):
    """ This context processor adds functionality that should be available on
    every page, such as sidebars. 
    """
    try:
        recent_posts = Post.objects.all().order_by('published')[0:5]
    except Exception as e:
        logger.exception('Could not get recent Posts')
        recent_posts = None
    logger.debug("Recent posts are {}".format(recent_posts))
    categories = Category.objects.all()
    logger.debug("All categories are {}".format(categories))
    return {'recent_posts': recent_posts, 'categories': categories}

