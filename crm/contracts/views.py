from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def show_contracts(request: HttpRequest) -> HttpResponse:
    return render(request, "contracts/contracts-list.html")
