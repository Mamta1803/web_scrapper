from django.shortcuts import render, HttpResponse
from .scrapper import scrap

import pandas as pd

def sort_comments(request):
    df = scrap()
    sort_df = df.sort_values(by=['Comments'])
    dff = sort_df.reset_index(drop=True)
    html = dff.to_html()
    return HttpResponse(html)


def karma_count(request):
    df = scrap()
    dff = df[['Author', 'Karma']]
    html = dff.to_html()
    return HttpResponse(html)