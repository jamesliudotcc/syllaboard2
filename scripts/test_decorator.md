In [53]: r = requests.post('http://localhost:5000/auth/login', json={"email": "james@jamesliu.
    ...: cc", 'password':'password'})                                                         

In [54]: r.json()                                                                             
Out[54]: 
{'access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODc5Njg1MTIsIm5iZiI6MTU4Nzk2ODUxMiwianRpIjoiY2IxMDBkOGItMGE4My00MTYxLWE5ZGYtZjM4NTNlZjc2ZTc1IiwiZXhwIjoxNTg3OTY5NDEyLCJpZGVudGl0eSI6ImphbWVzQGphbWVzbGl1LmNjIiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.IATA_yWIVNLDRxm7-hjuDsXAoYUMK4QgcfnVZ0Ai0qQ',
 'status': 200}

In [55]: token = r.json()['access_token']                                                     

In [56]: token                                                                                
Out[56]: 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1ODc5Njg1MTIsIm5iZiI6MTU4Nzk2ODUxMiwianRpIjoiY2IxMDBkOGItMGE4My00MTYxLWE5ZGYtZjM4NTNlZjc2ZTc1IiwiZXhwIjoxNTg3OTY5NDEyLCJpZGVudGl0eSI6ImphbWVzQGphbWVzbGl1LmNjIiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.IATA_yWIVNLDRxm7-hjuDsXAoYUMK4QgcfnVZ0Ai0qQ'

In [57]: r = requests.get('http://localhost:5000/user/', headers={"Authorization": f"Bearer {t
    ...: oken}"})                                                                             

In [58]: r                                                                                    
Out[58]: <Response [200]>

In [59]: r.json()                                                                             
Out[59]: 
[{'email': 'james@jamesliu.cc',
  'first_name': 'James',
  'is_admin': True,
  'is_instructor': False,
  'last_name': 'liu'},
 {'email': 'echastenet0@google.fr',
  'first_name': 'Eduino',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Chastenet'},
 {'email': 'tbaudou1@ifeng.com',
  'first_name': 'Trudey',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Baudou'},
 {'email': 'faubrey2@lulu.com',
  'first_name': 'Filia',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Aubrey'},
 {'email': 'mextill3@shutterfly.com',
  'first_name': 'Meggi',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Extill'},
 {'email': 'pburston4@ca.gov',
  'first_name': 'Preston',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Burston'},
 {'email': 'imaides5@narod.ru',
  'first_name': 'Ingamar',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Maides'},
 {'email': 'eeadie6@shinystat.com',
  'first_name': 'Eduardo',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Eadie'},
 {'email': 'esaiz7@google.cn',
  'first_name': 'Ephrem',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Saiz'},
 {'email': 'cwace8@360.cn',
  'first_name': 'Cullin',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Wace'},
 {'email': 'ocaffery9@live.com',
  'first_name': 'Obediah',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Caffery'},
 {'email': 'ezellanda@360.cn',
  'first_name': 'Ermina',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Zelland'},
 {'email': 'spolgreenb@digg.com',
  'first_name': 'Selena',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Polgreen'},
 {'email': 'cspillmanc@marriott.com',
  'first_name': 'Chaddy',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Spillman'},
 {'email': 'shillittd@reuters.com',
  'first_name': 'Sigismund',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Hillitt'},
 {'email': 'audye@answers.com',
  'first_name': 'Ahmed',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Udy'},
 {'email': 'calmeyf@redcross.org',
  'first_name': 'Clint',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Almey'},
 {'email': 'cledinghamg@state.tx.us',
  'first_name': 'Clem',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Ledingham'},
 {'email': 'smassingberdh@patch.com',
  'first_name': 'Silvester',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Massingberd'},
 {'email': 'wgalvani@discovery.com',
  'first_name': 'Willard',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Galvan'},
 {'email': 'gcorneliusj@redcross.org',
  'first_name': 'Gualterio',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Cornelius'},
 {'email': 'dwodhamk@booking.com',
  'first_name': 'Doralyn',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Wodham'},
 {'email': 'cwinsletl@epa.gov',
  'first_name': 'Chane',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Winslet'},
 {'email': 'mcheekm@woothemes.com',
  'first_name': 'Malchy',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Cheek'},
 {'email': 'strimmingn@creativecommons.org',
  'first_name': 'Shae',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Trimming'},
 {'email': 'ezumbuscho@weather.com',
  'first_name': 'Evangeline',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Zumbusch'},
 {'email': 'lallixp@1und1.de',
  'first_name': 'Laverne',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Allix'},
 {'email': 'oeyreeq@addtoany.com',
  'first_name': 'Ode',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Eyree'},
 {'email': 'dknapmanr@businesswire.com',
  'first_name': 'Dev',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Knapman'},
 {'email': 'tsyddons@cdc.gov',
  'first_name': 'Tate',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Syddon'},
 {'email': 'hhouldt@blinklist.com',
  'first_name': 'Herman',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Hould'},
 {'email': 'amouldenu@state.gov',
  'first_name': 'Arther',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Moulden'},
 {'email': 'acurtisv@hexun.com',
  'first_name': 'Augusto',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Curtis'},
 {'email': 'dbrikw@eventbrite.com',
  'first_name': 'Dorothee',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Brik'},
 {'email': 'dfarninx@aboutads.info',
  'first_name': 'Drucill',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Farnin'},
 {'email': 'smcfetridgey@apache.org',
  'first_name': 'Stanton',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'McFetridge'},
 {'email': 'alippingwellz@netvibes.com',
  'first_name': 'Alix',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Lippingwell'},
 {'email': 'vsygroves10@gmpg.org',
  'first_name': 'Vi',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Sygroves'},
 {'email': 'tmalacrida11@oakley.com',
  'first_name': 'Tamra',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Malacrida'},
 {'email': 'mcopner12@dell.com',
  'first_name': 'Mohammed',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Copner'},
 {'email': 'gvear13@google.co.uk',
  'first_name': 'Gerry',
  'is_admin': False,
  'is_instructor': False,
  'last_name': 'Vear'}]

In [60]: r = requests.post('http://localhost:5000/auth/login', json={"email": "echastenet0@goo
    ...: gle.fr", 'password':'Euphorbiaceae'})                                                

In [61]: token = r.json()['access_token']                                                     

In [62]: r = requests.get('http://localhost:5000/user/', headers={"Authorization": f"Bearer {t
    ...: oken}"})                                                                             

In [63]: r.json()                                                                             
Out[63]: {'msg': 'Not admin'}
