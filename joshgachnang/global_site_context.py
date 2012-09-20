
from website.models import Post, Category, NavBar, NavBarItem
import logging
logger = logging.getLogger('views')
from website.forms import ContactForm

def site_context(request):
    """ This context processor adds functionality that should be available on
    every page, such as sidebars. 
    """
    try:
        recent_posts = Post.objects.all().order_by('published')[0:5]
    except Exception as e:
        logger.exception('Could not get recent Posts')
        recent_posts = None
    logger.debug("Recent posts are {0}".format(recent_posts))
    categories = Category.objects.all()
    logger.debug("All categories are {0}".format(categories))
    navbars = {}
    print "Navbars all: ", NavBar.objects.all()
    for navbar in NavBar.objects.all():
        print  "Navbaritem:", NavBarItem.objects.filter(navbar=navbar).order_by('priority')
        navbars[navbar.name] = NavBarItem.objects.filter(navbar=navbar).order_by('priority')
    # Contact form
    contact_form = ContactForm()
    return {'recent_posts': recent_posts, 'categories': categories, 'navbars': navbars, 'contact_form': contact_form}

