from django.shortcuts import render

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