from django.shortcuts import render

# Posts list
posts_list = {
    "TestPost1":"Lorem ipsum dolor sit amet, consetetur sadipscing elitr.",
    "TestPost2":"Lorem ipsum dolor sit amet, consetetur sadipscing elitr.",
    "TestPost3":"Lorem ipsum dolor sit amet, consetetur sadipscing elitr.",
    "TestPost4":"Lorem ipsum dolor sit amet, consetetur sadipscing elitr.",
    "TestPost5":"Lorem ipsum dolor sit amet, consetetur sadipscing elitr."
}

#
# Loads the posts list for the index page. Gets the keys of the posts_list list and returns them 
#
def index(request):
    posts = list(posts_list.keys())
    return render(request, "templates/index.html", {
        "posts":posts
    })

