from django.shortcuts import render, redirect

from . import util
import markdown2
from .forms import NewPageForm

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def topic(request, md_entry):
    entry = util.get_entry(md_entry)
    #   If entry doesn't exist
    if not entry:
        return render(request, "encyclopedia/error.html", {
            "error_message": "Sorry! your requested page was not found."
        })
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
        # Returns function "topic" which takes search query as 2nd argument
        return topic(request, request.GET.get("q"))

    else:
        for md in util.list_entries():  # for loop will iterate over complete list
            if query in md.lower(): # if "query" is less than an item
                q_list.append(md)   # append selected items in blank list

        return render(request, "encyclopedia/search.html", {
            "q_list": q_list,
        })


def create(request):
    if request.method == "POST":

        # Take in the data, the user submitted and save it as form
        form = NewPageForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            title = form.cleaned_data["title"]
            content = form.cleaned_data["NewPage"]

            if util.get_entry(title):
                return render(request, "encyclopedia/error.html", {
                    "error_message": "Sorry! This title already exist"
                })
            util.save_entry(title, content)

            return topic(request, title)

    return render(request, "encyclopedia/create.html", {
        "form": NewPageForm()
    })