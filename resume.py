# -*- coding: utf-8 -*-

from datetime import date


class Person:

    FirstName = 'Vytautas'
    LastName = 'Butėnas'
    BirthDate = date(1982, 7, 7)
    BirthPlace = 'Rokiškis, Lithuania'
    Sex = 'Male'
    Occupation = 'Python developer'

    Education = [
        {
            'begin_year': 1982,
            'end_year': 2001,
            'type': 'School',
            'institution': 'Obeliai High School',
            'degree': 'High School diploma',
        },
        {
            'begin_year': 2002,
            'end_year': 2005,
            'type': 'College',
            'institution': 'Vilnius College in Higher Education',
            'degree': 'Computer programming',
        }
    ]

    Work_Experience = [
        {
            'begin': date(2005, 7, 7),
            'end': date(2007, 7, 15),
            'company': 'ASPA',
            'occupation': 'Engineer',
            'activities': [
                'POS systems support',
                'Electronic cash registers support',
                'Assembly of computers',
                'Software testing',
                'Software installation'
            ],
            'technologies': [
                'Visual FoxPro',
                'POS Systems',
                'Electronic cash registers'
            ]
        },
        {
            'begin': date(2007, 7, 16),
            'end': date(2010, 2, 19),
            'company': 'Vikarinos Technologijos',
            'occupation': 'Sofware developer',
            'activities': [
                'Development of HR systems',
                'Integration with external systems',
                'Report creation',
            ],
            'technologies': [
                'Delphi 7',
                'MS SQL Server',
                'Sybase SQL server',
                'RAVE reports',
            ]
        },
        {
            'begin': date(2010, 2, 20),
            'end': date(2010, 9, 12),
            'company': 'Sandas',
            'occupation': 'ERP System developer',
            'activities': [
                'Creation of OpenERP modules',
                'Integration with external systems',
                'Report creation',
            ],
            'technologies': [
                'Python',
                'OpenERP',
                'XML',
                'ReportLab',
            ]
        },
        {
            'begin': date(2010, 9, 13),
            'end': date(2011, 7, 25),
            'company': 'Self Employed',
            'occupation': 'Freelance developer',
            'activities': [
                'Web systems development',
                'Web systems support',
            ],
            'technologies': [
                'Python',
                'Django',
                'HTML',
                'CSS',
                'JavaScript',
                'JQuery',
                'Wordpress',
            ]
        },
        {
            'begin': date(2011, 7, 26),
            'end': None,
            'company': 'Idiles systems',
            'occupation': 'Web developer',
            'activities': [
                'Web systems development',
                'Web systems support',
            ],
            'technologies': [
                'Python',
                'Django',
                'Zope2',
                'HTML',
                'CSS',
                'JQuery'
            ]
        },
    ]

    Computer_Skills = {
        'Windows': 'Good',
        'Ubuntu Linux': 'Good',
        'Linux': 'Intermediate',
        'Python': 'Good',
        'Delphi': 'Intermediate',
        'Java': 'Basic',
        'Ruby': 'Basic',
        'HTML': 'Good',
        'JavaScript': 'Intermediate',
        'JQuery': 'Intermediate',
        'SQL': 'Basic',
        'Django': 'Good',
        'Computer Assembly': 'Intermediate',
        'Apache': 'Basic',
    }

    Social_Skills = {
        'Sense of humor': 'Sarcastic',
        'Communication': 'Sociable',
        'Team': 'Likes to be with people',
    }

    Contacts = {
        'Email': 'kroitus@gmailcom',
        'Phone': '+37065811744',
        'Address': '',
    }

    Languages = {
        'English': {'reading': 'good', 'speaking': 'intermediate'},
        'Russian': {'reading': 'perfect', 'speaking': 'good'}
    }

    Interests = {
        'Music': [
            'I like Electronic and Jazz music.',
            'I create electronic music and have performed live 2 times.',
            'I was a DJ in school.'
        ],
        'Movies': [
            'Science Fiction', 'Fantasy', 'Comedy', 'Animation'
        ],
        'Games': [
            'Heroes of Might and Magic', 'Civilization', 'Guitar Hero',
            'Rock Band', 'Batman: Arkham Asylum'
        ],
        'Books': [
            'G. Orwell: 1984', 'A. Huxley: Brave new world',
            'H. G. Wells: The Time Machine',
            'Various superhero related comics',
        ],
        'Other': [
            'I am a fan and user of Open Source software',
            'I am interested in Piracy and Copyright Industry actions',
            'I am participating in movement against E-voting',
        ]
    }

    Projects = {
        'parasykjiems.lt': 'Social project, where people can find their\
 representatives and write a letter to them. Participated in initial verson',
        'masinis.lt': 'Group discounts e-shop',
    }

    Links = {
        'webpage': 'http://www.kroitus.com',
        'twitter': 'http://twitter.com/kroitus',
        'linkedin': 'http://www.linkedin.com/pub/vytautas-butenas/1/865/4a9',
        'bitbucket': 'https://bitbucket.org/kroitus',
        'github': 'https://github.com/kroitus',
    }

    About = 'I am a geek. But that does not make me a bad person ;)'

    def __init__(self):
        print 'Hello,', self.FirstName, self.LastName
