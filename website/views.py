from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect 
from django.template import RequestContext
from website.models import Post, Category, Tag, ContactEmail
import logging
import joshgachnang.settings as settings
from forms import ContactForm
from django.core.mail import send_mail

logger = logging.getLogger('views')

def homepage(request):
    template_data = {}
    return render_to_response('site_base.html', template_data, context_instance=RequestContext(request))

def posts(request, link=None, page=1):
    # Try to coerce page to an int.
    page = int(page)
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
    # Try coercing page to int
    page = int(page)
    template_data = {}

    # Pagination
    start_post = (page - 1) * settings.posts_per_page
    # End post is 1 more than the actual number of the end post for slicing
    end_post = (page * settings.posts_per_page)
    if Post.objects.count() % settings.posts_per_page == 0:
        total_pages = (Post.objects.count() / settings.posts_per_page)
    else:
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

    template_data['posts'] = Post.objects.filter(in_blog_posts=True).order_by('-published')[start_post:end_post]
    logger.debug("Found these blog posts: {0}".format(template_data['posts']))
    return render_to_response('blog_base.html', template_data, context_instance=RequestContext(request))

def contact_send(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            print "Form: ", form.cleaned_data
            contact_email = ContactEmail(**form.cleaned_data)
            contact_email.save()
            send_all_mail()
            return HttpResponseRedirect('/contact_thanks/')
        else:
            return HttpResponseRedirect('/contact')
    else:
        return HttpResponseForbidden()

def contact_thanks(request):
    template_data = {}
    return render_to_response('thanks.html', template_data, context_instance=RequestContext(request))

def send_all_mail():
    emails = ContactEmail.objects.filter(sent=False)
    for email in emails:
        subject = "{0} Contact from {1}: {2}".format(settings.site_name, email.sender, email.subject)
        send_mail(subject=subject, message=email.message, from_email=email.sender_email, recipient_list=settings.emails, fail_silently=False)
        email.sent = True
        print email
        email.save()