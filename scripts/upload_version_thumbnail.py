import shotgun_api3

# sg = shotgun_api3.Shotgun("https://randymills.shotgrid.autodesk.com",
#                           login="randy.mills@me.com",
#                           password="MsfVHW!77DMzVeCzCr-P")

SERVER_PATH = "https://randymills.shotgrid.autodesk.com"
SCRIPT_NAME = 'upload_version_thumbnail'
SCRIPT_KEY = 'eiaykxukmmayvq$prfzfqsoE5'

sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_NAME, SCRIPT_KEY)

# upload thumbnail to Version (ex. ID 6990)
sg.upload_thumbnail("Version", 6990, "C:\\Users\\randy\\OneDrive\\Desktop\\randymills_rblwy_introtohoudinifx_wk01_01-02.png")