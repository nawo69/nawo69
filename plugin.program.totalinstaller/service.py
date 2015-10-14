import xbmc
import xbmcaddon
import os

#################################################
AddonID        = 'plugin.program.totalinstaller'
#################################################
ADDON          =  xbmcaddon.Addon(id=AddonID)
ADDONDATA      =  xbmc.translatePath('special://home/userdata/addon_data')
internetcheck  =  ADDON.getSetting('internetcheck')
cbnotifycheck  =  ADDON.getSetting('cbnotifycheck')
idfile         =  xbmc.translatePath(os.path.join(ADDONDATA,AddonID,'id.xml'))

print"##### Total Installer Update Service #####"

if not os.path.exists(idfile):
    localfile = open(idfile, mode='w+')
    localfile.write('id="None"\nname="None"')
    localfile.close()	

xbmc.executebuiltin('XBMC.RunScript(special://home/addons/'+AddonID+'/notify.py)')

if internetcheck == 'true':
    xbmc.executebuiltin('XBMC.AlarmClock(internetloop,XBMC.RunScript(special://home/addons/'+AddonID+'/connectivity.py,silent=true),00:00:30,silent,loop)')

if cbnotifycheck=='true':
    xbmc.executebuiltin('XBMC.AlarmClock(Notifyloop,XBMC.RunScript(special://home/addons/'+AddonID+'/notify.py,silent=true),00:30:00,silent,loop)')
