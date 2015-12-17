import urllib, sys, xbmcplugin ,xbmcgui, xbmcaddon, xbmc, os, json, base64


addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = '[B]          Welcome to Project Cypher XXX[/B]'
line2 = '[B]THIS IS AN ADULT ADDON IF YOU ARE NOT OVER 18 PLEASE CLOSE THIS ADDON NOW, THANKS[/B]'
line3 = '         Project Cypher Streaming since 2012'

 
xbmcgui.Dialog().ok(addonname, line1, line2, line3)

plugin_handle = int(sys.argv[1])

_id = 'plugin.video.ProjectCypherxxx'
_icondir = "special://home/addons/" + _id + "/icons/"
_resources = "special://home/addons/" + _id + "/resources/"

fanart = "special://home/addons/" + _id + '/fanart.jpg'
icon = xbmc.translatePath(os.path.join('special://home/addons/' + _id, 'icon.png'))

def add_video_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=False)
	
def add_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'False')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=True)


# adult

add_video_item('http://repo.run/cypher/adult.m3u',{ 'title': 'Project Cypher Adult'}, '%s/adult.png'% _icondir)





xbmcplugin.endOfDirectory(int(sys.argv[1]))

xbmc.executebuiltin("Container.SetViewMode(500)")

