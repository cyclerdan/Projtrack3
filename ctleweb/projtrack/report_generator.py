from datetime import datetime

from .models import Project, Semester, User, Client, Department, Type

from django.core.exceptions import ObjectDoesNotExist

def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l) - i - 1):
            if l[j].date > l[j+1].date:
                tmp = l[j]
                l[j] = l[j+1]
                l[j+1] = tmp
    return l

def retrieve_most_recent_techcon(client):
    try:
        proj = list(Project.objects.filter(client=client))
        proj = bubble_sort(proj)
        return [proj.pop()]
    except TypeError:
        return [Project.objects.filter(client=client)]

def check_dates(s_d, e_d):
    try:
        result = list(Project.objects.all())
        ret = []
        if s_d != '':
            s_d = datetime.strptime(s_d, "%Y-%m-%d").date()
            for x in result:
                if x.date > s_d:
                    ret.append(x)
        if e_d != '':
            e_d = datetime.strptime(e_d, "%Y-%m-%d").date()
            for x in result:
                if x.date < e_d:
                    ret.append(x)
                elif x in ret:
                    ret.remove(x)
        if e_d == '' and s_d == '' and ret == []:
            return list(Project.objects.all())
        else:
            return ret
    except ObjectDoesNotExist:
        return []

def check_semester(sem):
    try:
        if sem != '':
            try:
                return list(Project.objects.filter(semester=sem))
            except TypeError:
                return [Project.objects.filter(semester=sem)]
        else:
            try:
                return list(Project.objects.all())
            except TypeError:
                return [Project.objects.all()]
    except ObjectDoesNotExist:
        return []

def check_user(use):
    try:
        if use != '':
            try:
                return list(Project.objects.filter(users=use))
            except TypeError:
                return [Project.objects.filter(users=use)]
        else:
            try:
                return list(Project.objects.all())
            except TypeError:
                return [Project.objects.all()]
    except ObjectDoesNotExist:
        return []

def check_client(cli):
    try:
        if cli != '':
            try:
                return list(Project.objects.filter(client=cli))
            except TypeError:
                return [Project.objects.filter(client=cli)]
        else:
            try:
                return list(Project.objects.all())
            except TypeError:
                return [Project.objects.all()]
    except ObjectDoesNotExist:
        return []

def check_department(depart):
    try:
        if depart != '':
            try:
                cli = Client.objects.filter(department=depart)
                return list(Project.objects.filter(client=cli))
            except TypeError:
                cli = Client.objects.filter(department=depart)
                return [Project.objects.filter(client=cli)]
        else:
            try:
                return list(Project.objects.all())
            except TypeError:
                return [Project.objects.all()]
    except ObjectDoesNotExist:
        return []

def check_type(proj):
    try:
        if proj != '':
            try:
                return list(Project.objects.filter(type=proj))
            except TypeError:
                return [Project.objects.filter(type=proj)]
        else:
            try:
                return list(Project.objects.all())
            except TypeError:
                return [Project.objects.all()]
    except ObjectDoesNotExist:
        return []

def generate_report(req):
    report = set(list(Project.objects.all()))
    rep = [
        (set(check_dates(req['start_date'], req['end_date']))),
        (set(check_semester(req['semester']))),
        (set(check_user(req['user']))),
        (set(check_department(req['department']))),
        (set(check_type(req['proj_type']))),
        (set(check_client(req['client'])))
        ]
    for x in rep:
        report = report & x
    if req['sort_by_date']:
        report = bubble_sort(list(report))
    return report
