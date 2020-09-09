from django.shortcuts import render, redirect


from . import util
import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def topic(request, md_entry):
    entry = util.get_entry(md_entry)
    #   If entry doesn't exist
    if not entry:
        return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": md_entry,
            "content": markdown2.markdown(entry)
        })

def search(request):
    # access the searched string and convert into lowercase
    query = request.GET.get("q").lower()
    
    # all entries list in lowercase
    # this code snippet took from "https://medium.com/@gilwellm/ho-to-convert-a-list-into-upper-or-lowercase-in-python-3-f2c4bbb71e5a"
    entries_list = [x.lower() for x in util.list_entries()]
    q_list = []
    #   check about query existance
    if query in entries_list:
        # Returns function "topic" which get searched query as 2nd argument
        return topic(request, request.GET.get("q"))

    else:
        for md in util.list_entries():
            if query in md.lower():
                q_list.append(md)

        return render(request, "encyclopedia/search.html", {
            "q_list": q_list,
        })