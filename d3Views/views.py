from django.shortcuts import render


# Create your views here.
def indenttree(request):
    return render(request, 'indenttree/index.html')


def voronoi(request):
    return render(request, 'voronoi/index.html')


def circlepacking(request):
    return render(request, 'circlepacking/index.html')


def sunburst(request):
    return render(request, 'sunburst/index.html')


def bubble(request):
    return render(request, 'bubble/index.html')


def plane(request):
    return render(request, 'plane/index.html')


def sankey(request):
    return render(request, 'sankey/index.html')


def sankeychart(request):
    return render(request, 'sankeychart/index.html')
