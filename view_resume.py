# -*- coding: utf-8 -*-

from resume import Person

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
