# !/usr/bin/python
# -*- coding: utf-8 -*-
from invest.models import lof
def jsontoobjects1(list1):
    objects=[]
    for item in list1:
        object=lof(
        code=item[0],
        shortname = item[1],
        longname = item[2],
        lx = item[3],
        pyname = item[4],
        )
        objects.append(object)
    return objects