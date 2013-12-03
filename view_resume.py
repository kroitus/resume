# -*- coding: utf-8 -*-

from resume import Person
from jinja2 import Environment, PackageLoader

#print basic information on a person, which description is in resume.py
def to_console():
    person = Person()

    print '%(firstname)s %(lastname)s' % {
        'firstname':person.FirstName,
        'lastname':person.LastName
    }
    print 'Born on %(date)s in %(place)s' % {
        'date':person.BirthDate.strftime('%Y-%m-%d'),
        'place':person.BirthPlace
    }

    print 'Got education here:'
    for school in person.Education:
        print '%(begin)d - %(end)d: %(institution)s' % {
            'begin':school['begin_year'],
            'end':school['end_year'],
            'institution':school['institution']
        }

    print 'Worked here:'
    for job in person.Work_Experience:
        if job['end']:
            print '%(begin)s - %(end)s, in %(company)s' % {
                'begin':job['begin'].strftime('%Y-%m-%d'),
                'end':job['end'].strftime('%Y-%m-%d'),
                'company':job['company'],
            }
        else:
            print '%(begin)s - now, %(company)s' % {
                'begin':job['begin'].strftime('%Y-%m-%d'),
                'company':job['company'],
            }
        print 'Occupation: %(occupation)s' % {
            'occupation':job['occupation'],
        }
        print 'Was responsible for:'
        for activity in job['activities']:
            print ' ',activity

        print 'Technologies used:'
        for technology in job['technologies']:
            print '  ',technology

    print 'Computer skills:'
    skills = person.Computer_Skills.items()
    skills.sort()
    for skill, level in skills:
        print '  %(skill)s: %(level)s' % {'skill':skill, 'level':level}

    print 'Social skills:'
    skills = person.Social_Skills.items()
    skills.sort()
    for skill, level in skills:
        print '  %(skill)s: %(level)s' % {'skill':skill, 'level':level}

    print 'Languages:'
    skills = person.Languages.items()
    skills.sort()
    for language, level in skills:
        print '  %(language)s:' % {'language':language}
        levels = level.items()
        levels.sort()
        for skill, rate in levels:
            print '    %(skill)s: %(rate)s' % {'skill':skill,'rate':rate}

    print 'Interests:'
    interests = person.Interests.items()
    interests.sort()
    for area, interests in interests:
        print '  %(area)s:' % {'area':area}
        for interest in interests:
            print '   ', interest

    print 'Participated in projects:'
    projects = person.Projects.items()
    projects.sort()
    for project, description in skills:
        print '  %(project)s: %(description)s' % {
            'project':project,
            'description':description
        }

    print 'Online resources:'
    link = person.Links.items()
    link.sort()
    for resource, url in skills:
        print '  %(resource)s: %(url)s' % {
            'resource':resource,
            'url':url
        }

    print 'Something about me:\n  %s' % (person.About)

# Now I think of it... This parsing is not necessary, I should change structure of resume.py
def to_html(template='boring.html'):
    person = Person()
    parsed_person = {}

    parsed_person['firstname'] = person.FirstName
    parsed_person['lastname'] = person.LastName
    parsed_person['birthdate'] = person.BirthDate.strftime('%Y-%m-%d')
    parsed_person['birthplace'] = person.BirthPlace
    parsed_person['education'] = []

    for school in person.Education:
        institution = {}
        institution['begin'] = school['begin_year']
        institution['end'] = school['end_year']
        institution['institution'] = school['institution']
        parsed_person['education'].append(institution)

    parsed_person['work_experience'] = []
    for job in person.Work_Experience:
        work = {}
        work['begin'] = job['begin'].strftime('%Y-%m-%d')
        work['company'] = job['company']
        if job['end']:
            work['end'] = job['end'].strftime('%Y-%m-%d')
        else:
            work['end'] = 'now'

        work['occupation'] = job['occupation']
        work['activities'] = job['activities']
        work['technologies'] = job['technologies']
        parsed_person['work_experience'].append(work)

    parsed_person['computer_skills'] = []
    skills = person.Computer_Skills.items()
    skills.sort()
    for skill, level in skills:
        parsed_person['computer_skills'].append({
            'skill':skill,
            'level':level
        })

    parsed_person['social_skills'] = []
    skills = person.Social_Skills.items()
    skills.sort()
    for skill, level in skills:
        parsed_person['social_skills'].append({
            'skill':skill,
            'level':level
        })

    parsed_person['languages'] = []
    skills = person.Languages.items()
    skills.sort()
    for language, level in skills:
        lang = {}
        lang['language'] = language
        levels = level.items()
        levels.sort()
        lang['levels'] = []
        for skill, rate in levels:
            lang['levels'].append({'skill':skill,'rate':rate})
        parsed_person['languages'].append(lang)

    parsed_person['languages'] = []
    interests = person.Interests.items()
    interests.sort()
    for area, interests in interests:
        parsed_person['languages'].append({
            'area':area,
            'interests':interests
        })

    parsed_person['projects'] = []
    projects = person.Projects.items()
    projects.sort()
    for project, description in skills:
        parsed_person['projects'].append({
            'project':project,
            'description':description
        })

    parsed_person['links'] = []
    link = person.Links.items()
    link.sort()
    for resource, url in skills:
        parsed_person['links'].append({
            'resource':resource,
            'url':url
        })

    parsed_person['about'] = person.About

    env = Environment(loader=PackageLoader('resume', 'templates'))
    template = env.get_template(template)
    rendered = template.render(data=parsed_person)
    output_file = open('resume.html', 'w')
    output_file.write(rendered)
    output_file.close()
