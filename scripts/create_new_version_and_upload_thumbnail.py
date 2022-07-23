import shotgun_api3

# sg = shotgun_api3.Shotgun("https://randymills.shotgrid.autodesk.com",
#                           login="randy.mills@me.com",
#                           password="MsfVHW!77DMzVeCzCr-P")

SERVER_PATH = "https://randymills.shotgrid.autodesk.com"
SCRIPT_NAME = 'create_new_version_and_upload_thumbnail'
SCRIPT_KEY = 'anqxhyhWryyda8ogvyg*hockd'

sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)

# find the shot
filters = [ ['project', 'is', {'type': 'Project', 'id': 122}],
            ['code', 'is', 'wk01-02'] ]
shot = sg.find_one('Shot', filters)

# find the task
filters = [ ['project', 'is', {'type': 'Project', 'id': 122}],
            ['entity', 'is',{'type':'Shot', 'id': shot['id']}],
            ['content', 'is', 'VFX'] ]
task = sg.find_one('Task', filters)

# find the user (if id unknown)
# filters = [['login', 'is', 'jschmoe']]
# user = sg.find('HumanUser', filters)

# create the version
data = { 'project': {'type': 'Project','id': 122},
         'code': 'wk01-02-02',
         'description': 'first pass at opening shot with bunnies',
         'sg_path_to_frames': 'C:\\Users\\randy\\OneDrive\\Desktop\\randymills_rblwy_introtohoudinifx_wk01_01-02.png',
         'sg_status_list': 'rev',
         'entity': {'type': 'Shot', 'id': shot['id']},
         'sg_task': {'type': 'Task', 'id': task['id']},
         'user': {'type': 'HumanUser', 'id': 88} }
result = sg.create('Version', data)

# upload thumbnail to Version (ex. ID 6990)
# sg.upload_thumbnail("Version", 6990, "C:\\Users\\randy\\OneDrive\\Desktop\\randymills_rblwy_introtohoudinifx_wk01_01-02.png")