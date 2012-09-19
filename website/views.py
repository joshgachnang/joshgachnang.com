from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render_to_response, redirect 
from django.template import RequestContext
from website.models import Post, Category, Tag
import logging
import joshgachnang.settings as settings

logger = logging.getLogger('views')

def homepage(request):
    template_data = {}
    return render_to_response('site_base.html', template_data, context_instance=RequestContext(request))

def posts(request, link=None, page=1):
    logger.debug("Trying to find object for link '{0}'.".format(link))
    template_data = {}
    if link is None:
        # For now, set this to home. Later, make it a part of the settings.
        link = settings.default_home_link
        logger.debug("Trying to find object for default link '{0}'.".format(link))

    # Pagination
    start_post = (page - 1) * settings.posts_per_page
    # End post is 1 more than the actual number of the end post for slicing
    end_post = (page * settings.posts_per_page)

    # Determine whether link is a post, category, or tag, in that order.
    try:
        post = Post.objects.get(url=link)
        return render_post(request, post)
    except (Post.DoesNotExist):
        pass
    except (Post.MultipleObjectsReturned):
        logger.exception("More than one Post with URL {0} exists.".format(link))
        return HttpResponseServerError("More than one Post with URL {0} exists.".format(link))
    try:
        category = Category.objects.get(name=link)
        return render_category(request, category)
    except (Category.DoesNotExist):
        pass
    except (Category.MultipleObjectsReturned):
        logger.exception("More than one Category with name {0} exists.".format(link))
        return HttpResponseServerError("More than one Category with name {0} exists.".format(link))
    try:
        tag = Tag.objects.get(name=link)
        return render(request, tag)
    except (Tag.DoesNotExist):
        pass
    except (Tag.MultipleObjectsReturned):
        logger.exception("More than one Tag with name {0} exists.".format(link))
        return HttpResponseServerError("More than one Tag with name {0} exists.".format(link))
    # Not found anywhere.
    return HttpResponseNotFound("Could not find a post, category, or tag matching {0}".format(link))

def render_post(request, post):
    template_data = {}
    logger.debug("Getting Post with URL {0}".format(post.url))
    template_data['post'] = post
    logger.debug("Found Post {0}".format(template_data['post']))
    logger.debug("Rendering {0}.".format(post.template_name))
    return render_to_response(post.template_name, template_data, context_instance=RequestContext(request))

def render_category(request, category):
    template_data = {}
    logger.debug("Getting Category with name {0}".format(category.name))
    template_data['category'] = category
    logger.debug("Found Category {0}".format(template_data['post']))
    return render_to_response('individual_post.html', template_data, context_instance=RequestContext(request))

def render_tag(request, tag):
    template_data = {}
    logger.debug("Getting Tag with name {0}".format(category.name))
    template_data['tag'] = tag
    logger.debug("Found Tag {0}".format(template_data['post']))
    return render_to_response('individual_post.html', template_data, context_instance=RequestContext(request))

def blogs(request, page=1):
    logger.debug("Rendering blog pages.")
    template_data = {}

    # Pagination
    start_post = (page - 1) * settings.posts_per_page
    # End post is 1 more than the actual number of the end post for slicing
    end_post = (page * settings.posts_per_page)
    total_pages = (Post.objects.count() / settings.posts_per_page) + 1
    template_data['page'] = page
    if page < total_pages:
        template_data['next_page'] = page + 1
    else:
        template_data['next_page'] = None
    if page > 1:
        template_data['prev_page'] = page - 1
    else:
        template_data['prev_page'] = None

    template_data['posts'] = Post.objects.filter(in_blog_posts=True).order_by('published')[start_post:end_post]
    logger.debug("Found these blog posts: {0}".format(template_data['posts']))
    return render_to_response('blog_base.html', template_data, context_instance=RequestContext(request))