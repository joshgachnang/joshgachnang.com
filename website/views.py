from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render_to_response, redirect 
from django.template import RequestContext
from website.models import Post, Category
import logging

logger = logging.getLogger('views')

def homepage(request):
    template_data = {}
    return render_to_response('site_base.html', template_data, context_instance=RequestContext(request))

def posts(request, category=None, page=1, posts_per_page=10):
    template_data = {}
    start_post = (page - 1) * posts_per_page
    # End post is 1 more than the actual number of the end post for slicing
    end_post = (page * posts_per_page)
    try:
        if category is None:
            template_data['posts'] = Post.objects.all().order_by('published')[start_post:end_post]
        else:
            # Get only posts for category
            cat = Category.objects.filter(name=category)
            template_data['posts'] = Post.objects.filter(category=cat).order_by('published')[start_post:end_post]
            template_data['category'] = category
            logger.debug("Category is {}".format(category))
        logger.debug("Posts are {}".format(template_data['posts']))
    except Exception as e:
        logger.exception('Could not get Posts')
        return HttpResponseNotFound("Could not find any posts for page {}".format(page) )
    return render_to_response('site_base.html', template_data, context_instance=RequestContext(request))

def individual_post(request, url):
    template_data = {}
    logger.debug("Getting Post with URL {}".format(url))
    try:
        template_data['post'] = Post.objects.get(url=url)
        logger.debug("Found Post {}".format(template_data['post']))
    except Post.DoesNotExist as e:
        logger.exception("Post with URL {} does not exist.".format(url))
        return HttpResponseNotFound("Post with URL {} does not exist.".format(url))
    except Post.MultipleObjectsReturned as e:
        logger.exception("More than one Post with URL {} exists.".format(url))
        return HttpResponseNotFound("More than one Post with URL {} exists.".format(url))
    return render_to_response('individual_post.html', template_data, context_instance=RequestContext(request))