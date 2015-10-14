import urllib , urllib2 , re , xbmcplugin , xbmcgui , xbmc , xbmcaddon
import os , sys , time , xbmcvfs , glob , shutil , datetime , zipfile , ntpath
import subprocess , threading
import yt , downloader , checkPath
import binascii
import hashlib
import speedtest
if 64 - 64: i11iIiiIii
try :
 from sqlite3 import dbapi2 as database
 if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
except :
 from pysqlite2 import dbapi2 as database
 if 73 - 73: II111iiii
from addon . common . addon import Addon
from addon . common . net import Net
if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
######################################################
I1IiI = 'plugin.program.totalinstaller'
o0OOO = 'The Community Portal'
if 13 - 13: ooOo + Oo
o0O = xbmcaddon . Addon ( id = I1IiI )
zip = o0O . getSetting ( 'zip' )
IiiIII111iI = o0O . getSetting ( 'localcopy' )
IiII = o0O . getSetting ( 'private' )
iI1Ii11111iIi = o0O . getSetting ( 'reseller' )
i1i1II = o0O . getSetting ( 'openelec' )
O0oo0OO0 = o0O . getSetting ( 'resellername' )
I1i1iiI1 = o0O . getSetting ( 'resellerid' )
iiIIIII1i1iI = o0O . getSetting ( 'favourites' )
o0oO0 = o0O . getSetting ( 'sources' )
oo00 = o0O . getSetting ( 'repositories' )
o00 = o0O . getSetting ( 'mastercopy' )
Oo0oO0ooo = o0O . getSetting ( 'username' ) . replace ( ' ' , '%20' )
o0oOoO00o = o0O . getSetting ( 'password' )
i1 = o0O . getSetting ( 'versionoverride' )
oOOoo00O0O = o0O . getSetting ( 'login' )
i1111 = o0O . getSetting ( 'addonportal' )
i11 = o0O . getSetting ( 'maintenance' )
I11 = o0O . getSetting ( 'hardwareportal' )
Oo0o0000o0o0 = o0O . getSetting ( 'maintenance' )
oOo0oooo00o = o0O . getSetting ( 'latestnews' )
oO0o0o0ooO0oO = o0O . getSetting ( 'tutorialportal' )
oo0o0O00 = o0O . getSetting ( 'startupvideo' )
oO = o0O . getSetting ( 'startupvideopath' )
i1iiIIiiI111 = o0O . getSetting ( 'wizardurl1' )
oooOOOOO = o0O . getSetting ( 'wizardname1' )
i1iiIII111ii = o0O . getSetting ( 'wizardurl2' )
i1iIIi1 = o0O . getSetting ( 'wizardname2' )
ii11iIi1I = o0O . getSetting ( 'wizardurl3' )
iI111I11I1I1 = o0O . getSetting ( 'wizardname3' )
OOooO0OOoo = o0O . getSetting ( 'wizardurl4' )
iIii1 = o0O . getSetting ( 'wizardname4' )
oOOoO0 = o0O . getSetting ( 'wizardurl5' )
O0OoO000O0OO = o0O . getSetting ( 'wizardname5' )
iiI1IiI = o0O . getSetting ( 'trcheck' )
II = xbmcgui . Dialog ( )
ooOoOoo0O = xbmcgui . DialogProgress ( )
OooO0 = xbmc . translatePath ( 'special://home/' )
II11iiii1Ii = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
OO0o = xbmc . translatePath ( os . path . join ( II11iiii1Ii , 'addon_data' ) )
Ooo = xbmc . translatePath ( os . path . join ( II11iiii1Ii , 'Database' ) )
O0o0Oo = xbmc . translatePath ( os . path . join ( II11iiii1Ii , 'Thumbnails' ) )
Oo00OOOOO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' , '' ) )
O0O = xbmc . translatePath ( os . path . join ( Oo00OOOOO , I1IiI , 'default.py' ) )
O00o0OO = xbmc . translatePath ( os . path . join ( Oo00OOOOO , I1IiI , 'fanart.jpg' ) )
I11i1 = xbmc . translatePath ( os . path . join ( Oo00OOOOO , I1IiI , 'resources' , 'addonxml' ) )
iIi1ii1I1 = xbmc . translatePath ( os . path . join ( II11iiii1Ii , 'guisettings.xml' ) )
o0 = xbmc . translatePath ( os . path . join ( II11iiii1Ii , 'guifix.xml' ) )
if 9 - 9: OO0oo0oOO + I1iii - IiiI11Iiiii / I1I1i / oOOOoo0O0OoO
ii1i1I1i = xbmc . translatePath ( os . path . join ( Oo00OOOOO , I1IiI , 'icon_menu.png' ) )
o00oOO0 = xbmc . translatePath ( os . path . join ( II11iiii1Ii , 'favourites.xml' ) )
oOoo = xbmc . translatePath ( os . path . join ( II11iiii1Ii , 'sources.xml' ) )
iIii11I = xbmc . translatePath ( os . path . join ( II11iiii1Ii , 'advancedsettings.xml' ) )
OOO0OOO00oo = xbmc . translatePath ( os . path . join ( II11iiii1Ii , 'profiles.xml' ) )
Iii111II = xbmc . translatePath ( os . path . join ( II11iiii1Ii , 'RssFeeds.xml' ) )
iiii11I = xbmc . translatePath ( os . path . join ( II11iiii1Ii , 'keymaps' , 'keyboard.xml' ) )
Ooo0OO0oOO = xbmc . translatePath ( os . path . join ( zip ) )
ii11i1 = xbmc . translatePath ( os . path . join ( Ooo0OO0oOO , 'Community Builds' , '' ) )
IIIii1II1II = xbmc . translatePath ( os . path . join ( OO0o , I1IiI , 'startup.xml' ) )
i1I1iI = xbmc . translatePath ( os . path . join ( OO0o , I1IiI , 'temp.xml' ) )
oo0OooOOo0 = xbmc . translatePath ( os . path . join ( OO0o , I1IiI , 'id.xml' ) )
o0OO00oO = xbmc . translatePath ( os . path . join ( Oo00OOOOO , 'repository.totalinstaller' ) )
I11i1I1I = xbmc . translatePath ( os . path . join ( Oo00OOOOO , 'repository.totalrevolution' ) )
oO0Oo = xbmc . translatePath ( os . path . join ( Oo00OOOOO , 'plugin.program.totalrevolution' ) )
oOOoo0Oo = xbmc . translatePath ( os . path . join ( OO0o , I1IiI , 'idtemp.xml' ) )
o00OO00OoO = xbmc . translatePath ( os . path . join ( OO0o , I1IiI , 'temp' ) )
OOOO0OOoO0O0 = xbmc . translatePath ( os . path . join ( Oo00OOOOO , I1IiI , 'resources/' ) )
O0Oo000ooO00 = xbmc . translatePath ( os . path . join ( Oo00OOOOO , I1IiI , 'default.py' ) )
oO0 = xbmc . getSkinDir ( )
Ii1iIiII1ii1 = xbmc . translatePath ( 'special://logpath/' )
ooOooo000oOO = '/storage/backup'
Oo0oOOo = '/storage/.restore/'
Oo0OoO00oOO0o = Net ( )
OOO00O = xbmc . translatePath ( os . path . join ( OO0o , I1IiI ) )
OOoOO0oo0ooO = xbmc . translatePath ( os . path . join ( OOO00O , 'guinew.xml' ) )
O0o0O00Oo0o0 = xbmc . translatePath ( os . path . join ( OOO00O , 'guitemp' , '' ) )
O00O0oOO00O00 = xbmc . translatePath ( os . path . join ( Ooo0OO0oOO , 'Database' ) )
i1Oo00 = os . path . join ( Oo00OOOOO , 'packages' )
i1i = os . path . join ( OooO0 , 'addontemp' )
iiI111I1iIiI = xbmc . translatePath ( os . path . join ( II11iiii1Ii , '.cbcfg' ) )
IIIi1I1IIii1II = 'http://urlshortbot.com/noobs'
O0ii1ii1ii = [ 'firstrun' , 'plugin.program.tbs' , 'plugin.program.totalinstaller' , 'script.module.addon.common' , 'addons' , 'addon_data' , 'userdata' , 'sources.xml' , 'favourites.xml' ]
oooooOoo0ooo = 0.0
I1I1IiI1 = 0.0
III1iII1I1ii = '0'
oOOo0 = [ '/storage/.kodi' , '/storage/.cache' , '/storage/.config' , '/storage/.ssh' ]
oo00O00oO = '1889903'
if 23 - 23: iIIi1i1 + O0 . OO0oo0oOO
if 82 - 82: I1ii11iIi11i - iIii1I11I1II1 / Oo + I1iii
if 87 - 87: ooOo * I1ii11iIi11i + Oo / iIii1I11I1II1 / IiiI11Iiiii
class I1111IIi ( xbmcgui . WindowXMLDialog ) :
 if 93 - 93: OoooooooOO / I1IiiI % i11iIiiIii + I1ii11iIi11i * OoO0O00
 def __init__ ( self , * args , ** kwargs ) :
  self . shut = kwargs [ 'close_time' ]
  xbmc . executebuiltin ( "Skin.Reset(AnimeWindowXMLDialogClose)" )
  xbmc . executebuiltin ( "Skin.SetBool(AnimeWindowXMLDialogClose)" )
  if 15 - 15: OO0oo0oOO . OoO0O00 / Oo0Ooo + OO0oo0oOO
 def onFocus ( self , controlID ) :
  pass
  if 78 - 78: O0 . ooOo . II111iiii % Oo
 def onClick ( self , controlID ) :
  if controlID == 12 :
   xbmc . Player ( ) . stop ( )
   self . _close_dialog ( )
   if 49 - 49: I1iii / OoO0O00 . II111iiii
 def onAction ( self , action ) :
  if action in [ 5 , 6 , 7 , 9 , 10 , 92 , 117 ] or action . getButtonCode ( ) in [ 275 , 257 , 261 ] :
   xbmc . Player ( ) . stop ( )
   self . _close_dialog ( )
   if 68 - 68: i11iIiiIii % I1ii11iIi11i + i11iIiiIii
 def _close_dialog ( self ) :
  xbmc . executebuiltin ( "Skin.Reset(AnimeWindowXMLDialogClose)" )
  time . sleep ( .4 )
  self . close ( )
  if 31 - 31: II111iiii . I1IiiI
  if 1 - 1: Oo0Ooo / o0oOOo0O0Ooo % IiiI11Iiiii * I1I1i . i11iIiiIii
def III1Iiii1I11 ( name , url , mode , iconimage , fanart , video , description , skins , guisettingslink , artpack ) :
 IIII = sys . argv [ 0 ]
 IIII += "?url=" + urllib . quote_plus ( url )
 IIII += "&mode=" + str ( mode )
 IIII += "&name=" + urllib . quote_plus ( name )
 IIII += "&iconimage=" + urllib . quote_plus ( iconimage )
 IIII += "&fanart=" + urllib . quote_plus ( fanart )
 IIII += "&video=" + urllib . quote_plus ( video )
 IIII += "&description=" + urllib . quote_plus ( description )
 IIII += "&skins=" + urllib . quote_plus ( skins )
 IIII += "&guisettingslink=" + urllib . quote_plus ( guisettingslink )
 IIII += "&artpack=" + urllib . quote_plus ( artpack )
 if 32 - 32: OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
 o00oooO0Oo = True
 o0O0OOO0Ooo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if 45 - 45: O0 / o0oOOo0O0Ooo
 o0O0OOO0Ooo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0O0OOO0Ooo . setProperty ( "Fanart_Image" , fanart )
 o0O0OOO0Ooo . setProperty ( "Build.Video" , video )
 if 32 - 32: IiiI11Iiiii . I1I1i . I1I1i
 if ( mode == None ) or ( mode == 'restore_option' ) or ( mode == 'backup_option' ) or ( mode == 'cb_root_menu' ) or ( mode == 'genres' ) or ( mode == 'grab_builds' ) or ( mode == 'community_menu' ) or ( mode == 'instructions' ) or ( mode == 'countries' ) or ( mode == 'update_build' ) or ( url == None ) or ( len ( url ) < 1 ) :
  if 62 - 62: I1ii11iIi11i + I1I1i % IiiI11Iiiii + Oo
  o00oooO0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IIII , listitem = o0O0OOO0Ooo , isFolder = True )
  if 33 - 33: O0 . I1I1i . I1IiiI
 else :
  o00oooO0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IIII , listitem = o0O0OOO0Ooo , isFolder = False )
  if 72 - 72: i1IIi / OoO0O00 + OoooooooOO - Oo0Ooo
 return o00oooO0Oo
 if 29 - 29: I1ii11iIi11i + ooOo % O0
 if 10 - 10: OO0oo0oOO / oOOOoo0O0OoO - I1IiiI * iIii1I11I1II1 - I1IiiI
def OO0oO0 ( handle , url , listitem , isFolder ) :
 xbmcplugin . addDirectoryItem ( handle , url , listitem , isFolder )
 if 82 - 82: OO0oo0oOO % o0oOOo0O0Ooo % OoO0O00 - Oo0Ooo + OoooooooOO
 if 22 - 22: i1IIi + O0 . iIii1I11I1II1 * IiiI11Iiiii % i11iIiiIii * I1IiiI
def oo000o ( name , url , mode , iconimage , fanart , buildname , author , version , description , updated , skins , videoaddons , audioaddons , programaddons , pictureaddons , sources , adult ) :
 if 44 - 44: i1IIi % II111iiii + OO0oo0oOO
 iconimage = ii1i1I1i
 if 45 - 45: IiiI11Iiiii / IiiI11Iiiii + oOOOoo0O0OoO + iIIi1i1
 IIII = sys . argv [ 0 ]
 IIII += "?url=" + urllib . quote_plus ( url )
 IIII += "&mode=" + str ( mode )
 IIII += "&name=" + urllib . quote_plus ( name )
 IIII += "&iconimage=" + urllib . quote_plus ( iconimage )
 IIII += "&fanart=" + urllib . quote_plus ( fanart )
 IIII += "&author=" + urllib . quote_plus ( author )
 IIII += "&description=" + urllib . quote_plus ( description )
 IIII += "&version=" + urllib . quote_plus ( version )
 IIII += "&buildname=" + urllib . quote_plus ( buildname )
 IIII += "&updated=" + urllib . quote_plus ( updated )
 IIII += "&skins=" + urllib . quote_plus ( skins )
 IIII += "&videoaddons=" + urllib . quote_plus ( videoaddons )
 IIII += "&audioaddons=" + urllib . quote_plus ( audioaddons )
 IIII += "&buildname=" + urllib . quote_plus ( buildname )
 IIII += "&programaddons=" + urllib . quote_plus ( programaddons )
 IIII += "&pictureaddons=" + urllib . quote_plus ( pictureaddons )
 IIII += "&sources=" + urllib . quote_plus ( sources )
 IIII += "&adult=" + urllib . quote_plus ( adult )
 if 47 - 47: o0oOOo0O0Ooo + iIIi1i1
 o00oooO0Oo = True
 o0O0OOO0Ooo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if 82 - 82: II111iiii . I1I1i - iIii1I11I1II1 - I1I1i * II111iiii
 o0O0OOO0Ooo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0O0OOO0Ooo . setProperty ( "Fanart_Image" , fanart )
 o0O0OOO0Ooo . setProperty ( "Build.Video" , ooO0oOOooOo0 )
 if 38 - 38: oOOOoo0O0OoO
 o00oooO0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = IIII , listitem = o0O0OOO0Ooo , isFolder = False )
 if 84 - 84: iIii1I11I1II1 % IiiI11Iiiii / iIii1I11I1II1 % OO0oo0oOO
 return o00oooO0Oo
 if 45 - 45: O0
def I1IiiiiI ( title , name , url , mode , iconimage = '' , fanart = '' , video = '' , description = '' , zip_link = '' , repo_link = '' , repo_id = '' , addon_id = '' , provider_name = '' , forum = '' , data_path = '' ) :
 if len ( iconimage ) > 0 :
  if 80 - 80: oOOOoo0O0OoO . i11iIiiIii - o0oOOo0O0Ooo
  iconimage = ii1i1I1i
 else :
  iconimage = 'DefaultFolder.png'
  if 25 - 25: OoO0O00
 if fanart == '' :
  fanart = O00o0OO
  if 62 - 62: Oo + O0
 IIII = sys . argv [ 0 ]
 IIII += "?url=" + urllib . quote_plus ( url )
 IIII += "&zip_link=" + urllib . quote_plus ( zip_link )
 IIII += "&repo_link=" + urllib . quote_plus ( repo_link )
 IIII += "&data_path=" + urllib . quote_plus ( data_path )
 IIII += "&provider_name=" + str ( provider_name )
 IIII += "&forum=" + str ( forum )
 IIII += "&repo_id=" + str ( repo_id )
 IIII += "&addon_id=" + str ( addon_id )
 IIII += "&mode=" + str ( mode )
 IIII += "&name=" + urllib . quote_plus ( name )
 IIII += "&fanart=" + urllib . quote_plus ( fanart )
 IIII += "&video=" + urllib . quote_plus ( video )
 IIII += "&description=" + urllib . quote_plus ( description )
 if 98 - 98: o0oOOo0O0Ooo
 o00oooO0Oo = True
 o0O0OOO0Ooo = xbmcgui . ListItem ( title , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if 51 - 51: Oo0Ooo - ooOo + II111iiii * I1iii . OO0oo0oOO + ooOo
 o0O0OOO0Ooo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0O0OOO0Ooo . setProperty ( "Fanart_Image" , fanart )
 o0O0OOO0Ooo . setProperty ( "Build.Video" , video )
 if 78 - 78: i11iIiiIii / IiiI11Iiiii - I1iii / Oo + ooOo
 OO0oO0 ( handle = int ( sys . argv [ 1 ] ) , url = IIII , listitem = o0O0OOO0Ooo , isFolder = False )
 if 82 - 82: I1iii
 if 46 - 46: OoooooooOO . i11iIiiIii
def OOo0oO00ooO00 ( type , name , url , mode , iconimage = '' , fanart = '' , video = '' , description = '' ) :
 if type != 'folder2' and type != 'addon' :
  if 90 - 90: OoOoOO00 * oOOOoo0O0OoO + o0oOOo0O0Ooo
  if 81 - 81: ooOo . o0oOOo0O0Ooo % O0 / I1IiiI - ooOo
  if 43 - 43: i11iIiiIii + Oo0Ooo * II111iiii * oOOOoo0O0OoO * O0
  if 64 - 64: Oo % iIii1I11I1II1 * ooOo
  if 79 - 79: O0
  if 78 - 78: I1ii11iIi11i + Oo - oOOOoo0O0OoO
  iconimage = ii1i1I1i
 if type == 'addon' :
  if 38 - 38: o0oOOo0O0Ooo - ooOo + iIii1I11I1II1 / OoOoOO00 % Oo0Ooo
  if len ( iconimage ) > 0 :
   iconimage = iconimage
  else :
   iconimage = 'DefaultFolder.png'
   if 57 - 57: OoO0O00 / iIIi1i1
   if 29 - 29: iIii1I11I1II1 + OoOoOO00 * OoO0O00 * Oo . I1IiiI * I1IiiI
   if 7 - 7: I1I1i * oOOOoo0O0OoO % I1iii - o0oOOo0O0Ooo
 if fanart == '' :
  fanart = O00o0OO
  if 13 - 13: I1iii . i11iIiiIii
 IIII = sys . argv [ 0 ]
 IIII += "?url=" + urllib . quote_plus ( url )
 IIII += "&mode=" + str ( mode )
 IIII += "&name=" + urllib . quote_plus ( name )
 IIII += "&fanart=" + urllib . quote_plus ( fanart )
 IIII += "&video=" + urllib . quote_plus ( video )
 IIII += "&description=" + urllib . quote_plus ( description )
 if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
 o00oooO0Oo = True
 o0O0OOO0Ooo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if 100 - 100: I1iii - O0 % ooOo * Oo + I1IiiI
 o0O0OOO0Ooo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0O0OOO0Ooo . setProperty ( "Fanart_Image" , fanart )
 o0O0OOO0Ooo . setProperty ( "Build.Video" , video )
 if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
 if ( type == 'folder' ) or ( type == 'folder2' ) or ( type == 'tutorial_folder' ) or ( type == 'news_folder' ) :
  o00oooO0Oo = OO0oO0 ( handle = int ( sys . argv [ 1 ] ) , url = IIII , listitem = o0O0OOO0Ooo , isFolder = True )
  if 33 - 33: oOOOoo0O0OoO + IiiI11Iiiii * ooOo / iIii1I11I1II1 - I1IiiI
 else :
  o00oooO0Oo = OO0oO0 ( handle = int ( sys . argv [ 1 ] ) , url = IIII , listitem = o0O0OOO0Ooo , isFolder = False )
  if 54 - 54: oOOOoo0O0OoO / Oo . ooOo % IiiI11Iiiii
 return o00oooO0Oo
 if 57 - 57: i11iIiiIii . I1ii11iIi11i - I1iii - ooOo + OoOoOO00
 if 63 - 63: OoOoOO00 * IiiI11Iiiii
def oo ( url ) :
 OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow][PLUGIN][/COLOR] Audio' , url + '&typex=audio' , 'grab_addons' , 'audio.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow][PLUGIN][/COLOR] Image (Picture)' , url + '&typex=image' , 'grab_addons' , 'pictures.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow][PLUGIN][/COLOR] Program' , url + '&typex=program' , 'grab_addons' , 'programs.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow][PLUGIN][/COLOR] Video' , url + '&typex=video' , 'grab_addons' , 'video.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=lime][SCRAPER][/COLOR] Movies (Used for library scanning)' , url + '&typex=movie%20scraper' , 'grab_addons' , 'movies.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=lime][SCRAPER][/COLOR] TV Shows (Used for library scanning)' , url + '&typex=tv%20show%20scraper' , 'grab_addons' , 'tvshows.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=lime][SCRAPER][/COLOR] Music Artists (Used for library scanning)' , url + '&typex=artist%20scraper' , 'grab_addons' , 'artists.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=lime][SCRAPER][/COLOR] Music Videos (Used for library scanning)' , url + '&typex=music%20video%20scraper' , 'grab_addons' , 'musicvideos.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=orange][SERVICE][/COLOR] All Services' , url + '&typex=service' , 'grab_addons' , 'services.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=orange][SERVICE][/COLOR] Weather Service' , url + '&typex=weather' , 'grab_addons' , 'weather.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Repositories' , url + '&typex=repository' , 'grab_addons' , 'repositories.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Scripts (Program Add-ons)' , url + '&typex=executable' , 'grab_addons' , 'scripts.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Screensavers' , url + '&typex=screensaver' , 'grab_addons' , 'screensaver.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Script Modules' , url + '&typex=script%20module' , 'grab_addons' , 'scriptmodules.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Skins' , url + '&typex=skin' , 'grab_addons' , 'skins.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Subtitles' , url + '&typex=subtitles' , 'grab_addons' , 'subtitles.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][OTHER][/COLOR] Web Interface' , url + '&typex=web%20interface' , 'grab_addons' , 'webinterface.png' , '' , '' , '' )
 if 44 - 44: ooOo / OO0oo0oOO / OO0oo0oOO
 if 87 - 87: Oo0Ooo . I1IiiI - II111iiii + O0 / Oo0Ooo / ooOo
def IiI ( ) :
 IIIii1I ( )
 xbmc . executebuiltin ( 'ActivateWindow(10040,"addons://outdated/",return)' )
 if 97 - 97: O0 + OoOoOO00
 if 89 - 89: o0oOOo0O0Ooo + OoO0O00 * OO0oo0oOO * I1iii
def iiIiI1i1 ( url ) :
 OOo0oO00ooO00 ( 'folder' , 'African' , url + '&genre=african' , 'grab_addons' , 'african.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Arabic' , url + '&genre=arabic' , 'grab_addons' , 'arabic.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Asian' , url + '&genre=asian' , 'grab_addons' , 'asian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Australian' , url + '&genre=australian' , 'grab_addons' , 'australian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Austrian' , url + '&genre=austrian' , 'grab_addons' , 'austrian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Belgian' , url + '&genre=belgian' , 'grab_addons' , 'belgian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Brazilian' , url + '&genre=brazilian' , 'grab_addons' , 'brazilian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Canadian' , url + '&genre=canadian' , 'grab_addons' , 'canadian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Chinese' , url + '&genre=chinese' , 'grab_addons' , 'chinese.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Colombian' , url + '&genre=columbian' , 'grab_addons' , 'columbian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Croatian' , url + '&genre=croatian' , 'grab_addons' , 'croatian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Czech' , url + '&genre=czech' , 'grab_addons' , 'czech.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Danish' , url + '&genre=danish' , 'grab_addons' , 'danish.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Dominican' , url + '&genre=dominican' , 'grab_addons' , 'dominican.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Dutch' , url + '&genre=dutch' , 'grab_addons' , 'dutch.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Egyptian' , url + '&genre=egyptian' , 'grab_addons' , 'egyptian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Filipino' , url + '&genre=filipino' , 'grab_addons' , 'filipino.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Finnish' , url + '&genre=finnish' , 'grab_addons' , 'finnish.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'French' , url + '&genre=french' , 'grab_addons' , 'french.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'German' , url + '&genre=german' , 'grab_addons' , 'german.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Greek' , url + '&genre=greek' , 'grab_addons' , 'greek.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Hebrew' , url + '&genre=hebrew' , 'grab_addons' , 'hebrew.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Hungarian' , url + '&genre=hungarian' , 'grab_addons' , 'hungarian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Icelandic' , url + '&genre=icelandic' , 'grab_addons' , 'icelandic.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Indian' , url + '&genre=indian' , 'grab_addons' , 'indian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Irish' , url + '&genre=irish' , 'grab_addons' , 'irish.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Italian' , url + '&genre=italian' , 'grab_addons' , 'italian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Japanese' , url + '&genre=japanese' , 'grab_addons' , 'japanese.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Korean' , url + '&genre=korean' , 'grab_addons' , 'korean.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Lebanese' , url + '&genre=lebanese' , 'grab_addons' , 'lebanese.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Mongolian' , url + '&genre=mongolian' , 'grab_addons' , 'mongolian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Moroccan' , url + '&genre=moroccan' , 'grab_addons' , 'moroccan.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Nepali' , url + '&genre=nepali' , 'grab_addons' , 'nepali.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'New Zealand' , url + '&genre=newzealand' , 'grab_addons' , 'newzealand.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Norwegian' , url + '&genre=norwegian' , 'grab_addons' , 'norwegian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Pakistani' , url + '&genre=pakistani' , 'grab_addons' , 'pakistani.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Polish' , url + '&genre=polish' , 'grab_addons' , 'polish.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Portuguese' , url + '&genre=portuguese' , 'grab_addons' , 'portuguese.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Romanian' , url + '&genre=romanian' , 'grab_addons' , 'romanian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Russian' , url + '&genre=russian' , 'grab_addons' , 'russian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Singapore' , url + '&genre=singapore' , 'grab_addons' , 'singapore.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Spanish' , url + '&genre=spanish' , 'grab_addons' , 'spanish.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Swedish' , url + '&genre=swedish' , 'grab_addons' , 'swedish.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Swiss' , url + '&genre=swiss' , 'grab_addons' , 'swiss.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Syrian' , url + '&genre=syrian' , 'grab_addons' , 'syrian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Tamil' , url + '&genre=tamil' , 'grab_addons' , 'tamil.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Thai' , url + '&genre=thai' , 'grab_addons' , 'thai.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Turkish' , url + '&genre=turkish' , 'grab_addons' , 'turkish.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'UK' , url + '&genre=uk' , 'grab_addons' , 'uk.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'USA' , url + '&genre=usa' , 'grab_addons' , 'usa.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Vietnamese' , url + '&genre=vietnamese' , 'grab_addons' , 'vietnamese.png' , '' , '' , '' )
 if 69 - 69: iIIi1i1
 if 40 - 40: oOOOoo0O0OoO + OoooooooOO % o0oOOo0O0Ooo - iIii1I11I1II1 . I1IiiI
def iIiIi11iI ( url ) :
 Oo0O00O000 = 'http://totalxbmc.com/TI/AddonPortal/addondetails.php?id=%s' % ( url )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 14 - 14: Oo / o0oOOo0O0Ooo
 iII11I1IiiIi = re . compile ( 'addon_types="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oo0oO = re . compile ( 'name="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Oo0O0 = re . compile ( 'UID="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Ooo0OOoOoO0 = re . compile ( 'id="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oOo0OOoO0 = re . compile ( 'provider_name="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IIo0Oo0oO0oOO00 = re . compile ( 'version="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oo00OO0000oO = re . compile ( 'created="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1II1 = re . compile ( 'addon_types="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oooO = re . compile ( 'updated="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i1I1i111Ii = re . compile ( 'downloads="(.+?)"' ) . findall ( i11I1IiII1i1i )
 if 67 - 67: I1IiiI . i1IIi
 i1i1iI1iiiI = re . compile ( 'description="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Ooo0oOooo0 = re . compile ( 'devbroke="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oOOOoo00 = re . compile ( 'broken="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiIiIIIiiI = re . compile ( 'deleted="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiI1IIIi = re . compile ( 'mainbranch_notes="(.+?)"' ) . findall ( i11I1IiII1i1i )
 if 47 - 47: Oo0Ooo % OO0oo0oOO % i11iIiiIii - O0 + iIIi1i1
 ooO000OO0O00O = re . compile ( 'repo_url="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OOOoOO0o = re . compile ( 'data_url="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i1II1 = re . compile ( 'zip_url="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i11i1 = re . compile ( 'genres="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IiiiiI1i1Iii = re . compile ( 'forum="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oo00oO0o = re . compile ( 'repo_id="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiii111II = re . compile ( 'license="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I11iIiI1I1i11 = re . compile ( 'platform="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OOoooO00o0oo0 = re . compile ( 'visible="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O00O = re . compile ( 'script="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1i11 = re . compile ( 'program_plugin="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IiIi1I1 = re . compile ( 'script_module="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IiIIi1 = re . compile ( 'video_plugin="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IIIIiii1IIii = re . compile ( 'audio_plugin="(.+?)"' ) . findall ( i11I1IiII1i1i )
 II1i11I = re . compile ( 'image_plugin="(.+?)"' ) . findall ( i11I1IiII1i1i )
 ii1I1IIii11 = re . compile ( 'repository="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O0o0oO = re . compile ( 'weather_service="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IIIIiIiIi1 = re . compile ( 'skin="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I11iiiiI1i = re . compile ( 'service="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iI1i11 = re . compile ( 'warning="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OoOOoooOO0O = re . compile ( 'web_interface="(.+?)"' ) . findall ( i11I1IiII1i1i )
 ooo00Ooo = re . compile ( 'movie_scraper="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Oo0o0O00 = re . compile ( 'tv_scraper="(.+?)"' ) . findall ( i11I1IiII1i1i )
 ii1 = re . compile ( 'artist_scraper="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1i11OO = re . compile ( 'music_video_scraper="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0O0oo0OO0O = re . compile ( 'subtitles="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OO0 = re . compile ( 'requires="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0Oooo = re . compile ( 'modules="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiI = re . compile ( 'icon="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oOIIiIi = re . compile ( 'video_preview="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OOoOooOoOOOoo = re . compile ( 'video_guide="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Iiii1iI1i = re . compile ( 'video_guide1="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1ii1ii11i1I = re . compile ( 'video_guide2="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0OoOO = re . compile ( 'video_guide3="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O0O0Oo00 = re . compile ( 'video_guide4="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oOoO00o = re . compile ( 'video_guide5="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oO00O0 = re . compile ( 'video_guide6="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IIi1IIIi = re . compile ( 'video_guide7="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O00Ooo = re . compile ( 'video_guide8="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OOOO0OOO = re . compile ( 'video_guide9="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i1i1ii = re . compile ( 'video_guide10="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iII1ii1 = re . compile ( 'video_label1="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1i1iiiI1 = re . compile ( 'video_label2="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iIIi = re . compile ( 'video_label3="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oO0o00oo0 = re . compile ( 'video_label4="(.+?)"' ) . findall ( i11I1IiII1i1i )
 ii1IIII = re . compile ( 'video_label5="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oO00oOooooo0 = re . compile ( 'video_label6="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oOo = re . compile ( 'video_label7="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O0OOooOoO = re . compile ( 'video_label8="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i1II1I1Iii1 = re . compile ( 'video_label9="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiI11Iii = re . compile ( 'video_label10="(.+?)"' ) . findall ( i11I1IiII1i1i )
 if 78 - 78: IiiI11Iiiii + OO0oo0oOO . iIIi1i1 - IiiI11Iiiii . I1iii
 if 30 - 30: I1IiiI + OoO0O00 % I1iii * IiiI11Iiiii / Oo0Ooo - OO0oo0oOO
 if 64 - 64: iIii1I11I1II1
 iI = iII11I1IiiIi [ 0 ] if ( len ( iII11I1IiiIi ) > 0 ) else ''
 I1ii1 = oo0oO [ 0 ] if ( len ( oo0oO ) > 0 ) else ''
 O00 = Oo0O0 [ 0 ] if ( len ( Oo0O0 ) > 0 ) else ''
 Oo0o0000OOoO = Ooo0OOoOoO0 [ 0 ] if ( len ( Ooo0OOoOoO0 ) > 0 ) else ''
 IiIi1I1ii111 = oOo0OOoO0 [ 0 ] if ( len ( oOo0OOoO0 ) > 0 ) else ''
 IiIiIi = IIo0Oo0oO0oOO00 [ 0 ] if ( len ( IIo0Oo0oO0oOO00 ) > 0 ) else ''
 IIIII1 = oo00OO0000oO [ 0 ] if ( len ( oo00OO0000oO ) > 0 ) else ''
 iIi1Ii1i1iI = I1II1 [ 0 ] if ( len ( I1II1 ) > 0 ) else ''
 IIiI1 = oooO [ 0 ] if ( len ( oooO ) > 0 ) else ''
 i1iI1 = i1I1i111Ii [ 0 ] if ( len ( i1I1i111Ii ) > 0 ) else ''
 if 1 - 1: i1IIi . i11iIiiIii % Oo
 OooO0oo = '[CR][CR][COLOR=dodgerblue]Description: [/COLOR]' + i1i1iI1iiiI [ 0 ] if ( len ( i1i1iI1iiiI ) > 0 ) else ''
 o0o0oOoOO0O = Ooo0oOooo0 [ 0 ] if ( len ( Ooo0oOooo0 ) > 0 ) else ''
 i1ii1II1ii = oOOOoo00 [ 0 ] if ( len ( oOOOoo00 ) > 0 ) else ''
 iII111Ii = '[CR]' + iiIiIIIiiI [ 0 ] if ( len ( iiIiIIIiiI ) > 0 ) else ''
 Ooo00OoOOO = '[CR][CR][COLOR=dodgerblue]User Notes: [/COLOR]' + iiI1IIIi [ 0 ] if ( len ( iiI1IIIi ) > 0 ) else ''
 if 98 - 98: iIii1I11I1II1 * I1ii11iIi11i * Oo + iIIi1i1 % i11iIiiIii % O0
 i1OO0oOOoo = ooO000OO0O00O [ 0 ] if ( len ( ooO000OO0O00O ) > 0 ) else ''
 oOOO00o000o = OOOoOO0o [ 0 ] if ( len ( OOOoOO0o ) > 0 ) else ''
 iIi11i1 = i1II1 [ 0 ] if ( len ( i1II1 ) > 0 ) else ''
 oO00oo0o00o0o = i11i1 [ 0 ] if ( len ( i11i1 ) > 0 ) else ''
 IiIIIIIi = '[CR][CR][COLOR=dodgerblue]Support Forum: [/COLOR]' + IiiiiI1i1Iii [ 0 ] if ( len ( IiiiiI1i1Iii ) > 0 ) else '[CR][CR][COLOR=dodgerblue]Support Forum: [/COLOR]No forum details given by developer'
 IiIi1iIIi1 = IiiiiI1i1Iii [ 0 ] if ( len ( IiiiiI1i1Iii ) > 0 ) else 'None'
 O0OoO0ooOO0o = oo00oO0o [ 0 ] if ( len ( oo00oO0o ) > 0 ) else ''
 license = iiii111II [ 0 ] if ( len ( iiii111II ) > 0 ) else ''
 OoOo0oOooOoOO = '[COLOR=orange]     Platform: [/COLOR]' + I11iIiI1I1i11 [ 0 ] if ( len ( I11iIiI1I1i11 ) > 0 ) else ''
 oo00ooOoO00 = OOoooO00o0oo0 [ 0 ] if ( len ( OOoooO00o0oo0 ) > 0 ) else ''
 o00oOoOo0 = O00O [ 0 ] if ( len ( O00O ) > 0 ) else ''
 o0O0O0ooo0oOO = I1i11 [ 0 ] if ( len ( I1i11 ) > 0 ) else ''
 oo000 = IiIi1I1 [ 0 ] if ( len ( IiIi1I1 ) > 0 ) else ''
 ii = IiIIi1 [ 0 ] if ( len ( IiIIi1 ) > 0 ) else ''
 OoO = IIIIiii1IIii [ 0 ] if ( len ( IIIIiii1IIii ) > 0 ) else ''
 Iiiiii111i1ii = II1i11I [ 0 ] if ( len ( II1i11I ) > 0 ) else ''
 i1i1iII1 = ii1I1IIii11 [ 0 ] if ( len ( ii1I1IIii11 ) > 0 ) else ''
 iii11i1IIII = I11iiiiI1i [ 0 ] if ( len ( I11iiiiI1i ) > 0 ) else ''
 oO0 = IIIIiIiIi1 [ 0 ] if ( len ( IIIIiIiIi1 ) > 0 ) else ''
 Ii = iI1i11 [ 0 ] if ( len ( iI1i11 ) > 0 ) else ''
 o00iiI1Ii1 = OoOOoooOO0O [ 0 ] if ( len ( OoOOoooOO0O ) > 0 ) else ''
 ii1i = O0o0oO [ 0 ] if ( len ( O0o0oO ) > 0 ) else ''
 oOOoo = ooo00Ooo [ 0 ] if ( len ( ooo00Ooo ) > 0 ) else ''
 iII1111III1I = Oo0o0O00 [ 0 ] if ( len ( Oo0o0O00 ) > 0 ) else ''
 ii11i = ii1 [ 0 ] if ( len ( ii1 ) > 0 ) else ''
 O00oOo00o0o = I1i11OO [ 0 ] if ( len ( I1i11OO ) > 0 ) else ''
 O00oO0 = o0O0oo0OO0O [ 0 ] if ( len ( o0O0oo0OO0O ) > 0 ) else ''
 O0Oo00OoOo = OO0 [ 0 ] if ( len ( OO0 ) > 0 ) else ''
 ii1ii111 = o0Oooo [ 0 ] if ( len ( o0Oooo ) > 0 ) else ''
 i11111I1I = iiI [ 0 ] if ( len ( iiI ) > 0 ) else ''
 ii1Oo0000oOo = oOIIiIi [ 0 ] if ( len ( oOIIiIi ) > 0 ) else 'None'
 I11o0oO00oO0o0o0 = OOoOooOoOOOoo [ 0 ] if ( len ( OOoOooOoOOOoo ) > 0 ) else 'None'
 I1I = Iiii1iI1i [ 0 ] if ( len ( Iiii1iI1i ) > 0 ) else 'None'
 ooooo = I1ii1ii11i1I [ 0 ] if ( len ( I1ii1ii11i1I ) > 0 ) else 'None'
 i11IIIiI1I = o0OoOO [ 0 ] if ( len ( o0OoOO ) > 0 ) else 'None'
 o0iiiI1I1iIIIi1 = O0O0Oo00 [ 0 ] if ( len ( O0O0Oo00 ) > 0 ) else 'None'
 Iii = oOoO00o [ 0 ] if ( len ( oOoO00o ) > 0 ) else 'None'
 I1iiiiI1iI = oO00O0 [ 0 ] if ( len ( oO00O0 ) > 0 ) else 'None'
 iIiiiii1i = IIi1IIIi [ 0 ] if ( len ( IIi1IIIi ) > 0 ) else 'None'
 iiIi1IIiI = O00Ooo [ 0 ] if ( len ( O00Ooo ) > 0 ) else 'None'
 i1oO0OO0 = OOOO0OOO [ 0 ] if ( len ( OOOO0OOO ) > 0 ) else 'None'
 o0O0Oo00 = i1i1ii [ 0 ] if ( len ( i1i1ii ) > 0 ) else 'None'
 O0Oo0o000oO = iII1ii1 [ 0 ] if ( len ( iII1ii1 ) > 0 ) else 'None'
 oO0o00oOOooO0 = I1i1iiiI1 [ 0 ] if ( len ( I1i1iiiI1 ) > 0 ) else 'None'
 OOOoO000 = iIIi [ 0 ] if ( len ( iIIi ) > 0 ) else 'None'
 oOOOO = oO0o00oo0 [ 0 ] if ( len ( oO0o00oo0 ) > 0 ) else 'None'
 IiIi1ii111i1 = ii1IIII [ 0 ] if ( len ( ii1IIII ) > 0 ) else 'None'
 i1i1i1I = oO00oOooooo0 [ 0 ] if ( len ( oO00oOooooo0 ) > 0 ) else 'None'
 oOoo000 = oOo [ 0 ] if ( len ( oOo ) > 0 ) else 'None'
 OooOo00o = O0OOooOoO [ 0 ] if ( len ( O0OOooOoO ) > 0 ) else 'None'
 IiI11i1IIiiI = i1II1I1Iii1 [ 0 ] if ( len ( i1II1I1Iii1 ) > 0 ) else 'None'
 oOOo000oOoO0 = iiI11Iii [ 0 ] if ( len ( iiI11Iii ) > 0 ) else 'None'
 if 86 - 86: II111iiii % i11iIiiIii + I1iii % i11iIiiIii
 if iII111Ii != '' :
  Ooo0o0OOO = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR][COLOR=red]This add-on is depreciated, it\'s no longer available.[/COLOR]'
  if 35 - 35: Oo + IiiI11Iiiii
 elif i1ii1II1ii == '' and o0o0oOoOO0O == '' and Ii == '' :
  Ooo0o0OOO = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR][COLOR=lime]No reported problems[/COLOR]'
  if 40 - 40: o0oOOo0O0Ooo
 elif i1ii1II1ii == '' and o0o0oOoOO0O == '' and Ii != '' and iII111Ii == '' :
  Ooo0o0OOO = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR][COLOR=orange]Although there have been no reported problems there may be issues with this add-on, see below.[/COLOR]'
  if 67 - 67: ooOo + II111iiii - O0 . ooOo * II111iiii * OO0oo0oOO
 elif i1ii1II1ii == '' and o0o0oOoOO0O != '' :
  Ooo0o0OOO = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR]Marked as broken by the add-on developer.[CR][COLOR=dodgerblue]Developer Comments: [/COLOR]' + o0o0oOoOO0O
  if 90 - 90: I1iii . I1I1i
 elif i1ii1II1ii != '' and o0o0oOoOO0O == '' :
  Ooo0o0OOO = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR]Marked as broken by a member of the community at [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR][CR][COLOR=dodgerblue]User Comments: [/COLOR]' + i1ii1II1ii
  if 81 - 81: Oo - OO0oo0oOO % iIIi1i1 - OoO0O00 / Oo0Ooo
 elif i1ii1II1ii != '' and o0o0oOoOO0O != '' :
  Ooo0o0OOO = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR]Marked as broken by both the add-on developer and a member of the community at [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR][CR][COLOR=dodgerblue]Developer Comments: [/COLOR]' + o0o0oOoOO0O + '[CR][COLOR=dodgerblue]User Comments: [/COLOR]' + i1ii1II1ii
  if 4 - 4: OoooooooOO - i1IIi % I1iii - Oo * o0oOOo0O0Ooo
  if 85 - 85: OoooooooOO * iIii1I11I1II1 . IiiI11Iiiii / OoooooooOO % I1IiiI % O0
 I1iiioO0o0O0Ooo0o = str ( '[COLOR=orange]Name: [/COLOR]' + I1ii1 + '[COLOR=orange]     Author(s): [/COLOR]' + IiIi1I1ii111 + '[COLOR=orange][CR][CR]Version: [/COLOR]' + IiIiIi + '[COLOR=orange]     Created: [/COLOR]' + IIIII1 + '[COLOR=orange]     Updated: [/COLOR]' + IIiI1 + '[COLOR=orange][CR][CR]Repository: [/COLOR]' + O0OoO0ooOO0o + OoOo0oOooOoOO + '[COLOR=orange]     Add-on Type(s): [/COLOR]' + iIi1Ii1i1iI + O0Oo00OoOo + Ooo0o0OOO + iII111Ii + Ii + IiIIIIIi + OooO0oo + Ooo00OoOOO )
 if 21 - 21: oOOOoo0O0OoO - I1IiiI + OO0oo0oOO
 if 78 - 78: OoooooooOO - i11iIiiIii - II111iiii
 if os . path . exists ( os . path . join ( Oo00OOOOO , Oo0o0000OOoO ) ) :
  if 'script.module' in Oo0o0000OOoO or 'repo' in Oo0o0000OOoO :
   OOo0oO00ooO00 ( '' , '[COLOR=orange]Already installed[/COLOR]' , '' , '' , i11111I1I , '' , '' , '' )
  else :
   OOo0oO00ooO00 ( '' , '[COLOR=orange]Already installed -[/COLOR] Click here to run the add-on' , Oo0o0000OOoO , 'run_addon' , i11111I1I , '' , '' , '' )
   if 77 - 77: OoOoOO00 % I1iii
   if 9 - 9: OoO0O00 - Oo0Ooo * OoooooooOO . Oo0Ooo
 if I1ii1 == '' :
  OOo0oO00ooO00 ( '' , '[COLOR=yellow]Sorry request failed due to high traffic on server, please try again[/COLOR]' , '' , '' , i11111I1I , '' , '' , '' )
  if 2 - 2: OoooooooOO % Oo
  if 63 - 63: I1IiiI % iIii1I11I1II1
 elif I1ii1 != '' :
  if 39 - 39: IiiI11Iiiii / II111iiii / I1ii11iIi11i % I1IiiI
  if ( i1ii1II1ii == '' ) and ( o0o0oOoOO0O == '' ) and ( iII111Ii == '' ) and ( Ii == '' ) :
   OOo0oO00ooO00 ( 'addon' , '[COLOR=yellow][FULL DETAILS][/COLOR] No problems reported' , I1iiioO0o0O0Ooo0o , 'text_guide' , i11111I1I , '' , '' , I1iiioO0o0O0Ooo0o )
   if 89 - 89: oOOOoo0O0OoO + OoooooooOO + oOOOoo0O0OoO * i1IIi + iIii1I11I1II1 % OO0oo0oOO
  if ( i1ii1II1ii != '' and iII111Ii == '' ) or ( o0o0oOoOO0O != '' and iII111Ii == '' ) or ( Ii != '' and iII111Ii == '' ) :
   OOo0oO00ooO00 ( 'addon' , '[COLOR=yellow][FULL DETAILS][/COLOR][COLOR=orange] Possbile problems reported[/COLOR]' , I1iiioO0o0O0Ooo0o , 'text_guide' , i11111I1I , '' , '' , I1iiioO0o0O0Ooo0o )
   if 59 - 59: Oo + i11iIiiIii
  if iII111Ii != '' :
   OOo0oO00ooO00 ( 'addon' , '[COLOR=yellow][FULL DETAILS][/COLOR][COLOR=red] Add-on now depreciated[/COLOR]' , I1iiioO0o0O0Ooo0o , 'text_guide' , i11111I1I , '' , '' , I1iiioO0o0O0Ooo0o )
   if 88 - 88: i11iIiiIii - iIIi1i1
   if 67 - 67: Oo . Oo0Ooo + OoOoOO00 - OoooooooOO
  if iII111Ii == '' :
   if 70 - 70: Oo / II111iiii - iIii1I11I1II1 - IiiI11Iiiii
   if O0OoO0ooOO0o != '' and 'superrepo' not in O0OoO0ooOO0o :
    I1IiiiiI ( '[COLOR=lime][INSTALL - Recommended] [/COLOR]' + I1ii1 , I1ii1 , '' , 'addon_install_zero' , 'Install.png' , '' , '' , OooO0oo , iI , i1OO0oOOoo , O0OoO0ooOO0o , Oo0o0000OOoO , IiIi1I1ii111 , IiIi1iIIi1 , oOOO00o000o )
    I1IiiiiI ( '[COLOR=lime][INSTALL - Backup Option] [/COLOR]' + I1ii1 , I1ii1 , '' , 'addon_install' , 'Install.png' , '' , '' , OooO0oo , iIi11i1 , i1OO0oOOoo , O0OoO0ooOO0o , Oo0o0000OOoO , IiIi1I1ii111 , IiIi1iIIi1 , oOOO00o000o )
    if 11 - 11: iIii1I11I1II1 . OoooooooOO . II111iiii / i1IIi - OO0oo0oOO
   if O0OoO0ooOO0o == '' or 'superrepo' in O0OoO0ooOO0o :
    I1IiiiiI ( '[COLOR=lime][INSTALL] [/COLOR]' + I1ii1 + ' - THIS IS NOT IN A SELF UPDATING REPO' , I1ii1 , '' , 'addon_install' , 'Install.png' , '' , '' , OooO0oo , iIi11i1 , i1OO0oOOoo , O0OoO0ooOO0o , Oo0o0000OOoO , IiIi1I1ii111 , IiIi1iIIi1 , oOOO00o000o )
    if 30 - 30: OoOoOO00
    if 21 - 21: i11iIiiIii / oOOOoo0O0OoO % Oo * O0 . OO0oo0oOO - iIii1I11I1II1
  if ii1Oo0000oOo != 'None' :
   OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  Preview' , I1I , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 26 - 26: II111iiii * OoOoOO00
  if I1I != 'None' :
   OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + O0Oo0o000oO , I1I , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 10 - 10: II111iiii . IiiI11Iiiii
  if ooooo != 'None' :
   OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + oO0o00oOOooO0 , ooooo , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 32 - 32: I1iii . I1I1i . OoooooooOO - OoO0O00 + ooOo
  if i11IIIiI1I != 'None' :
   OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + OOOoO000 , i11IIIiI1I , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 88 - 88: IiiI11Iiiii
  if o0iiiI1I1iIIIi1 != 'None' :
   OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + oOOOO , o0iiiI1I1iIIIi1 , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 19 - 19: II111iiii * I1I1i + I1iii
  if Iii != 'None' :
   OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + IiIi1ii111i1 , Iii , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 65 - 65: Oo . oOOOoo0O0OoO . OoO0O00 . IiiI11Iiiii - Oo
  if I1iiiiI1iI != 'None' :
   OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + i1i1i1I , I1iiiiI1iI , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 19 - 19: i11iIiiIii + IiiI11Iiiii % iIIi1i1
  if iIiiiii1i != 'None' :
   OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + oOoo000 , iIiiiii1i , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 14 - 14: OoO0O00 . II111iiii . OO0oo0oOO / I1iii % I1ii11iIi11i - iIIi1i1
  if iiIi1IIiI != 'None' :
   OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + OooOo00o , iiIi1IIiI , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 67 - 67: OO0oo0oOO - Oo . i1IIi
  if i1oO0OO0 != 'None' :
   OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + IiI11i1IIiiI , i1oO0OO0 , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 35 - 35: IiiI11Iiiii + iIIi1i1 - ooOo . IiiI11Iiiii . I1I1i
  if o0O0Oo00 != 'None' :
   OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + oOOo000oOoO0 , o0O0Oo00 , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 87 - 87: OoOoOO00
   if 25 - 25: i1IIi . OoO0O00 - OoOoOO00 / OoO0O00 % OoO0O00 * iIii1I11I1II1
def III ( url ) :
 OOo0oO00ooO00 ( 'folder' , 'Anime' , url + '&genre=anime' , 'grab_addons' , 'anime.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Audiobooks' , url + '&genre=audiobooks' , 'grab_addons' , 'audiobooks.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Comedy' , url + '&genre=comedy' , 'grab_addons' , 'comedy.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Comics' , url + '&genre=comics' , 'grab_addons' , 'comics.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Documentary' , url + '&genre=documentary' , 'grab_addons' , 'documentary.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Downloads' , url + '&genre=downloads' , 'grab_addons' , 'downloads.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Food' , url + '&genre=food' , 'grab_addons' , 'food.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Gaming' , url + '&genre=gaming' , 'grab_addons' , 'gaming.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Health' , url + '&genre=health' , 'grab_addons' , 'health.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'How To...' , url + '&genre=howto' , 'grab_addons' , 'howto.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Kids' , url + '&genre=kids' , 'grab_addons' , 'kids.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Live TV' , url + '&genre=livetv' , 'grab_addons' , 'livetv.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Movies' , url + '&genre=movies' , 'grab_addons' , 'movies.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Music' , url + '&genre=music' , 'grab_addons' , 'music.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'News' , url + '&genre=news' , 'grab_addons' , 'news.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Photos' , url + '&genre=photos' , 'grab_addons' , 'photos.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Podcasts' , url + '&genre=podcasts' , 'grab_addons' , 'podcasts.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Radio' , url + '&genre=radio' , 'grab_addons' , 'radio.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Religion' , url + '&genre=religion' , 'grab_addons' , 'religion.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Space' , url + '&genre=space' , 'grab_addons' , 'space.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Sports' , url + '&genre=sports' , 'grab_addons' , 'sports.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Technology' , url + '&genre=tech' , 'grab_addons' , 'tech.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Trailers' , url + '&genre=trailers' , 'grab_addons' , 'trailers.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'TV Shows' , url + '&genre=tv' , 'grab_addons' , 'tv.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Misc.' , url + '&genre=other' , 'grab_addons' , 'other.png' , '' , '' , '' )
 if 1 - 1: ooOo
 if o0O . getSetting ( 'adult' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , 'XXX' , url + '&genre=adult' , 'grab_addons' , 'adult.png' , '' , '' , '' )
  if 62 - 62: i1IIi - Oo
  if 96 - 96: i1IIi . I1ii11iIi11i + ooOo
def Ii1iI11iI1 ( name , zip_link , repo_link , repo_id , addon_id , provider_name , forum , data_path ) :
 forum = str ( forum )
 repo_id = str ( repo_id )
 i11I1II = 1
 OO0OOO0oOOo00O = 1
 OO0oIII111i11IiI = 1
 O0000 = xbmc . translatePath ( os . path . join ( Oo00OOOOO , addon_id ) )
 if 64 - 64: II111iiii - I1IiiI
 if os . path . exists ( O0000 ) :
  O0O0ooOOO = 1
  if 67 - 67: IiiI11Iiiii % IiiI11Iiiii / IiiI11Iiiii
 else :
  O0O0ooOOO = 0
  if 53 - 53: iIii1I11I1II1
 oooo00o0o0o = xbmc . translatePath ( os . path . join ( i1Oo00 , name + '.zip' ) )
 O0Oo00oO0O00 = xbmc . translatePath ( os . path . join ( Oo00OOOOO , addon_id ) )
 if 32 - 32: II111iiii . I1iii - IiiI11Iiiii * oOOOoo0O0OoO
 ooOoOoo0O . create ( "Installing Addon" , "Please wait whilst your addon is installed" , '' , '' )
 if 71 - 71: o0oOOo0O0Ooo % I1iii - II111iiii * OoooooooOO
 try :
  downloader . download ( repo_link , oooo00o0o0o , ooOoOoo0O )
  oOOO ( oooo00o0o0o , Oo00OOOOO , ooOoOoo0O )
  if 56 - 56: I1ii11iIi11i
 except :
  if 26 - 26: OoooooooOO % OoooooooOO
  try :
   downloader . download ( zip_link , oooo00o0o0o , ooOoOoo0O )
   oOOO ( oooo00o0o0o , Oo00OOOOO , ooOoOoo0O )
   if 33 - 33: oOOOoo0O0OoO
  except :
   if 62 - 62: I1ii11iIi11i + I1iii + i1IIi / OoooooooOO
   try :
    if not os . path . exists ( O0Oo00oO0O00 ) :
     os . makedirs ( O0Oo00oO0O00 )
     if 7 - 7: o0oOOo0O0Ooo + i1IIi . I1IiiI / Oo0Ooo
    i11I1IiII1i1i = ooI1111i ( data_path ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
    I111i1I1 = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( i11I1IiII1i1i )
    if 62 - 62: Oo * oOOOoo0O0OoO / Oo0Ooo * o0oOOo0O0Ooo
    for II1Ii1iI1i1 in I111i1I1 :
     o0OoO000O = xbmc . translatePath ( os . path . join ( O0Oo00oO0O00 , II1Ii1iI1i1 ) )
     if 94 - 94: OoOoOO00 . O0 / I1iii . I1ii11iIi11i - i1IIi
     if addon_id not in II1Ii1iI1i1 and '/' not in II1Ii1iI1i1 :
      if 26 - 26: OoO0O00 - Oo . o0oOOo0O0Ooo
      try :
       ooOoOoo0O . update ( 0 , "Downloading [COLOR=yellow]" + II1Ii1iI1i1 + '[/COLOR]' , '' , 'Please wait...' )
       downloader . download ( data_path + II1Ii1iI1i1 , o0OoO000O , ooOoOoo0O )
       if 65 - 65: I1ii11iIi11i % O0 % iIii1I11I1II1 * I1iii
      except :
       print "failed to install" + II1Ii1iI1i1
       if 31 - 31: I1iii
     if '/' in II1Ii1iI1i1 and '..' not in II1Ii1iI1i1 and 'http' not in II1Ii1iI1i1 :
      iIIiI1I1i = data_path + II1Ii1iI1i1
      O0O0OOooOO0 ( o0OoO000O , iIIiI1I1i )
      if 31 - 31: I1IiiI * ooOo + OoooooooOO - IiiI11Iiiii / OoooooooOO
   except :
    II . ok ( "Error downloading add-on" , 'There was an error downloading [COLOR=yellow]' + name , '[/COLOR]Please consider updating the add-on portal with details or report the error on the forum at [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR]' )
    i11I1II = 0
    if 19 - 19: I1I1i * iIIi1i1 * o0oOOo0O0Ooo + O0 / O0
 if i11I1II == 1 :
  time . sleep ( 1 )
  ooOoOoo0O . update ( 0 , "[COLOR=yellow]" + name + '[/COLOR]  [COLOR=lime]Successfully Installed[/COLOR]' , '' , 'Now installing repository' )
  time . sleep ( 1 )
  ooOoO = xbmc . translatePath ( os . path . join ( Oo00OOOOO , repo_id ) )
  if 91 - 91: ooOo + I1IiiI
  if ( repo_id != 'repository.xbmc.org' ) and not ( os . path . exists ( ooOoO ) ) and ( repo_id != '' ) and ( 'superrepo' not in repo_id ) :
   OoOooo ( repo_id )
   if 74 - 74: iIii1I11I1II1 * I1I1i % OoOoOO00
  xbmc . sleep ( 2000 )
  if 36 - 36: OoooooooOO - ooOo
  if os . path . exists ( O0000 ) and O0O0ooOOO == 0 :
   OOo = 'http://totalxbmc.com/TI/AddonPortal/downloadcount.php?id=%s' % ( addon_id )
   ooI1111i ( OOo )
   if 89 - 89: O0
  IIIII1I1Ii11iI ( name , addon_id )
  xbmc . executebuiltin ( 'UpdateLocalAddons' )
  xbmc . sleep ( 1000 )
  xbmc . executebuiltin ( 'UpdateAddonRepos' )
  if 52 - 52: Oo - IiiI11Iiiii * ooOo
  if OO0OOO0oOOo00O == 0 :
   II . ok ( name + " Install Complete" , 'The add-on has been successfully installed but' , 'there was an error installing the repository.' , 'This will mean the add-on fails to update' )
   if 17 - 17: OoooooooOO + Oo * OO0oo0oOO * OoOoOO00
  if OO0oIII111i11IiI == 0 :
   II . ok ( name + " Install Complete" , 'The add-on has been successfully installed but' , 'there was an error installing modules.' , 'This could result in errors with the add-on.' )
   if 36 - 36: O0 + Oo0Ooo
  if OO0oIII111i11IiI != 0 and OO0OOO0oOOo00O != 0 and forum != 'None' :
   II . ok ( name + " Install Complete" , 'Please support the developer(s) [COLOR=dodgerblue]' + provider_name , '[/COLOR]Support for this add-on can be found at [COLOR=yellow]' + forum , '[/COLOR][CR]Visit [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR] for all your Kodi needs.' )
   if 5 - 5: Oo0Ooo * OoOoOO00
  if OO0oIII111i11IiI != 0 and OO0OOO0oOOo00O != 0 and forum == 'None' :
   II . ok ( name + " Install Complete" , 'Please support the developer(s) [COLOR=dodgerblue]' + provider_name , '[/COLOR]No details of forum support have been given.' )
   if 46 - 46: iIIi1i1
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 33 - 33: IiiI11Iiiii - II111iiii * OoooooooOO - Oo0Ooo - Oo
 if 84 - 84: oOOOoo0O0OoO + Oo0Ooo - OoOoOO00 * OoOoOO00
def OoooO0o ( name , contenttypes , repo_link , repo_id , addon_id , provider_name , forum , data_path ) :
 O0000 = xbmc . translatePath ( os . path . join ( Oo00OOOOO , addon_id ) )
 forum = str ( forum )
 if 24 - 24: OoOoOO00 % i1IIi + IiiI11Iiiii . i11iIiiIii . I1ii11iIi11i
 if not os . path . exists ( O0000 ) :
  IIi1II = 1
  if 2 - 2: II111iiii - OoO0O00 . I1I1i * IiiI11Iiiii / ooOo
 else :
  IIi1II = 0
  if 80 - 80: Oo / OO0oo0oOO / OoOoOO00 + i1IIi - Oo0Ooo
 repo_id = str ( repo_id )
 ooOoO = xbmc . translatePath ( os . path . join ( Oo00OOOOO , repo_id ) )
 if 11 - 11: o0oOOo0O0Ooo * OoO0O00
 if os . path . exists ( O0000 ) :
  O0O0ooOOO = 1
  iIi1IiI = II . yesno ( 'Add-on Already Installed' , 'This add-on has already been detected on your system. Would you like to remove the old version and re-install? There should be no need for this unless you\'ve manually opened up the add-on code and edited in a text editor.' )
  if 14 - 14: I1I1i % ooOo % Oo0Ooo - i11iIiiIii
  if iIi1IiI == 1 :
   o0OO000ooOo ( O0000 )
   IIi1II = 1
 else :
  O0O0ooOOO = 0
  if 86 - 86: OoO0O00 * OoooooooOO
 if IIi1II == 1 :
  if 71 - 71: iIii1I11I1II1 - Oo . I1IiiI % OoooooooOO + Oo
  if ( repo_id != 'repository.xbmc.org' ) and not ( os . path . exists ( ooOoO ) ) and ( repo_id != '' ) and ( 'superrepo' not in repo_id ) :
   OoOooo ( repo_id )
   if 26 - 26: Oo0Ooo + Oo / OoO0O00 % OoOoOO00 % I1ii11iIi11i + II111iiii
  if not os . path . exists ( O0000 ) :
   os . makedirs ( O0000 )
   if 31 - 31: OO0oo0oOO % Oo * OO0oo0oOO
  IiII1i1iii1Ii = os . path . join ( Oo00OOOOO , addon_id , 'addon.xml' )
  iIO0O00OOo = os . path . join ( Oo00OOOOO , addon_id , 'default.py' )
  if 66 - 66: i11iIiiIii / o0oOOo0O0Ooo - OoooooooOO / i1IIi . i11iIiiIii
  shutil . copyfile ( I11i1 , IiII1i1iii1Ii )
  if 16 - 16: Oo0Ooo % I1ii11iIi11i + OO0oo0oOO - O0 . IiiI11Iiiii / oOOOoo0O0OoO
  IIi1I = open ( os . path . join ( IiII1i1iii1Ii ) , mode = 'r' )
  iii = IIi1I . read ( )
  IIi1I . close ( )
  if 95 - 95: I1I1i * I1ii11iIi11i % iIIi1i1 % I1iii - I1iii
  if 97 - 97: I1ii11iIi11i + iIii1I11I1II1 . O0
  Ooo0Oo0oo0 = re . compile ( 'testid[\s\S]*?' ) . findall ( iii )
  Ooo0OOoOoO0 = Ooo0Oo0oo0 [ 0 ] if ( len ( Ooo0Oo0oo0 ) > 0 ) else 'None'
  oOO0o000Oo00o = re . compile ( 'testname[\s\S]*?' ) . findall ( iii )
  oo0oO = oOO0o000Oo00o [ 0 ] if ( len ( oOO0o000Oo00o ) > 0 ) else 'None'
  iii11II1I = re . compile ( 'testprovider[\s\S]*?' ) . findall ( iii )
  iI111I11i = iii11II1I [ 0 ] if ( len ( iii11II1I ) > 0 ) else 'None'
  I1 = re . compile ( 'testprovides[\s\S]*?' ) . findall ( iii )
  II1i11I1 = I1 [ 0 ] if ( len ( I1 ) > 0 ) else 'None'
  iiIiIiII = iii . replace ( Ooo0OOoOoO0 , addon_id ) . replace ( oo0oO , name ) . replace ( iI111I11i , provider_name ) . replace ( II1i11I1 , contenttypes )
  if 37 - 37: OO0oo0oOO / I1I1i + II111iiii
  iiiiiIIi = open ( IiII1i1iii1Ii , mode = 'w+' )
  iiiiiIIi . write ( str ( iiIiIiII ) )
  iiiiiIIi . close ( )
  if 96 - 96: IiiI11Iiiii
  i1I11iIII1i1I = open ( iIO0O00OOo , mode = 'w' )
  i1I11iIII1i1I . write ( 'import xbmcplugin,xbmcgui,xbmc,xbmcaddon,os,sys\nAddonID="' + addon_id + '"\nAddonName="' + name + '"\ndialog=xbmcgui.Dialog()\nxbmc.executebuiltin("UpdateLocalAddons")\nxbmc.executebuiltin("UpdateAddonRepos")\nchoice=dialog.yesno(AddonName+" Add-on Requires Update","This add-on may still be in the process of the updating, would you like check the status of your add-on updates or try re-installing via the Total Installer backup method? We highly recommend checking for updates.",yeslabel="Install Option 2", nolabel="Check Updates")\nif choice==0: xbmc.executebuiltin(\'ActivateWindow(10040,"addons://outdated/",return)\')\nelse: xbmc.executebuiltin(\'ActivateWindow(10001,"plugin://plugin.program.tbs/?mode=grab_addons&url=%26redirect%26addonid%3d\'+AddonID+\'")\')\nxbmcplugin.endOfDirectory(int(sys.argv[1]))' )
  i1I11iIII1i1I . close ( )
  if 63 - 63: Oo0Ooo + oOOOoo0O0OoO - II111iiii
  xbmc . sleep ( 1000 )
  if 2 - 2: I1I1i
  if os . path . exists ( O0000 ) and O0O0ooOOO == 0 :
   OOo = 'http://totalxbmc.com/TI/AddonPortal/downloadcount.php?id=%s' % ( addon_id )
   ooI1111i ( OOo )
   if 97 - 97: ooOo - OoooooooOO
  xbmc . executebuiltin ( 'UpdateLocalAddons' )
  xbmc . executebuiltin ( 'UpdateAddonRepos' )
  II . ok ( name + " Install Complete" , '[COLOR=dodgerblue]' + name + '[/COLOR] has now been installed, please allow a few moments for Kodi to update the add-on and it\'s dependencies.' )
  if 79 - 79: OoOoOO00 % I1I1i % Oo0Ooo
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 29 - 29: OoooooooOO . I1IiiI % I1ii11iIi11i - IiiI11Iiiii
 if 8 - 8: i1IIi
def iIiI1 ( name , contenttypes , repo_link , repo_id , addon_id , provider_name , forum , data_path ) :
 ooOoO = xbmc . translatePath ( os . path . join ( Oo00OOOOO , repo_id ) )
 O0000 = xbmc . translatePath ( os . path . join ( Oo00OOOOO , addon_id ) )
 if 37 - 37: OoO0O00 * i11iIiiIii / Oo % oOOOoo0O0OoO
 if os . path . exists ( O0000 ) :
  if 71 - 71: OoooooooOO
  iIi1IiI = II . yesno ( 'Add-on Already Installed' , 'This add-on has already been detected on your system. Would you like to remove the old version and re-install? There should be no need for this unless you\'ve manually opened up the add-on code and edited in a text editor.' )
  if 11 - 11: I1I1i
  if iIi1IiI == 1 :
   o0OO000ooOo ( O0000 )
   if 55 - 55: Oo0Ooo
 if os . path . exists ( ooOoO ) :
  if 77 - 77: II111iiii
  if os . path . exists ( O0000 ) :
   O0O0ooOOO = 1
   if 16 - 16: I1IiiI * II111iiii / iIii1I11I1II1 - IiiI11Iiiii
  else :
   O0O0ooOOO = 0
   if 3 - 3: I1IiiI * iIIi1i1 + II111iiii - OoO0O00
  iIi1IiI = II . yesno ( 'WARNING!' , '[COLOR=orange]This Add-on may be unlawful in your region.[/COLOR][CR]The repository required for installation of this add-on has been detected on your system. Would you like to continue to the Kodi addon browser to install?' )
  if 97 - 97: I1ii11iIi11i / ooOo - o0oOOo0O0Ooo - I1IiiI - I1IiiI
  if iIi1IiI == 1 :
   if 54 - 54: Oo0Ooo + I1IiiI / IiiI11Iiiii . I1IiiI * OoOoOO00
   if 'video' in contenttypes :
    xbmc . executebuiltin ( 'ActivateWindow(10040,"addons://' + repo_id + '/xbmc.addon.video/?",return)' )
    if 1 - 1: OoOoOO00 * OoO0O00 . i1IIi / Oo0Ooo . I1ii11iIi11i + Oo0Ooo
   elif 'executable' in contenttypes :
    xbmc . executebuiltin ( 'ActivateWindow(10040,"addons://' + repo_id + '/xbmc.addon.executable/?",return)' )
    if 17 - 17: Oo0Ooo + OoO0O00 / I1iii / IiiI11Iiiii * Oo
   elif 'audio' in contenttypes :
    xbmc . executebuiltin ( 'ActivateWindow(10040,"addons://' + repo_id + '/xbmc.addon.audio/?",return)' )
    if 29 - 29: OoO0O00 % OoooooooOO * ooOo / II111iiii - ooOo
  xbmc . sleep ( 2000 )
  if 19 - 19: i11iIiiIii
  if os . path . exists ( O0000 ) and O0O0ooOOO == 0 :
   OOo = 'http://totalxbmc.com/TI/AddonPortal/downloadcount.php?id=%s' % ( addon_id )
   ooI1111i ( OOo )
   if 54 - 54: II111iiii . OO0oo0oOO
 else :
  II . ok ( 'WARNING!' , '[COLOR=orange]This add-on may possibly be unlawful in your region.[/COLOR][CR]If you\'ve investigated the legality of it and are happy to install then you must have the following repository installed: [COLOR=dodgerblue]' + repo_id + '[/COLOR]' )
  if 73 - 73: OoOoOO00 . I1IiiI
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 32 - 32: OoOoOO00 * I1IiiI % iIIi1i1 * I1iii . O0
 if 48 - 48: IiiI11Iiiii * IiiI11Iiiii
def I1I1 ( name , contenttypes , repo_link , repo_id , addon_id , provider_name , forum , data_path ) :
 II . ok ( 'Add-on Not Approved' , 'Sorry there are no repository details for this add-on and it\'s been marked as potentially giving access to unlawful content. The most likely cause for this is the add-on has only been released via social media groups.' )
 if 4 - 4: o0oOOo0O0Ooo % OoOoOO00 * Oo
 if 32 - 32: i11iIiiIii - oOOOoo0O0OoO
def oo00ooOoo ( ) :
 OOo0oO00ooO00 ( '' , o0OOO + ' Storage Folder Check' , 'url' , 'check_storage' , 'Check_Download.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Completely remove an add-on (inc. passwords)' , 'plugin' , 'addon_removal_menu' , 'Remove_Addon.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Make Add-ons Gotham/Helix Compatible' , 'none' , 'gotham' , 'Gotham_Compatible.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Make Skins Kodi (Helix) Compatible' , 'none' , 'helix' , 'Kodi_Compatible.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Hide my add-on passwords' , 'none' , 'hide_passwords' , 'Hide_Passwords.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'OnTapp.TV / OSS Integration' , 'none' , 'addonfix' , 'Addon_Fixes.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Test My Download Speed' , 'none' , 'speedtest_menu' , 'Speed_Test.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Unhide my add-on passwords' , 'none' , 'unhide_passwords' , 'Unhide_Passwords.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Update My Add-ons (Force Refresh)' , 'none' , 'update' , 'Update_Addons.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Wipe All Add-on Settings (addon_data)' , 'url' , 'remove_addon_data' , 'Delete_Addon_Data.png' , '' , '' , '' )
 if 28 - 28: I1iii
 if 1 - 1: I1iii
def IiiiI1 ( sign ) :
 OOo0oO00ooO00 ( '' , '[COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] Keyword Install' , IIIi1I1IIii1II , 'keywords' , 'Keywords.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=darkcyan][Manual Search][/COLOR] Search By Name' , 'pass=' + sign + '&name=' , 'search_addons' , 'Search_Addons.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=darkcyan][Manual Search][/COLOR] Search By Author' , 'pass=' + sign + '&author=' , 'search_addons' , 'Search_Addons.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=darkcyan][Manual Search][/COLOR] Search In Description' , 'pass=' + sign + '&desc=' , 'search_addons' , 'Search_Addons.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=darkcyan][Manual Search][/COLOR] Search By Add-on ID' , 'pass=' + sign + '&addonid=' , 'search_addons' , 'Search_Addons.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][Filter Results][/COLOR] By Genres' , 'pass=' + sign , 'addon_genres' , 'Search_Genre.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][Filter Results][/COLOR] By Countries' , 'pass=' + sign , 'addon_countries' , 'Search_Country.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][Filter Results][/COLOR] By Kodi Categories' , 'pass=' + sign , 'addon_categories' , 'Search_Category.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=orange][Kodi Add-on Browser][/COLOR] Install From Zip' , '' , 'install_from_zip' , 'Search_Addons.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=orange][Kodi Add-on Browser][/COLOR] Browse My Repositories' , '' , 'browse_repos' , 'Search_Addons.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=orange][Kodi Add-on Browser][/COLOR] Check For Add-on Updates' , '' , 'check_updates' , 'Search_Addons.png' , '' , '' , '' )
 if 100 - 100: ooOo . I1iii % i1IIi . iIIi1i1
 if 79 - 79: OoO0O00 % Oo / iIii1I11I1II1 + OoOoOO00 * OoO0O00
 if 30 - 30: OoooooooOO / OO0oo0oOO + IiiI11Iiiii / I1ii11iIi11i * O0
 if 16 - 16: Oo0Ooo / i11iIiiIii
def oo00IIIIIIIiI ( ) :
 for file in glob . glob ( os . path . join ( Oo00OOOOO , '*' ) ) :
  I1ii1 = str ( file ) . replace ( Oo00OOOOO , '[COLOR=red]REMOVE [/COLOR]' ) . replace ( 'plugin.' , '[COLOR=dodgerblue](PLUGIN) [/COLOR]' ) . replace ( 'audio.' , '' ) . replace ( 'video.' , '' ) . replace ( 'skin.' , '[COLOR=yellow](SKIN) [/COLOR]' ) . replace ( 'repository.' , '[COLOR=orange](REPOSITORY) [/COLOR]' ) . replace ( 'script.' , '[COLOR=cyan](SCRIPT) [/COLOR]' ) . replace ( 'metadata.' , '[COLOR=orange](METADATA) [/COLOR]' ) . replace ( 'service.' , '[COLOR=pink](SERVICE) [/COLOR]' ) . replace ( 'weather.' , '[COLOR=green](WEATHER) [/COLOR]' ) . replace ( 'module.' , '[COLOR=orange](MODULE) [/COLOR]' )
  I1IIiI = ( os . path . join ( file , 'icon.png' ) )
  O0oOOo0o = ( os . path . join ( file , 'fanart.jpg' ) )
  OOo0oO00ooO00 ( '' , I1ii1 , file , 'remove_addons' , I1IIiI , O0oOOo0o , '' , '' )
  if 50 - 50: IiiI11Iiiii . I1ii11iIi11i . OoO0O00 * OO0oo0oOO + II111iiii % i11iIiiIii
  if 8 - 8: iIIi1i1 * O0
def OOoO ( ) :
 o0O . openSettings ( sys . argv [ 0 ] )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 18 - 18: iIii1I11I1II1 + Oo0Ooo - Oo + OoooooooOO * OoooooooOO
 if 41 - 41: iIIi1i1 . Oo0Ooo + I1IiiI
def o0O0OO ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 Ii1II11II1iii = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 o0oOO0ooOoO = len ( sourcefile )
 ooO0000o00O = [ ]
 O0Ooo = [ ]
 if 78 - 78: OoO0O00 % I1I1i * i1IIi
 ooOoOoo0O . create ( message_header , message1 , message2 , message3 )
 if 66 - 66: I1iii . I1IiiI + o0oOOo0O0Ooo . iIii1I11I1II1
 for o0iIiiIiiIi , i1iiIIIi , Oo0o in os . walk ( sourcefile ) :
  if 93 - 93: Oo
  for file in Oo0o :
   O0Ooo . append ( file )
   if 43 - 43: I1ii11iIi11i / I1IiiI . iIIi1i1
 Ooo0oO0 = len ( O0Ooo )
 if 86 - 86: O0
 for o0iIiiIiiIi , i1iiIIIi , Oo0o in os . walk ( sourcefile ) :
  if 95 - 95: IiiI11Iiiii * Oo . OoOoOO00 . i1IIi . i1IIi - o0oOOo0O0Ooo
  i1iiIIIi [ : ] = [ ii1iIIiii1 for ii1iIIiii1 in i1iiIIIi if ii1iIIiii1 not in exclude_dirs ]
  Oo0o [ : ] = [ ooOo0O0o0 for ooOo0O0o0 in Oo0o if ooOo0O0o0 not in exclude_files and not 'crashlog' in ooOo0O0o0 and not 'stacktrace' in ooOo0O0o0 ]
  if 65 - 65: iIIi1i1 + O0
  for file in Oo0o :
   if 32 - 32: OoooooooOO - OoOoOO00 - i11iIiiIii * o0oOOo0O0Ooo / Oo0Ooo + OoooooooOO
   try :
    ooO0000o00O . append ( file )
    ii1I1I111 = len ( ooO0000o00O ) / float ( Ooo0oO0 ) * 100
    ooOoOoo0O . update ( 0 , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % ii1iIIiii1 , 'Please Wait' )
    Ii1Ii = os . path . join ( o0iIiiIiiIi , file )
    if 39 - 39: ooOo - i1IIi / iIIi1i1 . I1IiiI * i1IIi - iIii1I11I1II1
   except :
    print "Unable to backup file: " + file
    if 55 - 55: I1IiiI * o0oOOo0O0Ooo % iIIi1i1 . iIii1I11I1II1 * oOOOoo0O0OoO
   if not 'temp' in i1iiIIIi :
    if 92 - 92: oOOOoo0O0OoO - iIii1I11I1II1
    if not I1IiI in i1iiIIIi :
     if 32 - 32: I1iii % OoO0O00 * OoO0O00 + I1I1i * II111iiii * I1iii
     try :
      iIiIii1I1II = '01/01/1980'
      O0Oooo = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( Ii1Ii ) ) )
      if 77 - 77: II111iiii
      if O0Oooo > iIiIii1I1II :
       Ii1II11II1iii . write ( Ii1Ii , Ii1Ii [ o0oOO0ooOoO : ] )
       if 42 - 42: I1iii * oOOOoo0O0OoO . I1I1i * I1IiiI + OoOoOO00
     except :
      print "Unable to backup file: " + file
      if 25 - 25: OO0oo0oOO . I1IiiI + ooOo
 Ii1II11II1iii . close ( )
 ooOoOoo0O . close ( )
 if 75 - 75: I1I1i - o0oOOo0O0Ooo % IiiI11Iiiii + i11iIiiIii
 if 100 - 100: OO0oo0oOO + o0oOOo0O0Ooo - i11iIiiIii - II111iiii
def iIIIiIi1I1i ( sourcefile , destfile ) :
 Ii1II11II1iii = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 o0oOO0ooOoO = len ( sourcefile )
 ooO0000o00O = [ ]
 O0Ooo = [ ]
 if 78 - 78: iIii1I11I1II1 % OoOoOO00 + I1ii11iIi11i / i1IIi % II111iiii + Oo
 ooOoOoo0O . create ( "Backing Up Files" , "Archiving..." , '' , 'Please Wait' )
 if 91 - 91: iIii1I11I1II1 % OoO0O00 . o0oOOo0O0Ooo + I1iii + o0oOOo0O0Ooo
 for o0iIiiIiiIi , i1iiIIIi , Oo0o in os . walk ( sourcefile ) :
  if 95 - 95: I1iii + I1ii11iIi11i * Oo
  for file in Oo0o :
   O0Ooo . append ( file )
   if 16 - 16: OO0oo0oOO / I1IiiI + OoO0O00 % iIii1I11I1II1 - i1IIi . ooOo
 Ooo0oO0 = len ( O0Ooo )
 if 26 - 26: o0oOOo0O0Ooo * I1I1i . i1IIi
 for o0iIiiIiiIi , i1iiIIIi , Oo0o in os . walk ( sourcefile ) :
  if 59 - 59: O0 + i1IIi - o0oOOo0O0Ooo
  for file in Oo0o :
   ooO0000o00O . append ( file )
   ii1I1I111 = len ( ooO0000o00O ) / float ( Ooo0oO0 ) * 100
   ooOoOoo0O . update ( int ( ii1I1I111 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   Ii1Ii = os . path . join ( o0iIiiIiiIi , file )
   if 62 - 62: i11iIiiIii % Oo . I1I1i . Oo
   if not 'temp' in i1iiIIIi :
    if 84 - 84: i11iIiiIii * OoO0O00
    if not I1IiI in i1iiIIIi :
     if 18 - 18: Oo - I1iii - OoOoOO00 / oOOOoo0O0OoO - O0
     import time
     iIiIii1I1II = '01/01/1980'
     O0Oooo = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( Ii1Ii ) ) )
     if 30 - 30: O0 + I1ii11iIi11i + II111iiii
     if O0Oooo > iIiIii1I1II :
      Ii1II11II1iii . write ( Ii1Ii , Ii1Ii [ o0oOO0ooOoO : ] )
 Ii1II11II1iii . close ( )
 ooOoOoo0O . close ( )
 if 14 - 14: o0oOOo0O0Ooo / Oo - iIii1I11I1II1 - ooOo % iIIi1i1
 if 49 - 49: iIIi1i1 * ooOo / o0oOOo0O0Ooo / Oo0Ooo * iIii1I11I1II1
def OOoO00ooO ( ) :
 OOo0oO00ooO00 ( '' , 'Create My Own [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] Community Build' , 'url' , 'community_backup' , 'Backup.png' , '' , '' , 'Back Up Your Full System' )
 if I1IIIIiii1i ( ) :
  OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue]Create OpenELEC Backup[/COLOR] (full backup can only be used on OpenELEC)' , 'none' , 'openelec_backup' , 'Backup.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue]Create My Own Universal Build[/COLOR] (For copying to other devices)' , 'none' , 'community_backup_2' , 'Backup.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue]Create My Own Full Backup[/COLOR] (will only work on THIS device)' , 'local' , 'local_backup' , 'Backup.png' , '' , '' , 'Back Up Your Full System' )
 OOo0oO00ooO00 ( '' , 'Backup Addons Only' , 'addons' , 'restore_zip' , 'Backup.png' , '' , '' , 'Back Up Your Addons' )
 OOo0oO00ooO00 ( '' , 'Backup Addon Data Only' , 'addon_data' , 'restore_zip' , 'Backup.png' , '' , '' , 'Back Up Your Addon Userdata' )
 OOo0oO00ooO00 ( '' , 'Backup Guisettings.xml' , iIi1ii1I1 , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your guisettings.xml' )
 if 51 - 51: Oo . I1IiiI
 if os . path . exists ( o00oOO0 ) :
  OOo0oO00ooO00 ( '' , 'Backup Favourites.xml' , o00oOO0 , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your favourites.xml' )
  if 73 - 73: OoooooooOO . I1IiiI / oOOOoo0O0OoO % I1iii
 if os . path . exists ( oOoo ) :
  OOo0oO00ooO00 ( '' , 'Backup Source.xml' , oOoo , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your sources.xml' )
  if 65 - 65: I1I1i - I1IiiI - I1iii
 if os . path . exists ( iIii11I ) :
  OOo0oO00ooO00 ( '' , 'Backup Advancedsettings.xml' , iIii11I , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your advancedsettings.xml' )
  if 42 - 42: II111iiii * I1IiiI % i1IIi - I1iii % I1I1i
 if os . path . exists ( iiii11I ) :
  OOo0oO00ooO00 ( '' , 'Backup Advancedsettings.xml' , iiii11I , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your keyboard.xml' )
  if 36 - 36: i11iIiiIii / ooOo * I1ii11iIi11i * I1ii11iIi11i + I1iii * OO0oo0oOO
 if os . path . exists ( Iii111II ) :
  OOo0oO00ooO00 ( '' , 'Backup RssFeeds.xml' , Iii111II , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your RssFeeds.xml' )
  if 32 - 32: OoO0O00
  if 50 - 50: iIIi1i1 + i1IIi
def i11IiIIi11I ( ) :
 OOo0oO00ooO00 ( 'folder' , 'Backup My Content' , 'none' , 'backup_option' , 'Backup.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Restore My Content' , 'none' , 'restore_option' , 'Restore.png' , '' , '' , '' )
 if 78 - 78: I1I1i
 if 83 - 83: iIii1I11I1II1 % OoOoOO00 % o0oOOo0O0Ooo % oOOOoo0O0OoO . I1ii11iIi11i % O0
def iIiIi1ii ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(10040,"addons://repos/",return)' )
 if 28 - 28: iIii1I11I1II1 + iIii1I11I1II1
 if 28 - 28: ooOo
def ooo0oo ( localbuildcheck , localversioncheck , id , welcometext ) :
 if ( Oo0oO0ooo . replace ( '%20' , ' ' ) in welcometext ) and ( 'elc' in welcometext ) :
  OOo0oO00ooO00 ( '' , welcometext , 'show' , 'user_info' , 'noobsandnerds.png' , '' , '' , '' )
  if 8 - 8: OoO0O00 + OoOoOO00 . iIii1I11I1II1 % O0
  if id != 'None' :
   if 43 - 43: I1ii11iIi11i - IiiI11Iiiii
   if id != 'Local' :
    O000O = Oo00OO0 ( localbuildcheck , localversioncheck , id )
    if 72 - 72: i1IIi / ooOo * oOOOoo0O0OoO
    if O000O == True :
     if 40 - 40: I1iii - OoOoOO00 * OoOoOO00 . OoOoOO00 + OoooooooOO
     if not 'Partially installed' in localbuildcheck :
      OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]' + localbuildcheck + ':[/COLOR] [COLOR=lime]NEW VERSION AVAILABLE[/COLOR]' , id , 'showinfo' , 'noobsandnerds.png' , '' , '' , '' )
      if 77 - 77: iIii1I11I1II1 . I1iii % ooOo / I1iii
     if '(Partially installed)' in localbuildcheck :
      OOo0oO00ooO00 ( 'folder' , '[COLOR=lime]Current Build Installed: [/COLOR][COLOR=dodgerblue]' + localbuildcheck + '[/COLOR]' , id , 'showinfo2' , 'noobsandnerds.png' , '' , '' , '' )
    else :
     OOo0oO00ooO00 ( 'folder' , '[COLOR=lime]Current Build Installed: [/COLOR][COLOR=dodgerblue]' + localbuildcheck + '[/COLOR]' , id , 'showinfo' , 'noobsandnerds.png' , '' , '' , '' )
     if 54 - 54: ooOo + iIIi1i1 - Oo0Ooo
   else :
    if 35 - 35: I1iii - I1iii + i1IIi - O0 - oOOOoo0O0OoO
    if localbuildcheck == 'Incomplete' :
     OOo0oO00ooO00 ( '' , '[COLOR=lime]Your last restore is not yet completed[/COLOR]' , 'url' , oOO0o0oo0 ( ) , 'noobsandnerds.png' , '' , '' , '' )
     if 78 - 78: Oo + IiiI11Iiiii . I1I1i
    else :
     OOo0oO00ooO00 ( '' , '[COLOR=lime]Current Build Installed: [/COLOR][COLOR=dodgerblue]Local Build (' + localbuildcheck + ')[/COLOR]' , 'noobsandnerds.png' , '' , '' , '' , '' , '' )
  OOo0oO00ooO00 ( '' , '[COLOR=orange]---------------------------------------[/COLOR]' , 'None' , '' , 'noobsandnerds.png' , '' , '' , '' )
  if 91 - 91: iIii1I11I1II1 . o0oOOo0O0Ooo . I1ii11iIi11i + OoooooooOO
 if Oo0oO0ooo != '' and o0oOoO00o != '' and not 'elc' in welcometext :
  OOo0oO00ooO00 ( '' , '[COLOR=lime]Unable to login, please check your details[/COLOR]' , 'None' , 'addon_settings' , 'noobsandnerds.png' , '' , '' , '' )
  if 69 - 69: oOOOoo0O0OoO - I1IiiI
 if not 'elc' in welcometext :
  OOo0oO00ooO00 ( '' , welcometext , 'None' , 'register' , 'noobsandnerds.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=yellow]Settings[/COLOR]' , 'settings' , 'addon_settings' , 'SETTINGS.png' , '' , '' , '' )
 if 95 - 95: I1IiiI * i11iIiiIii . iIIi1i1
 if i1111 == 'true' :
  OOo0oO00ooO00 ( 'folder' , 'Add-on Portal' , oo00O00oO , 'addonmenu' , 'Search_Addons.png' , '' , '' , '' )
  if 41 - 41: II111iiii
 if i11 == 'true' :
  OOo0oO00ooO00 ( 'folder' , 'Community Builds' , welcometext , 'community' , 'Community_Builds.png' , '' , '' , '' )
  if 37 - 37: OO0oo0oOO . Oo0Ooo % I1I1i * i1IIi
 if I11 == 'true' :
  OOo0oO00ooO00 ( 'folder' , 'Hardware Reviews' , 'none' , 'hardware_root_menu' , 'hardware.png' , '' , '' , '' )
  if 71 - 71: Oo0Ooo / o0oOOo0O0Ooo + Oo
 if oOo0oooo00o == 'true' :
  OOo0oO00ooO00 ( 'folder' , 'Latest News' , 'none' , 'news_root_menu' , 'LatestNews.png' , '' , '' , '' )
  if 48 - 48: oOOOoo0O0OoO + IiiI11Iiiii
 if oO0o0o0ooO0oO == 'true' :
  OOo0oO00ooO00 ( 'folder' , 'Tutorials' , '' , 'tutorial_root_menu' , 'Tutorials.png' , '' , '' , '' )
  if 16 - 16: iIii1I11I1II1 % i11iIiiIii . OoOoOO00 % iIIi1i1 + ooOo . OoO0O00
 if Oo0o0000o0o0 == 'true' :
  OOo0oO00ooO00 ( 'folder' , 'Maintenance' , 'none' , 'tools' , 'Additional_Tools.png' , '' , '' , '' )
  if 46 - 46: OoO0O00 - o0oOOo0O0Ooo / OoOoOO00 - OoooooooOO + ooOo
  if 58 - 58: o0oOOo0O0Ooo / o0oOOo0O0Ooo + iIIi1i1 + OO0oo0oOO - OoOoOO00 . Oo
def I11Ii1iI11iI1 ( ) :
 i1III1 = 'defaultskindependecycheck'
 if os . path . exists ( i1i ) :
  shutil . rmtree ( i1i )
  if 43 - 43: II111iiii % oOOOoo0O0OoO . OO0oo0oOO % O0 - OoooooooOO + O0
 if not os . path . exists ( i1i ) :
  os . makedirs ( i1i )
  if 100 - 100: II111iiii - o0oOOo0O0Ooo . II111iiii * II111iiii . I1I1i
  if 2 - 2: OoooooooOO
  if 60 - 60: OoO0O00
 if oO0 != 'skin.confluence' :
  oO00Ooo0oO = os . path . join ( Oo00OOOOO , oO0 , 'addon.xml' )
  OOOo = open ( oO00Ooo0oO , mode = 'r' )
  o0ooOo00O = OOOo . read ( )
  OOOo . close ( )
  if 38 - 38: iIii1I11I1II1 + i11iIiiIii * OoO0O00 * iIIi1i1 % Oo
  I1I11IiiI = re . compile ( '<requires[\s\S]*?\/requires' ) . findall ( o0ooOo00O )
  i1III1 = I1I11IiiI [ 0 ] if ( len ( I1I11IiiI ) > 0 ) else 'None'
  if 40 - 40: OO0oo0oOO % OoooooooOO - Oo + o0oOOo0O0Ooo / Oo
 ooO = ooI1111i ( 'http://totalxbmc.com/TI/AddonPortal/approved.php' )
 if 22 - 22: i11iIiiIii / O0
 ooOoOoo0O . create ( 'Backing Up Add-ons' , '' , 'Please Wait...' )
 if 94 - 94: iIIi1i1 * OO0oo0oOO - I1I1i . iIii1I11I1II1
 for I1ii1 in os . listdir ( Oo00OOOOO ) :
  if 66 - 66: iIIi1i1 - Oo * OoOoOO00 / ooOo * II111iiii * OoO0O00
  if 91 - 91: OoooooooOO / I1iii . I1IiiI + iIIi1i1 . II111iiii
  if not 'totalinstaller' in I1ii1 and not 'plugin.program.tbs' in I1ii1 and not 'packages' in I1ii1 and os . path . isdir ( os . path . join ( Oo00OOOOO , I1ii1 ) ) :
   if 45 - 45: ooOo * OoOoOO00 / iIii1I11I1II1
   if 77 - 77: oOOOoo0O0OoO - OO0oo0oOO
   if I1ii1 in ooO and not I1ii1 in i1III1 and not 'script.skin' in I1ii1 and not 'script.common.plugin' in I1ii1 and not 'script.module' in I1ii1 and not 'repo.' in I1ii1 and not 'repository' in I1ii1 and os . path . isdir ( os . path . join ( Oo00OOOOO , I1ii1 ) ) :
    if 11 - 11: I1ii11iIi11i
    if 26 - 26: iIii1I11I1II1 * oOOOoo0O0OoO - Oo
    if not 'service.xbmc.versioncheck' in I1ii1 and not 'packages' in I1ii1 and os . path . isdir ( os . path . join ( Oo00OOOOO , I1ii1 ) ) :
     if 27 - 27: I1ii11iIi11i * oOOOoo0O0OoO - OoO0O00 + I1iii * I1iii
     try :
      ooOoOoo0O . update ( 0 , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % I1ii1 , 'Please Wait...' )
      os . makedirs ( os . path . join ( i1i , I1ii1 ) )
      if 55 - 55: iIIi1i1
      IiII1i1iii1Ii = os . path . join ( i1i , I1ii1 , 'addon.xml' )
      iIO0O00OOo = os . path . join ( i1i , I1ii1 , 'default.py' )
      IIi1I = open ( os . path . join ( Oo00OOOOO , I1ii1 , 'addon.xml' ) , mode = 'r' )
      iii = IIi1I . read ( )
      IIi1I . close ( )
      if 82 - 82: oOOOoo0O0OoO - Oo + OoO0O00
      oOO0o000Oo00o = re . compile ( ' name="(.+?)"' ) . findall ( iii )
      iii11II1I = re . compile ( 'provider-name="(.+?)"' ) . findall ( iii )
      OO0iIiiIi11IIi = re . compile ( '<addon[\s\S]*?">' ) . findall ( iii )
      Oo0 = re . compile ( '<description[\s\S]*?<\/description>' ) . findall ( iii )
      oo0oO = oOO0o000Oo00o [ 0 ] if ( len ( oOO0o000Oo00o ) > 0 ) else 'None'
      oOo0OOoO0 = iii11II1I [ 0 ] if ( len ( iii11II1I ) > 0 ) else 'Anonymous'
      oOII1ii1ii11I1 = OO0iIiiIi11IIi [ 0 ] if ( len ( OO0iIiiIi11IIi ) > 0 ) else 'None'
      i1i1iI1iiiI = Oo0 [ 0 ] if ( len ( Oo0 ) > 0 ) else 'None'
      if 88 - 88: I1ii11iIi11i
      oOO = '<addon id="' + I1ii1 + '" name="' + oo0oO + '" version="0" provider-name="' + oOo0OOoO0 + '">'
      I1iiioO0o0O0Ooo0o = '<description>If you\'re seeing this message it means the add-on is still updating, please wait for the update process to complete.</description>'
      if 92 - 92: OO0oo0oOO
      if oOII1ii1ii11I1 != 'None' :
       iiIiIiII = iii . replace ( i1i1iI1iiiI , I1iiioO0o0O0Ooo0o ) . replace ( oOII1ii1ii11I1 , oOO )
       if 14 - 14: I1IiiI . I1iii
      else :
       iiIiIiII = iii . replace ( i1i1iI1iiiI , I1iiioO0o0O0Ooo0o )
       if 46 - 46: IiiI11Iiiii - iIii1I11I1II1
      iiiiiIIi = open ( IiII1i1iii1Ii , mode = 'w+' )
      iiiiiIIi . write ( str ( iiIiIiII ) )
      iiiiiIIi . close ( )
      i1I11iIII1i1I = open ( iIO0O00OOo , mode = 'w+' )
      i1I11iIII1i1I . write ( 'import xbmcplugin,xbmcgui,xbmc,xbmcaddon,os,sys\nAddonID="' + I1ii1 + '"\nAddonName="' + oo0oO + '"\ndialog=xbmcgui.Dialog()\nxbmc.executebuiltin("UpdateLocalAddons")\nxbmc.executebuiltin("UpdateAddonRepos")\nchoice=dialog.yesno(AddonName+" Add-on Requires Update","This add-on may still be in the process of the updating, would you like check the status of your add-on updates or try re-installing via the Total Installer backup method? We highly recommend checking for updates.",yeslabel="Install Option 2", nolabel="Check Updates")\nif choice==0: xbmc.executebuiltin(\'ActivateWindow(10040,"addons://outdated/",return)\')\nelse: xbmc.executebuiltin(\'ActivateWindow(10001,"plugin://plugin.program.totalinstaller/?mode=grab_addons&url=%26redirect%26addonid%3d\'+AddonID+\'")\')\nxbmcplugin.endOfDirectory(int(sys.argv[1]))' )
      i1I11iIII1i1I . close ( )
      if 50 - 50: IiiI11Iiiii / IiiI11Iiiii + Oo * iIIi1i1 / I1ii11iIi11i
     except :
      print "### Failed to backup: " + I1ii1
      if 14 - 14: I1iii % I1IiiI - iIii1I11I1II1 . Oo + OoO0O00 - oOOOoo0O0OoO
      if 5 - 5: IiiI11Iiiii
   else :
    shutil . copytree ( os . path . join ( Oo00OOOOO , I1ii1 ) , os . path . join ( i1i , I1ii1 ) )
    if 62 - 62: OoOoOO00 . OoooooooOO . Oo . OoO0O00 * IiiI11Iiiii
 ooOoOoo0O . close ( )
 if 78 - 78: ooOo / OoO0O00 - ooOo * OoooooooOO . OoOoOO00
 OOoooOoO0Oo = "Creating Backup"
 Oo000 = "Archiving..."
 iiIiII11i1 = ""
 oOo00Ooo0o0 = "Please Wait"
 if 33 - 33: OO0oo0oOO
 o0O0OO ( i1i , iiI111I1iIiI , OOoooOoO0Oo , Oo000 , iiIiII11i1 , oOo00Ooo0o0 , '' , '' )
 if 87 - 87: OoOoOO00 / I1I1i + iIii1I11I1II1
 try :
  shutil . rmtree ( i1i )
  if 93 - 93: iIii1I11I1II1 + ooOo % iIIi1i1
 except :
  print "### COMMUNITY BUILDS: Failed to remove temp addons folder - manual delete required ###"
  if 21 - 21: Oo
  if 6 - 6: I1I1i
def i1I1II ( url ) :
 ooOoOoo0O . create ( 'Cleaning Temp Paths' , '' , 'Please wait...' )
 if os . path . exists ( i1i ) :
  shutil . rmtree ( i1i )
  if 17 - 17: O0 * OoOoOO00 * I1ii11iIi11i * II111iiii * OO0oo0oOO % i1IIi
 if not os . path . exists ( i1i ) :
  os . makedirs ( i1i )
  if 33 - 33: I1ii11iIi11i * I1ii11iIi11i . iIIi1i1 . i11iIiiIii
 oOOO ( iiI111I1iIiI , i1i )
 if 48 - 48: o0oOOo0O0Ooo . I1iii + OoOoOO00 % I1ii11iIi11i / i11iIiiIii
 for I1ii1 in os . listdir ( i1i ) :
  if 74 - 74: II111iiii . O0 - I1IiiI + I1I1i % i11iIiiIii % OoOoOO00
  if not 'totalinstaller' in I1ii1 and not 'plugin.program.tbs' in I1ii1 :
   if not os . path . exists ( os . path . join ( Oo00OOOOO , I1ii1 ) ) :
    os . rename ( os . path . join ( i1i , I1ii1 ) , os . path . join ( Oo00OOOOO , I1ii1 ) )
    ooOoOoo0O . update ( 0 , "Installing: [COLOR=yellow]" + I1ii1 + '[/COLOR]' , '' , 'Please wait...' )
    print "### Successfully installed: " + I1ii1
    if 78 - 78: I1iii + OoOoOO00 + I1I1i - I1I1i . i11iIiiIii / OoO0O00
   else :
    print "### " + I1ii1 + " Already exists on system"
    if 27 - 27: I1iii - O0 % OO0oo0oOO * oOOOoo0O0OoO . I1I1i % iIii1I11I1II1
    if 37 - 37: OoooooooOO + O0 - i1IIi % iIIi1i1
def i1I1i1i ( welcometext ) :
 iiiIIIi11I ( 'disclaimer.xml' )
 if iiI1IiI == 'true' :
  OOo0oO00ooO00 ( 'folder' , 'I have read and understand the disclaimer.' , welcometext , 'CB_Menu' , 'Community_Builds.png' , '' , '' , '' )
 else :
  OOo0oO00ooO00 ( 'folder' , 'I have read and understand the disclaimer.' , 'welcome' , 'CB_Menu' , 'Community_Builds.png' , '' , '' , '' )
  if 30 - 30: oOOOoo0O0OoO % oOOOoo0O0OoO % I1I1i . OoOoOO00
  if 9 - 9: iIIi1i1 / II111iiii . OoOoOO00 % o0oOOo0O0Ooo * II111iiii - iIIi1i1
def oOOoo0 ( welcometext ) :
 IIIIiI11I = xbmc . getInfoLabel ( "System.BuildVersion" )
 iiiI11iIIi1 = float ( IIIIiI11I [ : 2 ] )
 IiIiIi = int ( iiiI11iIIi1 )
 if 72 - 72: IiiI11Iiiii * Oo
 if iI1Ii11111iIi == 'true' :
  if 67 - 67: i1IIi
  if i1i1II == 'true' :
   iiioOOOo ( 'yes' )
   if 31 - 31: OoOoOO00 + OoOoOO00 . i11iIiiIii / iIIi1i1 % OO0oo0oOO / OoOoOO00
  if i1i1II == 'false' :
   iiioOOOo ( 'no' )
   if 29 - 29: I1ii11iIi11i * I1ii11iIi11i . OoO0O00 * OO0oo0oOO % iIii1I11I1II1 * I1ii11iIi11i
 if not 'elc' in welcometext :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]To access community builds you must be logged in[/COLOR]' , 'settings' , 'addon_settings' , 'noobsandnerds.png' , '' , '' , 'Register at [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR]' )
  if 31 - 31: OoO0O00 * O0 . ooOo
 if IiII == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Show My Private List[/COLOR]' , '&visibility=private' , 'grab_builds' , 'Private_builds.png' , '' , '' , '' )
  if 59 - 59: II111iiii * i11iIiiIii
 if ( ( Oo0oO0ooo . replace ( '%20' , ' ' ) in welcometext ) and ( 'elc' in welcometext ) ) or ( iI1Ii11111iIi == 'true' ) :
  if 54 - 54: O0 % OoooooooOO - I1IiiI
  if ( IiIiIi < 14 ) or ( i1 == 'true' ) :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Show All Gotham Compatible Builds[/COLOR]' , '&xbmc=gotham&visibility=public' , 'grab_builds' , 'TRCOMMUNITYGOTHAMBUILDS.png' , '' , '' , '' )
   if 61 - 61: Oo0Ooo * I1I1i . Oo0Ooo + Oo0Ooo / I1I1i * O0
  if ( IiIiIi == 14 ) or ( i1 == 'true' ) :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Show All Helix Compatible Builds[/COLOR]' , '&xbmc=helix&visibility=public' , 'grab_builds' , 'TRCOMMUNITYHELIXBUILDS.png' , '' , '' , '' )
   if 73 - 73: IiiI11Iiiii * IiiI11Iiiii / iIIi1i1
  if ( IiIiIi == 15 ) or ( i1 == 'true' ) :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Show All Isengard Compatible Builds[/COLOR]' , '&xbmc=isengard&visibility=public' , 'grab_builds' , 'TRCOMMUNITYHELIXBUILDS.png' , '' , '' , '' )
   if 43 - 43: I1ii11iIi11i . i1IIi . I1I1i + O0 * I1iii * O0
   if 41 - 41: I1ii11iIi11i + I1iii % OoooooooOO . I1ii11iIi11i + IiiI11Iiiii . IiiI11Iiiii
   if 31 - 31: i11iIiiIii + II111iiii . IiiI11Iiiii * OoOoOO00
  if i1iiIIiiI111 != '' :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=darkcyan]Show ' + oooOOOOO + ' Builds[/COLOR]' , '&id=1' , 'grab_builds' , 'TRCOMMUNITYGOTHAMBUILDS.png' , '' , '' , '' )
  if i1iiIII111ii != '' :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=darkcyan]Show ' + i1iIIi1 + ' Builds[/COLOR]' , '&id=2' , 'grab_builds' , 'TRCOMMUNITYGOTHAMBUILDS.png' , '' , '' , '' )
  if ii11iIi1I != '' :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=darkcyan]Show ' + iI111I11I1I1 + ' Builds[/COLOR]' , '&id=3' , 'grab_builds' , 'TRCOMMUNITYGOTHAMBUILDS.png' , '' , '' , '' )
  if OOooO0OOoo != '' :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=darkcyan]Show ' + iIii1 + ' Builds[/COLOR]' , '&id=4' , 'grab_builds' , 'TRCOMMUNITYGOTHAMBUILDS.png' , '' , '' , '' )
  if oOOoO0 != '' :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=darkcyan]Show ' + O0OoO000O0OO + ' Builds[/COLOR]' , '&id=5' , 'grab_builds' , 'TRCOMMUNITYGOTHAMBUILDS.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Create My Own Community Build' , 'url' , 'community_backup' , 'Backup.png' , '' , '' , 'Back Up Your Full System' )
 if 66 - 66: OoOoOO00 + i1IIi % II111iiii . O0 * I1ii11iIi11i % I1ii11iIi11i
 if 87 - 87: Oo + o0oOOo0O0Ooo . IiiI11Iiiii - OoooooooOO
def iiiiI1IiI1I1 ( skin ) :
 iI111i11iI1 = '<onleft>%s</onleft>'
 III1ii = '<onright>%s</onright>'
 iI1III1iIi11 = '<onup>%s</onup>'
 i11I1I = '<ondown>%s</ondown>'
 oo0ooooo00o = '<control type="button" id="%s">'
 if 78 - 78: iIii1I11I1II1 . o0oOOo0O0Ooo % iIii1I11I1II1 . O0 / Oo
 if 76 - 76: i1IIi * OoooooooOO * O0 + oOOOoo0O0OoO * oOOOoo0O0OoO
 i1iIiIii = [
 ( '65' , '140' ) ,
 ( '66' , '164' ) ,
 ( '67' , '162' ) ,
 ( '68' , '142' ) ,
 ( '69' , '122' ) ,
 ( '70' , '143' ) ,
 ( '71' , '144' ) ,
 ( '72' , '145' ) ,
 ( '73' , '127' ) ,
 ( '74' , '146' ) ,
 ( '75' , '147' ) ,
 ( '76' , '148' ) ,
 ( '77' , '166' ) ,
 ( '78' , '165' ) ,
 ( '79' , '128' ) ,
 ( '80' , '129' ) ,
 ( '81' , '120' ) ,
 ( '82' , '123' ) ,
 ( '83' , '141' ) ,
 ( '84' , '124' ) ,
 ( '85' , '126' ) ,
 ( '86' , '163' ) ,
 ( '87' , '121' ) ,
 ( '88' , '161' ) ,
 ( '89' , '125' ) ,
 ( '90' , '160' ) ]
 if 20 - 20: o0oOOo0O0Ooo * iIIi1i1
 for i1III1iI , ii1ii1IiiiiIi1I in i1iIiIii :
  ooo0O0o0OoOO = open ( skin ) . read ( )
  iIi11i = ooo0O0o0OoOO . replace ( oo0ooooo00o % i1III1iI , oo0ooooo00o % ii1ii1IiiiiIi1I ) . replace ( iI111i11iI1 % i1III1iI , iI111i11iI1 % ii1ii1IiiiiIi1I ) . replace ( III1ii % i1III1iI , III1ii % ii1ii1IiiiiIi1I ) . replace ( iI1III1iIi11 % i1III1iI , iI1III1iIi11 % ii1ii1IiiiiIi1I ) . replace ( i11I1I % i1III1iI , i11I1I % ii1ii1IiiiiIi1I )
  ooOo0O0o0 = open ( skin , mode = 'w' )
  ooOo0O0o0 . write ( iIi11i )
  ooOo0O0o0 . close ( )
  if 98 - 98: iIIi1i1 - IiiI11Iiiii . OO0oo0oOO
def Ii1IIIII ( u , skin ) :
 iI111i11iI1 = '<onleft>%s</onleft>'
 III1ii = '<onright>%s</onright>'
 iI1III1iIi11 = '<onup>%s</onup>'
 i11I1I = '<ondown>%s</ondown>'
 oo0ooooo00o = '<control type="button" id="%s">'
 if 49 - 49: iIii1I11I1II1 % II111iiii
 if u < 49 :
  IiiII1iIii111iII = u + 61
  if 27 - 27: o0oOOo0O0Ooo * i11iIiiIii * OoO0O00
 else :
  IiiII1iIii111iII = u + 51
  if 92 - 92: Oo0Ooo / i11iIiiIii + I1ii11iIi11i
 ooo0O0o0OoOO = open ( skin ) . read ( )
 iIi11i = ooo0O0o0OoOO . replace ( iI111i11iI1 % u , iI111i11iI1 % IiiII1iIii111iII ) . replace ( III1ii % u , III1ii % IiiII1iIii111iII ) . replace ( iI1III1iIi11 % u , iI1III1iIi11 % IiiII1iIii111iII ) . replace ( i11I1I % u , i11I1I % IiiII1iIii111iII ) . replace ( oo0ooooo00o % u , oo0ooooo00o % IiiII1iIii111iII )
 ooOo0O0o0 = open ( skin , mode = 'w' )
 ooOo0O0o0 . write ( iIi11i )
 ooOo0O0o0 . close ( )
 if 87 - 87: OoOoOO00 % iIii1I11I1II1
 if 72 - 72: Oo . Oo - I1ii11iIi11i
def III1II1i ( ) :
 iI1i1IiIIIIi = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if 65 - 65: O0 * I1IiiI / I1IiiI . OoOoOO00
 if not os . path . exists ( zip ) :
  II . ok ( 'Download/Storage Path Check' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' )
  o0O . openSettings ( sys . argv [ 0 ] )
  if 87 - 87: II111iiii * I1ii11iIi11i % Oo0Ooo * Oo0Ooo
  if 58 - 58: Oo . o0oOOo0O0Ooo + I1IiiI % Oo0Ooo - OoO0O00
def Oo00OO0 ( localbuildcheck , localversioncheck , id ) :
 Oo0O00O000 = 'http://120.24.252.100/TI/Community_Builds/buildupdate.php?id=%s' % ( id )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 50 - 50: IiiI11Iiiii % II111iiii - iIIi1i1 . i1IIi + O0 % IiiI11Iiiii
 if id != 'None' :
  i1iIi1IIiIII1 = re . compile ( 'version="(.+?)"' ) . findall ( i11I1IiII1i1i )
  i1Ii11I1II = i1iIi1IIiIII1 [ 0 ] if ( len ( i1iIi1IIiIII1 ) > 0 ) else ''
  if 77 - 77: ooOo - Oo0Ooo - iIii1I11I1II1
  if localversioncheck < i1Ii11I1II :
   return True
   if 16 - 16: OoO0O00 / IiiI11Iiiii / i1IIi . IiiI11Iiiii + ooOo
 else :
  return False
  if 26 - 26: iIii1I11I1II1 + i1IIi / OoOoOO00 % I1ii11iIi11i
  if 44 - 44: OoooooooOO . II111iiii . Oo % OoooooooOO
def oOO0o0oo0 ( ) :
 Oo0oO00 = open ( oo0OooOOo0 , mode = 'r' )
 iii = Oo0oO00 . read ( )
 Oo0oO00 . close ( )
 if 41 - 41: O0 - OO0oo0oOO * iIii1I11I1II1
 II111i1ii1iII = re . compile ( 'name="(.+?)"' ) . findall ( iii )
 ooo0OoO = II111i1ii1iII [ 0 ] if ( len ( II111i1ii1iII ) > 0 ) else ''
 if 50 - 50: I1IiiI * Oo + iIIi1i1
 if ooo0OoO == "Incomplete" :
  iIi1IiI = xbmcgui . Dialog ( ) . yesno ( "Finish Restore Process" , 'If you\'re certain the correct skin has now been set click OK' , 'to finish the install process, once complete XBMC/Kodi will' , ' then close. Do you want to finish the install process?' , yeslabel = 'Yes' , nolabel = 'No' )
  if 88 - 88: OO0oo0oOO + i11iIiiIii % ooOo * Oo * Oo * I1iii
  if iIi1IiI == 1 :
   I1I1iO0O0oo ( )
   if 83 - 83: I1I1i / oOOOoo0O0OoO
  elif iIi1IiI == 0 :
   return
   if 64 - 64: OoO0O00 % I1I1i . oOOOoo0O0OoO % OoO0O00 + OO0oo0oOO * I1I1i
def OOOO00OooO ( ) :
 iI1i1IiIIIIi = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if 64 - 64: OoO0O00 . I1IiiI - OoooooooOO . iIIi1i1 - IiiI11Iiiii
 try :
  os . makedirs ( iI1i1IiIIIIi )
  os . removedirs ( iI1i1IiIIIIi )
  II . ok ( '[COLOR=lime]SUCCESS[/COLOR]' , 'Great news, the path you chose is writeable.' , 'Some of these builds are rather big, we recommend a minimum of 1GB storage space.' )
  if 77 - 77: I1iii % OoOoOO00 / II111iiii % IiiI11Iiiii % OoooooooOO % OoO0O00
 except :
  II . ok ( '[COLOR=red]CANNOT WRITE TO PATH[/COLOR]' , 'Kodi cannot write to the path you\'ve chosen. Please click OK in the settings menu to save the path then try again. Some devices give false results, we recommend using a USB stick as the backup path.' )
  if 19 - 19: I1I1i * oOOOoo0O0OoO / ooOo * oOOOoo0O0OoO - OoooooooOO * OO0oo0oOO
  if 17 - 17: II111iiii + Oo0Ooo . oOOOoo0O0OoO
def I1I1i1i ( data ) :
 data = data . replace ( '</p><p>' , '[CR][CR]' ) . replace ( '&ndash;' , '-' ) . replace ( '&mdash;' , '-' ) . replace ( "\n" , " " ) . replace ( "\r" , " " ) . replace ( "&rsquo;" , "'" ) . replace ( "&rdquo;" , '"' ) . replace ( "</a>" , " " ) . replace ( "&hellip;" , '...' ) . replace ( "&lsquo;" , "'" ) . replace ( "&ldquo;" , '"' )
 data = " " . join ( data . split ( ) )
 OOo0O = re . compile ( r'< script[^<>]*?>.*?< / script >' )
 data = OOo0O . sub ( '' , data )
 OOo0O = re . compile ( r'< style[^<>]*?>.*?< / style >' )
 data = OOo0O . sub ( '' , data )
 OOo0O = re . compile ( r'' )
 data = OOo0O . sub ( '' , data )
 OOo0O = re . compile ( r'<[^<]*?>' )
 data = OOo0O . sub ( '' , data )
 data = data . replace ( '&nbsp;' , ' ' )
 return data
 if 100 - 100: OoO0O00 % OoO0O00
 if 15 - 15: ooOo / oOOOoo0O0OoO
def Iiii111 ( ) :
 iIi1IiI = xbmcgui . Dialog ( ) . yesno ( 'Clear All Known Cache?' , 'This will clear all known cache files and can help if you\'re encountering kick-outs during playback as well as other random issues. There is no harm in using this.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if 71 - 71: O0 / I1IiiI . oOOOoo0O0OoO / oOOOoo0O0OoO * iIIi1i1
 if iIi1IiI == 1 :
  OooO0OOo ( )
  OooOoooo0000 ( )
  if 29 - 29: I1iii - I1IiiI / I1IiiI * I1iii * I1I1i . Oo
  if 80 - 80: iIii1I11I1II1
def i1I11 ( url ) :
 OOo0oO00ooO00 ( 'folder' , 'African' , str ( url ) + '&genre=african' , 'grab_builds' , 'african.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Arabic' , str ( url ) + '&genre=arabic' , 'grab_builds' , 'arabic.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Asian' , str ( url ) + '&genre=asian' , 'grab_builds' , 'asian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Australian' , str ( url ) + '&genre=australian' , 'grab_builds' , 'australian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Austrian' , str ( url ) + '&genre=austrian' , 'grab_builds' , 'austrian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Belgian' , str ( url ) + '&genre=belgian' , 'grab_builds' , 'belgian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Brazilian' , str ( url ) + '&genre=brazilian' , 'grab_builds' , 'brazilian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Canadian' , str ( url ) + '&genre=canadian' , 'grab_builds' , 'canadian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Columbian' , str ( url ) + '&genre=columbian' , 'grab_builds' , 'columbian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Czech' , str ( url ) + '&genre=czech' , 'grab_builds' , 'czech.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Danish' , str ( url ) + '&genre=danish' , 'grab_builds' , 'danish.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Dominican' , str ( url ) + '&genre=dominican' , 'grab_builds' , 'dominican.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Dutch' , str ( url ) + '&genre=dutch' , 'grab_builds' , 'dutch.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Egyptian' , str ( url ) + '&genre=egyptian' , 'grab_builds' , 'egyptian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Filipino' , str ( url ) + '&genre=filipino' , 'grab_builds' , 'filipino.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Finnish' , str ( url ) + '&genre=finnish' , 'grab_builds' , 'finnish.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'French' , str ( url ) + '&genre=french' , 'grab_builds' , 'french.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'German' , str ( url ) + '&genre=german' , 'grab_builds' , 'german.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Greek' , str ( url ) + '&genre=greek' , 'grab_builds' , 'greek.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Hebrew' , str ( url ) + '&genre=hebrew' , 'grab_builds' , 'hebrew.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Hungarian' , str ( url ) + '&genre=hungarian' , 'grab_builds' , 'hungarian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Icelandic' , str ( url ) + '&genre=icelandic' , 'grab_builds' , 'icelandic.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Indian' , str ( url ) + '&genre=indian' , 'grab_builds' , 'indian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Irish' , str ( url ) + '&genre=irish' , 'grab_builds' , 'irish.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Italian' , str ( url ) + '&genre=italian' , 'grab_builds' , 'italian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Japanese' , str ( url ) + '&genre=japanese' , 'grab_builds' , 'japanese.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Korean' , str ( url ) + '&genre=korean' , 'grab_builds' , 'korean.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Lebanese' , str ( url ) + '&genre=lebanese' , 'grab_builds' , 'lebanese.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Mongolian' , str ( url ) + '&genre=mongolian' , 'grab_builds' , 'mongolian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Nepali' , str ( url ) + '&genre=nepali' , 'grab_builds' , 'nepali.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'New Zealand' , str ( url ) + '&genre=newzealand' , 'grab_builds' , 'newzealand.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Norwegian' , str ( url ) + '&genre=norwegian' , 'grab_builds' , 'norwegian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Pakistani' , str ( url ) + '&genre=pakistani' , 'grab_builds' , 'pakistani.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Polish' , str ( url ) + '&genre=polish' , 'grab_builds' , 'polish.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Portuguese' , str ( url ) + '&genre=portuguese' , 'grab_builds' , 'portuguese.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Romanian' , str ( url ) + '&genre=romanian' , 'grab_builds' , 'romanian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Russian' , str ( url ) + '&genre=russian' , 'grab_builds' , 'russian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Singapore' , str ( url ) + '&genre=singapore' , 'grab_builds' , 'singapore.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Spanish' , str ( url ) + '&genre=spanish' , 'grab_builds' , 'spanish.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Swedish' , str ( url ) + '&genre=swedish' , 'grab_builds' , 'swedish.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Swiss' , str ( url ) + '&genre=swiss' , 'grab_builds' , 'swiss.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Syrian' , str ( url ) + '&genre=syrian' , 'grab_builds' , 'syrian.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Tamil' , str ( url ) + '&genre=tamil' , 'grab_builds' , 'tamil.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Thai' , str ( url ) + '&genre=thai' , 'grab_builds' , 'thai.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Turkish' , str ( url ) + '&genre=turkish' , 'grab_builds' , 'turkish.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'UK' , str ( url ) + '&genre=uk' , 'grab_builds' , 'uk.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'USA' , str ( url ) + '&genre=usa' , 'grab_builds' , 'usa.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Vietnamese' , str ( url ) + '&genre=vietnamese' , 'grab_builds' , 'vietnamese.png' , '' , '' , '' )
 if 5 - 5: OoOoOO00 % IiiI11Iiiii + I1I1i
 if 13 - 13: I1I1i
def ii1II1II ( ) :
 i11i11II11i = 1
 III1II1i ( )
 II1Ii1I1i = xbmc . translatePath ( os . path . join ( Ooo0OO0oOO , 'Community Builds' , 'My Builds' , '' ) )
 OOooOooo0OOo0 = xbmc . translatePath ( os . path . join ( Ooo0OO0oOO , 'Community Builds' , 'My Builds' , 'my_full_backup.zip' ) )
 oo0o0OoOO0o0 = xbmc . translatePath ( os . path . join ( Ooo0OO0oOO , 'Community Builds' , 'My Builds' , 'my_full_backup_GUI_Settings.zip' ) )
 if 14 - 14: o0oOOo0O0Ooo % I1I1i + I1ii11iIi11i + OoO0O00
 if not os . path . exists ( II1Ii1I1i ) :
  os . makedirs ( II1Ii1I1i )
  if 76 - 76: OoO0O00 - i11iIiiIii + OoOoOO00 + Oo / OoooooooOO
 IiI1Iii1 = Ooooo ( heading = "Enter a name for this backup" )
 if ( not IiI1Iii1 ) :
  return False , 0
  if 43 - 43: Oo
 ooOoOii1iII = urllib . quote_plus ( IiI1Iii1 )
 O00oo = xbmc . translatePath ( os . path . join ( II1Ii1I1i , ooOoOii1iII + '.zip' ) )
 OoOoooO000OO = [ I1IiI ]
 O00Oooi1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'Thumbs.db' , '.gitignore' ]
 oOOO0ooOO = [ I1IiI , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 i11IiI1iiI11 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' , 'Thumbs.db' , '.gitignore' ]
 OOoooOoO0Oo = "Creating full backup of existing build"
 OOoOOOO00 = "Creating Community Build"
 Oo000 = "Archiving..."
 iiIiII11i1 = ""
 oOo00Ooo0o0 = "Please Wait"
 if 49 - 49: OoO0O00 - O0 / OoO0O00 * OoOoOO00 + oOOOoo0O0OoO
 if o00 == 'true' :
  o0O0OO ( OooO0 , OOooOooo0OOo0 , OOoooOoO0Oo , Oo000 , iiIiII11i1 , oOo00Ooo0o0 , OoOoooO000OO , O00Oooi1 )
  if 35 - 35: II111iiii . I1IiiI / i1IIi / I1IiiI * ooOo
 iIi1IiI = xbmcgui . Dialog ( ) . yesno ( "Do you want to include your addon_data folder?" , 'This contains ALL addon settings including passwords but may also contain important information such as skin shortcuts. We recommend MANUALLY removing the addon_data folders that aren\'t required.' , yeslabel = 'Yes' , nolabel = 'No' )
 if 85 - 85: II111iiii . iIIi1i1 % Oo % OO0oo0oOO
 if iIi1IiI == 0 :
  oOOO0ooOO = [ I1IiI , 'cache' , 'system' , 'peripheral_data' , 'library' , 'keymaps' , 'addon_data' , 'Thumbnails' ]
  if 80 - 80: ooOo * OO0oo0oOO / iIii1I11I1II1 % ooOo / iIii1I11I1II1
 elif iIi1IiI == 1 :
  pass
  if 42 - 42: i1IIi / i11iIiiIii . Oo0Ooo * IiiI11Iiiii . i11iIiiIii * O0
 Iiii1 ( OooO0 )
 o0O0OO ( OooO0 , O00oo , OOoOOOO00 , Oo000 , iiIiII11i1 , oOo00Ooo0o0 , oOOO0ooOO , i11IiI1iiI11 )
 time . sleep ( 1 )
 if 27 - 27: Oo
 O0OO0ooO00 = xbmc . translatePath ( os . path . join ( II1Ii1I1i , ooOoOii1iII + '_guisettings.zip' ) )
 oO0oOO0o = zipfile . ZipFile ( O0OO0ooO00 , mode = 'w' )
 if 65 - 65: IiiI11Iiiii . OoO0O00 + I1iii
 try :
  oO0oOO0o . write ( iIi1ii1I1 , 'guisettings.xml' , zipfile . ZIP_DEFLATED )
 except : i11i11II11i = 0
 if 25 - 25: o0oOOo0O0Ooo + Oo0Ooo . Oo0Ooo % OoooooooOO - I1iii
 try :
  oO0oOO0o . write ( xbmc . translatePath ( os . path . join ( OooO0 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 if 43 - 43: OoO0O00 % OoO0O00
 oO0oOO0o . close ( )
 if 46 - 46: Oo0Ooo % iIii1I11I1II1 . IiiI11Iiiii . O0 * iIIi1i1 / OoooooooOO
 if o00 == 'true' :
  II1iI1IIi = zipfile . ZipFile ( oo0o0OoOO0o0 , mode = 'w' )
  try :
   II1iI1IIi . write ( iIi1ii1I1 , 'guisettings.xml' , zipfile . ZIP_DEFLATED )
  except : i11i11II11i = 0
  if 41 - 41: I1IiiI - oOOOoo0O0OoO % II111iiii . oOOOoo0O0OoO - OO0oo0oOO
  try :
   II1iI1IIi . write ( xbmc . translatePath ( os . path . join ( OooO0 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
  except : pass
  II1iI1IIi . close ( )
  if 45 - 45: I1iii - Oo
  if i11i11II11i == 0 :
   II . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your system, please reboot and try again.' , '' , '' )
   if 70 - 70: OoO0O00 % I1IiiI / I1IiiI . OO0oo0oOO % iIIi1i1 . II111iiii
  else :
   II . ok ( "SUCCESS!" , 'You Are Now Backed Up and can share this build with the community.' )
   if 10 - 10: I1iii - i11iIiiIii . I1ii11iIi11i % i1IIi
   if o00 == 'true' :
    II . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=dodgerblue]' + OOooOooo0OOo0 , '[/COLOR]Universal Backup: [COLOR=dodgerblue]' + O00oo + '[/COLOR]' )
    if 78 - 78: iIii1I11I1II1 * Oo0Ooo . Oo0Ooo - Oo . iIii1I11I1II1
   else :
    II . ok ( "Build Location" , 'Universal Backup:[CR][COLOR=dodgerblue]' + O00oo + '[/COLOR]' )
    if 30 - 30: iIIi1i1 + iIIi1i1 % I1I1i - o0oOOo0O0Ooo - I1ii11iIi11i
    if 36 - 36: OO0oo0oOO % Oo
def OoO0 ( ) :
 III1II1i ( )
 iIi1IiI = II . yesno ( '[COLOR=gold]Create[/COLOR] [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] [COLOR=gold]Build[/COLOR]' , 'This backup will only work if you share your build on the [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] portal with the rest of the community. It will not work with any other installer/wizard, do you wish to continue?' )
 if 37 - 37: OO0oo0oOO
 if iIi1IiI == 1 :
  i11i11II11i = 1
  II1Ii1I1i = xbmc . translatePath ( os . path . join ( Ooo0OO0oOO , 'Community Builds' , 'My Builds' , '' ) )
  OOooOooo0OOo0 = xbmc . translatePath ( os . path . join ( Ooo0OO0oOO , 'Community Builds' , 'My Builds' , 'my_full_backup.zip' ) )
  oo0o0OoOO0o0 = xbmc . translatePath ( os . path . join ( Ooo0OO0oOO , 'Community Builds' , 'My Builds' , 'my_full_backup_GUI_Settings.zip' ) )
  if 83 - 83: O0
  if not os . path . exists ( II1Ii1I1i ) :
   os . makedirs ( II1Ii1I1i )
   if 89 - 89: Oo0Ooo + I1ii11iIi11i - o0oOOo0O0Ooo
  IiI1Iii1 = Ooooo ( heading = "Enter a name for this backup" )
  if 40 - 40: OoO0O00 + OoO0O00
  if ( not IiI1Iii1 ) :
   return False , 0
   if 94 - 94: IiiI11Iiiii * iIii1I11I1II1 . OO0oo0oOO
  ooOoOii1iII = urllib . quote_plus ( IiI1Iii1 )
  O00oo = xbmc . translatePath ( os . path . join ( II1Ii1I1i , ooOoOii1iII + '.zip' ) )
  if 13 - 13: iIii1I11I1II1 * OoOoOO00 / oOOOoo0O0OoO % iIIi1i1 + ooOo
  if 41 - 41: I1ii11iIi11i
  OoOoooO000OO = [ I1IiI ]
  O00Oooi1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'Thumbs.db' , '.gitignore' ]
  oOOO0ooOO = [ I1IiI , 'cache' , 'system' , 'addons' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' , 'script.module.metahandler' , 'script.artistslideshow' , 'ArtistSlideshow' ]
  i11IiI1iiI11 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' , 'Thumbs.db' , '.gitignore' ]
  OOoooOoO0Oo = "Creating full backup of existing build"
  OOoOOOO00 = "Creating Community Build"
  Oo000 = "Archiving..."
  iiIiII11i1 = ""
  oOo00Ooo0o0 = "Please Wait"
  if 5 - 5: Oo0Ooo
  if 100 - 100: I1iii + iIii1I11I1II1
  if o00 == 'true' :
   o0O0OO ( OooO0 , OOooOooo0OOo0 , OOoooOoO0Oo , Oo000 , iiIiII11i1 , oOo00Ooo0o0 , OoOoooO000OO , O00Oooi1 )
   if 59 - 59: I1I1i
  iIi1IiI = xbmcgui . Dialog ( ) . yesno ( "Do you want to include your addon_data folder?" , 'This contains ALL addon settings including passwords but may also contain important information such as skin shortcuts. We recommend MANUALLY removing the addon_data folders that aren\'t required.' , yeslabel = 'Yes' , nolabel = 'No' )
  if 89 - 89: OoOoOO00 % iIii1I11I1II1
  if 35 - 35: I1ii11iIi11i + oOOOoo0O0OoO - OoOoOO00 % ooOo % o0oOOo0O0Ooo % OoOoOO00
  if iIi1IiI == 0 :
   oOOO0ooOO = [ I1IiI , 'cache' , 'system' , 'addons' , 'peripheral_data' , 'library' , 'keymaps' , 'addon_data' , 'Thumbnails' ]
   if 45 - 45: I1IiiI * Oo % OoO0O00
  elif iIi1IiI == 1 :
   pass
   if 24 - 24: iIIi1i1 - OO0oo0oOO * ooOo
   if 87 - 87: I1iii - I1ii11iIi11i % I1ii11iIi11i . ooOo / I1ii11iIi11i
  I11Ii1iI11iI1 ( )
  Iiii1 ( OooO0 )
  o0O0OO ( OooO0 , O00oo , OOoOOOO00 , Oo000 , iiIiII11i1 , oOo00Ooo0o0 , oOOO0ooOO , i11IiI1iiI11 )
  if 6 - 6: OoOoOO00 / iIii1I11I1II1 * OoooooooOO * i11iIiiIii
  if 79 - 79: I1I1i % OoO0O00
  try :
   os . remove ( iiI111I1iIiI )
  except :
   pass
   if 81 - 81: i11iIiiIii + i11iIiiIii * OoO0O00 + I1I1i
  try :
   os . remove ( i1i )
  except :
   pass
   if 32 - 32: O0 . OoooooooOO
  time . sleep ( 1 )
  if 15 - 15: I1IiiI . OoO0O00
  if 17 - 17: i11iIiiIii / Oo0Ooo . OoO0O00 / I1IiiI
  O0OO0ooO00 = xbmc . translatePath ( os . path . join ( II1Ii1I1i , ooOoOii1iII + '_guisettings.zip' ) )
  oO0oOO0o = zipfile . ZipFile ( O0OO0ooO00 , mode = 'w' )
  if 38 - 38: i1IIi . I1ii11iIi11i % I1iii + iIii1I11I1II1 + O0
  try :
   oO0oOO0o . write ( iIi1ii1I1 , 'guisettings.xml' , zipfile . ZIP_DEFLATED )
   if 47 - 47: OoO0O00 + I1I1i / II111iiii
  except :
   i11i11II11i = 0
   if 97 - 97: I1ii11iIi11i / I1IiiI % O0 + i1IIi - iIIi1i1
  try :
   oO0oOO0o . write ( xbmc . translatePath ( os . path . join ( OooO0 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
   if 38 - 38: o0oOOo0O0Ooo % oOOOoo0O0OoO + i11iIiiIii + IiiI11Iiiii + iIIi1i1 / i11iIiiIii
  except :
   pass
   if 94 - 94: IiiI11Iiiii - Oo0Ooo + ooOo
  oO0oOO0o . close ( )
  if 59 - 59: OO0oo0oOO . I1IiiI - iIii1I11I1II1 + iIii1I11I1II1
  if 56 - 56: ooOo + iIIi1i1
  if o00 == 'true' :
   II1iI1IIi = zipfile . ZipFile ( oo0o0OoOO0o0 , mode = 'w' )
   if 32 - 32: II111iiii + OoOoOO00 % iIIi1i1 / OoOoOO00 + I1ii11iIi11i
   try :
    II1iI1IIi . write ( iIi1ii1I1 , 'guisettings.xml' , zipfile . ZIP_DEFLATED )
    if 2 - 2: i11iIiiIii - oOOOoo0O0OoO + OoO0O00 % OO0oo0oOO * I1iii
   except :
    i11i11II11i = 0
    if 54 - 54: O0 - IiiI11Iiiii . Oo % IiiI11Iiiii + IiiI11Iiiii
   try :
    II1iI1IIi . write ( xbmc . translatePath ( os . path . join ( OooO0 , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
    if 36 - 36: Oo % i11iIiiIii
   except :
    pass
    if 47 - 47: i1IIi + II111iiii . Oo0Ooo * ooOo . OO0oo0oOO / i1IIi
   II1iI1IIi . close ( )
   if 50 - 50: oOOOoo0O0OoO / i1IIi % OoooooooOO
  if i11i11II11i == 0 :
   II . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your system, please reboot and try again.' , '' , '' )
   if 83 - 83: I1ii11iIi11i * I1ii11iIi11i + Oo
  else :
   II . ok ( "SUCCESS!" , 'You Are Now Backed Up and can share this build with the community.' )
   if 57 - 57: O0 - O0 . I1ii11iIi11i / o0oOOo0O0Ooo / I1iii
   if o00 == 'true' :
    II . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=dodgerblue]' + OOooOooo0OOo0 , '[/COLOR]Universal Backup (this will ONLY work for sharing on the [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] portal):[CR][COLOR=dodgerblue]' + O00oo + '[/COLOR]' )
    if 20 - 20: Oo * II111iiii - OoOoOO00 - ooOo * oOOOoo0O0OoO
   else :
    II . ok ( "Build Location" , 'Universal Backup (this will ONLY work for sharing on the [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] portal):[CR][COLOR=dodgerblue]' + O00oo + '[/COLOR]' )
    if 6 - 6: iIIi1i1 + Oo / Oo0Ooo + I1I1i % II111iiii / OoO0O00
    if 45 - 45: OoooooooOO
def I1oo ( url , video ) :
 Oo0O00O000 = 'http://120.24.252.100/TI/Community_Builds/community_builds_premium.php?id=%s' % ( url )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiI1IIIii = re . compile ( 'path="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iIOO0OOoooo0o = re . compile ( 'myart="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IiIi1Ii = re . compile ( 'artpack="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oOIIiIi = re . compile ( 'videopreview="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiIIiI11II1 = re . compile ( 'videoguide1="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oooOo = re . compile ( 'videoguide2="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oOoO0Oo0 = re . compile ( 'videoguide3="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i11i11i = re . compile ( 'videoguide4="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiI1iI = re . compile ( 'videoguide5="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Ooo00O0 = re . compile ( 'videolabel1="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OoO0OOoO0 = re . compile ( 'videolabel2="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiI11i = re . compile ( 'videolabel3="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0Oo = re . compile ( 'videolabel4="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiI1i = re . compile ( 'videolabel5="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oo0oO = re . compile ( 'name="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i11I = re . compile ( 'author="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IIo0Oo0oO0oOO00 = re . compile ( 'version="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Oo0 = re . compile ( 'description="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0oO0o0oo0O0 = re . compile ( 'DownloadURL="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O0oo00oOOO0o = re . compile ( 'UpdateURL="(.+?)"' ) . findall ( i11I1IiII1i1i )
 II1i = re . compile ( 'UpdateDate="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I111iiIIiI1I = re . compile ( 'UpdateDesc="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oooO = re . compile ( 'updated="(.+?)"' ) . findall ( i11I1IiII1i1i )
 ooO00Oo = re . compile ( 'defaultskin="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Iiii1Ii1I = re . compile ( 'skins="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oooOOOOOi1iIii = re . compile ( 'videoaddons="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0O0ooooooo00 = re . compile ( 'audioaddons="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1111ii11IIII = re . compile ( 'programaddons="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IiIi1II111I = re . compile ( 'pictureaddons="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o00o = re . compile ( 'sources="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IIi1i1 = re . compile ( 'adult="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0O0Ooo = re . compile ( 'guisettings="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O0o = re . compile ( 'thumb="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O00oOOooO = re . compile ( 'fanart="(.+?)"' ) . findall ( i11I1IiII1i1i )
 if 46 - 46: iIii1I11I1II1 . i11iIiiIii - OoOoOO00 % O0 / II111iiii * i1IIi
 oOIiiIIi = iIOO0OOoooo0o [ 0 ] if ( len ( iIOO0OOoooo0o ) > 0 ) else ''
 OoOo0OO0oooo = IiIi1Ii [ 0 ] if ( len ( IiIi1Ii ) > 0 ) else ''
 iI1i1IiIIIIi = iiI1IIIii [ 0 ] if ( len ( iiI1IIIii ) > 0 ) else ''
 I1ii1 = oo0oO [ 0 ] if ( len ( oo0oO ) > 0 ) else ''
 I11II1i1 = i11I [ 0 ] if ( len ( i11I ) > 0 ) else ''
 IiIiIi = IIo0Oo0oO0oOO00 [ 0 ] if ( len ( IIo0Oo0oO0oOO00 ) > 0 ) else ''
 I1iiioO0o0O0Ooo0o = Oo0 [ 0 ] if ( len ( Oo0 ) > 0 ) else 'No information available'
 IIiI1 = oooO [ 0 ] if ( len ( oooO ) > 0 ) else ''
 IiI1ii11I1 = ooO00Oo [ 0 ] if ( len ( ooO00Oo ) > 0 ) else ''
 I1i1iI = Iiii1Ii1I [ 0 ] if ( len ( Iiii1Ii1I ) > 0 ) else ''
 I1iI1I1ii1 = oooOOOOOi1iIii [ 0 ] if ( len ( oooOOOOOi1iIii ) > 0 ) else ''
 iIIi1 = o0O0ooooooo00 [ 0 ] if ( len ( o0O0ooooooo00 ) > 0 ) else ''
 o0Ooo0o0Oo = I1111ii11IIII [ 0 ] if ( len ( I1111ii11IIII ) > 0 ) else ''
 oo00ooooOOo00 = IiIi1II111I [ 0 ] if ( len ( IiIi1II111I ) > 0 ) else ''
 ii1iOO00Oooo000 = o00o [ 0 ] if ( len ( o00o ) > 0 ) else ''
 iI1 = IIi1i1 [ 0 ] if ( len ( IIi1i1 ) > 0 ) else ''
 ii111iiIii = o0O0Ooo [ 0 ] if ( len ( o0O0Ooo ) > 0 ) else 'None'
 oO0o = o0oO0o0oo0O0 [ 0 ] if ( len ( o0oO0o0oo0O0 ) > 0 ) else 'None'
 iIiI = O0oo00oOOO0o [ 0 ] if ( len ( O0oo00oOOO0o ) > 0 ) else 'None'
 iIIiiiI1iI1 = II1i [ 0 ] if ( len ( II1i ) > 0 ) else 'None'
 oO00000oO0o0O = I111iiIIiI1I [ 0 ] if ( len ( I111iiIIiI1I ) > 0 ) else 'None'
 ii1Oo0000oOo = oOIIiIi [ 0 ] if ( len ( oOIIiIi ) > 0 ) else 'None'
 I1I = iiIIiI11II1 [ 0 ] if ( len ( iiIIiI11II1 ) > 0 ) else 'None'
 ooooo = oooOo [ 0 ] if ( len ( oooOo ) > 0 ) else 'None'
 i11IIIiI1I = oOoO0Oo0 [ 0 ] if ( len ( oOoO0Oo0 ) > 0 ) else 'None'
 o0iiiI1I1iIIIi1 = i11i11i [ 0 ] if ( len ( i11i11i ) > 0 ) else 'None'
 Iii = iiI1iI [ 0 ] if ( len ( iiI1iI ) > 0 ) else 'None'
 O0Oo0o000oO = Ooo00O0 [ 0 ] if ( len ( Ooo00O0 ) > 0 ) else 'None'
 oO0o00oOOooO0 = OoO0OOoO0 [ 0 ] if ( len ( OoO0OOoO0 ) > 0 ) else 'None'
 OOOoO000 = iiI11i [ 0 ] if ( len ( iiI11i ) > 0 ) else 'None'
 oOOOO = o0Oo [ 0 ] if ( len ( o0Oo ) > 0 ) else 'None'
 IiIi1ii111i1 = iiI1i [ 0 ] if ( len ( iiI1i ) > 0 ) else 'None'
 I1IIiI = O0o [ 0 ] if ( len ( O0o ) > 0 ) else 'None'
 O0oOOo0o = O00oOOooO [ 0 ] if ( len ( O00oOOooO ) > 0 ) else 'None'
 if 34 - 34: Oo0Ooo - i1IIi - iIIi1i1 - i1IIi
 Oo0oO00 = open ( i1I1iI , mode = 'w+' )
 Oo0oO00 . write ( 'id="' + str ( video ) + '"\nname="' + I1ii1 + '"\nversion="' + IiIiIi + '"' )
 Oo0oO00 . close ( )
 if 62 - 62: OO0oo0oOO / ooOo % Oo0Ooo . OoooooooOO / i11iIiiIii / oOOOoo0O0OoO
 OooO0O0Ooo = open ( oo0OooOOo0 , mode = 'r' )
 oO0O = OooO0O0Ooo . read ( )
 OooO0O0Ooo . close ( )
 if 25 - 25: ooOo % I1IiiI + i11iIiiIii + O0 * OoooooooOO
 Ooo0Oo0oo0 = re . compile ( 'id="(.+?)"' ) . findall ( oO0O )
 ooO0 = Ooo0Oo0oo0 [ 0 ] if ( len ( Ooo0Oo0oo0 ) > 0 ) else 'None'
 o0Iiii = re . compile ( 'version="(.+?)"' ) . findall ( oO0O )
 III1iII1I1ii = o0Iiii [ 0 ] if ( len ( o0Iiii ) > 0 ) else 'None'
 I1i1I , i1111iI1 , Oo0oOOOOo = url . partition ( '&' )
 OOo0oO00ooO00 ( '' , '[COLOR=yellow]IMPORTANT:[/COLOR] Install Instructions' , '' , 'instructions_2' , 'noobsandnerds.png' , '' , '' , '' )
 oo000o ( '[COLOR=yellow]Description:[/COLOR] This contains important info from the build author' , 'None' , 'description' , 'BUILDDETAILS.png' , O0oOOo0o , I1ii1 , I11II1i1 , IiIiIi , I1iiioO0o0O0Ooo0o , IIiI1 , I1i1iI , I1iI1I1ii1 , iIIi1 , o0Ooo0o0Oo , oo00ooooOOo00 , ii1iOO00Oooo000 , iI1 )
 if 14 - 14: OoooooooOO . o0oOOo0O0Ooo . OO0oo0oOO
 if ooO0 == I1i1I and III1iII1I1ii != IiIiIi :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]----------------- UPDATE AVAILABLE ------------------[/COLOR]' , 'None' , '' , 'noobsandnerds.png' , '' , '' , '' )
  III1Iiii1I11 ( '[COLOR=dodgerblue]1. Update:[/COLOR] Overwrite my existing library and profiles' , oO0o , 'restore_community' , I1IIiI , '' , 'update' , I1ii1 , IiI1ii11I1 , ii111iiIii , OoOo0OO0oooo )
  III1Iiii1I11 ( '[COLOR=dodgerblue]2. Update:[/COLOR] Keep My Library & Profiles' , oO0o , 'restore_community' , I1IIiI , '' , 'updatelibprofile' , I1ii1 , IiI1ii11I1 , ii111iiIii , OoOo0OO0oooo )
  III1Iiii1I11 ( '[COLOR=dodgerblue]3. Update:[/COLOR] Keep My Library Only' , oO0o , 'restore_community' , I1IIiI , '' , 'updatelibrary' , I1ii1 , IiI1ii11I1 , ii111iiIii , OoOo0OO0oooo )
  III1Iiii1I11 ( '[COLOR=dodgerblue]4. Update:[/COLOR] Keep My Profiles Only' , oO0o , 'restore_community' , I1IIiI , '' , 'updateprofiles' , I1ii1 , IiI1ii11I1 , ii111iiIii , OoOo0OO0oooo )
  if 50 - 50: iIIi1i1 * OoOoOO00 + I1ii11iIi11i - i11iIiiIii + Oo0Ooo * I1ii11iIi11i
 if ii1Oo0000oOo != 'None' or I1I != 'None' or ooooo != 'None' or i11IIIiI1I != 'None' or o0iiiI1I1iIIIi1 != 'None' or Iii != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]------------------ VIDEO GUIDES -----------------[/COLOR]' , 'None' , '' , 'noobsandnerds.png' , '' , '' , '' )
  if 20 - 20: oOOOoo0O0OoO / o0oOOo0O0Ooo % OoOoOO00
 if ii1Oo0000oOo != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] Preview[/COLOR]' , ii1Oo0000oOo , 'play_video' , 'Video_Preview.png' , O0oOOo0o , '' , '' )
  if 69 - 69: oOOOoo0O0OoO - i1IIi % IiiI11Iiiii . Oo - Oo
 if I1I != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + O0Oo0o000oO + '[/COLOR]' , I1I , 'play_video' , 'Video_Guide.png' , O0oOOo0o , '' , '' )
  if 65 - 65: Oo + II111iiii
 if ooooo != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + oO0o00oOOooO0 + '[/COLOR]' , ooooo , 'play_video' , 'Video_Guide.png' , O0oOOo0o , '' , '' )
  if 61 - 61: i11iIiiIii * ooOo % Oo0Ooo * oOOOoo0O0OoO - OoooooooOO - OoO0O00
 if i11IIIiI1I != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + OOOoO000 + '[/COLOR]' , i11IIIiI1I , 'play_video' , 'Video_Guide.png' , O0oOOo0o , '' , '' )
  if 83 - 83: iIIi1i1 / Oo
 if o0iiiI1I1iIIIi1 != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + oOOOO + '[/COLOR]' , o0iiiI1I1iIIIi1 , 'play_video' , 'Video_Guide.png' , O0oOOo0o , '' , '' )
  if 39 - 39: I1I1i + OO0oo0oOO
 if Iii != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + IiIi1ii111i1 + '[/COLOR]' , Iii , 'play_video' , 'Video_Guide.png' , O0oOOo0o , '' , '' )
  if 9 - 9: I1IiiI % OO0oo0oOO . Oo0Ooo * I1IiiI
 if ooO0 != I1i1I :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]------------------ INSTALL OPTIONS ------------------[/COLOR]' , 'None' , '' , 'noobsandnerds.png' , '' , '' , '' )
  if 99 - 99: O0 . o0oOOo0O0Ooo % OO0oo0oOO - Oo0Ooo / OO0oo0oOO
 if oO0o == 'None' :
  III1Iiii1I11 ( '[COLOR=orange]Sorry this build is currently unavailable[/COLOR]' , '' , '' , '' , '' , '' , '' , '' , '' , '' )
  if 20 - 20: OoOoOO00 * IiiI11Iiiii
 if ooO0 != I1i1I :
  if I1IIIIiii1i ( ) :
   III1Iiii1I11 ( '[COLOR=grey]1. Fresh Install:[/COLOR] NOT YET AVAILABLE ON OPENELEC' , '' , '' , '' , '' , '' , '' , '' , '' , '' )
  else :
   III1Iiii1I11 ( '[COLOR=dodgerblue]1. Fresh Install:[/COLOR] This will wipe all existing settings' , oO0o , 'restore_community' , I1IIiI , O0oOOo0o , 'fresh' , I1ii1 , IiI1ii11I1 , ii111iiIii , OoOo0OO0oooo )
  III1Iiii1I11 ( '[COLOR=dodgerblue]2. Install:[/COLOR] Keep My Library & Profiles' , oO0o , 'restore_community' , I1IIiI , O0oOOo0o , 'libprofile' , I1ii1 , IiI1ii11I1 , ii111iiIii , OoOo0OO0oooo )
  III1Iiii1I11 ( '[COLOR=dodgerblue]3. Install:[/COLOR] Keep My Library Only' , oO0o , 'restore_community' , I1IIiI , O0oOOo0o , 'library' , I1ii1 , IiI1ii11I1 , ii111iiIii , OoOo0OO0oooo )
  III1Iiii1I11 ( '[COLOR=dodgerblue]4. Install:[/COLOR] Keep My Profiles Only' , oO0o , 'restore_community' , I1IIiI , O0oOOo0o , 'profiles' , I1ii1 , IiI1ii11I1 , ii111iiIii , OoOo0OO0oooo )
  if 19 - 19: OoooooooOO
 if ii111iiIii != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]---------- (OPTIONAL) Guisettings Fix ----------[/COLOR]' , 'None' , '' , 'noobsandnerds.png' , '' , '' , '' )
  OOo0oO00ooO00 ( '' , '[COLOR=orange]Install Step 2:[/COLOR] Apply guisettings.xml fix' , ii111iiIii , 'guisettingsfix' , 'Fix_My_Build.png' , O0oOOo0o , '' , '' )
  if 76 - 76: OoO0O00 * ooOo
  if 63 - 63: II111iiii . II111iiii + I1ii11iIi11i + Oo + O0 . I1iii
  if 1 - 1: O0 * i11iIiiIii - iIIi1i1 - I1iii
  if 94 - 94: OoO0O00 + I1I1i + iIIi1i1
  if 82 - 82: Oo0Ooo - Oo0Ooo . iIii1I11I1II1 / Oo + I1I1i % iIii1I11I1II1
  if 61 - 61: Oo / Oo0Ooo % Oo - OoO0O00 + iIIi1i1 / iIIi1i1
  if 82 - 82: Oo0Ooo
  if 5 - 5: OoO0O00 / OoO0O00 - O0 - oOOOoo0O0OoO + oOOOoo0O0OoO
  if 99 - 99: OO0oo0oOO * OoooooooOO / o0oOOo0O0Ooo . I1I1i - iIii1I11I1II1 - I1iii
def I1iIiIii ( ) :
 print '############################################################       DELETING USERDATA             ###############################################################'
 OO0I1iiI1iiI1i1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data' , '' ) )
 if 88 - 88: ooOo % Oo0Ooo - OO0oo0oOO % ooOo + I1I1i - IiiI11Iiiii
 for ii1OO0 , i1iiIIIi , Oo0o in os . walk ( OO0I1iiI1iiI1i1 ) :
  OoOoO00OOoOOOo0 = 0
  OoOoO00OOoOOOo0 += len ( Oo0o )
  if 84 - 84: ooOo + Oo . IiiI11Iiiii
  if OoOoO00OOoOOOo0 >= 0 :
   if 71 - 71: iIIi1i1 / iIIi1i1 . OoOoOO00 % IiiI11Iiiii
   for ooOo0O0o0 in Oo0o :
    os . unlink ( os . path . join ( ii1OO0 , ooOo0O0o0 ) )
    if 50 - 50: iIIi1i1 + IiiI11Iiiii / OO0oo0oOO / OO0oo0oOO % O0
   for ii1iIIiii1 in i1iiIIIi :
    shutil . rmtree ( os . path . join ( ii1OO0 , ii1iIIiii1 ) )
    if 87 - 87: Oo0Ooo + iIIi1i1
    if 66 - 66: o0oOOo0O0Ooo * Oo + I1iii * o0oOOo0O0Ooo + Oo / OoooooooOO
def o0OOOoo0ooo00 ( ) :
 for I11i1I11 in glob . glob ( os . path . join ( Ii1iIiII1ii1 , 'xbmc_crashlog*.*' ) ) :
  Ii1I = I11i1I11
  os . remove ( I11i1I11 )
  II = xbmcgui . Dialog ( )
  II . ok ( "Crash Logs Deleted" , "Your old crash logs have now been deleted." )
  if 60 - 60: OoO0O00 - i1IIi . Oo + Oo * Oo + I1iii
  if 66 - 66: Oo * Oo / iIii1I11I1II1 + OoOoOO00 . Oo
def oOo00oOO ( ) :
 print '############################################################       DELETING PACKAGES             ###############################################################'
 Ii1 = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 if 80 - 80: i11iIiiIii % I1ii11iIi11i
 for ii1OO0 , i1iiIIIi , Oo0o in os . walk ( Ii1 ) :
  OoOoO00OOoOOOo0 = 0
  OoOoO00OOoOOOo0 += len ( Oo0o )
  if 54 - 54: o0oOOo0O0Ooo + OO0oo0oOO - iIii1I11I1II1 % iIIi1i1 % I1I1i
  if OoOoO00OOoOOOo0 > 0 :
   if 19 - 19: I1ii11iIi11i / iIii1I11I1II1 % i1IIi . OoooooooOO
   for ooOo0O0o0 in Oo0o :
    os . unlink ( os . path . join ( ii1OO0 , ooOo0O0o0 ) )
    if 57 - 57: iIIi1i1 . Oo0Ooo - OoO0O00 - i11iIiiIii * oOOOoo0O0OoO / o0oOOo0O0Ooo
   for ii1iIIiii1 in i1iiIIIi :
    shutil . rmtree ( os . path . join ( ii1OO0 , ii1iIIiii1 ) )
    if 79 - 79: I1ii11iIi11i + o0oOOo0O0Ooo % Oo0Ooo * o0oOOo0O0Ooo
    if 21 - 21: IiiI11Iiiii
def i11Ii ( ) :
 print '############################################################       DELETING USERDATA             ###############################################################'
 OO0I1iiI1iiI1i1 = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data' , '' ) )
 if 36 - 36: ooOo
 for ii1OO0 , i1iiIIIi , Oo0o in os . walk ( OO0I1iiI1iiI1i1 ) :
  OoOoO00OOoOOOo0 = 0
  OoOoO00OOoOOOo0 += len ( Oo0o )
  if 8 - 8: oOOOoo0O0OoO + OoO0O00
  if OoOoO00OOoOOOo0 >= 0 :
   if 9 - 9: Oo + o0oOOo0O0Ooo
   for ooOo0O0o0 in Oo0o :
    os . unlink ( os . path . join ( ii1OO0 , ooOo0O0o0 ) )
    if 8 - 8: Oo * Oo0Ooo / IiiI11Iiiii - OoO0O00 - OoooooooOO
   for ii1iIIiii1 in i1iiIIIi :
    shutil . rmtree ( os . path . join ( ii1OO0 , ii1iIIiii1 ) )
    if 100 - 100: ooOo . iIii1I11I1II1 . iIii1I11I1II1
    if 55 - 55: ooOo
def IIIII1I1Ii11iI ( name , addon_id ) :
 OO0oIII111i11IiI = 1
 i11I1II = 1
 i1iiI = xbmc . translatePath ( os . path . join ( Oo00OOOOO , addon_id , 'addon.xml' ) )
 o0o = open ( i1iiI , mode = 'r' )
 oOO00OO0o0O = o0o . read ( )
 o0o . close ( )
 III1IiiIiiI1i = re . compile ( 'import addon="(.+?)"' ) . findall ( oOO00OO0o0O )
 if 73 - 73: i1IIi % OO0oo0oOO - iIIi1i1 / o0oOOo0O0Ooo % OoO0O00 / oOOOoo0O0OoO
 for O0Oo00OoOo in III1IiiIiiI1i :
  if 89 - 89: I1I1i / OoO0O00 * O0 / OO0oo0oOO . oOOOoo0O0OoO
  if not 'xbmc.python' in O0Oo00OoOo :
   print 'Script Requires --- ' + O0Oo00OoOo
   iII11II1II = xbmc . translatePath ( os . path . join ( Oo00OOOOO , O0Oo00OoOo ) )
   if 100 - 100: OoO0O00 % oOOOoo0O0OoO - OO0oo0oOO % OO0oo0oOO % OO0oo0oOO / iIIi1i1
   if not os . path . exists ( iII11II1II ) :
    Oo0O00O000 = 'http://totalxbmc.com/TI/AddonPortal/dependencyinstall.php?id=%s' % ( O0Oo00OoOo )
    i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
    oo0oO = re . compile ( 'name="(.+?)"' ) . findall ( i11I1IiII1i1i )
    IIo0Oo0oO0oOO00 = re . compile ( 'version="(.+?)"' ) . findall ( i11I1IiII1i1i )
    ooO000OO0O00O = re . compile ( 'repo_url="(.+?)"' ) . findall ( i11I1IiII1i1i )
    OOOoOO0o = re . compile ( 'data_url="(.+?)"' ) . findall ( i11I1IiII1i1i )
    i1II1 = re . compile ( 'zip_url="(.+?)"' ) . findall ( i11I1IiII1i1i )
    oo00oO0o = re . compile ( 'repo_id="(.+?)"' ) . findall ( i11I1IiII1i1i )
    OOO000Oo = oo0oO [ 0 ] if ( len ( oo0oO ) > 0 ) else ''
    IiIiIi = IIo0Oo0oO0oOO00 [ 0 ] if ( len ( IIo0Oo0oO0oOO00 ) > 0 ) else ''
    I1IIIi1i = ooO000OO0O00O [ 0 ] if ( len ( ooO000OO0O00O ) > 0 ) else ''
    OooIii1I1iI = OOOoOO0o [ 0 ] if ( len ( OOOoOO0o ) > 0 ) else ''
    oOoOo0 = i1II1 [ 0 ] if ( len ( i1II1 ) > 0 ) else ''
    iIi = oo00oO0o [ 0 ] if ( len ( oo00oO0o ) > 0 ) else ''
    oOoooOo0o = xbmc . translatePath ( os . path . join ( i1Oo00 , OOO000Oo + '.zip' ) )
    if 44 - 44: Oo0Ooo . Oo0Ooo + OoooooooOO * i11iIiiIii / OO0oo0oOO + oOOOoo0O0OoO
    try :
     downloader . download ( I1IIIi1i , oOoooOo0o , ooOoOoo0O )
     oOOO ( oOoooOo0o , Oo00OOOOO , ooOoOoo0O )
     if 17 - 17: Oo + II111iiii
    except :
     if 43 - 43: OO0oo0oOO % I1iii / o0oOOo0O0Ooo * oOOOoo0O0OoO
     try :
      downloader . download ( oOoOo0 , oOoooOo0o , ooOoOoo0O )
      oOOO ( oOoooOo0o , Oo00OOOOO , ooOoOoo0O )
      if 85 - 85: iIii1I11I1II1 . OoooooooOO . o0oOOo0O0Ooo
     except :
      if 77 - 77: I1IiiI % iIIi1i1
      try :
       if 74 - 74: OoOoOO00 / i1IIi % OoooooooOO
       if not os . path . exists ( iII11II1II ) :
        os . makedirs ( iII11II1II )
        if 52 - 52: I1I1i % iIIi1i1
       i11I1IiII1i1i = ooI1111i ( OooIii1I1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
       I111i1I1 = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( i11I1IiII1i1i )
       if 25 - 25: OO0oo0oOO / OO0oo0oOO % OoooooooOO - I1ii11iIi11i * ooOo
       for II1Ii1iI1i1 in I111i1I1 :
        o0OoO000O = xbmc . translatePath ( os . path . join ( iII11II1II , II1Ii1iI1i1 ) )
        if 23 - 23: i11iIiiIii
        if addon_id not in II1Ii1iI1i1 and '/' not in II1Ii1iI1i1 :
         if 100 - 100: ooOo + O0 . I1IiiI + i1IIi - OoOoOO00 + o0oOOo0O0Ooo
         try :
          ooOoOoo0O . update ( 0 , "Downloading [COLOR=yellow]" + II1Ii1iI1i1 + '[/COLOR]' , '' , 'Please wait...' )
          downloader . download ( OooIii1I1iI + II1Ii1iI1i1 , o0OoO000O , ooOoOoo0O )
          if 65 - 65: II111iiii / Oo0Ooo
         except :
          print "failed to install" + II1Ii1iI1i1
          if 42 - 42: i11iIiiIii . O0
        if '/' in II1Ii1iI1i1 and '..' not in II1Ii1iI1i1 and 'http' not in II1Ii1iI1i1 :
         iIIiI1I1i = OooIii1I1iI + II1Ii1iI1i1
         O0O0OOooOO0 ( o0OoO000O , iIIiI1I1i )
         if 75 - 75: oOOOoo0O0OoO + iIii1I11I1II1
      except :
       II . ok ( "Error downloading dependency" , 'There was an error downloading [COLOR=dodgerblue]' + OOO000Oo + '[/COLOR]. Please consider updating the add-on portal with details or report the error on the forum at [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR]' )
       i11I1II = 0
       OO0oIII111i11IiI = 0
       if 19 - 19: I1IiiI + i11iIiiIii . I1I1i - OO0oo0oOO / I1iii + o0oOOo0O0Ooo
    if i11I1II == 1 :
     time . sleep ( 1 )
     ooOoOoo0O . update ( 0 , "[COLOR=yellow]" + OOO000Oo + '[/COLOR]  [COLOR=lime]Successfully Installed[/COLOR]' , '' , 'Please wait...' )
     time . sleep ( 1 )
     OOo = 'http://totalxbmc.com/TI/AddonPortal/downloadcount.php?id=%s' % ( O0Oo00OoOo )
     ooI1111i ( OOo )
 ooOoOoo0O . close ( )
 time . sleep ( 1 )
 if 38 - 38: Oo0Ooo / iIii1I11I1II1 * iIii1I11I1II1 % I1ii11iIi11i
 if 92 - 92: OO0oo0oOO / O0 * I1IiiI - OO0oo0oOO
def oooOo00000 ( name , url , buildname , author , version , description , updated , skins , videoaddons , audioaddons , programaddons , pictureaddons , sources , adult ) :
 IiI1IiI1iiI1 ( buildname + '     v.' + version , '[COLOR=yellow][B]Author:   [/B][/COLOR]' + author + '[COLOR=yellow][B]               Last Updated:   [/B][/COLOR]' + updated + '[COLOR=yellow][B]               Adult Content:   [/B][/COLOR]' + adult + '[CR][CR][COLOR=yellow][B]Description:[CR][/B][/COLOR]' + description +
 '[CR][CR][COLOR=blue][B]Skins:   [/B][/COLOR]' + skins + '[CR][CR][COLOR=blue][B]Video Addons:   [/B][/COLOR]' + videoaddons + '[CR][CR][COLOR=blue][B]Audio Addons:   [/B][/COLOR]' + audioaddons +
 '[CR][CR][COLOR=blue][B]Program Addons:   [/B][/COLOR]' + programaddons + '[CR][CR][COLOR=blue][B]Picture Addons:   [/B][/COLOR]' + pictureaddons + '[CR][CR][COLOR=blue][B]Sources:   [/B][/COLOR]' + sources +
 '[CR][CR][COLOR=orange]Disclaimer: [/COLOR]These are community builds and they may overwrite some of your existing settings, '
 'It\'s purely the responsibility of the user to choose whether or not they wish to install these builds, the individual who uploads the build should state what\'s included and then it\'s the users decision to decide whether or not that content is suitable for them.' )
 if 70 - 70: Oo + iIIi1i1 * I1iii . I1iii + OoO0O00
 if 28 - 28: i1IIi . Oo
def O0Ooo0O ( path ) :
 ooOoOoo0O . create ( "[COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR]" , "Wiping..." , '' , 'Please Wait' )
 shutil . rmtree ( path , ignore_errors = True )
 if 18 - 18: i1IIi
 if 4 - 4: I1I1i
def oOOO ( _in , _out , dp = None ) :
 if dp :
  return oOo0OoOOOo0 ( _in , _out , dp )
  if 55 - 55: ooOo + O0 / IiiI11Iiiii % iIIi1i1 / OoooooooOO
 return O00o0OO0OO0oo ( _in , _out )
 if 59 - 59: OoooooooOO % OO0oo0oOO / oOOOoo0O0OoO + OoooooooOO . OoooooooOO
 if 87 - 87: OO0oo0oOO + ooOo
def O00o0OO0OO0oo ( _in , _out ) :
 try :
  iIIii1iI11IIi11I = zipfile . ZipFile ( _in , 'r' )
  iIIii1iI11IIi11I . extractall ( _out )
  if 5 - 5: iIii1I11I1II1 . ooOo
 except Exception , Ii1I1iIIIiiii :
  print str ( Ii1I1iIIIiiii )
  return False
  if 70 - 70: IiiI11Iiiii . II111iiii . IiiI11Iiiii - iIii1I11I1II1
 return True
 if 92 - 92: OoO0O00
 if 15 - 15: I1I1i / I1I1i + iIii1I11I1II1 % OoooooooOO
def oOo0OoOOOo0 ( _in , _out , dp ) :
 iIIii1iI11IIi11I = zipfile . ZipFile ( _in , 'r' )
 iIIi111IiII1i = float ( len ( iIIii1iI11IIi11I . infolist ( ) ) )
 oOo0O000oo0 = 0
 if 15 - 15: Oo0Ooo / I1iii % O0 + I1ii11iIi11i
 try :
  if 96 - 96: iIIi1i1 . OoooooooOO
  for i1I1I1I in iIIii1iI11IIi11I . infolist ( ) :
   oOo0O000oo0 += 1
   iII1III = oOo0O000oo0 / iIIi111IiII1i * 100
   dp . update ( int ( iII1III ) )
   iIIii1iI11IIi11I . extract ( i1I1I1I , _out )
   if 58 - 58: OO0oo0oOO % i11iIiiIii / i11iIiiIii * iIIi1i1 - oOOOoo0O0OoO
 except Exception , Ii1I1iIIIiiii :
  print str ( Ii1I1iIIIiiii )
  return False
  if 6 - 6: I1I1i * II111iiii % iIii1I11I1II1
 return True
 if 86 - 86: i1IIi * O0 % iIIi1i1 . Oo0Ooo % iIIi1i1 . Oo0Ooo
def I1I1iO0O0oo ( ) :
 os . remove ( oo0OooOOo0 )
 os . rename ( oOOoo0Oo , oo0OooOOo0 )
 xbmc . executebuiltin ( 'UnloadSkin' )
 xbmc . executebuiltin ( "ReloadSkin" )
 II . ok ( "Local Restore Complete" , 'XBMC/Kodi will now close.' , '' , '' )
 xbmc . executebuiltin ( "Quit" )
 if 71 - 71: IiiI11Iiiii . i11iIiiIii * O0 + O0
 if 57 - 57: OoooooooOO . OO0oo0oOO % II111iiii % I1IiiI + I1iii
def Iiii1 ( url ) :
 ooOoOoo0O . create ( "Changing Physical Paths To Special" , "Renaming paths..." , '' , 'Please Wait' )
 if 70 - 70: I1I1i . i11iIiiIii
 for ii1OO0 , i1iiIIIi , Oo0o in os . walk ( url ) :
  if 76 - 76: IiiI11Iiiii . I1I1i % IiiI11Iiiii - oOOOoo0O0OoO
  for file in Oo0o :
   if 51 - 51: OoooooooOO + o0oOOo0O0Ooo * iIii1I11I1II1 * ooOo / i1IIi
   if file . endswith ( ".xml" ) :
    ooOoOoo0O . update ( 0 , "Fixing" , file , 'Please Wait' )
    ooo0O0o0OoOO = open ( ( os . path . join ( ii1OO0 , file ) ) ) . read ( )
    I11IiI1i = ooo0O0o0OoOO . replace ( OooO0 , 'special://home/' )
    ooOo0O0o0 = open ( ( os . path . join ( ii1OO0 , file ) ) , mode = 'w' )
    ooOo0O0o0 . write ( str ( I11IiI1i ) )
    ooOo0O0o0 . close ( )
    if 81 - 81: iIii1I11I1II1 / ooOo . i11iIiiIii * II111iiii
    if 55 - 55: I1ii11iIi11i
def oOoo0OO0 ( ) :
 iiIiIi1111iI1 = 'http://totalxbmc.com/TI/AddonPortal/Addon_Fix/addonfix.txt'
 i11I1IiII1i1i = ooI1111i ( iiIiIi1111iI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I111i1I1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11I1IiII1i1i )
 if 11 - 11: I1ii11iIi11i . I1ii11iIi11i + II111iiii * OoOoOO00 . I1I1i
 for I1ii1 , I1I1i1I1I1I1 , I1IIiI , O0oOOo0o , I1iiioO0o0O0Ooo0o in I111i1I1 :
  OOo0oO00ooO00 ( '' , I1ii1 , I1I1i1I1I1I1 , 'OSS' , I1IIiI , O0oOOo0o , '' , I1iiioO0o0O0Ooo0o )
  if 34 - 34: OoO0O00 * I1iii * Oo0Ooo
  if 21 - 21: OoooooooOO . OoOoOO00 - iIii1I11I1II1 % I1I1i
def Oooo0ooOoo0 ( ) :
 OoOoooO000OO = [ ]
 O00Oooi1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , '.gitignore' ]
 OOoooOoO0Oo = "Creating full backup of existing build"
 OOoOOOO00 = "Creating Community Build"
 Oo000 = "Archiving..."
 iiIiII11i1 = ""
 oOo00Ooo0o0 = "Please Wait"
 if 26 - 26: I1I1i / iIii1I11I1II1 - iIii1I11I1II1
 o0O0OO ( OooO0 , myfullbackup , OOoooOoO0Oo , Oo000 , iiIiII11i1 , oOo00Ooo0o0 , OoOoooO000OO , O00Oooi1 )
 if 57 - 57: I1I1i
 if 41 - 41: iIii1I11I1II1 * IiiI11Iiiii + Oo0Ooo * o0oOOo0O0Ooo % I1I1i / Oo
def Oo0o0ooOoO ( url ) :
 OOo0oO00ooO00 ( 'folder' , 'Anime' , str ( url ) + '&genre=anime' , 'grab_builds' , 'anime.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Audiobooks' , str ( url ) + '&genre=audiobooks' , 'grab_builds' , 'audiobooks.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Comedy' , str ( url ) + '&genre=comedy' , 'grab_builds' , 'comedy.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Comics' , str ( url ) + '&genre=comics' , 'grab_builds' , 'comics.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Documentary' , str ( url ) + '&genre=documentary' , 'grab_builds' , 'documentary.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Downloads' , str ( url ) + '&genre=downloads' , 'grab_builds' , 'downloads.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Food' , str ( url ) + '&genre=food' , 'grab_builds' , 'food.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Gaming' , str ( url ) + '&genre=gaming' , 'grab_builds' , 'gaming.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Health' , str ( url ) + '&genre=health' , 'grab_builds' , 'health.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'How To...' , str ( url ) + '&genre=howto' , 'grab_builds' , 'howto.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Kids' , str ( url ) + '&genre=kids' , 'grab_builds' , 'kids.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Live TV' , str ( url ) + '&genre=livetv' , 'grab_builds' , 'livetv.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Movies' , str ( url ) + '&genre=movies' , 'grab_builds' , 'movies.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Music' , str ( url ) + '&genre=music' , 'grab_builds' , 'music.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'News' , str ( url ) + '&genre=news' , 'grab_builds' , 'news.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Photos' , str ( url ) + '&genre=photos' , 'grab_builds' , 'photos.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Podcasts' , str ( url ) + '&genre=podcasts' , 'grab_builds' , 'podcasts.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Radio' , str ( url ) + '&genre=radio' , 'grab_builds' , 'radio.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Religion' , str ( url ) + '&genre=religion' , 'grab_builds' , 'religion.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Space' , str ( url ) + '&genre=space' , 'grab_builds' , 'space.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Sports' , str ( url ) + '&genre=sports' , 'grab_builds' , 'sports.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Technology' , str ( url ) + '&genre=tech' , 'grab_builds' , 'tech.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Trailers' , str ( url ) + '&genre=trailers' , 'grab_builds' , 'trailers.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'TV Shows' , str ( url ) + '&genre=tv' , 'grab_builds' , 'tv.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Misc.' , str ( url ) + '&genre=other' , 'grab_builds' , 'other.png' , '' , '' , '' )
 if 47 - 47: OoOoOO00
 if o0O . getSetting ( 'adult' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , 'XXX' , str ( url ) + '&genre=adult' , 'grab_builds' , 'adult.png' , '' , '' , '' )
  if 65 - 65: O0 + oOOOoo0O0OoO % I1iii * I1IiiI / iIIi1i1 / OoOoOO00
def Ooooo ( default = "" , heading = "" , hidden = False ) :
 oooOO = xbmc . Keyboard ( default , heading , hidden )
 if 33 - 33: ooOo
 oooOO . doModal ( )
 if ( oooOO . isConfirmed ( ) ) :
  return unicode ( oooOO . getText ( ) , "utf-8" )
 return default
 if 39 - 39: OoO0O00 + O0 + iIIi1i1 * II111iiii % O0 - O0
 if 41 - 41: I1I1i % o0oOOo0O0Ooo
def oo0O0oOOO0o ( ) :
 oOo0Oo0Oo0 = [ ]
 OooOo0o0OO = sys . argv [ 2 ]
 if len ( OooOo0o0OO ) >= 2 :
  iiI1ii1IIiI = sys . argv [ 2 ]
  IIi1i1I11IIII = iiI1ii1IIiI . replace ( '?' , '' )
  if ( iiI1ii1IIiI [ len ( iiI1ii1IIiI ) - 1 ] == '/' ) :
   iiI1ii1IIiI = iiI1ii1IIiI [ 0 : len ( iiI1ii1IIiI ) - 2 ]
  OooOoOOO00O = IIi1i1I11IIII . split ( '&' )
  oOo0Oo0Oo0 = { }
  for I111iIIII11iI in range ( len ( OooOoOOO00O ) ) :
   oOoOO = { }
   oOoOO = OooOoOOO00O [ I111iIIII11iI ] . split ( '=' )
   if ( len ( oOoOO ) ) == 2 :
    oOo0Oo0Oo0 [ oOoOO [ 0 ] ] = oOoOO [ 1 ]
    if 20 - 20: iIIi1i1 . OoO0O00 * IiiI11Iiiii
 return oOo0Oo0Oo0
 if 71 - 71: Oo0Ooo . II111iiii / II111iiii * I1iii * OoO0O00
def IiiI11 ( ) :
 iI1i1IiIIIIi = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 ooOoOoo0O = xbmcgui . DialogProgress ( )
 ooOoOoo0O . create ( "Gotham Addon Fix" , "Please wait whilst your addons" , '' , 'are being made Gotham compatible.' )
 if 60 - 60: iIIi1i1 * iIIi1i1 / OoooooooOO
 for I11i1I11 in glob . glob ( os . path . join ( iI1i1IiIIIIi , '*.*' ) ) :
  if 65 - 65: I1ii11iIi11i % ooOo . OoooooooOO * o0oOOo0O0Ooo * OoO0O00
  for file in glob . glob ( os . path . join ( I11i1I11 , '*.*' ) ) :
   if 10 - 10: ooOo - IiiI11Iiiii % II111iiii - oOOOoo0O0OoO - i1IIi
   if 'addon.xml' in file :
    ooOoOoo0O . update ( 0 , "Fixing" , file , 'Please Wait' )
    ooo0O0o0OoOO = open ( file ) . read ( )
    I11IiI1i = ooo0O0o0OoOO . replace ( 'addon="xbmc.python" version="1.0"' , 'addon="xbmc.python" version="2.1.0"' ) . replace ( 'addon="xbmc.python" version="2.0"' , 'addon="xbmc.python" version="2.1.0"' )
    ooOo0O0o0 = open ( file , mode = 'w' )
    ooOo0O0o0 . write ( str ( I11IiI1i ) )
    ooOo0O0o0 . close ( )
    if 10 - 10: I1ii11iIi11i - OO0oo0oOO . oOOOoo0O0OoO
 II = xbmcgui . Dialog ( )
 II . ok ( "Your addons have now been made compatible" , "If you still find you have addons that aren't working please run the addon so it throws up a script error, upload a log and post details on the relevant support forum." )
 if 8 - 8: iIii1I11I1II1 % ooOo + Oo0Ooo
 if 24 - 24: o0oOOo0O0Ooo / I1iii / I1iii % II111iiii - ooOo * ooOo
def oOoo0oO ( ) :
 II = xbmcgui . Dialog ( )
 IIii1i = xbmcgui . Dialog ( ) . yesno ( 'Convert Addons To Gotham' , 'This will edit your addon.xml files so they show as Gotham compatible. It\'s doubtful this will have any effect on whether or not they work but it will get rid of the annoying incompatible pop-up message. Do you wish to continue?' )
 if 69 - 69: oOOOoo0O0OoO / OoooooooOO % i11iIiiIii
 if IIii1i == 1 :
  IiiI11 ( )
  if 18 - 18: i11iIiiIii - iIIi1i1 * ooOo + o0oOOo0O0Ooo
  if 16 - 16: OoooooooOO * i11iIiiIii . OoooooooOO - iIii1I11I1II1 * i1IIi
def i1iI1IIi1I ( url ) :
 global oo00O00oO
 if 52 - 52: OoooooooOO / I1I1i % II111iiii
 if o0O . getSetting ( 'adult' ) == 'true' :
  iI1 = 'yes'
  if 40 - 40: I1IiiI % iIIi1i1 % I1I1i + OoO0O00
 else :
  iI1 = 'no'
  if 75 - 75: ooOo - I1ii11iIi11i + ooOo + OoooooooOO . i11iIiiIii
 O0O0O = 'http://totalxbmc.com/TI/AddonPortal/sortby_new.php?sortx=name&user=%s&adult=%s&%s' % ( Oo0oO0ooo , iI1 , url )
 i11I1IiII1i1i = ooI1111i ( O0O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I111i1I1 = re . compile ( 'name="(.+?)" <br> downloads="(.+?)" <br> icon="(.+?)" <br> broken="(.+?)" <br> UID="(.+?)" <br>' , re . DOTALL ) . findall ( i11I1IiII1i1i )
 if 3 - 3: I1iii / Oo0Ooo
 if I111i1I1 != [ ] :
  I1iiii ( O0O0O , 'addons' )
  if 47 - 47: I1ii11iIi11i * ooOo + iIii1I11I1II1 - ooOo / I1I1i
  for I1ii1 , i1iI1 , i11111I1I , i1ii1II1ii , oO0ooo0O0Ooo in I111i1I1 :
   if 33 - 33: II111iiii - I1I1i - iIIi1i1
   if i1ii1II1ii == '0' :
    OOo0oO00ooO00 ( 'folder2' , I1ii1 + '[COLOR=lime] [' + i1iI1 + ' downloads][/COLOR]' , oO0ooo0O0Ooo , 'addon_final_menu' , i11111I1I , '' , '' )
    if 92 - 92: OoO0O00 * I1I1i
   if i1ii1II1ii == '1' :
    OOo0oO00ooO00 ( 'folder2' , '[COLOR=red]' + I1ii1 + ' [REPORTED AS BROKEN][/COLOR]' , oO0ooo0O0Ooo , 'addon_final_menu' , i11111I1I , '' , '' )
    if 92 - 92: ooOo
 elif '&redirect' in url :
  iIi1IiI = II . yesno ( 'No Content Found' , 'This add-on cannot be found on the Add-on Portal.' , '' , 'Would you like to remove this item from your setup?' )
  if 7 - 7: IiiI11Iiiii
  if iIi1IiI == 1 : print "remove"
  if 73 - 73: OoO0O00 % I1ii11iIi11i
 else :
  II . ok ( 'No Content Found' , 'Sorry no content can be found that matches' , 'your search criteria.' , '' )
  if 32 - 32: Oo + IiiI11Iiiii + iIii1I11I1II1 * Oo0Ooo
  if 62 - 62: i11iIiiIii
def i1Iii ( url ) :
 if zip == '' :
  II . ok ( 'Storage/Download Folder Not Set' , 'You have not set your backup storage folder.\nPlease update the addon settings and try again.' , '' , '' )
  o0O . openSettings ( sys . argv [ 0 ] )
  if 91 - 91: iIIi1i1 * I1I1i * II111iiii
 if o0O . getSetting ( 'adult' ) == 'true' :
  iI1 = ''
  if 79 - 79: oOOOoo0O0OoO
 else :
  iI1 = 'no'
  if 8 - 8: IiiI11Iiiii - II111iiii
 if not 'id=' in url :
  O0O0O = 'http://120.24.252.100/TI/Community_Builds/sortby.php?sortx=name&orderx=ASC&adult=%s&%s' % ( iI1 , url )
  i11I1IiII1i1i = ooI1111i ( O0O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  I111i1I1 = re . compile ( 'name="(.+?)"  <br> id="(.+?)"  <br> Thumbnail="(.+?)"  <br> Fanart="(.+?)"  <br> downloads="(.+?)"  <br> <br>' , re . DOTALL ) . findall ( i11I1IiII1i1i )
  if 18 - 18: OoOoOO00
  I1iiii ( url , 'communitybuilds' )
  if 13 - 13: I1I1i % OoO0O00 * iIii1I11I1II1 + I1ii11iIi11i - iIIi1i1 - I1IiiI
  for I1ii1 , id , oooO0 , Oo0oiiiiII11iIi , i1iI1 in I111i1I1 :
   III1Iiii1I11 ( I1ii1 + '[COLOR=lime] (' + i1iI1 + ' downloads)[/COLOR]' , id + url , 'community_menu' , oooO0 , Oo0oiiiiII11iIi , id , '' , '' , '' , '' )
   if 51 - 51: Oo0Ooo / I1I1i * I1iii - II111iiii / I1IiiI . I1I1i
 if 'id=1' in url : O0O0O = i1iiIIiiI111
 if 'id=2' in url : O0O0O = i1iiIII111ii
 if 'id=3' in url : O0O0O = ii11iIi1I
 if 'id=4' in url : O0O0O = OOooO0OOoo
 if 'id=5' in url : O0O0O = oOOoO0
 if 65 - 65: I1I1i
 i11I1IiII1i1i = ooI1111i ( O0O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I111i1I1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11I1IiII1i1i )
 if 75 - 75: OoooooooOO * i11iIiiIii
 for I1ii1 , url , I1IIiI , O0oOOo0o , I1iiioO0o0O0Ooo0o in I111i1I1 :
  if not 'viewport' in I1ii1 :
   OOo0oO00ooO00 ( 'addon' , I1ii1 , url , 'restore_local_CB' , I1IIiI , O0oOOo0o , I1iiioO0o0O0Ooo0o , '' )
   if 67 - 67: oOOOoo0O0OoO / OoO0O00 . OoooooooOO
   if 51 - 51: II111iiii . ooOo . OoO0O00 % II111iiii
def III1I1ii ( url ) :
 O0O0O = 'http://totalxbmc.com/TI/HardwarePortal/sortby.php?sortx=Added&orderx=DESC&%s' % ( url )
 i11I1IiII1i1i = ooI1111i ( O0O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I111i1I1 = re . compile ( 'name="(.+?)" <br> id="(.+?)" <br> thumb="(.+?)" <br><br>' , re . DOTALL ) . findall ( i11I1IiII1i1i )
 if 4 - 4: iIii1I11I1II1 . i1IIi
 I1iiii ( O0O0O , 'hardware' )
 if 63 - 63: iIii1I11I1II1 + I1I1i % i1IIi / I1IiiI % II111iiii
 for I1ii1 , id , OO0iiiii1iiIIii in I111i1I1 :
  OOo0oO00ooO00 ( 'folder2' , I1ii1 , id , 'hardware_final_menu' , OO0iiiii1iiIIii , '' , '' )
  if 8 - 8: I1ii11iIi11i * I1ii11iIi11i * i1IIi + IiiI11Iiiii . I1ii11iIi11i
  if 100 - 100: OoooooooOO - O0 . OO0oo0oOO / OO0oo0oOO + II111iiii * OoOoOO00
def i11111 ( url ) :
 O0O0O = 'http://totalxbmc.com/TI/LatestNews/sortby.php?sortx=item_date&orderx=DESC&%s' % ( url )
 i11I1IiII1i1i = ooI1111i ( O0O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I111i1I1 = re . compile ( 'name="(.+?)" <br> date="(.+?)" <br> source="(.+?)" <br> id="(.+?)" <br><br>' , re . DOTALL ) . findall ( i11I1IiII1i1i )
 if 60 - 60: Oo
 for I1ii1 , o0OoOo00O0o0O , O0O0Oo00OO , id in I111i1I1 :
  if 100 - 100: o0oOOo0O0Ooo . I1IiiI
  if "OpenELEC" in O0O0Oo00OO :
   OOo0oO00ooO00 ( '' , I1ii1 + '  (' + o0OoOo00O0o0O + ')' , id , 'news_menu' , 'OpenELEC.png' , '' , '' )
   if 62 - 62: iIIi1i1 + II111iiii % iIIi1i1
  if "Official" in O0O0Oo00OO :
   OOo0oO00ooO00 ( '' , I1ii1 + '  (' + o0OoOo00O0o0O + ')' , id , 'news_menu' , 'XBMC.png' , '' , '' )
   if 50 - 50: OoooooooOO + ooOo * I1IiiI - I1iii / i11iIiiIii
  if "Raspbmc" in O0O0Oo00OO :
   OOo0oO00ooO00 ( '' , I1ii1 + '  (' + o0OoOo00O0o0O + ')' , id , 'news_menu' , 'Raspbmc.png' , '' , '' )
   if 5 - 5: O0 - I1IiiI
  if "XBMC4Xbox" in O0O0Oo00OO :
   OOo0oO00ooO00 ( '' , I1ii1 + '  (' + o0OoOo00O0o0O + ')' , id , 'news_menu' , 'XBMC4Xbox.png' , '' , '' )
   if 44 - 44: II111iiii . II111iiii + Oo * I1iii
  if "noobsandnerds" in O0O0Oo00OO :
   OOo0oO00ooO00 ( '' , I1ii1 + '  (' + o0OoOo00O0o0O + ')' , id , 'news_menu' , 'noobsandnerds.png' , '' , '' )
   if 16 - 16: II111iiii
   if 100 - 100: O0 - i1IIi
def iII1iiiiI1i ( url ) :
 O0O0O = 'http://totalxbmc.com/TI/TutorialPortal/sortby.php?sortx=Name&orderx=ASC&%s' % ( url )
 i11I1IiII1i1i = ooI1111i ( O0O0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I111i1I1 = re . compile ( 'name="(.+?)" <br> about="(.+?)" <br> id="(.+?)" <br><br>' , re . DOTALL ) . findall ( i11I1IiII1i1i )
 if 58 - 58: iIii1I11I1II1 / I1IiiI - I1ii11iIi11i . o0oOOo0O0Ooo - Oo0Ooo
 I1iiii ( O0O0O , 'tutorials' )
 if 88 - 88: OoO0O00 . oOOOoo0O0OoO / OO0oo0oOO
 for I1ii1 , iIiI1I1 , id in I111i1I1 :
  OOo0oO00ooO00 ( 'folder' , I1ii1 , id , 'tutorial_final_menu' , 'Tutorials.png' , '' , iIiI1I1 )
  if 62 - 62: o0oOOo0O0Ooo / iIii1I11I1II1
  if 55 - 55: I1iii / OoO0O00 + IiiI11Iiiii . I1I1i
def i1ooO ( url , local ) :
 III1II1i ( )
 iIi1IiI = xbmcgui . Dialog ( ) . yesno ( I1ii1 , 'This will over-write your existing guisettings.xml.' , 'Are you sure this is the build you have installed?' , '' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Fix' )
 if 34 - 34: OO0oo0oOO
 if iIi1IiI == 1 :
  OoIi11ii1 ( url , local )
  if 1 - 1: iIii1I11I1II1 % ooOo . iIii1I11I1II1
  if 10 - 10: IiiI11Iiiii + OoO0O00
def OoIi11ii1 ( url , local ) :
 i111I1 = False
 OOOo0Oo0O = 0
 i1I1I1iIIi = 1
 if 46 - 46: I1IiiI . I1I1i - i11iIiiIii - oOOOoo0O0OoO
 if os . path . exists ( OOoOO0oo0ooO ) :
  os . remove ( OOoOO0oo0ooO )
  if 97 - 97: II111iiii % Oo0Ooo * I1I1i
 if os . path . exists ( o0 ) :
  os . remove ( o0 )
  if 51 - 51: Oo0Ooo % Oo . Oo0Ooo
 if os . path . exists ( OOO0OOO00oo ) :
  os . remove ( OOO0OOO00oo )
  if 72 - 72: I1iii % I1iii / I1IiiI
 if not os . path . exists ( O0o0O00Oo0o0 ) :
  os . makedirs ( O0o0O00Oo0o0 )
  if 40 - 40: Oo0Ooo - Oo + oOOOoo0O0OoO - o0oOOo0O0Ooo % I1IiiI . iIIi1i1
  if 35 - 35: i11iIiiIii + OoooooooOO * iIii1I11I1II1 . oOOOoo0O0OoO
 try :
  shutil . copyfile ( iIi1ii1I1 , OOoOO0oo0ooO )
  if 48 - 48: IiiI11Iiiii * i1IIi % OoooooooOO * I1iii * OoO0O00
 except :
  print "No guisettings found, most likely due to a previously failed attempt at install"
  if 7 - 7: IiiI11Iiiii . I1iii . IiiI11Iiiii - oOOOoo0O0OoO
 if local != 1 :
  I1IiiIi11 = os . path . join ( Ooo0OO0oOO , 'guifix.zip' )
  if 20 - 20: Oo - IiiI11Iiiii / Oo0Ooo * OoO0O00
 else :
  I1IiiIi11 = xbmc . translatePath ( url )
  if 55 - 55: OoooooooOO
  if 73 - 73: OoOoOO00 - I1ii11iIi11i % Oo0Ooo + I1ii11iIi11i - O0 . OoO0O00
 i1iIii = str ( os . path . getsize ( I1IiiIi11 ) )
 ooOoOoo0O . create ( "Installing Skin Fix" , "Checking " , '' , 'Please Wait' )
 ooOoOoo0O . update ( 0 , "" , "Extracting Zip Please Wait" )
 oOOO ( I1IiiIi11 , O0o0O00Oo0o0 , ooOoOoo0O )
 if 95 - 95: OO0oo0oOO / I1I1i . O0 * I1I1i - o0oOOo0O0Ooo * Oo0Ooo
 if local != 'library' or local != 'updatelibrary' or local != 'fresh' :
  if 6 - 6: OoOoOO00 . II111iiii * I1IiiI . I1IiiI / I1iii
  try :
   I1I1ii1111 = open ( O0o0O00Oo0o0 + 'profiles.xml' , mode = 'r' )
   IIIiI1iiiIIIi = I1I1ii1111 . read ( )
   I1I1ii1111 . close ( )
   if 85 - 85: O0 . IiiI11Iiiii % I1I1i - OO0oo0oOO % O0 - I1iii
   if os . path . exists ( O0o0O00Oo0o0 + 'profiles.xml' ) :
    if 70 - 70: iIii1I11I1II1 + I1I1i + iIIi1i1
    if local == None :
     iIi1IiI = xbmcgui . Dialog ( ) . yesno ( "PROFILES DETECTED" , 'This build has profiles included, would you like to overwrite your existing profiles or keep the ones you have?' , '' , '' , nolabel = 'Keep my profiles' , yeslabel = 'Use new profiles' )
     if 37 - 37: O0 + i1IIi
    if local != None :
     iIi1IiI = 1
     if 59 - 59: I1I1i % I1iii
    if iIi1IiI == 1 :
     iiiiiIIi = open ( OOO0OOO00oo , mode = 'w' )
     time . sleep ( 1 )
     iiiiiIIi . write ( IIIiI1iiiIIIi )
     time . sleep ( 1 )
     iiiiiIIi . close ( )
     i1I1I1iIIi = 0
     if 57 - 57: OO0oo0oOO . O0 % OoooooooOO . I1IiiI . i1IIi - II111iiii
  except :
   print "no profiles.xml file"
   if 61 - 61: O0 . o0oOOo0O0Ooo / OoOoOO00
   if 74 - 74: i1IIi * oOOOoo0O0OoO % I1iii
 os . rename ( O0o0O00Oo0o0 + 'guisettings.xml' , o0 )
 if 30 - 30: II111iiii - o0oOOo0O0Ooo % oOOOoo0O0OoO . OO0oo0oOO
 if local != 'fresh' :
  oo0o = II . yesno ( "Do You Want To Keep Your Kodi Settings?" , 'Would you like to keep your existing Kodi settings or would you rather wipe and install the ones created by the build author?' , nolabel = 'Keep my settings' , yeslabel = 'Replace my settings' )
  if 75 - 75: IiiI11Iiiii + iIii1I11I1II1
 if local == 'fresh' :
  oo0o = 1
  if 98 - 98: OoOoOO00 - OoOoOO00 . II111iiii . IiiI11Iiiii + O0
 if oo0o == 1 :
  if 28 - 28: I1I1i + i11iIiiIii + OoooooooOO / OoO0O00
  if os . path . exists ( iIi1ii1I1 ) :
   if 6 - 6: I1IiiI - i11iIiiIii
   try :
    print "Attempting to remove guisettings"
    os . remove ( iIi1ii1I1 )
    i111I1 = True
    if 61 - 61: oOOOoo0O0OoO * I1ii11iIi11i % I1IiiI % OoO0O00 % OO0oo0oOO + OO0oo0oOO
   except :
    print "Problem removing guisettings"
    i111I1 = False
    if 6 - 6: Oo0Ooo
   try :
    print "Attempting to replace guisettings with new"
    os . rename ( o0 , iIi1ii1I1 )
    i111I1 = True
    if 73 - 73: oOOOoo0O0OoO * I1ii11iIi11i + o0oOOo0O0Ooo - Oo0Ooo . OO0oo0oOO
   except :
    print "Failed to replace guisettings with new"
    i111I1 = False
    if 93 - 93: i11iIiiIii
    if 80 - 80: i1IIi . I1IiiI - ooOo + Oo + IiiI11Iiiii % ooOo
 if oo0o == 0 :
  Oo0oO00 = open ( OOoOO0oo0ooO , mode = 'r' )
  iii = Oo0oO00 . read ( )
  Oo0oO00 . close ( )
  if 13 - 13: II111iiii / OoOoOO00 / OoOoOO00 + iIIi1i1
  Ii1i = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( iii )
  ooooOoOooo00Oo = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( iii )
  ooo00O0OOo = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( iii )
  IiI1 = Ii1i [ 0 ] if ( len ( Ii1i ) > 0 ) else ''
  Iii1IIII1Iii = ooooOoOooo00Oo [ 0 ] if ( len ( ooooOoOooo00Oo ) > 0 ) else ''
  OO = ooo00O0OOo [ 0 ] if ( len ( ooo00O0OOo ) > 0 ) else ''
  if 81 - 81: o0oOOo0O0Ooo % I1IiiI - IiiI11Iiiii / i11iIiiIii
  if 73 - 73: O0 * oOOOoo0O0OoO . i1IIi
  OooO0O0Ooo = open ( o0 , mode = 'r' )
  oO0O = OooO0O0Ooo . read ( )
  OooO0O0Ooo . close ( )
  if 51 - 51: OoO0O00 - IiiI11Iiiii % O0 - OoOoOO00
  o0ooo = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( oO0O )
  o0oo00O = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( oO0O )
  IIIIII1iI1II = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( oO0O )
  iiiI1 = o0ooo [ 0 ] if ( len ( o0ooo ) > 0 ) else ''
  O00oooO00oo = o0oo00O [ 0 ] if ( len ( o0oo00O ) > 0 ) else ''
  Ii111III1i11I = IIIIII1iI1II [ 0 ] if ( len ( IIIIII1iI1II ) > 0 ) else ''
  iiIiIiII = iii . replace ( IiI1 , iiiI1 ) . replace ( OO , Ii111III1i11I ) . replace ( Iii1IIII1Iii , O00oooO00oo )
  if 62 - 62: OO0oo0oOO . OoO0O00 + OoO0O00 + II111iiii * iIii1I11I1II1 + OoooooooOO
  iiiiiIIi = open ( OOoOO0oo0ooO , mode = 'w+' )
  iiiiiIIi . write ( str ( iiIiIiII ) )
  iiiiiIIi . close ( )
  if 77 - 77: O0 * I1ii11iIi11i * ooOo + OoO0O00 + I1ii11iIi11i - oOOOoo0O0OoO
  if 10 - 10: I1ii11iIi11i + I1I1i
  if os . path . exists ( iIi1ii1I1 ) :
   if 58 - 58: I1IiiI + OoooooooOO / IiiI11Iiiii . iIIi1i1 % o0oOOo0O0Ooo / I1ii11iIi11i
   try :
    os . remove ( iIi1ii1I1 )
    i111I1 = True
    if 62 - 62: II111iiii
   except :
    i111I1 = False
    if 12 - 12: I1I1i + II111iiii
  try :
   os . rename ( OOoOO0oo0ooO , iIi1ii1I1 )
   os . remove ( o0 )
   i111I1 = True
   if 92 - 92: oOOOoo0O0OoO % iIii1I11I1II1 - IiiI11Iiiii / i11iIiiIii % iIIi1i1 * o0oOOo0O0Ooo
  except :
   i111I1 = False
   if 80 - 80: IiiI11Iiiii
   if 3 - 3: I1ii11iIi11i * OO0oo0oOO
 if i111I1 == True or local == None :
  if 53 - 53: iIii1I11I1II1 / IiiI11Iiiii % OoO0O00 + I1I1i / iIIi1i1
  try :
   Oo0oO00 = open ( i1I1iI , mode = 'r' )
   iii = Oo0oO00 . read ( )
   Oo0oO00 . close ( )
   if 74 - 74: Oo0Ooo
   IiIiII11i1 = re . compile ( 'id="(.+?)"' ) . findall ( iii )
   Ii1I1iIiiI1 = re . compile ( 'name="(.+?)"' ) . findall ( iii )
   o00i111iiIiiIiI = re . compile ( 'version="(.+?)"' ) . findall ( iii )
   OOooooO = IiIiII11i1 [ 0 ] if ( len ( IiIiII11i1 ) > 0 ) else ''
   oOoo00 = Ii1I1iIiiI1 [ 0 ] if ( len ( Ii1I1iIiiI1 ) > 0 ) else ''
   i1Ii11I1II = o00i111iiIiiIiI [ 0 ] if ( len ( o00i111iiIiiIiI ) > 0 ) else ''
   if 29 - 29: Oo / OoOoOO00 . iIii1I11I1II1 / OO0oo0oOO % OoOoOO00 % IiiI11Iiiii
   iiiiiIIi = open ( oo0OooOOo0 , mode = 'w+' )
   iiiiiIIi . write ( 'id="' + str ( OOooooO ) + '"\nname="' + oOoo00 + '"\nversion="' + i1Ii11I1II + '"\ngui="' + i1iIii + '"' )
   iiiiiIIi . close ( )
   if 49 - 49: II111iiii / I1I1i - I1iii
   Oo0oO00 = open ( IIIii1II1II , mode = 'r' )
   iii = Oo0oO00 . read ( )
   Oo0oO00 . close ( )
   if 7 - 7: I1IiiI / OoO0O00 + oOOOoo0O0OoO + OO0oo0oOO / I1IiiI
   oOooO0 = re . compile ( 'version="(.+?)"' ) . findall ( iii )
   III1iII1I1ii = oOooO0 [ 0 ] if ( len ( oOooO0 ) > 0 ) else ''
   iiIiIiII = iii . replace ( III1iII1I1ii , i1Ii11I1II )
   if 62 - 62: i11iIiiIii - OO0oo0oOO
   iiiiiIIi = open ( IIIii1II1II , mode = 'w' )
   iiiiiIIi . write ( str ( iiIiIiII ) )
   iiiiiIIi . close ( )
   os . remove ( i1I1iI )
   if 81 - 81: OO0oo0oOO
  except :
   iiiiiIIi = open ( oo0OooOOo0 , mode = 'w+' )
   iiiiiIIi . write ( 'id="None"\nname="Unknown"\nversion="Unknown"\ngui="' + i1iIii + '"' )
   iiiiiIIi . close ( )
   if 92 - 92: Oo - Oo0Ooo - OoooooooOO / I1I1i - i1IIi
   if 81 - 81: i1IIi / oOOOoo0O0OoO % i11iIiiIii . iIii1I11I1II1 * OoOoOO00 + OoooooooOO
 if os . path . exists ( O0o0O00Oo0o0 + 'profiles.xml' ) :
  os . remove ( O0o0O00Oo0o0 + 'profiles.xml' )
  time . sleep ( 1 )
  if 31 - 31: i1IIi % II111iiii
 if os . path . exists ( O0o0O00Oo0o0 ) :
  os . removedirs ( O0o0O00Oo0o0 )
  if 13 - 13: iIii1I11I1II1 - II111iiii % O0 . I1iii % OoO0O00
 Ii11iIiiI = xbmc . translatePath ( os . path . join ( OO0o , I1IiI , 'notification.txt' ) )
 if 3 - 3: II111iiii / Oo
 if os . path . exists ( Ii11iIiiI ) :
  os . remove ( Ii11iIiiI )
  if 48 - 48: iIIi1i1 . I1ii11iIi11i
 if i111I1 == True :
  IiiIIIIi ( )
  IiIIIi ( )
  if 81 - 81: OoooooooOO . OoOoOO00 * iIii1I11I1II1 / OoOoOO00 - I1ii11iIi11i % i1IIi
  if 77 - 77: I1IiiI / OoooooooOO
def Ii111I ( url ) :
 Oo0O00O000 = 'http://totalxbmc.com/TI/HardwarePortal/hardwaredetails.php?id=%s' % ( url )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0oO = re . compile ( 'name="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1I11 = re . compile ( 'manufacturer="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiIIiI11II1 = re . compile ( 'video_guide1="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oooOo = re . compile ( 'video_guide2="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oOoO0Oo0 = re . compile ( 'video_guide3="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i11i11i = re . compile ( 'video_guide4="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiI1iI = re . compile ( 'video_guide5="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Ooo00O0 = re . compile ( 'video_label1="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OoO0OOoO0 = re . compile ( 'video_label2="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiI11i = re . compile ( 'video_label3="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0Oo = re . compile ( 'video_label4="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiI1i = re . compile ( 'video_label5="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iI1i1iI1iI = re . compile ( 'shops="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Oo0 = re . compile ( 'description="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1IIiIi = re . compile ( 'screenshot1="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OOOOoOoO = re . compile ( 'screenshot2="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OO000 = re . compile ( 'screenshot3="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0oOoo0o = re . compile ( 'screenshot4="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IiiIiIIi = re . compile ( 'screenshot5="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O00Oo = re . compile ( 'screenshot6="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oOOoooo0O0 = re . compile ( 'screenshot7="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Ii111Ii11 = re . compile ( 'screenshot8="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Ii1II = re . compile ( 'screenshot9="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IIiII = re . compile ( 'screenshot10="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iII11 = re . compile ( 'screenshot11="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O00OO00OOOoO = re . compile ( 'screenshot12="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IiI11Ii1iI = re . compile ( 'screenshot13="(.+?)"' ) . findall ( i11I1IiII1i1i )
 ooOo0 = re . compile ( 'screenshot14="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oOo0o = re . compile ( 'added="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I11iIiI1I1i11 = re . compile ( 'platform="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O000OOO000o = re . compile ( 'chipset="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I11iiIiiI1iIi11 = re . compile ( 'official_guide="(.+?)"' ) . findall ( i11I1IiII1i1i )
 II1I1I11i1I1 = re . compile ( 'official_preview="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O0o = re . compile ( 'thumbnail="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiIi1 = re . compile ( 'stock_rom="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oOOO0 = re . compile ( 'CPU="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oo0 = re . compile ( 'GPU="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I11iIi1i1I1i1 = re . compile ( 'RAM="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiiiii1ii1 = re . compile ( 'flash="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iIIII1i1 = re . compile ( 'wifi="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1I1oO00o0oOoo = re . compile ( 'bluetooth="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oOOI1 = re . compile ( 'LAN="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OOI1i = re . compile ( 'xbmc_version="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i1II1iII1 = re . compile ( 'pros="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I11II11IiI11 = re . compile ( 'cons="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O00o = re . compile ( 'library_scan="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Ii11Iiii1iiii = re . compile ( '4k="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i1IIII1111 = re . compile ( '1080="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Ooo0o0000OO = re . compile ( '720="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iIiI1II1I1 = re . compile ( '3D="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OooiIiI1i1Ii = re . compile ( 'DTS="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Oo0o00o = re . compile ( 'BootTime="(.+?)"' ) . findall ( i11I1IiII1i1i )
 III1I1 = re . compile ( 'CopyFiles="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iI1IIIIII = re . compile ( 'CopyVideo="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OO0oO0Oo = re . compile ( 'EthernetTest="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OoooOO0 = re . compile ( 'Slideshow="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oo0OoO = re . compile ( 'total_review="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iIIi1iii1 = re . compile ( 'whufclee_review="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o00o0 = re . compile ( 'CB_Premium="(.+?)"' ) . findall ( i11I1IiII1i1i )
 if 84 - 84: OoOoOO00 - Oo0Ooo . iIIi1i1 . I1I1i - Oo0Ooo
 I1ii1 = oo0oO [ 0 ] if ( len ( oo0oO ) > 0 ) else ''
 o0Oo0oO00Oooo = I1I11 [ 0 ] if ( len ( I1I11 ) > 0 ) else ''
 I1I = iiIIiI11II1 [ 0 ] if ( len ( iiIIiI11II1 ) > 0 ) else 'None'
 ooooo = oooOo [ 0 ] if ( len ( oooOo ) > 0 ) else 'None'
 i11IIIiI1I = oOoO0Oo0 [ 0 ] if ( len ( oOoO0Oo0 ) > 0 ) else 'None'
 o0iiiI1I1iIIIi1 = i11i11i [ 0 ] if ( len ( i11i11i ) > 0 ) else 'None'
 Iii = iiI1iI [ 0 ] if ( len ( iiI1iI ) > 0 ) else 'None'
 O0Oo0o000oO = Ooo00O0 [ 0 ] if ( len ( Ooo00O0 ) > 0 ) else 'None'
 oO0o00oOOooO0 = OoO0OOoO0 [ 0 ] if ( len ( OoO0OOoO0 ) > 0 ) else 'None'
 OOOoO000 = iiI11i [ 0 ] if ( len ( iiI11i ) > 0 ) else 'None'
 oOOOO = o0Oo [ 0 ] if ( len ( o0Oo ) > 0 ) else 'None'
 IiIi1ii111i1 = iiI1i [ 0 ] if ( len ( iiI1i ) > 0 ) else 'None'
 Ii1II1I11i1I = iI1i1iI1iI [ 0 ] if ( len ( iI1i1iI1iI ) > 0 ) else ''
 I1iiioO0o0O0Ooo0o = Oo0 [ 0 ] if ( len ( Oo0 ) > 0 ) else ''
 OOoOo = I1IIiIi [ 0 ] if ( len ( I1IIiIi ) > 0 ) else ''
 Iiiiiii11IIiI = OOOOoOoO [ 0 ] if ( len ( OOOOoOoO ) > 0 ) else ''
 oOOO0o = OO000 [ 0 ] if ( len ( OO000 ) > 0 ) else ''
 Oo00O = o0oOoo0o [ 0 ] if ( len ( o0oOoo0o ) > 0 ) else ''
 o0OoII = IiiIiIIi [ 0 ] if ( len ( IiiIiIIi ) > 0 ) else ''
 i1i1IIi = O00Oo [ 0 ] if ( len ( O00Oo ) > 0 ) else ''
 o0oo0Ooo0 = oOOoooo0O0 [ 0 ] if ( len ( oOOoooo0O0 ) > 0 ) else ''
 o0OOoO = Ii111Ii11 [ 0 ] if ( len ( Ii111Ii11 ) > 0 ) else ''
 I1iII1II1I1ii = Ii1II [ 0 ] if ( len ( Ii1II ) > 0 ) else ''
 oo0OO0O = IIiII [ 0 ] if ( len ( IIiII ) > 0 ) else ''
 OO0OooOOoO00OO00 = iII11 [ 0 ] if ( len ( iII11 ) > 0 ) else ''
 ii11ii1iIiI1 = O00OO00OOOoO [ 0 ] if ( len ( O00OO00OOOoO ) > 0 ) else ''
 OoOo0oO0 = IiI11Ii1iI [ 0 ] if ( len ( IiI11Ii1iI ) > 0 ) else ''
 i111iIi1i1 = ooOo0 [ 0 ] if ( len ( ooOo0 ) > 0 ) else ''
 OOo00O0O = oOo0o [ 0 ] if ( len ( oOo0o ) > 0 ) else ''
 OoOo0oOooOoOO = I11iIiI1I1i11 [ 0 ] if ( len ( I11iIiI1I1i11 ) > 0 ) else ''
 ooo = O000OOO000o [ 0 ] if ( len ( O000OOO000o ) > 0 ) else ''
 OoOIiiIi1IiiiI = I11iiIiiI1iIi11 [ 0 ] if ( len ( I11iiIiiI1iIi11 ) > 0 ) else 'None'
 OO0oooOO = II1I1I11i1I1 [ 0 ] if ( len ( II1I1I11i1I1 ) > 0 ) else 'None'
 OO0iiiii1iiIIii = O0o [ 0 ] if ( len ( O0o ) > 0 ) else ''
 IIIi1iiIIiiiI = iiIi1 [ 0 ] if ( len ( iiIi1 ) > 0 ) else ''
 I1IIiIi1iI = oOOO0 [ 0 ] if ( len ( oOOO0 ) > 0 ) else ''
 oOo0 = oo0 [ 0 ] if ( len ( oo0 ) > 0 ) else ''
 Iiii11 = I11iIi1i1I1i1 [ 0 ] if ( len ( I11iIi1i1I1i1 ) > 0 ) else ''
 o00000O = iiiiii1ii1 [ 0 ] if ( len ( iiiiii1ii1 ) > 0 ) else ''
 iIiiiII11 = iIIII1i1 [ 0 ] if ( len ( iIIII1i1 ) > 0 ) else ''
 ooo00Oo0 = I1I1oO00o0oOoo [ 0 ] if ( len ( I1I1oO00o0oOoo ) > 0 ) else ''
 iIii1i1Ii = oOOI1 [ 0 ] if ( len ( oOOI1 ) > 0 ) else ''
 IIIIiI11I = OOI1i [ 0 ] if ( len ( OOI1i ) > 0 ) else ''
 III1iIii = i1II1iII1 [ 0 ] if ( len ( i1II1iII1 ) > 0 ) else ''
 iiIII1i1 = I11II11IiI11 [ 0 ] if ( len ( I11II11IiI11 ) > 0 ) else ''
 oOOo0OOoOO0 = O00o [ 0 ] if ( len ( O00o ) > 0 ) else ''
 IiIi = Ii11Iiii1iiii [ 0 ] if ( len ( Ii11Iiii1iiii ) > 0 ) else ''
 IIi1IiiIi1III = i1IIII1111 [ 0 ] if ( len ( i1IIII1111 ) > 0 ) else ''
 IiIiIiiIIii = Ooo0o0000OO [ 0 ] if ( len ( Ooo0o0000OO ) > 0 ) else ''
 OOo00O00o0O0 = iIiI1II1I1 [ 0 ] if ( len ( iIiI1II1I1 ) > 0 ) else ''
 iI1III = OooiIiI1i1Ii [ 0 ] if ( len ( OooiIiI1i1Ii ) > 0 ) else ''
 I1I111 = Oo0o00o [ 0 ] if ( len ( Oo0o00o ) > 0 ) else ''
 I1iI = III1I1 [ 0 ] if ( len ( III1I1 ) > 0 ) else ''
 IIiiI = iI1IIIIII [ 0 ] if ( len ( iI1IIIIII ) > 0 ) else ''
 ooO0II = OO0oO0Oo [ 0 ] if ( len ( OO0oO0Oo ) > 0 ) else ''
 OoOOoOo = OoooOO0 [ 0 ] if ( len ( OoooOO0 ) > 0 ) else ''
 Ii1Iiiiii = oo0OoO [ 0 ] if ( len ( oo0OoO ) > 0 ) else ''
 IiIii1i11i1 = iIIi1iii1 [ 0 ] if ( len ( iIIi1iii1 ) > 0 ) else 'None'
 ooOOo00o0ooO = o00o0 [ 0 ] if ( len ( o00o0 ) > 0 ) else ''
 iIOO = str ( '[COLOR=dodgerblue]Added: [/COLOR]' + OOo00O0O + '[CR][COLOR=dodgerblue]Manufacturer: [/COLOR]' + o0Oo0oO00Oooo + '[CR][COLOR=dodgerblue]Supported Roms: [/COLOR]' + OoOo0oOooOoOO + '[CR][COLOR=dodgerblue]Chipset: [/COLOR]' + ooo + '[CR][COLOR=dodgerblue]CPU: [/COLOR]' + I1IIiIi1iI + '[CR][COLOR=dodgerblue]GPU: [/COLOR]' + oOo0 + '[CR][COLOR=dodgerblue]RAM: [/COLOR]' + Iiii11 + '[CR][COLOR=dodgerblue]Flash: [/COLOR]' + o00000O + '[CR][COLOR=dodgerblue]Wi-Fi: [/COLOR]' + iIiiiII11 + '[CR][COLOR=dodgerblue]Bluetooth: [/COLOR]' + ooo00Oo0 + '[CR][COLOR=dodgerblue]LAN: [/COLOR]' + iIii1i1Ii + '[CR][CR][COLOR=yellow]About: [/COLOR]' + I1iiioO0o0O0Ooo0o + '[CR][CR][COLOR=yellow]Summary:[/COLOR][CR][CR][COLOR=dodgerblue]Pros:[/COLOR]    ' + III1iIii + '[CR][CR][COLOR=dodgerblue]Cons:[/COLOR]  ' + iiIII1i1 + '[CR][CR][COLOR=yellow]Benchmark Results:[/COLOR][CR][CR][COLOR=dodgerblue]Boot Time:[/COLOR][CR]' + I1I111 + '[CR][CR][COLOR=dodgerblue]Time taken to scan 1,000 movies (local NFO files):[/COLOR][CR]' + oOOo0OOoOO0 + '[CR][CR][COLOR=dodgerblue]Copy 4,000 files (660.8MB) locally:[/COLOR][CR]' + I1iI + '[CR][CR][COLOR=dodgerblue]Copy a MP4 file (339.4MB) locally:[/COLOR][CR]' + IIiiI + '[CR][CR][COLOR=dodgerblue]Ethernet Speed - Copy MP4 (339.4MB) from SMB share to device:[/COLOR][CR]' + ooO0II + '[CR][CR][COLOR=dodgerblue]4k Playback:[/COLOR][CR]' + IiIi + '[CR][CR][COLOR=dodgerblue]1080p Playback:[/COLOR][CR]' + IIi1IiiIi1III + '[CR][CR][COLOR=dodgerblue]720p Playback:[/COLOR][CR]' + IiIiIiiIIii + '[CR][CR][COLOR=dodgerblue]Audio Playback:[/COLOR][CR]' + iI1III + '[CR][CR][COLOR=dodgerblue]Image Slideshow:[/COLOR][CR]' + OoOOoOo )
 I1III1I11I1 = str ( '[COLOR=dodgerblue]Added: [/COLOR]' + OOo00O0O + '[CR][COLOR=dodgerblue]Manufacturer: [/COLOR]' + o0Oo0oO00Oooo + '[CR][COLOR=dodgerblue]Supported Roms: [/COLOR]' + OoOo0oOooOoOO + '[CR][COLOR=dodgerblue]Chipset: [/COLOR]' + ooo + '[CR][COLOR=dodgerblue]CPU: [/COLOR]' + I1IIiIi1iI + '[CR][COLOR=dodgerblue]GPU: [/COLOR]' + oOo0 + '[CR][COLOR=dodgerblue]RAM: [/COLOR]' + Iiii11 + '[CR][COLOR=dodgerblue]Flash: [/COLOR]' + o00000O + '[CR][COLOR=dodgerblue]Wi-Fi: [/COLOR]' + iIiiiII11 + '[CR][COLOR=dodgerblue]Bluetooth: [/COLOR]' + ooo00Oo0 + '[CR][COLOR=dodgerblue]LAN: [/COLOR]' + iIii1i1Ii + '[CR][CR][COLOR=yellow]About: [/COLOR]' + I1iiioO0o0O0Ooo0o + '[CR][CR][COLOR=yellow]Summary:[/COLOR][CR][CR][COLOR=dodgerblue]Pros:[/COLOR]    ' + III1iIii + '[CR][CR][COLOR=dodgerblue]Cons:[/COLOR]  ' + iiIII1i1 + '[CR][CR][COLOR=orange]4k Playback:[/COLOR]  ' + IiIi + '[CR][CR][COLOR=orange]1080p Playback:[/COLOR]  ' + IIi1IiiIi1III + '[CR][CR][COLOR=orange]720p Playback:[/COLOR]  ' + IiIiIiiIIii + '[CR][CR][COLOR=orange]DTS Compatibility:[/COLOR]  ' + iI1III + '[CR][CR][COLOR=orange]Time taken to scan 100 movies:[/COLOR]  ' + oOOo0OOoOO0 )
 if 85 - 85: oOOOoo0O0OoO
 if I1iiioO0o0O0Ooo0o != '' and Ii1II1I11i1I != '' :
  OOo0oO00ooO00 ( '' , '[COLOR=yellow][Text Guide][/COLOR]  Official Description' , iIOO , 'text_guide' , 'Tutorials.png' , O00o0OO , '' , '' )
 if I1iiioO0o0O0Ooo0o != '' and Ii1II1I11i1I == '' :
  OOo0oO00ooO00 ( '' , '[COLOR=yellow][Text Guide][/COLOR]  Official Description' , I1III1I11I1 , 'text_guide' , 'Tutorials.png' , O00o0OO , '' , '' )
 if IiIii1i11i1 != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]   Benchmark Review' , IiIii1i11i1 , 'play_video' , 'Video_Guide.png' , O00o0OO , '' , '' )
 if OO0oooOO != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]   Official Video Preview' , OO0oooOO , 'play_video' , 'Video_Guide.png' , O00o0OO , '' , '' )
 if OoOIiiIi1IiiiI != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]   Official Video Guide' , OoOIiiIi1IiiiI , 'play_video' , 'Video_Guide.png' , O00o0OO , '' , '' )
 if I1I != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + O0Oo0o000oO , I1I , 'play_video' , 'Video_Guide.png' , O00o0OO , '' , '' )
 if ooooo != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + oO0o00oOOooO0 , ooooo , 'play_video' , 'Video_Guide.png' , O00o0OO , '' , '' )
 if i11IIIiI1I != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + OOOoO000 , i11IIIiI1I , 'play_video' , 'Video_Guide.png' , O00o0OO , '' , '' )
 if o0iiiI1I1iIIIi1 != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + oOOOO , o0iiiI1I1iIIIi1 , 'play_video' , 'Video_Guide.png' , O00o0OO , '' , '' )
 if Iii != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + IiIi1ii111i1 , Iii , 'play_video' , 'Video_Guide.png' , O00o0OO , '' , '' )
  if 62 - 62: I1iii % II111iiii + I1I1i + Oo % ooOo . I1IiiI
  if 53 - 53: OoO0O00 % I1ii11iIi11i . IiiI11Iiiii . i1IIi . OoO0O00
def iiII1II11i ( ) :
 OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , 'hardware' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=lime]All Devices[/COLOR]' , '' , 'grab_hardware' , 'All.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=orange][Hardware][/COLOR] Game Consoles' , 'device=Console' , 'grab_hardware' , 'Consoles.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=orange][Hardware][/COLOR] HTPC' , 'device=HTPC' , 'grab_hardware' , 'HTPC.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=orange][Hardware][/COLOR] Phones' , 'device=Phone' , 'grab_hardware' , 'Phones.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=orange][Hardware][/COLOR] Set Top Boxes' , 'device=STB' , 'grab_hardware' , 'STB.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=orange][Hardware][/COLOR] Tablets' , 'device=Tablet' , 'grab_hardware' , 'Tablets.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][Accessories][/COLOR] Remotes/Keyboards' , 'device=Remote' , 'grab_hardware' , 'Remotes.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][Accessories][/COLOR] Gaming Controllers' , 'device=Controller' , 'grab_hardware' , 'Controllers.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][Accessories][/COLOR] Dongles' , 'device=Dongle' , 'grab_hardware' , 'Dongles.png' , '' , '' , '' )
 if 78 - 78: i11iIiiIii / ooOo
 if 85 - 85: iIIi1i1 - I1IiiI / i1IIi / OoO0O00 / II111iiii
def oo0O0O ( url ) :
 OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow][CPU][/COLOR] Allwinner Devices' , str ( url ) + '&chip=Allwinner' , 'grab_hardware' , 'Allwinner.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow][CPU][/COLOR] AMLogic Devices' , str ( url ) + '&chip=AMLogic' , 'grab_hardware' , 'AMLogic.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow][CPU][/COLOR] Intel Devices' , str ( url ) + '&chip=Intel' , 'grab_hardware' , 'Intel.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow][CPU][/COLOR] Rockchip Devices' , str ( url ) + '&chip=Rockchip' , 'grab_hardware' , 'Rockchip.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=lime][Platform][/COLOR] Android' , str ( url ) + '&platform=Android' , 'grab_hardware' , 'Android.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=lime][Platform][/COLOR] iOS' , str ( url ) + '&platform=iOS' , 'grab_hardware' , 'iOS.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=lime][Platform][/COLOR] Linux' , str ( url ) + '&platform=Linux' , 'grab_hardware' , 'Linux.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=lime][Platform][/COLOR] OpenELEC' , str ( url ) + '&platform=OpenELEC' , 'grab_hardware' , 'OpenELEC.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=lime][Platform][/COLOR] OSX' , str ( url ) + '&platform=OSX' , 'grab_hardware' , 'OSX.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=lime][Platform][/COLOR] Pure Linux' , str ( url ) + '&platform=Custom_Linux' , 'grab_hardware' , 'Custom_Linux.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=lime][Platform][/COLOR] Windows' , str ( url ) + '&platform=Windows' , 'grab_hardware' , 'Windows.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=orange][Flash Storage][/COLOR] 4GB' , str ( url ) + '&flash=4GB' , 'grab_hardware' , 'Flash.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=orange][Flash Storage][/COLOR] 8GB' , str ( url ) + '&flash=8GB' , 'grab_hardware' , 'Flash.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=orange][Flash Storage][/COLOR] 16GB' , str ( url ) + '&flash=16GB' , 'grab_hardware' , 'Flash.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=orange][Flash Storage][/COLOR] 32GB' , str ( url ) + '&flash=32GB' , 'grab_hardware' , 'Flash.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=orange][Flash Storage][/COLOR] 64GB' , str ( url ) + '&flash=64GB' , 'grab_hardware' , 'Flash.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][RAM][/COLOR] 1GB' , str ( url ) + '&ram=1GB' , 'grab_hardware' , 'RAM.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][RAM][/COLOR] 2GB' , str ( url ) + '&ram=2GB' , 'grab_hardware' , 'RAM.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][RAM][/COLOR] 4GB' , str ( url ) + '&ram=4GB' , 'grab_hardware' , 'RAM.png' , '' , '' , '' )
 if 45 - 45: Oo0Ooo % Oo0Ooo + Oo0Ooo / O0 % OoooooooOO
 if 92 - 92: I1iii . OoOoOO00 . OO0oo0oOO - OoooooooOO / iIIi1i1
 if 80 - 80: iIii1I11I1II1 / i11iIiiIii + IiiI11Iiiii
def I11I1i ( ) :
 oO0 = xbmc . getSkinDir ( )
 iI1i1IiIIIIi = xbmc . translatePath ( os . path . join ( Oo00OOOOO , oO0 ) )
 if 100 - 100: ooOo
 for ii1OO0 , i1iiIIIi , Oo0o in os . walk ( iI1i1IiIIIIi ) :
  if 39 - 39: II111iiii * I1IiiI - iIii1I11I1II1
  for ooOo0O0o0 in Oo0o :
   if 25 - 25: OoooooooOO . I1iii % IiiI11Iiiii . I1I1i
   if 'DialogKeyboard.xml' in ooOo0O0o0 :
    oO0 = os . path . join ( ii1OO0 , ooOo0O0o0 )
    ooo0O0o0OoOO = open ( oO0 ) . read ( )
    iIi11i = ooo0O0o0OoOO . replace ( '<control type="label" id="310"' , '<control type="edit" id="312"' )
    ooOo0O0o0 = open ( oO0 , mode = 'w' )
    ooOo0O0o0 . write ( iIi11i )
    ooOo0O0o0 . close ( )
    iiiiI1IiI1I1 ( oO0 )
    if 67 - 67: OoooooooOO + oOOOoo0O0OoO / iIIi1i1
    for I111iIIII11iI in range ( 48 , 58 ) :
     Ii1IIIII ( I111iIIII11iI , oO0 )
     if 75 - 75: I1I1i / OoooooooOO . I1IiiI + oOOOoo0O0OoO - II111iiii
 II = xbmcgui . Dialog ( )
 II . ok ( "Skin Changes Successful" , 'A BIG thank you to Mikey1234 for this fix. The code used for this function was ported from the Xunity Maintenance add-on' )
 xbmc . executebuiltin ( 'ReloadSkin()' )
 if 33 - 33: I1I1i / I1I1i . i11iIiiIii * I1ii11iIi11i + o0oOOo0O0Ooo
def ii1iI11IiIIi ( ) :
 II = xbmcgui . Dialog ( )
 IIii1i = xbmcgui . Dialog ( ) . yesno ( 'Convert This Skin To Kodi (Helix)?' , 'This will fix the problem with a blank on-screen keyboard showing in skins designed for Gotham (being run on Kodi). This will only affect the currently running skin.' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Fix' )
 if 47 - 47: Oo . ooOo + OoOoOO00 % I1I1i % i1IIi / iIii1I11I1II1
 if IIii1i == 1 :
  I11I1i ( )
  if 95 - 95: O0 . OoO0O00
  if 89 - 89: i1IIi
def I11II ( ) :
 if II . yesno ( "Hide Passwords" , "This will hide all your passwords in your" , "add-on settings, are you sure you wish to continue?" ) :
  for ii1OO0 , i1iiIIIi , Oo0o in os . walk ( Oo00OOOOO ) :
   for ooOo0O0o0 in Oo0o :
    if ooOo0O0o0 == 'settings.xml' :
     OOO = open ( os . path . join ( ii1OO0 , ooOo0O0o0 ) ) . read ( )
     I111i1I1 = re . compile ( '<setting id=(.+?)>' ) . findall ( OOO )
     for O0iiii in I111i1I1 :
      if 'pass' in O0iiii :
       if not 'option="hidden"' in O0iiii :
        try :
         oOOOOOoOOoo0 = O0iiii . replace ( '/' , ' option="hidden"/' )
         ooOo0O0o0 = open ( os . path . join ( ii1OO0 , ooOo0O0o0 ) , mode = 'w' )
         ooOo0O0o0 . write ( str ( OOO ) . replace ( O0iiii , oOOOOOoOOoo0 ) )
         ooOo0O0o0 . close ( )
        except :
         pass
  II . ok ( "Passwords Hidden" , "Your passwords will now show as stars (hidden), if you want to undo this please use the option to unhide passwords." )
  if 93 - 93: II111iiii * OoOoOO00 % o0oOOo0O0Ooo
  if 67 - 67: o0oOOo0O0Ooo + Oo0Ooo . iIIi1i1 - i1IIi . OoOoOO00
def I1iI1 ( url ) :
 Oo0O00O000 = 'http://totalxbmc.com/IT/Community_Builds/guisettings.php?id=%s' % ( url )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 o0O0Ooo = re . compile ( 'guisettings="(.+?)"' ) . findall ( i11I1IiII1i1i )
 ii111iiIii = o0O0Ooo [ 0 ] if ( len ( o0O0Ooo ) > 0 ) else 'None'
 if 9 - 9: Oo0Ooo - iIIi1i1 * IiiI11Iiiii / i11iIiiIii / Oo0Ooo % ooOo
 OoIi11ii1 ( ii111iiIii , I1Ii1IIi )
 if 17 - 17: IiiI11Iiiii - OoooooooOO % ooOo * I1I1i
 if 28 - 28: II111iiii * iIIi1i1 * OoOoOO00 * oOOOoo0O0OoO . II111iiii . I1ii11iIi11i
def I1iIi1111 ( path ) :
 IIi1i1i1i = xbmc . translatePath ( os . path . join ( II11iiii1Ii , 'background_art' , '' ) )
 if 74 - 74: OoO0O00 . I1iii % iIii1I11I1II1 . iIii1I11I1II1 / OoOoOO00 - Oo
 if os . path . exists ( IIi1i1i1i ) :
  O0Ooo0O ( IIi1i1i1i )
  if 30 - 30: OO0oo0oOO
 time . sleep ( 1 )
 if 46 - 46: iIIi1i1
 if not os . path . exists ( IIi1i1i1i ) :
  os . makedirs ( IIi1i1i1i )
  if 92 - 92: iIIi1i1 / I1I1i + iIii1I11I1II1
 try :
  ooOoOoo0O . create ( "Installing Artwork" , "Downloading artwork pack" , '' , 'Please Wait' )
  OoOo0OO0oooo = os . path . join ( Ooo0OO0oOO , O0oo0OO0 + '_artpack.zip' )
  downloader . download ( path , OoOo0OO0oooo , ooOoOoo0O )
  time . sleep ( 1 )
  ooOoOoo0O . create ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "Checking " , '' , 'Please Wait' )
  ooOoOoo0O . update ( 0 , "" , "Extracting Zip Please Wait" )
  oOOO ( OoOo0OO0oooo , IIi1i1i1i , ooOoOoo0O )
  if 47 - 47: Oo * I1iii % iIii1I11I1II1 / iIIi1i1
 except :
  pass
  if 61 - 61: I1I1i + IiiI11Iiiii - OoO0O00 * ooOo
  if 87 - 87: II111iiii % II111iiii
def o0oo0oOOOo00 ( url ) :
 OOo0oO00ooO00 ( '' , '[COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] Keyword Install' , IIIi1I1IIii1II , 'keywords' , 'Keywords.png' , '' , '' , '' )
 if i1111 == 'true' :
  OOo0oO00ooO00 ( 'folder' , 'Manage Add-ons' , oo00O00oO , 'addonmenu' , 'Search_Addons.png' , '' , '' , '' )
  if 57 - 57: o0oOOo0O0Ooo + Oo0Ooo * I1ii11iIi11i - iIIi1i1 % iIii1I11I1II1 - I1iii
 if i11 == 'true' :
  OOo0oO00ooO00 ( 'folder' , 'Community Builds' , url , 'community' , 'Community_Builds.png' , '' , '' , '' )
  if 37 - 37: OoO0O00 * OO0oo0oOO + I1iii + I1ii11iIi11i * o0oOOo0O0Ooo
  if 95 - 95: I1iii - i11iIiiIii % i11iIiiIii - O0 * oOOOoo0O0OoO
def Oo0O0oOoO0o0 ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(10040,"addons://install/",return)' )
 if 21 - 21: I1IiiI - I1IiiI + IiiI11Iiiii % I1IiiI * ooOo
 if 74 - 74: IiiI11Iiiii / OO0oo0oOO . I1IiiI - OoooooooOO + II111iiii + OO0oo0oOO
def OoOooo ( repo_id ) :
 if 36 - 36: I1iii * I1IiiI * I1ii11iIi11i . OO0oo0oOO * I1ii11iIi11i
 if 76 - 76: Oo + O0 / I1I1i - OoO0O00
 OO0OOO0oOOo00O = 1
 Oo0O00O000 = 'http://totalxbmc.com/TI/AddonPortal/dependencyinstall.php?id=%s' % ( repo_id )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0oO = re . compile ( 'name="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IIo0Oo0oO0oOO00 = re . compile ( 'version="(.+?)"' ) . findall ( i11I1IiII1i1i )
 ooO000OO0O00O = re . compile ( 'repo_url="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OOOoOO0o = re . compile ( 'data_url="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i1II1 = re . compile ( 'zip_url="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oo00oO0o = re . compile ( 'repo_id="(.+?)"' ) . findall ( i11I1IiII1i1i )
 II1i111i = oo0oO [ 0 ] if ( len ( oo0oO ) > 0 ) else ''
 IiIiIi = IIo0Oo0oO0oOO00 [ 0 ] if ( len ( IIo0Oo0oO0oOO00 ) > 0 ) else ''
 I1IIIi1i = ooO000OO0O00O [ 0 ] if ( len ( ooO000OO0O00O ) > 0 ) else ''
 OooIii1I1iI = OOOoOO0o [ 0 ] if ( len ( OOOoOO0o ) > 0 ) else ''
 oOoOo0 = i1II1 [ 0 ] if ( len ( i1II1 ) > 0 ) else ''
 iIi = oo00oO0o [ 0 ] if ( len ( oo00oO0o ) > 0 ) else ''
 oOoO0oO00ooOo = xbmc . translatePath ( os . path . join ( i1Oo00 , iIi + '.zip' ) )
 iIoOO0OO00 = xbmc . translatePath ( os . path . join ( Oo00OOOOO , iIi ) )
 if 75 - 75: IiiI11Iiiii * Oo0Ooo / oOOOoo0O0OoO * Oo0Ooo / iIIi1i1
 ooOoOoo0O . create ( 'Installing Repository' , 'Please wait...' , '' )
 if 14 - 14: i1IIi * iIii1I11I1II1 - I1iii * OoOoOO00 - IiiI11Iiiii / ooOo
 try :
  downloader . download ( I1IIIi1i , oOoO0oO00ooOo , ooOoOoo0O )
  oOOO ( oOoO0oO00ooOo , Oo00OOOOO , ooOoOoo0O )
  xbmc . executebuiltin ( 'UpdateLocalAddons' )
  xbmc . executebuiltin ( 'UpdateAddonRepos' )
  if 73 - 73: I1ii11iIi11i - OoOoOO00 * O0 - OoOoOO00 - OoO0O00
 except :
  if 96 - 96: I1ii11iIi11i - O0
  try :
   downloader . download ( oOoOo0 , oOoO0oO00ooOo , ooOoOoo0O )
   oOOO ( oOoO0oO00ooOo , Oo00OOOOO , ooOoOoo0O )
   xbmc . executebuiltin ( 'UpdateLocalAddons' )
   xbmc . executebuiltin ( 'UpdateAddonRepos' )
   if 35 - 35: Oo . OO0oo0oOO . oOOOoo0O0OoO - OO0oo0oOO % OO0oo0oOO + oOOOoo0O0OoO
  except :
   if 99 - 99: o0oOOo0O0Ooo + Oo
   try :
    if 34 - 34: oOOOoo0O0OoO * o0oOOo0O0Ooo . I1IiiI % i11iIiiIii
    if not os . path . exists ( iIoOO0OO00 ) :
     os . makedirs ( iIoOO0OO00 )
     if 61 - 61: iIii1I11I1II1 + ooOo * OO0oo0oOO - i1IIi % ooOo
    i11I1IiII1i1i = ooI1111i ( OooIii1I1iI ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
    I111i1I1 = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( i11I1IiII1i1i )
    if 76 - 76: ooOo / OoOoOO00
    for II1Ii1iI1i1 in I111i1I1 :
     o0OoO000O = xbmc . translatePath ( os . path . join ( iIoOO0OO00 , II1Ii1iI1i1 ) )
     if 12 - 12: oOOOoo0O0OoO
     if Oo0o0000OOoO not in II1Ii1iI1i1 and '/' not in II1Ii1iI1i1 :
      if 58 - 58: OoO0O00 + iIii1I11I1II1 % O0 + OO0oo0oOO + OoOoOO00 * OoooooooOO
      try :
       ooOoOoo0O . update ( 0 , "Downloading [COLOR=yellow]" + II1Ii1iI1i1 + '[/COLOR]' , '' , 'Please wait...' )
       downloader . download ( OooIii1I1iI + II1Ii1iI1i1 , o0OoO000O , ooOoOoo0O )
       if 41 - 41: ooOo * I1IiiI
      except : print "failed to install" + II1Ii1iI1i1
      if 76 - 76: ooOo . O0 * OoooooooOO + iIIi1i1
     if '/' in II1Ii1iI1i1 and '..' not in II1Ii1iI1i1 and 'http' not in II1Ii1iI1i1 :
      iIIiI1I1i = OooIii1I1iI + II1Ii1iI1i1
      O0O0OOooOO0 ( o0OoO000O , iIIiI1I1i )
      if 53 - 53: Oo0Ooo
   except :
    II . ok ( "Error downloading repository" , 'There was an error downloading[CR][COLOR=dodgerblue]' + II1i111i + '[/COLOR]. Please consider updating the add-on portal with details or report the error on the forum at [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR]' )
    OO0OOO0oOOo00O = 0
    if 3 - 3: I1I1i - OoooooooOO * OoooooooOO - I1IiiI / oOOOoo0O0OoO * I1ii11iIi11i
    if 58 - 58: I1I1i % iIii1I11I1II1 / i11iIiiIii % o0oOOo0O0Ooo . oOOOoo0O0OoO * IiiI11Iiiii
 if OO0OOO0oOOo00O == 1 :
  time . sleep ( 1 )
  ooOoOoo0O . update ( 0 , "[COLOR=yellow]" + II1i111i + '[/COLOR]  [COLOR=lime]Successfully Installed[/COLOR]' , '' , 'Now installing dependencies' )
  time . sleep ( 1 )
  OOo = 'http://totalxbmc.com/TI/AddonPortal/downloadcount.php?id=%s' % ( repo_id )
  ooI1111i ( OOo )
  if 32 - 32: OoooooooOO + o0oOOo0O0Ooo
  if 91 - 91: iIIi1i1 - oOOOoo0O0OoO * oOOOoo0O0OoO
def ooOOOo0 ( ) :
 OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][TEXT GUIDE][/COLOR]  What is Community Builds?' , 'url' , 'instructions_3' , 'How_To.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][TEXT GUIDE][/COLOR]  Creating a Community Build' , 'url' , 'instructions_1' , 'How_To.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][TEXT GUIDE][/COLOR]  Installing a Community Build' , 'url' , 'instructions_2' , 'How_To.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  Add Your Own Guides @ [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR]' , 'K0XIxEodUhc' , 'play_video' , 'How_To.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  Community Builds FULL GUIDE' , "ewuxVfKZ3Fs" , 'play_video' , 'howto.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  IMPORTANT initial settings' , "1vXniHsEMEg" , 'play_video' , 'howto.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  Install a Community Build' , "kLsVOapuM1A" , 'play_video' , 'howto.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  Fixing a half installed build (guisettings.xml fix)' , "X8QYLziFzQU" , 'play_video' , 'howto.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  [COLOR=yellow](OLD METHOD)[/COLOR]Create a Community Build (part 1)' , "3rMScZF2h_U" , 'play_video' , 'howto.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO GUIDE][/COLOR]  [COLOR=yellow](OLD METHOD)[/COLOR]Create a Community Build (part 2)' , "C2IPhn0OSSw" , 'play_video' , 'howto.png' , '' , '' , '' )
 if 19 - 19: oOOOoo0O0OoO + IiiI11Iiiii * oOOOoo0O0OoO
 if 71 - 71: o0oOOo0O0Ooo . I1IiiI - I1ii11iIi11i - Oo0Ooo - i1IIi - I1IiiI
def iIIiiiIIi1111 ( ) :
 IiI1IiI1iiI1 ( 'Creating A Community Backup' ,
 '[COLOR=yellow]NEW METHOD[/COLOR][CR][COLOR=blue][B]Step 1:[/COLOR] Remove any sensitive data[/B][CR]Make sure you\'ve removed any sensitive data such as passwords and usernames in your addon_data folder.'
 '[CR][CR][COLOR=blue][B]Step 2:[/COLOR] Backup your system[/B][CR]Choose the backup option from the main menu, in there you\'ll find the option to create a Full Backup and this will create two zip files that you need to upload to a server.'
 '[CR][CR][COLOR=blue][B]Step 3:[/COLOR] Upload the zips[/B][CR]Upload the two zip files to a server that Kodi can access, it has to be a direct link and not somewhere that asks for captcha - Dropbox and archive.org are two good examples.'
 '[CR][CR][COLOR=blue][B]Step 4:[/COLOR] Submit build at [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR][/B]'
 '[CR]Create a thread on the Community Builds section of the forum at [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR].[CR]Full details can be found on there of the template you should use when posting, once you\'ve created your support thread (NOT BEFORE) you can request to become a member of the Community Builder group and you\'ll then have access to the web form for adding your builds to the portal.'
 '[CR][CR][COLOR=yellow]OLD METHOD[/COLOR][CR][COLOR=blue][B]Step 1: Backup your system[/B][/COLOR][CR]Choose the backup option from the main menu, you will be asked whether you would like to delete your addon_data folder. If you decide to choose this option [COLOR=yellow][B]make sure[/COLOR][/B] you already have a full backup of your system as it will completely wipe your addon settings (any stored settings such as passwords or any other changes you\'ve made to addons since they were first installed). If sharing a build with the community it\'s highly advised that you wipe your addon_data but if you\'ve made changes or installed extra data packages (e.g. skin artwork packs) then backup the whole build and then manually delete these on your PC and zip back up again (more on this later).'
 '[CR][CR][COLOR=blue][B]Step 2: Edit zip file on your PC[/B][/COLOR][CR]Copy your backup.zip file to your PC, extract it and delete all the addons and addon_data that isn\'t required.'
 '[CR][COLOR=blue]What to delete:[/COLOR][CR][COLOR=lime]/addons/packages[/COLOR] This folder contains zip files of EVERY addon you\'ve ever installed - it\'s not needed.'
 '[CR][COLOR=lime]/addons/<skin.xxx>[/COLOR] Delete any skins that aren\'t used, these can be very big files.'
 '[CR][COLOR=lime]/addons/<addon_id>[/COLOR] Delete any other addons that aren\'t used, it\'s easy to forget you\'ve got things installed that are no longer needed.'
 '[CR][COLOR=lime]/userdata/addon_data/<addon_id>[/COLOR] Delete any folders that don\'t contain important changes to addons. If you delete these the associated addons will just reset to their default values.'
 '[CR][COLOR=lime]/userdata/<all other folders>[/COLOR] Delete all other folders in here such as keymaps. If you\'ve setup profiles make sure you [COLOR=yellow][B]keep the profiles directory[/COLOR][/B].'
 '[CR][COLOR=lime]/userdata/Thumbnails/[/COLOR] Delete this folder, it contains all cached artwork. You can safely delete this but must also delete the file listed below.'
 '[CR][COLOR=lime]/userdata/Database/Textures13.db[/COLOR] Delete this and it will tell XBMC to regenerate your thumbnails - must do this if delting thumbnails folder.'
 '[CR][COLOR=lime]/xbmc.log (or Kodi.log)[/COLOR] Delete your log files, this includes any crashlog files you may have.'
 '[CR][CR][COLOR=blue][B]Step 3: Compress and upload[/B][/COLOR][CR]Use a program like 7zip to create a zip file of your remaining folders and upload to a file sharing site like dropbox.'
 '[CR][CR][COLOR=blue][B]Step 4: Submit build at [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR][/B][/COLOR]'
 '[CR]Create a thread on the Community Builds section of the forum at [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR][/B].[CR]Full details can be found on there of the template you should use when posting.' )
 if 53 - 53: oOOOoo0O0OoO
 if 31 - 31: o0oOOo0O0Ooo * OO0oo0oOO - i11iIiiIii - I1IiiI
def I1OoO00o00 ( ) :
 IiI1IiI1iiI1 ( 'Installing a build' , '[COLOR=blue][B]Step 1 (Optional): Backup your system[/B][/COLOR][CR]When selecting an install option you\'ll be asked if you want to create a backup - we strongly recommend creating a backup of your system in case you don\'t like the build and want to revert back. Remember your backup may be quite large so if you\'re using a device with a very small amount of storage we recommend using a USB stick or SD card as the storage location otherwise you may run out of space and the install may fail.'
 '[CR][CR][COLOR=blue][B]Step 2: Choose an install method:[/B][/COLOR][CR][CR]-------------------------------------------------------[CR][CR][COLOR=lime]1. Fresh Install:[/COLOR] This will wipe all existing settings[CR]As the title suggests this will completely wipe all your current Kodi settings. Your settings will be replaced with the ones uploaded by the build author, some builders like to use this method (especially if they have the Live TV PVR setup) so always check the description to find out if they recommend using this method. This method is also great if you feel there\'s content installed on your Kodi install that may be causing issues, it will fully wipe your Kodi and install the build over the top.'
 '[CR][CR]-------------------------------------------------------[CR][CR][COLOR=lime]2. Install:[/COLOR] Keep my library & profiles[CR]This will install a build over the top of your existing setup so you won\'t lose anything already installed in Kodi. Your library and any profiles you may have setup will also remain unchanged.'
 '[CR][CR]-------------------------------------------------------[CR][CR][COLOR=lime]3. Install:[/COLOR] Keep my library only[CR]This will do exactly the same as number 2 (above) but it will delete any profiles you may have and replace them with the ones the build author has created.'
 '[CR][CR]-------------------------------------------------------[CR][CR][COLOR=lime]4. Install:[/COLOR] Keep my profiles only[CR]Again, the same as number 2 but your library will be replaced with the one created by the build author. If you\'ve spent a long time setting up your library and have it just how you want it then use this with caution and make sure you do a backup!'
 '[CR][CR]-------------------------------------------------------[CR][CR][COLOR=blue][B]Step 3: Replace or keep settings?[/COLOR][/B][CR]When completing the install process (only on options 2-4) you\'ll be asked if you want to keep your existing Kodi settings or replace with the ones in the build. If you choose to keep your settings then only the important skin related settings are copied over from the build. All your other Kodi settings such as screen calibration, region, audio output, resolution etc. will remain intact. Choosing to replace your settings could possibly cause a few issues, unless the build author has specifically recommended you replace the settings with theirs we would always recommend keeping your own.'
 '[CR][CR][COLOR=blue][B]Step 4: [/COLOR][COLOR=red]VERY IMPORTANT[/COLOR][/B][CR]For the install to complete properly Kodi MUST force close, this means forcing it to close via your operating system rather than elegantly via the Kodi menu. By default this add-on will attempt to make your operating system force close Kodi but there are systems that will not allow this (devices that do not allow Kodi to have root permissions).'
 ' Once the final step of the install process has been completed you\'ll see a dialog explaining Kodi is attempting a force close, please be patient and give it a minute. If after a minute Kodi hasn\'t closed or restarted you will need to manually force close. The recommended solution for force closing is to go into your operating system menu and make it force close the Kodi app but if you dont\'t know how to do that you can just pull the power from the unit.'
 ' Pulling the power is fairly safe these days, on most set top boxes it\'s the only way to switch them off - they rarely have a power switch. Even though it\'s considered fairly safe nowadays you do this at your own risk and we would always recommend force closing via the operating system menu.' )
 if 72 - 72: i1IIi
 if 21 - 21: oOOOoo0O0OoO . Oo / i11iIiiIii * i1IIi
def O00O0ooo00OO0 ( ) :
 IiI1IiI1iiI1 ( 'What is a community build' , 'Community Builds are pre-configured builds of XBMC/Kodi based on different users setups. Have you ever watched youtube videos or seen screenshots of Kodi in action and thought "wow I wish I could do that"? Well now you can have a brilliant setup at the click of a button, completely pre-configured by users on the [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR][/B] forum. If you\'d like to get involved yourself and share your build with the community it\'s very simple to do, just go to the forum where you\'ll find full details or you can follow the guide in this addon.' )
 if 63 - 63: OO0oo0oOO * II111iiii
 if 70 - 70: II111iiii + IiiI11Iiiii * OoOoOO00
def O0OOoO ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 I111i1I1 = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( Oo0OoO00oOO0o . http_GET ( url ) . content )
 for Iii1i11 , IIii1 , OOo0Ooo0 , IiIIiIi11ii in I111i1I1 :
  if inc < 2 : II = xbmcgui . Dialog ( ) ; II . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % Iii1i11 , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % OOo0Ooo0 , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % IiIIiIi11ii )
  inc = inc + 1
  if 32 - 32: I1IiiI * oOOOoo0O0OoO * i1IIi + ooOo
  if 40 - 40: II111iiii
def iII1 ( url ) :
 if not os . path . exists ( i1Oo00 ) :
  os . makedirs ( i1Oo00 )
  if 7 - 7: I1ii11iIi11i - iIii1I11I1II1
 oOOOo0Oooo = ''
 ooOoOii1iII = 'Enter Keyword'
 I1iiIIiI11I = I11II1I ( ooOoOii1iII )
 oOOOo0Oooo = url + I1iiIIiI11I
 I1IiiIi11 = os . path . join ( i1Oo00 , I1iiIIiI11I + '.zip' )
 if 92 - 92: o0oOOo0O0Ooo
 if I1iiIIiI11I != '' :
  ii111Ii1i = II . yesno ( 'Backup existing setup' , 'Installing certain keywords can result in some existing settings or add-ons to be replaced. Would you like to create a backup before proceeding?' )
  if 46 - 46: i1IIi - IiiI11Iiiii + oOOOoo0O0OoO + OoO0O00 + OO0oo0oOO
  if ii111Ii1i == 1 :
   iiI1ii ( )
   if 20 - 20: Oo * ooOo
  try :
   print "Attempting download " + oOOOo0Oooo + " to " + I1IiiIi11
   ooOoOoo0O . create ( "Web Installer" , "Downloading " , '' , 'Please Wait' )
   downloader . download ( oOOOo0Oooo , I1IiiIi11 )
   print "### Keyword " + I1iiIIiI11I + " Successfully downloaded"
   ooOoOoo0O . update ( 0 , "" , "Extracting Zip Please Wait" )
   if 91 - 91: OoO0O00 % i1IIi - iIii1I11I1II1 . Oo
   if zipfile . is_zipfile ( I1IiiIi11 ) :
    if 31 - 31: ooOo % i1IIi . OoooooooOO - o0oOOo0O0Ooo + OoooooooOO
    try :
     oOOO ( I1IiiIi11 , OooO0 , ooOoOoo0O )
     xbmc . executebuiltin ( 'UpdateLocalAddons' )
     xbmc . executebuiltin ( 'UpdateAddonRepos' )
     II . ok ( "[COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR]" , "" , "Content now installed" , "" )
     ooOoOoo0O . close ( )
     if 45 - 45: Oo + OO0oo0oOO / OoooooooOO - I1iii + OoooooooOO
    except :
     II . ok ( "Error with zip" , 'There was an error trying to install this file. It may possibly be corrupt, either try again or contact the author of this keyword.' )
     print "### Unable to install keyword (passed zip check): " + I1iiIIiI11I
   else :
    II . ok ( "Keyword Error" , 'The keyword you typed could not be installed. Please check the spelling and if you continue to receive this message it probably means that keyword is no longer available.' )
    if 42 - 42: iIii1I11I1II1 * I1IiiI * oOOOoo0O0OoO
  except :
   II . ok ( "Keyword Error" , 'The keyword you typed could not be installed. Please check the spelling and if you continue to receive this message it probably means that keyword is no longer available.' )
   print "### Unable to install keyword (unknown error, most likely a typo in keyword entry): " + I1iiIIiI11I
   if 62 - 62: Oo * O0 % I1I1i . I1I1i . I1IiiI
 if os . path . exists ( I1IiiIi11 ) :
  os . remove ( I1IiiIi11 )
  if 91 - 91: i1IIi . IiiI11Iiiii
  if 37 - 37: IiiI11Iiiii - OO0oo0oOO + iIii1I11I1II1 / oOOOoo0O0OoO - OoO0O00 . o0oOOo0O0Ooo
def IiIIIi ( ) :
 II . ok ( '[COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR]' , 'The system will now attempt to force close Kodi.' , 'You may encounter a freeze, if that happens give it a minute' , 'and if it doesn\'t close please restart your system.' )
 if xbmc . getCondVisibility ( 'system.platform.windows' ) :
  print "############   try windows force close  #################"
  try :
   os . system ( '@ECHO off' )
   os . system ( 'TASKKILL /im Kodi.exe /f' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'tskill Kodi.exe' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'tskill XBMC.exe' )
  except : pass
  try :
   os . system ( '@ECHO off' )
   os . system ( 'TASKKILL /im XBMC.exe /f' )
  except : pass
 elif xbmc . getCondVisibility ( 'system.platform.osx' ) :
  print "############   try osx force close  #################"
  try : os . system ( 'killall -9 XBMC' )
  except : pass
  try : os . system ( 'killall -9 Kodi' )
  except : pass
 else :
  if 62 - 62: I1ii11iIi11i
  print "############   try linux force close  #################"
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  if 47 - 47: oOOOoo0O0OoO % Oo * OoO0O00 . iIii1I11I1II1 % Oo0Ooo + OoooooooOO
  print "############   try atv force close  #################"
  try : os . system ( 'killall AppleTV' )
  except : pass
  print "############   try raspbmc force close  #################"
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  if 2 - 2: oOOOoo0O0OoO % OoooooooOO - iIIi1i1 * I1ii11iIi11i * I1I1i
  print "############   try android force close  #################"
  try : os . system ( 'adb shell am force-stop org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.kodi' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell am force-stop org.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.kodi' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc.xbmc' )
  except : pass
  try : os . system ( 'adb shell kill org.xbmc' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc,kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.kodi());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc.xbmc());' )
  except : pass
  try : os . system ( 'Process.killProcess(android.os.Process.org.xbmc());' )
  except : pass
  try : xbmc . executebuiltin ( 'StartAndroidActivity(android.provider.Settings)' )
  except : pass
  if 99 - 99: iIii1I11I1II1 . Oo0Ooo / iIIi1i1 . Oo % I1IiiI * OO0oo0oOO
  if 95 - 95: ooOo
def oOo0ooO0O0oo ( ) :
 xbmc . executebuiltin ( 'ReplaceWindow(settings)' )
 if 31 - 31: i11iIiiIii + I1iii % OoOoOO00
 if 9 - 9: iIIi1i1 . OO0oo0oOO - Oo0Ooo . oOOOoo0O0OoO
 if 39 - 39: Oo
 if 70 - 70: I1I1i % OoO0O00 % I1IiiI
def iiI1ii ( ) :
 III1II1i ( )
 if 95 - 95: OoOoOO00 - oOOOoo0O0OoO / O0 * I1IiiI - o0oOOo0O0Ooo
 II1Ii1I1i = xbmc . translatePath ( os . path . join ( Ooo0OO0oOO , 'Community Builds' , 'My Builds' , '' ) )
 OOooOooo0OOo0 = xbmc . translatePath ( os . path . join ( Ooo0OO0oOO , 'Community Builds' , 'My Builds' , 'my_full_backup.zip' ) )
 oo0o0OoOO0o0 = xbmc . translatePath ( os . path . join ( Ooo0OO0oOO , 'Community Builds' , 'My Builds' , 'my_full_backup_GUI_Settings.zip' ) )
 if 12 - 12: iIii1I11I1II1 % Oo0Ooo . IiiI11Iiiii . I1I1i % i11iIiiIii
 if not os . path . exists ( II1Ii1I1i ) :
  os . makedirs ( II1Ii1I1i )
  if 2 - 2: ooOo * ooOo . OoOoOO00 * I1iii * iIii1I11I1II1
 IiI1Iii1 = Ooooo ( heading = "Enter a name for this backup" )
 if 13 - 13: OO0oo0oOO / O0 . i11iIiiIii * i1IIi % i11iIiiIii
 if ( not IiI1Iii1 ) :
  return False , 0
  if 8 - 8: OoOoOO00 - OoooooooOO
 ooOoOii1iII = urllib . quote_plus ( IiI1Iii1 )
 O00oo = xbmc . translatePath ( os . path . join ( II1Ii1I1i , ooOoOii1iII + '.zip' ) )
 OoOoooO000OO = [ I1IiI ]
 O00Oooi1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'Thumbs.db' , '.gitignore' ]
 OOoooOoO0Oo = "Creating full backup of existing build"
 OOoOOOO00 = "Creating Community Build"
 Oo000 = "Archiving..."
 iiIiII11i1 = ""
 oOo00Ooo0o0 = "Please Wait"
 if 99 - 99: II111iiii / I1I1i % OoooooooOO . i11iIiiIii
 o0O0OO ( OooO0 , OOooOooo0OOo0 , OOoooOoO0Oo , Oo000 , iiIiII11i1 , oOo00Ooo0o0 , OoOoooO000OO , O00Oooi1 )
 II . ok ( 'Full Backup Complete' , 'You can locate your backup at:[COLOR=dodgerblue]' , OOooOooo0OOo0 + '[/COLOR]' )
 if 18 - 18: o0oOOo0O0Ooo . iIIi1i1
 if 70 - 70: OoooooooOO . iIIi1i1 / ooOo . ooOo - o0oOOo0O0Ooo
def i1II1i1iiI1 ( ) :
 IIIIiI11I = xbmc . getInfoLabel ( "System.BuildVersion" )
 IiIiIi = float ( IIIIiI11I [ : 4 ] )
 if 62 - 62: I1iii . i11iIiiIii % O0 % oOOOoo0O0OoO - Oo0Ooo
 if IiIiIi < 14 :
  OooOO0o0oOoO = os . path . join ( Ii1iIiII1ii1 , 'xbmc.log' )
  IiI1IiI1iiI1 ( 'XBMC Log' , OooOO0o0oOoO )
  if 47 - 47: IiiI11Iiiii * OoOoOO00 * I1I1i
 else :
  OooOO0o0oOoO = os . path . join ( Ii1iIiII1ii1 , 'kodi.log' )
  IiI1IiI1iiI1 ( 'Kodi Log' , OooOO0o0oOoO )
  if 46 - 46: I1iii
  if 42 - 42: iIii1I11I1II1
def IIi1IiIii ( ) :
 II . ok ( "Restore local guisettings fix" , "You should [COLOR=lime]ONLY[/COLOR] use this option if the guisettings fix is failing to download via the addon. Installing via this method means you do not receive notifications of updates" )
 iiIi1I ( )
 if 23 - 23: OoO0O00 % OoooooooOO * iIIi1i1
 if 6 - 6: I1IiiI . II111iiii + oOOOoo0O0OoO / OoO0O00 % I1IiiI . OoooooooOO
def Oooo000 ( mode ) :
 if not mode . endswith ( "premium" ) and not mode . endswith ( "public" ) and not mode . endswith ( "private" ) :
  IiI1Iii1 = Ooooo ( heading = "Search for content" )
  if 37 - 37: OoO0O00 . i1IIi + i1IIi / I1IiiI * iIIi1i1 * I1iii
  if ( not IiI1Iii1 ) :
   return False , 0
   if 56 - 56: OoooooooOO / I1IiiI . iIIi1i1 - i1IIi
  ooOoOii1iII = urllib . quote_plus ( IiI1Iii1 )
  if 60 - 60: OoOoOO00 % OoOoOO00
  if mode == 'tutorials' :
   iII1iiiiI1i ( 'name=' + ooOoOii1iII )
   if 2 - 2: I1iii . O0 - ooOo + I1I1i
  if mode == 'hardware' :
   III1I1ii ( 'name=' + ooOoOii1iII )
   if 96 - 96: I1iii + I1iii
  if mode == 'news' :
   i11111 ( 'name=' + ooOoOii1iII )
   if 28 - 28: IiiI11Iiiii
 if mode . endswith ( "premium" ) or mode . endswith ( "public" ) or mode . endswith ( "private" ) :
  OOo0oO00ooO00 ( 'folder' , 'Search By Name' , mode + '&name=' , 'search_builds' , 'Manual_Search.png' , '' , '' , '' )
  OOo0oO00ooO00 ( 'folder' , 'Search By Uploader' , mode + '&author=' , 'search_builds' , 'Search_Genre.png' , '' , '' , '' )
  OOo0oO00ooO00 ( 'folder' , 'Search By Audio Addons Installed' , mode + '&audio=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  OOo0oO00ooO00 ( 'folder' , 'Search By Picture Addons Installed' , mode + '&pics=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  OOo0oO00ooO00 ( 'folder' , 'Search By Program Addons Installed' , mode + '&progs=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  OOo0oO00ooO00 ( 'folder' , 'Search By Video Addons Installed' , mode + '&vids=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  OOo0oO00ooO00 ( 'folder' , 'Search By Skins Installed' , mode + '&skins=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  if 6 - 6: I1IiiI - IiiI11Iiiii
  if 49 - 49: II111iiii
def II1I1Ii11 ( url ) :
 Oo0O00O000 = 'http://totalxbmc.com/TI/LatestNews/LatestNews.php?id=%s' % ( url )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0oO = re . compile ( 'name="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i11I = re . compile ( 'author="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1I1iiI = re . compile ( 'date="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1II1 = re . compile ( 'content="(.+?)###END###"' ) . findall ( i11I1IiII1i1i )
 if 77 - 77: OoOoOO00
 I1ii1 = oo0oO [ 0 ] if ( len ( oo0oO ) > 0 ) else ''
 I11II1i1 = i11I [ 0 ] if ( len ( i11I ) > 0 ) else ''
 o0OoOo00O0o0O = I1I1iiI [ 0 ] if ( len ( I1I1iiI ) > 0 ) else ''
 iii = I1II1 [ 0 ] if ( len ( I1II1 ) > 0 ) else ''
 oOO0ooo0O = I1I1i1i ( iii )
 I1iiioO0o0O0Ooo0o = str ( '[COLOR=orange]Source: [/COLOR]' + I11II1i1 + '     [COLOR=orange]Date: [/COLOR]' + o0OoOo00O0o0O + '[CR][CR][COLOR=lime]Details: [/COLOR][CR]' + oOO0ooo0O )
 if 17 - 17: iIIi1i1
 IiI1IiI1iiI1 ( I1ii1 , I1iiioO0o0O0Ooo0o )
 if 13 - 13: Oo0Ooo - OO0oo0oOO / ooOo - Oo0Ooo - IiiI11Iiiii / i11iIiiIii
 if 29 - 29: I1I1i - OO0oo0oOO . O0 . O0
def Ii11II1IIIIIi ( url ) :
 if iI1Ii11111iIi == 'true' :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]Latest ' + O0oo0OO0 + ' news[/COLOR]' , O0oo0OO0 , 'notify_msg' , 'LatestNews.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , 'news' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=lime][All News][/COLOR] From all sites' , str ( url ) + '' , 'grab_news' , 'Latest.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Official Kodi.tv News' , str ( url ) + '&author=Official%20Kodi' , 'grab_news' , 'XBMC.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'OpenELEC News' , str ( url ) + '&author=OpenELEC' , 'grab_news' , 'OpenELEC.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Raspbmc News' , str ( url ) + '&author=Raspbmc' , 'grab_news' , 'Raspbmc.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] News' , str ( url ) + '&author=noobsandnerds' , 'grab_news' , 'noobsandnerds.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'XBMC4Xbox News' , str ( url ) + '&author=XBMC4Xbox' , 'grab_news' , 'XBMC4Xbox.png' , '' , '' , '' )
 if 83 - 83: iIii1I11I1II1 + II111iiii * ooOo / O0 - IiiI11Iiiii
 if 23 - 23: i1IIi
def iIi11i1I11Ii ( title , message , times , icon ) :
 icon = OOOO0OOoO0O0 + icon
 xbmc . executebuiltin ( "XBMC.Notification(" + title + "," + message + "," + times + "," + icon + ")" )
 if 59 - 59: i11iIiiIii - OO0oo0oOO
def oooO00oOOooO ( url ) :
 Ii11iIiiI = xbmc . translatePath ( os . path . join ( OO0o , I1IiI , 'notification.txt' ) )
 if 34 - 34: iIii1I11I1II1 / II111iiii
 if not os . path . exists ( Ii11iIiiI ) :
  Oo0oO00 = open ( Ii11iIiiI , mode = 'w' )
  Oo0oO00 . write ( '20150101000000' )
  Oo0oO00 . close ( )
  if 3 - 3: o0oOOo0O0Ooo - OoooooooOO + IiiI11Iiiii . OO0oo0oOO
 o00000Oo = open ( Ii11iIiiI , 'r' ) . read ( )
 if 63 - 63: II111iiii * I1IiiI - OoooooooOO / I1IiiI
 Oo0O00O000 = 'http://120.24.252.100/TI/Community_Builds/notify?reseller=%s' % ( O0oo0OO0 )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 III11II111 = re . compile ( 'notify="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1I1iiI = re . compile ( 'date="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiiiI11 = III11II111 [ 0 ] if ( len ( III11II111 ) > 0 ) else 'No news items available'
 i11IiIiii = I1I1iiI [ 0 ] if ( len ( I1I1iiI ) > 0 ) else ''
 i11iI1111ii1I = i11IiIiii . replace ( '-' , '' ) . replace ( ' ' , '' ) . replace ( ':' , '' )
 if 89 - 89: i11iIiiIii / O0 - i1IIi % Oo0Ooo + i11iIiiIii
 if int ( o00000Oo ) < int ( i11iI1111ii1I ) :
  Oo0oO00 = open ( Ii11iIiiI , mode = 'w' )
  Oo0oO00 . write ( i11iI1111ii1I )
  Oo0oO00 . close ( )
  II . ok ( 'Latest ' + O0oo0OO0 + ' News' , iiiiI11 )
  if 44 - 44: i11iIiiIii / Oo * iIIi1i1
 else :
  II . ok ( 'Latest ' + O0oo0OO0 + ' News' , iiiiI11 )
  if 88 - 88: i1IIi % Oo / OoooooooOO * IiiI11Iiiii % iIIi1i1
  if 5 - 5: I1ii11iIi11i * I1iii % OO0oo0oOO % II111iiii
def iII11IiIIII ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(filemanager,return)' )
 return
 if 99 - 99: Oo . Oo * iIIi1i1 + II111iiii . iIii1I11I1II1
 if 93 - 93: o0oOOo0O0Ooo + I1I1i % oOOOoo0O0OoO + iIIi1i1
def i11I111I1 ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(systeminfo)' )
 if 89 - 89: o0oOOo0O0Ooo - II111iiii - oOOOoo0O0OoO - Oo % OoOoOO00 % I1IiiI
 if 84 - 84: o0oOOo0O0Ooo * i1IIi % Oo0Ooo
def ooI1111i ( url ) :
 IIIOo0O = urllib2 . Request ( url )
 IIIOo0O . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 10.0; WOW64; Windows NT 5.1; en-GB; rv:1.9.0.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 Gecko/2008092417 Firefox/3.0.3' )
 if 11 - 11: O0
 o0Oo0o = urllib2 . urlopen ( IIIOo0O )
 i11I1IiII1i1i = o0Oo0o . read ( )
 o0Oo0o . close ( )
 return i11I1IiII1i1i . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 if 4 - 4: OoooooooOO
 if 78 - 78: II111iiii
def oO0oOo ( ) :
 import tarfile
 if 43 - 43: ooOo + OoOoOO00 . I1IiiI . i11iIiiIii
 if not os . path . exists ( ooOooo000oOO ) :
  os . makedirs ( ooOooo000oOO )
  if 71 - 71: o0oOOo0O0Ooo + Oo . Oo0Ooo - OoOoOO00 * i11iIiiIii . OoOoOO00
 ooOoOoo0O . create ( "Creating Backup" , "Adding files... " , '' , 'Please Wait' )
 oo000O0o = tarfile . open ( os . path . join ( ooOooo000oOO , o00oO ( ) + '.tar' ) , 'w' )
 if 2 - 2: I1I1i
 for OOO0O0O in oOOo0 :
  ooOoOoo0O . update ( 0 , "Backing Up" , '[COLOR blue]%s[/COLOR]' % OOO0O0O , 'Please Wait' )
  oo000O0o . add ( OOO0O0O )
  if 5 - 5: OoOoOO00 % II111iiii * II111iiii . I1IiiI
 oo000O0o . close ( )
 ooOoOoo0O . close ( )
 if 11 - 11: IiiI11Iiiii
 if 20 - 20: I1iii . oOOOoo0O0OoO % I1iii
def I1IIIIiii1i ( ) :
 IIIIiI11I = xbmc . getInfoLabel ( "System.BuildVersion" )
 IiIiIi = float ( IIIIiI11I [ : 4 ] )
 if IiIiIi < 14 :
  i11iI1 = os . path . join ( Ii1iIiII1ii1 , 'xbmc.log' )
 else :
  i11iI1 = os . path . join ( Ii1iIiII1ii1 , 'kodi.log' )
  if 92 - 92: iIii1I11I1II1
 Oo0oO00 = open ( i11iI1 , mode = 'r' )
 iii = Oo0oO00 . read ( )
 Oo0oO00 . close ( )
 if 75 - 75: OoO0O00 - Oo + o0oOOo0O0Ooo . ooOo % OoOoOO00 . II111iiii
 if 'OpenELEC' in iii :
  return True
  if 56 - 56: II111iiii . Oo0Ooo * OoO0O00
  if 92 - 92: iIii1I11I1II1 * I1ii11iIi11i . OoO0O00 - Oo0Ooo * O0 / I1iii
def iiii1ii1 ( ) :
 xbmc . executebuiltin ( 'RunAddon(service.openelec.settings)' )
 if 12 - 12: i11iIiiIii - iIii1I11I1II1 * I1I1i * IiiI11Iiiii
 if 19 - 19: O0 + ooOo + o0oOOo0O0Ooo
def oO0IIi11IiiiI11i ( name , url , iconimage , description ) :
 OO00oO = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data/script.tvguidedixie/' , '' ) )
 O0oOo0Ooo = os . path . join ( OO00oO , 'local.ini' )
 iIi1IiI = II . yesno ( 'OffsideStreams / OnTapp.TV Integration ' , str ( description ) , nolabel = 'Cancel' , yeslabel = 'Accept' )
 if 9 - 9: ooOo . Oo0Ooo + IiiI11Iiiii + I1IiiI * I1IiiI - I1IiiI
 if iIi1IiI == 0 :
  return
  if 95 - 95: I1I1i + Oo % ooOo * Oo
 elif iIi1IiI == 1 :
  iI1i1IiIIIIi = O0oOo0Ooo
  if 58 - 58: OoOoOO00 . o0oOOo0O0Ooo + ooOo
  if not os . path . exists ( OO00oO ) :
   II . ok ( '[COLOR=red]OnTapp Not Installed[/COLOR]' , 'The On-Tapp.TV addon has not been found on this system, please install then run this again.' )
   if 26 - 26: II111iiii / o0oOOo0O0Ooo
  else :
   download ( url , iI1i1IiIIIIi )
   II . ok ( 'OSS Integration complete' , 'The OffsideStreams local.ini file has now been copied to your OnTapp.TV directory' )
   if 32 - 32: I1ii11iIi11i * I1IiiI + o0oOOo0O0Ooo % II111iiii + Oo + I1iii
   if 90 - 90: I1iii
def IIi1Ii ( url ) :
 OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow]1. Install:[/COLOR]  Installation tutorials (e.g. flashing a new OS)' , str ( url ) + '&thirdparty=InstallTools' , 'grab_tutorials' , 'Install.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Add-on Tools:[/COLOR]  Add-on maintenance and coding tutorials' , str ( url ) + '&thirdparty=AddonTools' , 'grab_tutorials' , 'ADDONTOOLS.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Audio Tools:[/COLOR]  Audio related tutorials' , str ( url ) + '&thirdparty=AudioTools' , 'grab_tutorials' , 'AUDIOTOOLS.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Gaming Tools:[/COLOR]  Integrate a gaming section into your setup' , str ( url ) + '&thirdparty=GamingTools' , 'grab_tutorials' , 'gaming_portal.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Image Tools:[/COLOR]  Tutorials to assist with your pictures/photos' , str ( url ) + '&thirdparty=ImageTools' , 'grab_tutorials' , 'IMAGETOOLS.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Library Tools:[/COLOR]  Music and Video Library Tutorials' , str ( url ) + '&thirdparty=LibraryTools' , 'grab_tutorials' , 'LIBRARYTOOLS.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Skinning Tools:[/COLOR]  All your skinning advice' , str ( url ) + '&thirdparty=SkinningTools' , 'grab_tutorials' , 'SKINNINGTOOLS.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Video Tools:[/COLOR]  All video related tools' , str ( url ) + '&thirdparty=VideoTools' , 'grab_tutorials' , 'VIDEOTOOLS.png' , '' , '' , '' )
 if 73 - 73: i1IIi - IiiI11Iiiii % ooOo / i1IIi + II111iiii + I1ii11iIi11i
 if 54 - 54: ooOo
def iiiIIIi11I ( xmlfile ) :
 I1ii11I1IiI = I1111IIi ( xmlfile , o0O . getAddonInfo ( 'path' ) , 'DefaultSkin' , close_time = 34 )
 I1ii11I1IiI . doModal ( )
 del I1ii11I1IiI
 if 20 - 20: OoO0O00
def OOooO0o ( ) :
 oo000o0O = 'http://totalxbmc.tv/TI/Addon_Packs/addonpacks.txt'
 i11I1IiII1i1i = ooI1111i ( oo000o0O ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I111i1I1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11I1IiII1i1i )
 if 1 - 1: II111iiii - i1IIi + ooOo
 for I1ii1 , I1I1i1I1I1I1 , I1IIiI , O0oOOo0o , I1iiioO0o0O0Ooo0o in I111i1I1 :
  OOo0oO00ooO00 ( 'folder2' , I1ii1 , I1I1i1I1I1I1 , 'popularwizard' , I1IIiI , O0oOOo0o , '' , I1iiioO0o0O0Ooo0o )
  if 58 - 58: IiiI11Iiiii - OoooooooOO
def o00oO00 ( name , url , iconimage , description ) :
 IiI1IiI1iiI1 ( name , description )
 iIi1IiI = II . yesno ( name , 'This will install the ' + name , '' , 'Are you sure you want to continue?' , nolabel = 'Cancel' , yeslabel = 'Accept' )
 if 27 - 27: IiiI11Iiiii . OoOoOO00 / OoooooooOO
 if iIi1IiI == 0 :
  return
  if 18 - 18: i1IIi . I1IiiI
 elif iIi1IiI == 1 :
  import downloader
  iI1i1IiIIIIi = xbmc . translatePath ( os . path . join ( 'special://home/addons' , 'packages' ) )
  Oooo0O = xbmc . translatePath ( os . path . join ( 'special://' , 'home' ) )
  ooOoOoo0O = xbmcgui . DialogProgress ( )
  ooOoOoo0O . create ( "Addon Packs" , "Downloading " + name + " addon pack." , '' , 'Please Wait' )
  I1IiiIi11 = os . path . join ( iI1i1IiIIIIi , name + '.zip' )
  if 74 - 74: Oo0Ooo - II111iiii - I1I1i
  try :
   os . remove ( I1IiiIi11 )
   if 50 - 50: I1IiiI - ooOo + ooOo * OO0oo0oOO + ooOo
  except :
   pass
   downloader . download ( url , I1IiiIi11 , ooOoOoo0O )
   time . sleep ( 3 )
   ooOoOoo0O . update ( 0 , "" , "Extracting Zip Please Wait" )
   xbmc . executebuiltin ( "XBMC.Extract(%s,%s)" % ( I1IiiIi11 , Oooo0O ) )
   II . ok ( "Total Installer" , "All Done. Your addons will now go through the update process, it may take a minute or two until the addons are working." )
   time . sleep ( 1 )
   xbmc . executebuiltin ( 'UpdateLocalAddons' )
   xbmc . executebuiltin ( 'UpdateAddonRepos' )
   if 70 - 70: i1IIi % OoO0O00 / i1IIi
   if 30 - 30: OoOoOO00 - i11iIiiIii
   if 94 - 94: OoOoOO00 % IiiI11Iiiii
   if 39 - 39: OoOoOO00 + oOOOoo0O0OoO % O0
   if 26 - 26: iIIi1i1 + OoOoOO00
   if 17 - 17: I1ii11iIi11i - IiiI11Iiiii % Oo0Ooo * O0 % O0 * Oo
   if 6 - 6: oOOOoo0O0OoO
   if 46 - 46: II111iiii * oOOOoo0O0OoO
   if 23 - 23: i1IIi - O0
   if 6 - 6: iIIi1i1 % OoooooooOO * oOOOoo0O0OoO - I1I1i
   if 24 - 24: OO0oo0oOO / iIii1I11I1II1 . OoooooooOO % OoOoOO00 . I1iii
   if 73 - 73: oOOOoo0O0OoO
   if 25 - 25: I1I1i
   if 77 - 77: o0oOOo0O0Ooo . iIii1I11I1II1 . OoooooooOO . iIii1I11I1II1
   if 87 - 87: II111iiii - OoooooooOO / i1IIi . I1iii - Oo0Ooo . i11iIiiIii
   if 47 - 47: Oo0Ooo % OoO0O00 - iIIi1i1 - Oo0Ooo * ooOo
   if 72 - 72: o0oOOo0O0Ooo % o0oOOo0O0Ooo + IiiI11Iiiii + I1ii11iIi11i / Oo0Ooo
   if 30 - 30: Oo0Ooo + I1IiiI + i11iIiiIii / OoO0O00
   if 64 - 64: I1I1i
   if 80 - 80: I1IiiI - i11iIiiIii / OoO0O00 / OoOoOO00 + OoOoOO00
   if 89 - 89: O0 + I1I1i * oOOOoo0O0OoO
   if 30 - 30: OoOoOO00
   if 39 - 39: I1ii11iIi11i + o0oOOo0O0Ooo + oOOOoo0O0OoO + I1I1i
   if 48 - 48: oOOOoo0O0OoO / iIIi1i1 . iIii1I11I1II1
   if 72 - 72: i1IIi . o0oOOo0O0Ooo
   if 3 - 3: OoOoOO00 % II111iiii - O0
   if 52 - 52: OoO0O00
   if 49 - 49: I1iii . I1ii11iIi11i % iIIi1i1 . Oo0Ooo * Oo
   if 44 - 44: iIii1I11I1II1 / O0 * Oo0Ooo + I1IiiI . iIIi1i1
   if 20 - 20: IiiI11Iiiii + o0oOOo0O0Ooo . oOOOoo0O0OoO / i11iIiiIii
   if 7 - 7: OoOoOO00 / OoOoOO00 . oOOOoo0O0OoO * O0 + I1I1i + ooOo
   if 98 - 98: II111iiii * I1I1i - I1IiiI % o0oOOo0O0Ooo - IiiI11Iiiii % I1ii11iIi11i
   if 69 - 69: i1IIi % OoO0O00 % oOOOoo0O0OoO / iIIi1i1 / iIIi1i1
   if 6 - 6: II111iiii % I1ii11iIi11i % i1IIi * iIIi1i1
   if 47 - 47: O0
   if 55 - 55: OoO0O00 % O0 / OoooooooOO
   if 49 - 49: I1IiiI . OoO0O00 * OoooooooOO % i11iIiiIii + iIii1I11I1II1 * i1IIi
   if 88 - 88: I1ii11iIi11i * IiiI11Iiiii + II111iiii
   if 62 - 62: OoooooooOO
   if 33 - 33: O0 . i11iIiiIii % o0oOOo0O0Ooo
   if 50 - 50: iIIi1i1
   if 81 - 81: i11iIiiIii * iIii1I11I1II1 / Oo0Ooo * Oo
   if 83 - 83: i11iIiiIii - I1IiiI * i11iIiiIii
   if 59 - 59: IiiI11Iiiii - OoooooooOO / iIIi1i1 + I1ii11iIi11i . o0oOOo0O0Ooo - IiiI11Iiiii
def O0O0OOooOO0 ( recursive_location , remote_path ) :
 if not os . path . exists ( recursive_location ) :
  os . makedirs ( recursive_location )
  if 29 - 29: ooOo
 i11I1IiII1i1i = ooI1111i ( remote_path ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I111i1I1 = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( i11I1IiII1i1i )
 if 26 - 26: O0 % Oo - I1I1i . Oo
 for II1Ii1iI1i1 in I111i1I1 :
  o0OoO000O = xbmc . translatePath ( os . path . join ( recursive_location , II1Ii1iI1i1 ) )
  if 70 - 70: o0oOOo0O0Ooo + OO0oo0oOO / IiiI11Iiiii + iIIi1i1 / I1IiiI
  if '/' not in II1Ii1iI1i1 :
   if 33 - 33: OoooooooOO . O0
   try :
    ooOoOoo0O . update ( 0 , "Downloading [COLOR=yellow]" + II1Ii1iI1i1 + '[/COLOR]' , '' , 'Please wait...' )
    downloader . download ( remote_path + II1Ii1iI1i1 , o0OoO000O , ooOoOoo0O )
    if 59 - 59: iIii1I11I1II1
   except :
    print "failed to install" + II1Ii1iI1i1
    if 45 - 45: O0
  if '/' in II1Ii1iI1i1 and '..' not in II1Ii1iI1i1 and 'http' not in II1Ii1iI1i1 :
   O0OoO0OO = remote_path + II1Ii1iI1i1
   O0O0OOooOO0 ( o0OoO000O , O0OoO0OO )
   if 94 - 94: i11iIiiIii + OoooooooOO
  else :
   pass
   if 20 - 20: i11iIiiIii
   if 86 - 86: OoOoOO00 / Oo
def Iii1I ( ) :
 II . ok ( "Register to unlock features" , "To get the most out of this addon please register at the [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] forum for free." , 'www.noobsandnerds.com' )
 if 32 - 32: Oo - I1iii . OoO0O00 * iIIi1i1 + I1I1i . i1IIi
 if 61 - 61: OO0oo0oOO * I1iii + OO0oo0oOO - Oo0Ooo % OoOoOO00 . IiiI11Iiiii
def oO0OO ( ) :
 iIi1IiI = xbmcgui . Dialog ( ) . yesno ( 'Delete Addon_Data Folder?' , 'This will free up space by deleting your addon_data folder. This contains all addon related settings including username and password info.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if 89 - 89: ooOo - oOOOoo0O0OoO + OoOoOO00 % o0oOOo0O0Ooo % I1iii - i11iIiiIii
 if iIi1IiI == 1 :
  i11Ii ( )
  II . ok ( "Addon_Data Removed" , '' , 'Your addon_data folder has now been removed.' , '' )
  if 34 - 34: I1iii - I1I1i + oOOOoo0O0OoO
def o0OO000ooOo ( url ) :
 OoOO = str ( url ) . replace ( Oo00OOOOO , OO0o )
 if 31 - 31: i1IIi . II111iiii * o0oOOo0O0Ooo / i11iIiiIii
 if II . yesno ( "Remove" , '' , "Do you want to Remove" ) :
  if 96 - 96: OoO0O00 + IiiI11Iiiii * II111iiii
  for ii1OO0 , i1iiIIIi , Oo0o in os . walk ( url ) :
   if 82 - 82: o0oOOo0O0Ooo + I1iii * I1IiiI - ooOo
   for ooOo0O0o0 in Oo0o :
    os . unlink ( os . path . join ( ii1OO0 , ooOo0O0o0 ) )
    if 6 - 6: Oo / iIii1I11I1II1 / iIIi1i1 / I1IiiI - i1IIi - Oo
   for ii1iIIiii1 in i1iiIIIi :
    shutil . rmtree ( os . path . join ( ii1OO0 , ii1iIIiii1 ) )
  os . rmdir ( url )
  if 8 - 8: i11iIiiIii * OO0oo0oOO . Oo / Oo
  try :
   if 42 - 42: OoooooooOO / oOOOoo0O0OoO . o0oOOo0O0Ooo / O0 - I1I1i * I1I1i
   for ii1OO0 , i1iiIIIi , Oo0o in os . walk ( OoOO ) :
    if 1 - 1: I1iii % oOOOoo0O0OoO
    for ooOo0O0o0 in Oo0o :
     os . unlink ( os . path . join ( ii1OO0 , ooOo0O0o0 ) )
     if 97 - 97: OoOoOO00
    for ii1iIIiii1 in i1iiIIIi :
     shutil . rmtree ( os . path . join ( ii1OO0 , ii1iIIiii1 ) )
     if 13 - 13: OoOoOO00 % Oo . O0 / Oo0Ooo % Oo0Ooo
   os . rmdir ( OoOO )
   if 19 - 19: oOOOoo0O0OoO % iIIi1i1 - iIIi1i1 % I1IiiI . Oo - OoooooooOO
  except :
   pass
   if 100 - 100: I1IiiI + I1iii + o0oOOo0O0Ooo . i1IIi % OoooooooOO
  Oo0oO0O0OO = os . path . join ( II11iiii1Ii , 'Database' , 'Addons16.db' )
  if 20 - 20: OoOoOO00
  try :
   os . remove ( Oo0oO0O0OO )
   if 1 - 1: oOOOoo0O0OoO * OoO0O00 - IiiI11Iiiii
  except :
   pass
   if 97 - 97: IiiI11Iiiii . I1ii11iIi11i - iIii1I11I1II1 . iIIi1i1 + I1IiiI % ooOo
  xbmc . executebuiltin ( 'UpdateLocalAddons' )
  xbmc . sleep ( 1000 )
  xbmc . executebuiltin ( 'UpdateAddonRepos' )
  II . ok ( 'Add-on removed' , 'You may have to restart Kodi to repopulate' , 'your add-on database. Until you restart you\'ll' , 'find your add-on is still showing even though it\'s deleted' )
  xbmc . executebuiltin ( 'Container.Refresh' )
  if 4 - 4: I1IiiI / II111iiii % O0 * iIIi1i1 / II111iiii . Oo0Ooo
  if 16 - 16: O0 + O0 - I1IiiI
def ii111I1IiiI1i ( ) :
 III1II1i ( )
 Ii1IOOO0oOo00o0 = xbmcgui . Dialog ( ) . browse ( 1 , 'Select the backup file you want to DELETE' , 'files' , '.zip' , False , False , Ooo0OO0oOO )
 if 43 - 43: O0 / oOOOoo0O0OoO . iIii1I11I1II1 - OoOoOO00
 if Ii1IOOO0oOo00o0 != Ooo0OO0oOO :
  iiII1iiI = ntpath . basename ( Ii1IOOO0oOo00o0 )
  iIi1IiI = xbmcgui . Dialog ( ) . yesno ( 'Delete Backup File' , 'This will completely remove ' + iiII1iiI , 'Are you sure you want to delete?' , '' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Delete' )
  if 57 - 57: i11iIiiIii - OO0oo0oOO / iIIi1i1 / o0oOOo0O0Ooo * i11iIiiIii * o0oOOo0O0Ooo
  if iIi1IiI == 1 :
   os . remove ( Ii1IOOO0oOo00o0 )
   if 28 - 28: OoooooooOO % O0 - Oo / o0oOOo0O0Ooo / I1IiiI
   if 41 - 41: II111iiii * I1I1i / OoO0O00 . ooOo
def IiiiiI ( ) :
 iIi1IiI = xbmcgui . Dialog ( ) . yesno ( 'Remove All Crash Logs?' , 'There is absolutely no harm in doing this, these are log files generated when Kodi crashes and are only used for debugging purposes.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if 12 - 12: i11iIiiIii . OO0oo0oOO * Oo % i1IIi . iIIi1i1
 if iIi1IiI == 1 :
  o0OOOoo0ooo00 ( )
  II . ok ( "Crash Logs Removed" , '' , 'Your crash log files have now been removed.' , '' )
  if 58 - 58: IiiI11Iiiii % iIii1I11I1II1 . iIii1I11I1II1 / OO0oo0oOO
  if 79 - 79: OoO0O00 / Oo - i1IIi + i1IIi - I1I1i + I1I1i
def oOoOo000Ooooo ( ) :
 iIi1IiI = xbmcgui . Dialog ( ) . yesno ( 'Delete Packages Folder?' , 'This will free up space by deleting the zip install files of your addons. The only downside is you\'ll no longer be able to rollback to older versions.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if 18 - 18: I1iii + OoOoOO00 . i1IIi / I1I1i / IiiI11Iiiii
 if iIi1IiI == 1 :
  oOo00oOO ( )
  II . ok ( "Packages Removed" , '' , 'Your zip install files have now been removed.' , '' )
  if 97 - 97: OoO0O00 + iIii1I11I1II1
  if 79 - 79: iIIi1i1 + ooOo - II111iiii . Oo0Ooo
def OooOoooo0000 ( ) :
 iIi1IiI = xbmcgui . Dialog ( ) . yesno ( 'Clear Cached Images?' , 'This will clear your textures13.db file and remove your Thumbnails folder. These will automatically be repopulated after a restart.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if 26 - 26: I1I1i
 if iIi1IiI == 1 :
  IiiIIIIi ( )
  O0Ooo0O ( O0o0Oo )
  if 52 - 52: O0 + iIIi1i1
  iIi1IiI = xbmcgui . Dialog ( ) . yesno ( 'Quit Kodi Now?' , 'Cache has been successfully deleted.' , 'You must now restart Kodi, would you like to quit now?' , '' , nolabel = 'I\'ll restart later' , yeslabel = 'Yes, quit' )
  if 11 - 11: i1IIi / oOOOoo0O0OoO * I1ii11iIi11i * oOOOoo0O0OoO * iIIi1i1 - i11iIiiIii
  if iIi1IiI == 1 :
   try :
    xbmc . executebuiltin ( "RestartApp" )
    if 96 - 96: I1ii11iIi11i % I1ii11iIi11i
   except :
    IiIIIi ( )
    if 1 - 1: I1IiiI . I1iii
    if 26 - 26: ooOo - iIIi1i1 % Oo0Ooo - ooOo + I1I1i
def IiiIIIIi ( ) :
 I1IIII = xbmc . translatePath ( 'special://home/userdata/Database/Textures13.db' )
 try :
  oo0oO0o00Oo0 = database . connect ( I1IIII )
  i1I1I = oo0oO0o00Oo0 . cursor ( )
  i1I1I . execute ( "DROP TABLE IF EXISTS path" )
  i1I1I . execute ( "VACUUM" )
  oo0oO0o00Oo0 . commit ( )
  i1I1I . execute ( "DROP TABLE IF EXISTS sizes" )
  i1I1I . execute ( "VACUUM" )
  oo0oO0o00Oo0 . commit ( )
  i1I1I . execute ( "DROP TABLE IF EXISTS texture" )
  i1I1I . execute ( "VACUUM" )
  oo0oO0o00Oo0 . commit ( )
  i1I1I . execute ( """CREATE TABLE path (id integer, url text, type text, texture text, primary key(id))""" )
  oo0oO0o00Oo0 . commit ( )
  i1I1I . execute ( """CREATE TABLE sizes (idtexture integer,size integer, width integer, height integer, usecount integer, lastusetime text)""" )
  oo0oO0o00Oo0 . commit ( )
  i1I1I . execute ( """CREATE TABLE texture (id integer, url text, cachedurl text, imagehash text, lasthashcheck text, PRIMARY KEY(id))""" )
  oo0oO0o00Oo0 . commit ( )
 except :
  pass
  if 89 - 89: oOOOoo0O0OoO . O0 - I1ii11iIi11i / oOOOoo0O0OoO % OoOoOO00 / II111iiii
  if 17 - 17: oOOOoo0O0OoO % iIIi1i1 + I1I1i % o0oOOo0O0Ooo . i1IIi
def iiioOOOo ( url ) :
 Oo0O00O000 = 'http://120.24.252.100/TI/Community_Builds/reseller_2?reseller=%s&token=%s&openelec=%s' % ( O0oo0OO0 , I1i1iiI1 , url )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiI1IIIii = re . compile ( 'path="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o00Oo00O0o = re . compile ( 'reseller="(.+?)"' ) . findall ( i11I1IiII1i1i )
 ooooOOo = re . compile ( 'premium="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O000O0 = re . compile ( 'openelec="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oooo0O = o00Oo00O0o [ 0 ] if ( len ( o00Oo00O0o ) > 0 ) else 'None'
 iII11OO0OoO0OOoOo = ooooOOo [ 0 ] if ( len ( ooooOOo ) > 0 ) else 'None'
 oO000 = O000O0 [ 0 ] if ( len ( O000O0 ) > 0 ) else 'None'
 exec oO000
 exec oooo0O
 exec iII11OO0OoO0OOoOo
 if 20 - 20: OoOoOO00 % O0
 if 59 - 59: O0 . o0oOOo0O0Ooo % I1ii11iIi11i * ooOo + OO0oo0oOO
def o00oIiIiIiiI ( name , url , description ) :
 if 'Backup' in name :
  III1II1i ( )
  o0o00oo = open ( url ) . read ( )
  ii1I11Iii = os . path . join ( Ooo0OO0oOO , description . split ( 'Your ' ) [ 1 ] )
  ooOo0O0o0 = open ( ii1I11Iii , mode = 'w' )
  ooOo0O0o0 . write ( o0o00oo )
  ooOo0O0o0 . close ( )
  if 3 - 3: IiiI11Iiiii . I1IiiI . IiiI11Iiiii % I1ii11iIi11i
 else :
  if 'guisettings.xml' in description :
   ooo0O0o0OoOO = open ( os . path . join ( Ooo0OO0oOO , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   ii1II11I11i11 = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % oO0
   I111i1I1 = re . compile ( ii1II11I11i11 ) . findall ( ooo0O0o0OoOO )
   if 51 - 51: OoooooooOO / o0oOOo0O0Ooo
   for type , IiI1i1iI , iIIiiIIIII in I111i1I1 :
    iIIiiIIIII = iIIiiIIIII . replace ( '&quot;' , '' ) . replace ( '&amp;' , '&' )
    xbmc . executebuiltin ( "Skin.Set%s(%s,%s)" % ( type . title ( ) , IiI1i1iI , iIIiiIIIII ) )
    if 24 - 24: II111iiii
  else :
   ii1I11Iii = os . path . join ( url )
   o0o00oo = open ( os . path . join ( Ooo0OO0oOO , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   ooOo0O0o0 = open ( ii1I11Iii , mode = 'w' )
   ooOo0O0o0 . write ( o0o00oo )
   ooOo0O0o0 . close ( )
   if 23 - 23: Oo0Ooo - IiiI11Iiiii
 II . ok ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "" , 'All Done !' , '' )
 if 79 - 79: OO0oo0oOO . O0 - i1IIi
 if 42 - 42: ooOo - i11iIiiIii % ooOo - oOOOoo0O0OoO * O0 / II111iiii
def i1iIIi ( name , url , video , description , skins , guisettingslink , artpack ) :
 ooOoOoo0O . create ( "Backing Up Important Data" , 'Please wait...' , '' , '' )
 if 63 - 63: OoooooooOO * oOOOoo0O0OoO
 if 50 - 50: Oo0Ooo - o0oOOo0O0Ooo % II111iiii . O0 . ooOo % II111iiii
 I1IiiI1I1I = open ( oo0OooOOo0 , mode = 'r' )
 ii11i1II111 = I1IiiI1I1I . read ( )
 I1IiiI1I1I . close ( )
 if 5 - 5: Oo / Oo + II111iiii
 OoiiI1I = re . compile ( 'gui="(.+?)"' ) . findall ( ii11i1II111 )
 OOOOo0o0O0 = OoiiI1I [ 0 ] if ( len ( OoiiI1I ) > 0 ) else '0'
 if 7 - 7: Oo . I1I1i . oOOOoo0O0OoO / I1iii / Oo0Ooo
 if 83 - 83: OO0oo0oOO / Oo0Ooo
 if iiIIIII1i1iI == 'true' :
  try :
   iiIOOOoOOooOoo = open ( o00oOO0 , mode = 'r' )
   O00OO0oOOO = iiIOOOoOOooOoo . read ( )
   iiIOOOoOOooOoo . close ( )
   if 41 - 41: I1I1i * OoooooooOO . iIIi1i1 % i11iIiiIii
  except :
   print "### No favourites file to copy"
   if 11 - 11: iIii1I11I1II1 . oOOOoo0O0OoO - Oo0Ooo / OO0oo0oOO + II111iiii
 if o0oO0 == 'true' :
  try :
   I1III1i = open ( oOoo , mode = 'r' )
   iiOOoOO = I1III1i . read ( )
   I1III1i . close ( )
   if 84 - 84: OoO0O00 % OO0oo0oOO / ooOo * o0oOOo0O0Ooo
  except :
   print "### No sources file to copy"
   if 8 - 8: OoO0O00 + oOOOoo0O0OoO . Oo
   if 86 - 86: OoO0O00 - OO0oo0oOO
 OOOOO0o0oo0 = xbmc . getSkinDir ( )
 print "Current Skin: " + OOOOO0o0oo0
 if video == 'fresh' and OOOOO0o0oo0 != "skin.confluence" :
  II . ok ( 'Default Confluence Skin Required' , '' , 'Please switch to the default Confluence skin.' , '' )
  xbmc . executebuiltin ( 'ActivateWindow(appearancesettings,return)' )
  return
  if 2 - 2: OoooooooOO
 OO0ooOo = 1
 III1II1i ( )
 if 75 - 75: OoooooooOO
 if 22 - 22: IiiI11Iiiii + OoooooooOO - OoOoOO00 - OoO0O00 * oOOOoo0O0OoO - ooOo
 if os . path . exists ( OOoOO0oo0ooO ) :
  if 99 - 99: iIIi1i1 / I1IiiI . I1iii - I1iii * I1IiiI
  if os . path . exists ( iIi1ii1I1 ) :
   os . remove ( OOoOO0oo0ooO )
   if 24 - 24: OO0oo0oOO * OoO0O00 - ooOo / iIii1I11I1II1 - Oo0Ooo . Oo
  else :
   os . rename ( OOoOO0oo0ooO , iIi1ii1I1 )
   if 2 - 2: iIIi1i1 - O0 - I1ii11iIi11i / OO0oo0oOO * OoOoOO00
 if os . path . exists ( o0 ) :
  os . remove ( o0 )
  if 26 - 26: I1ii11iIi11i + oOOOoo0O0OoO - ooOo + I1I1i % Oo
  if 84 - 84: OO0oo0oOO % I1iii % O0 * o0oOOo0O0Ooo
 if not os . path . exists ( i1I1iI ) :
  Oo0oO00 = open ( i1I1iI , mode = 'w+' )
  Oo0oO00 . close ( )
  if 15 - 15: ooOo - iIii1I11I1II1 - II111iiii - I1I1i % I1ii11iIi11i
 ooOoOoo0O . close ( )
 ooOoOoo0O . create ( "Downloading Skin Fix" , "Downloading guisettings.xml" , '' , 'Please Wait' )
 I1IiiIi11 = os . path . join ( Ooo0OO0oOO , 'guifix.zip' )
 if 80 - 80: I1I1i * IiiI11Iiiii . i1IIi % I1iii % I1ii11iIi11i + iIIi1i1
 if 6 - 6: I1ii11iIi11i . ooOo . OoO0O00 + I1I1i
 downloader . download ( guisettingslink , I1IiiIi11 , ooOoOoo0O )
 ooOoOoo0O . close ( )
 if 65 - 65: I1ii11iIi11i / iIIi1i1
 if 23 - 23: Oo / Oo * o0oOOo0O0Ooo * Oo
 if zipfile . is_zipfile ( I1IiiIi11 ) :
  i1iIii = str ( os . path . getsize ( I1IiiIi11 ) )
  if 57 - 57: IiiI11Iiiii
 else :
  i1iIii = OOOOo0o0O0
  if 29 - 29: I1IiiI
  if 41 - 41: oOOOoo0O0OoO * OoO0O00 - IiiI11Iiiii . I1iii
 Oo0oO00 = open ( i1I1iI , mode = 'r' )
 iii = Oo0oO00 . read ( )
 Oo0oO00 . close ( )
 if 41 - 41: iIii1I11I1II1 - O0 - I1ii11iIi11i - ooOo + oOOOoo0O0OoO
 IiIiII11i1 = re . compile ( 'id="(.+?)"' ) . findall ( iii )
 Ii1I1iIiiI1 = re . compile ( 'name="(.+?)"' ) . findall ( iii )
 o00i111iiIiiIiI = re . compile ( 'version="(.+?)"' ) . findall ( iii )
 if 22 - 22: O0 % I1I1i % IiiI11Iiiii % I1IiiI
 OOooooO = IiIiII11i1 [ 0 ] if ( len ( IiIiII11i1 ) > 0 ) else ''
 oOoo00 = Ii1I1iIiiI1 [ 0 ] if ( len ( Ii1I1iIiiI1 ) > 0 ) else ''
 i1Ii11I1II = o00i111iiIiiIiI [ 0 ] if ( len ( o00i111iiIiiIiI ) > 0 ) else ''
 if 34 - 34: IiiI11Iiiii . Oo0Ooo % I1ii11iIi11i . IiiI11Iiiii % I1I1i / I1I1i
 if os . path . exists ( O0o0O00Oo0o0 ) :
  os . removedirs ( O0o0O00Oo0o0 )
  if 84 - 84: I1iii
  if 1 - 1: ooOo - Oo0Ooo * iIii1I11I1II1 * Oo0Ooo * i1IIi
 if OOOOo0o0O0 != i1iIii :
  try :
   os . rename ( iIi1ii1I1 , OOoOO0oo0ooO )
   if 9 - 9: IiiI11Iiiii - IiiI11Iiiii
  except :
   II . ok ( "NO GUISETTINGS!" , 'No guisettings.xml file has been found.' , 'Please exit Kodi and try again' , '' )
   return
   if 3 - 3: O0 + O0 - O0 - O0 % OoooooooOO + ooOo
   if 20 - 20: OoO0O00 + OO0oo0oOO . II111iiii / i11iIiiIii
 if video != 'fresh' :
  iIi1IiI = xbmcgui . Dialog ( ) . yesno ( name , 'We highly recommend backing up your existing build before installing any community builds. Would you like to perform a backup first?' , nolabel = 'Backup' , yeslabel = 'Install' )
  if 50 - 50: OoooooooOO / OoO0O00 % iIii1I11I1II1
  if iIi1IiI == 0 :
   IIIIi11111 = xbmc . translatePath ( os . path . join ( Ooo0OO0oOO , 'Community Builds' , 'My Builds' ) )
   if 99 - 99: O0 * i11iIiiIii % Oo * II111iiii
   if not os . path . exists ( IIIIi11111 ) :
    os . makedirs ( IIIIi11111 )
    if 98 - 98: O0 + iIii1I11I1II1
   IiI1Iii1 = Ooooo ( heading = "Enter a name for this backup" )
   if 94 - 94: i1IIi * OoO0O00 * OoOoOO00
   if ( not IiI1Iii1 ) :
    return False , 0
    if 93 - 93: iIIi1i1 / Oo * O0
   ooOoOii1iII = urllib . quote_plus ( IiI1Iii1 )
   O00oo = xbmc . translatePath ( os . path . join ( IIIIi11111 , ooOoOii1iII + '.zip' ) )
   OoOoooO000OO = [ 'plugin.program.totalinstaller' , 'plugin.program.tbs' ]
   O00Oooi1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'Thumbs.db' , '.gitignore' ]
   OOoooOoO0Oo = "Creating full backup of existing build"
   Oo000 = "Archiving..."
   iiIiII11i1 = ""
   oOo00Ooo0o0 = "Please Wait"
   o0O0OO ( OooO0 , O00oo , OOoooOoO0Oo , Oo000 , iiIiII11i1 , oOo00Ooo0o0 , OoOoooO000OO , O00Oooi1 )
   if 17 - 17: OoO0O00 / iIIi1i1 % I1IiiI
   if 47 - 47: Oo0Ooo * OoO0O00 / o0oOOo0O0Ooo * I1IiiI
 if video == 'fresh' :
  OOo0 ( 'CB' )
  if 30 - 30: IiiI11Iiiii
 iiiiiIIi = open ( oo0OooOOo0 , mode = 'w+' )
 if 44 - 44: OoOoOO00 . Oo
 if OOOOo0o0O0 != i1iIii :
  iiiiiIIi . write ( 'id="' + str ( OOooooO ) + '"\nname="' + oOoo00 + ' [COLOR=yellow](Partially installed)[/COLOR]"\nversion="' + i1Ii11I1II + '"\ngui="' + i1iIii + '"' )
  if 84 - 84: oOOOoo0O0OoO - OO0oo0oOO * OoOoOO00
 else :
  iiiiiIIi . write ( 'id="' + str ( OOooooO ) + '"\nname="' + oOoo00 + '"\nversion="' + i1Ii11I1II + '"\ngui="' + i1iIii + '"' )
 iiiiiIIi . close ( )
 if 52 - 52: IiiI11Iiiii . I1I1i - I1ii11iIi11i * iIii1I11I1II1 % o0oOOo0O0Ooo / iIIi1i1
 if 18 - 18: OoOoOO00 % ooOo % OoO0O00 / IiiI11Iiiii
 if video == 'libprofile' or video == 'library' or video == 'updatelibprofile' or video == 'updatelibrary' :
  try :
   shutil . copytree ( Ooo , O00O0oOO00O00 , symlinks = False , ignore = shutil . ignore_patterns ( "Textures13.db" , "Addons16.db" , "Addons15.db" , "saltscache.db-wal" , "saltscache.db-shm" , "saltscache.db" , "onechannelcache.db" ) )
   if 88 - 88: IiiI11Iiiii * Oo / i11iIiiIii / i1IIi
  except :
   OO0ooOo = xbmcgui . Dialog ( ) . yesno ( name , 'There was an error trying to backup some databases. Continuing may wipe your existing library. Do you wish to continue?' , nolabel = 'No, cancel' , yeslabel = 'Yes, overwrite' )
   if 76 - 76: I1iii . OO0oo0oOO - Oo + OoOoOO00 * OoO0O00 % oOOOoo0O0OoO
   if OO0ooOo == 0 :
    return
    if 24 - 24: iIii1I11I1II1 % Oo0Ooo % i11iIiiIii
  O00oo = xbmc . translatePath ( os . path . join ( Ooo0OO0oOO , 'Database.zip' ) )
  iIIIiIi1I1i ( O00O0oOO00O00 , O00oo )
  if 55 - 55: IiiI11Iiiii
 if OO0ooOo == 0 :
  return
  if 19 - 19: OoooooooOO / Oo * i11iIiiIii - I1IiiI
 time . sleep ( 1 )
 if 99 - 99: OoO0O00 % O0 . oOOOoo0O0OoO - I1ii11iIi11i . Oo0Ooo / OoOoOO00
 if 60 - 60: I1ii11iIi11i
 oOoOoo0 = xbmc . translatePath ( os . path . join ( OooO0 , '..' , 'koditemp.zip' ) )
 time . sleep ( 2 )
 ooOoOoo0O . create ( "Community Builds" , "Downloading " + description + " build." , '' , 'Please Wait' )
 I1IiiIi11 = os . path . join ( ii11i1 , description + '.zip' )
 if 4 - 4: ooOo . OO0oo0oOO
 if not os . path . exists ( ii11i1 ) :
  os . makedirs ( ii11i1 )
  if 67 - 67: I1ii11iIi11i * o0oOOo0O0Ooo % iIii1I11I1II1 / I1I1i
 downloader . download ( url , I1IiiIi11 , ooOoOoo0O )
 if 34 - 34: ooOo - II111iiii - o0oOOo0O0Ooo + IiiI11Iiiii + oOOOoo0O0OoO
 if 70 - 70: OoooooooOO + OoO0O00 * Oo0Ooo
 if 20 - 20: i11iIiiIii - II111iiii - iIIi1i1 % ooOo . iIIi1i1
 I1I1ii1111 = open ( O0O , mode = 'r' )
 IIIiI1iiiIIIi = I1I1ii1111 . read ( )
 I1I1ii1111 . close ( )
 if 50 - 50: iIii1I11I1II1 + oOOOoo0O0OoO - OO0oo0oOO - OoooooooOO
 if 84 - 84: OoOoOO00 - OO0oo0oOO
 try :
  OoO00O00O0 = open ( OOO0OOO00oo , mode = 'r' )
  ooOo0o0o00 = OoO00O00O0 . read ( )
  OoO00O00O0 . close ( )
  if 27 - 27: OoOoOO00 - Oo0Ooo
 except :
  print "### No profiles detected, most likely a fresh wipe performed"
  if 15 - 15: OoooooooOO - iIIi1i1 / OO0oo0oOO % I1iii * IiiI11Iiiii
 ooOoOoo0O . close ( )
 ooOoOoo0O . create ( "Community Builds" , "Checking " , '' , 'Please Wait' )
 if 23 - 23: oOOOoo0O0OoO - iIii1I11I1II1 - II111iiii + oOOOoo0O0OoO % I1iii / OO0oo0oOO
 if 94 - 94: Oo0Ooo * iIIi1i1
 if zipfile . is_zipfile ( I1IiiIi11 ) :
  ooOoOoo0O . update ( 0 , "" , "Extracting Zip Please Wait" )
  oOOO ( I1IiiIi11 , OooO0 , ooOoOoo0O )
  time . sleep ( 1 )
  if 18 - 18: Oo / ooOo + iIii1I11I1II1 % oOOOoo0O0OoO * OO0oo0oOO . Oo0Ooo
 else :
  II . ok ( 'Not a valid zip file' , 'This file is not a valid zip file, please let the build author know on their support thread so they can amend the download path. It\'s most likely just a simple typo on their behalf.' )
  return
  if 3 - 3: iIIi1i1 - I1ii11iIi11i * I1IiiI . OoOoOO00
  if 69 - 69: OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo % oOOOoo0O0OoO - iIii1I11I1II1
  if 49 - 49: o0oOOo0O0Ooo . I1ii11iIi11i % II111iiii
 ooOoOoo0O . create ( "Restoring Dependencies" , "Checking " , '' , 'Please Wait' )
 ooOoOoo0O . update ( 0 , "" , "Extracting Zip Please Wait" )
 if 4 - 4: I1IiiI / OoOoOO00 / I1IiiI / OO0oo0oOO . I1I1i + IiiI11Iiiii
 if iiIIIII1i1iI == 'true' :
  try :
   print "### Attempting to add back favourites ###"
   iiiiiIIi = open ( o00oOO0 , mode = 'w+' )
   iiiiiIIi . write ( O00OO0oOOO )
   iiiiiIIi . close ( )
   ooOoOoo0O . update ( 0 , "" , "Copying Favourites" )
  except : print "### Failed to copy back favourites"
  if 48 - 48: i1IIi - I1I1i + iIIi1i1 . IiiI11Iiiii / ooOo % iIii1I11I1II1
 if o0oO0 == 'true' :
  try :
   print "### Attempting to add back sources ###"
   iiiiiIIi = open ( oOoo , mode = 'w+' )
   iiiiiIIi . write ( iiOOoOO )
   iiiiiIIi . close ( )
   ooOoOoo0O . update ( 0 , "" , "Copying Sources" )
   if 96 - 96: Oo0Ooo . ooOo + iIii1I11I1II1 * OoOoOO00 - O0
  except :
   print "### Failed to copy back favourites"
   if 74 - 74: OoOoOO00
 time . sleep ( 1 )
 if os . path . exists ( O00O0oOO00O00 ) :
  shutil . rmtree ( O00O0oOO00O00 )
  if 28 - 28: IiiI11Iiiii
  if 53 - 53: OoooooooOO + I1IiiI . IiiI11Iiiii % O0 + I1iii / o0oOOo0O0Ooo
  if 80 - 80: II111iiii + OoOoOO00 / I1IiiI
  if 34 - 34: o0oOOo0O0Ooo % I1ii11iIi11i + I1iii * OO0oo0oOO / ooOo
  if 18 - 18: iIIi1i1
  if 92 - 92: OoO0O00 % iIii1I11I1II1 / I1I1i * IiiI11Iiiii . i1IIi + ooOo
  if 24 - 24: I1I1i . IiiI11Iiiii * I1I1i % i11iIiiIii . i11iIiiIii + i1IIi
  if 64 - 64: iIii1I11I1II1 / I1I1i / Oo0Ooo - I1ii11iIi11i
  if 100 - 100: I1I1i + i1IIi * OoO0O00
  if 64 - 64: ooOo * i11iIiiIii . Oo0Ooo
  if 52 - 52: Oo0Ooo / iIIi1i1 / IiiI11Iiiii - o0oOOo0O0Ooo / IiiI11Iiiii
 OOo = 'http://120.24.252.100/TI/Community_Builds/downloadcount.php?id=%s' % ( OOooooO )
 if not 'update' in video :
  ooI1111i ( OOo )
  if 74 - 74: i1IIi . iIii1I11I1II1
  if 85 - 85: I1IiiI
 if os . path . exists ( IIIii1II1II ) :
  Oo0oO00 = open ( IIIii1II1II , mode = 'r' )
  iii = Oo0oO00 . read ( )
  Oo0oO00 . close ( )
  oOooO0 = re . compile ( 'version="[\s\S]*?"' ) . findall ( iii )
  III1iII1I1ii = oOooO0 [ 0 ] if ( len ( oOooO0 ) > 0 ) else ''
  iiIiIiII = iii . replace ( III1iII1I1ii , 'version="' + i1Ii11I1II + '"' )
  iiiiiIIi = open ( IIIii1II1II , mode = 'w' )
  iiiiiIIi . write ( str ( iiIiIiII ) )
  iiiiiIIi . close ( )
  if 10 - 10: O0 . II111iiii / OoooooooOO
 else :
  iiiiiIIi = open ( IIIii1II1II , mode = 'w+' )
  iiiiiIIi . write ( 'date="01011001"\nversion="' + i1Ii11I1II + '"' )
  iiiiiIIi . close ( )
  if 72 - 72: OoooooooOO . o0oOOo0O0Ooo + O0
  if 46 - 46: OoOoOO00 * OO0oo0oOO / ooOo + Oo0Ooo + I1I1i
 if IiiIII111iI == 'false' :
  os . remove ( I1IiiIi11 )
  if 95 - 95: o0oOOo0O0Ooo - I1iii
  if 67 - 67: I1ii11iIi11i * Oo0Ooo % o0oOOo0O0Ooo
 iIio00O000ooOO = open ( O0O , mode = 'w+' )
 iIio00O000ooOO . write ( IIIiI1iiiIIIi )
 iIio00O000ooOO . close ( )
 if 62 - 62: iIIi1i1 * I1iii % I1ii11iIi11i - i1IIi - I1ii11iIi11i
 if 24 - 24: Oo
 if 'prof' in video :
  try :
   o0oOoOOO = open ( OOO0OOO00oo , mode = 'w+' )
   o0oOoOOO . write ( ooOo0o0o00 )
   o0oOoOOO . close ( )
  except : print "### Failed to write existing profile info back into profiles.xml"
  if 74 - 74: IiiI11Iiiii / oOOOoo0O0OoO / II111iiii - IiiI11Iiiii / ooOo % OO0oo0oOO
  if 19 - 19: I1I1i % OoooooooOO + OoooooooOO
 if video == 'library' or video == 'libprofile' or video == 'updatelibprofile' or video == 'updatelibrary' :
  oOOO ( O00oo , Ooo , ooOoOoo0O )
  if 7 - 7: i1IIi
  if 91 - 91: OoOoOO00 - OoOoOO00 . I1I1i
  if OO0ooOo != 1 :
   shutil . rmtree ( O00O0oOO00O00 )
 ooOoOoo0O . close ( )
 if 33 - 33: oOOOoo0O0OoO - iIii1I11I1II1 / I1iii % O0
 if 80 - 80: I1I1i % OoooooooOO - I1I1i
 if os . path . exists ( iiI111I1iIiI ) :
  i1I1II ( description )
  if 27 - 27: oOOOoo0O0OoO - o0oOOo0O0Ooo * I1ii11iIi11i - I1IiiI
  try :
   os . remove ( iiI111I1iIiI )
   if 22 - 22: Oo0Ooo % OoooooooOO - Oo0Ooo - IiiI11Iiiii . I1iii
  except :
   print "##' Failed to remove: " + iiI111I1iIiI
   if 100 - 100: II111iiii / oOOOoo0O0OoO / IiiI11Iiiii - I1ii11iIi11i * iIii1I11I1II1
  try :
   shutil . rmtree ( i1i )
   if 7 - 7: i1IIi . I1I1i % i11iIiiIii * I1ii11iIi11i . OO0oo0oOO % I1ii11iIi11i
  except :
   print "##' Failed to remove: " + i1i
   if 35 - 35: I1IiiI
 else : print "### Community Builds - using an old build"
 if 48 - 48: OoooooooOO % OoooooooOO - OoO0O00 . OoOoOO00
 if 22 - 22: iIIi1i1 . i11iIiiIii . OoooooooOO . i1IIi
 if OOOOo0o0O0 != i1iIii :
  print "### GUI SIZE DIFFERENT ATTEMPTING MERGE ###"
  IIIIiI1iiI = os . path . join ( OooO0 , 'newbuild' )
  if 13 - 13: OO0oo0oOO . OoO0O00
  if not os . path . exists ( IIIIiI1iiI ) :
   os . makedirs ( IIIIiI1iiI )
   if 73 - 73: I1iii * OoooooooOO * OO0oo0oOO - i11iIiiIii
  os . makedirs ( O0o0O00Oo0o0 )
  time . sleep ( 1 )
  OoIi11ii1 ( guisettingslink , video )
  time . sleep ( 1 )
  xbmc . executebuiltin ( 'UnloadSkin()' )
  time . sleep ( 1 )
  xbmc . executebuiltin ( 'ReloadSkin()' )
  time . sleep ( 1 )
  II . ok ( "Force Close Required" , "If you\'re seeing this message it means the force close was unsuccessful. Please close XBMC/Kodi via your operating system or pull the power." )
  if 58 - 58: o0oOOo0O0Ooo + OoOoOO00 - I1I1i
 if OOOOo0o0O0 == i1iIii :
  II . ok ( 'Successfully Updated' , 'Congratulations the following build:[COLOR=dodgerblue]' , description , '[/COLOR]has been successfully updated!' )
  if 82 - 82: I1iii . iIii1I11I1II1 / I1iii / ooOo % iIii1I11I1II1
  if 34 - 34: Oo
def oo0O0 ( url ) :
 I1i1I1i1Ii = 0
 OO0ooOo = 0
 print "Restore Location: " + url
 if 70 - 70: O0 . iIii1I11I1II1 * II111iiii
 iiiIIIi11I ( 'noobsandnerds.xml' )
 if 43 - 43: Oo0Ooo / oOOOoo0O0OoO / i1IIi
 III1II1i ( )
 if 3 - 3: I1iii * iIIi1i1 . OoO0O00 * OoooooooOO + OoOoOO00 / O0
 if url == 'local' :
  Ii1IOOO0oOo00o0 = xbmcgui . Dialog ( ) . browse ( 1 , 'Select the backup file you want to restore' , 'files' , '.zip' , False , False , Ooo0OO0oOO )
  if Ii1IOOO0oOo00o0 == '' :
   I1i1I1i1Ii = 1
   if 60 - 60: OO0oo0oOO
 if I1i1I1i1Ii == 1 :
  print "### No file selected, quitting restore process ###"
  return
  if 97 - 97: i11iIiiIii * iIii1I11I1II1 / II111iiii
 if url != 'local' :
  ooOoOoo0O . create ( "Community Builds" , "Downloading build." , '' , 'Please Wait' )
  Ii1IOOO0oOo00o0 = os . path . join ( ii11i1 , o00oO ( ) + '.zip' )
  if 66 - 66: II111iiii + IiiI11Iiiii * ooOo % OO0oo0oOO / i1IIi / iIii1I11I1II1
  if not os . path . exists ( ii11i1 ) :
   os . makedirs ( ii11i1 )
   if 62 - 62: OoOoOO00 + ooOo * I1I1i + O0 / Oo + iIIi1i1
  downloader . download ( url , Ii1IOOO0oOo00o0 , ooOoOoo0O )
  if 38 - 38: i1IIi / iIii1I11I1II1 + IiiI11Iiiii
 if os . path . exists ( OOoOO0oo0ooO ) :
  if os . path . exists ( iIi1ii1I1 ) :
   os . remove ( OOoOO0oo0ooO )
  else :
   os . rename ( OOoOO0oo0ooO , iIi1ii1I1 )
   if 26 - 26: I1ii11iIi11i . I1iii % o0oOOo0O0Ooo
 if os . path . exists ( o0 ) :
  os . remove ( o0 )
  if 4 - 4: oOOOoo0O0OoO
  if 80 - 80: Oo0Ooo . O0 % o0oOOo0O0Ooo . o0oOOo0O0Ooo
 if not os . path . exists ( i1I1iI ) :
  Oo0oO00 = open ( i1I1iI , mode = 'w+' )
  if 52 - 52: OoO0O00 % i11iIiiIii . iIIi1i1 % OoOoOO00 % OoooooooOO
 if os . path . exists ( O0o0O00Oo0o0 ) :
  os . removedirs ( O0o0O00Oo0o0 )
  if 5 - 5: OoOoOO00 / O0 / i11iIiiIii
  if 88 - 88: II111iiii - IiiI11Iiiii / OoooooooOO
 try :
  os . rename ( iIi1ii1I1 , OOoOO0oo0ooO )
  if 71 - 71: I1ii11iIi11i
 except :
  II . ok ( "NO GUISETTINGS!" , 'No guisettings.xml file has been found.' , 'Please exit XBMC and try again' , '' )
  return
  if 19 - 19: Oo0Ooo - OoO0O00 + i11iIiiIii / iIii1I11I1II1
 iIi1IiI = xbmcgui . Dialog ( ) . yesno ( I1ii1 , 'We highly recommend backing up your existing build before installing any builds. Would you like to perform a backup first?' , nolabel = 'Backup' , yeslabel = 'Install' )
 if iIi1IiI == 0 :
  IIIIi11111 = xbmc . translatePath ( os . path . join ( Ooo0OO0oOO , 'Community Builds' , 'My Builds' ) )
  if 1 - 1: I1I1i % i1IIi
  if not os . path . exists ( IIIIi11111 ) :
   os . makedirs ( IIIIi11111 )
   if 41 - 41: OoO0O00 * OoO0O00 / IiiI11Iiiii + I1ii11iIi11i . o0oOOo0O0Ooo
  IiI1Iii1 = Ooooo ( heading = "Enter a name for this backup" )
  if ( not IiI1Iii1 ) :
   return False , 0
   if 84 - 84: i11iIiiIii + OoO0O00 * I1IiiI + I1ii11iIi11i / I1iii
  ooOoOii1iII = urllib . quote_plus ( IiI1Iii1 )
  O00oo = xbmc . translatePath ( os . path . join ( IIIIi11111 , ooOoOii1iII + '.zip' ) )
  OoOoooO000OO = [ I1IiI ]
  O00Oooi1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , '.gitignore' ]
  OOoooOoO0Oo = "Creating full backup of existing build"
  Oo000 = "Archiving..."
  iiIiII11i1 = ""
  oOo00Ooo0o0 = "Please Wait"
  if 80 - 80: I1ii11iIi11i
  o0O0OO ( OooO0 , O00oo , OOoooOoO0Oo , Oo000 , iiIiII11i1 , oOo00Ooo0o0 , OoOoooO000OO , O00Oooi1 )
 ooOOO = xbmcgui . Dialog ( ) . yesno ( I1ii1 , 'Would you like to keep your existing database files or overwrite? Overwriting will wipe any existing music or video library you may have scanned in.' , nolabel = 'Overwrite' , yeslabel = 'Keep Existing' )
 if ooOOO == 1 :
  if os . path . exists ( O00O0oOO00O00 ) :
   shutil . rmtree ( O00O0oOO00O00 )
   if 95 - 95: OO0oo0oOO
  try :
   shutil . copytree ( Ooo , O00O0oOO00O00 , symlinks = False , ignore = shutil . ignore_patterns ( "Textures13.db" , "Addons16.db" , "Addons15.db" , "saltscache.db-wal" , "saltscache.db-shm" , "saltscache.db" , "onechannelcache.db" ) )
   if 76 - 76: II111iiii - i1IIi . O0 * i11iIiiIii % o0oOOo0O0Ooo - IiiI11Iiiii
  except :
   OO0ooOo = xbmcgui . Dialog ( ) . yesno ( I1ii1 , 'There was an error trying to backup some databases. Continuing may wipe your existing library. Do you wish to continue?' , nolabel = 'No, cancel' , yeslabel = 'Yes, overwrite' )
   if OO0ooOo == 1 : pass
   if OO0ooOo == 0 : I1i1I1i1Ii = 1 ; return
   if 30 - 30: oOOOoo0O0OoO % ooOo + ooOo * OoooooooOO - I1ii11iIi11i
  O00oo = xbmc . translatePath ( os . path . join ( Ooo0OO0oOO , 'Database.zip' ) )
  iIIIiIi1I1i ( O00O0oOO00O00 , O00oo )
  if 69 - 69: I1ii11iIi11i + OoO0O00 / O0 + II111iiii / i11iIiiIii
 if I1i1I1i1Ii == 1 :
  print "### Chose to exit restore function ###"
  return
  if 48 - 48: OoooooooOO / I1IiiI
 else :
  time . sleep ( 1 )
  I1I1ii1111 = open ( O0O , mode = 'r' )
  IIIiI1iiiIIIi = I1I1ii1111 . read ( )
  I1I1ii1111 . close ( )
  if 19 - 19: Oo * I1ii11iIi11i - iIIi1i1 * i11iIiiIii + OO0oo0oOO
  if 92 - 92: OoO0O00
  print "### Checking zip file structure ###"
  OOOooooOo0 = zipfile . ZipFile ( Ii1IOOO0oOo00o0 )
  if 'xbmc.log' in OOOooooOo0 . namelist ( ) or 'kodi.log' in OOOooooOo0 . namelist ( ) or '.git' in OOOooooOo0 . namelist ( ) or '.svn' in OOOooooOo0 . namelist ( ) :
   print "### Whoever created this build has used completely the wrong backup method, lets try and fix it! ###"
   II . ok ( 'Fixing Bad Zip' , 'Whoever created this build has used the wrong backup method, please wait while we fix it - this could take some time! Click OK to proceed' )
   iIIii1iI11IIi11I = zipfile . ZipFile ( Ii1IOOO0oOo00o0 , 'r' )
   o000o00OO00Oo = os . path . join ( ii11i1 , 'fixed.zip' )
   I1II11I11111i = zipfile . ZipFile ( o000o00OO00Oo , 'w' )
   if 14 - 14: I1I1i + o0oOOo0O0Ooo + I1ii11iIi11i * o0oOOo0O0Ooo + OoO0O00
   ooOoOoo0O . create ( "Fixing Build" , "Checking " , '' , 'Please Wait' )
   if 2 - 2: II111iiii % i11iIiiIii
   for i1I1I1I in iIIii1iI11IIi11I . infolist ( ) :
    buffer = iIIii1iI11IIi11I . read ( i1I1I1I . filename )
    i11iiIii11I1 = str ( i1I1I1I . filename )
    if 60 - 60: OoooooooOO * Oo0Ooo % oOOOoo0O0OoO
    if ( i1I1I1I . filename [ - 4 : ] != '.log' ) and not '.git' in i11iiIii11I1 and not '.svn' in i11iiIii11I1 :
     I1II11I11111i . writestr ( i1I1I1I , buffer )
     ooOoOoo0O . update ( 0 , "Fixing..." , '[COLOR yellow]%s[/COLOR]' % i1I1I1I . filename , 'Please Wait' )
     if 68 - 68: O0 - Oo0Ooo . II111iiii % I1iii % Oo0Ooo + i11iIiiIii
   ooOoOoo0O . close ( )
   I1II11I11111i . close ( )
   iIIii1iI11IIi11I . close ( )
   Ii1IOOO0oOo00o0 = o000o00OO00Oo
   if 90 - 90: II111iiii / Oo * I1IiiI - Oo0Ooo
  ooOoOoo0O . create ( "Restoring Backup Build" , "Checking " , '' , 'Please Wait' )
  ooOoOoo0O . update ( 0 , "" , "Extracting Zip Please Wait" )
  if 11 - 11: I1I1i - ooOo - ooOo / oOOOoo0O0OoO * II111iiii % ooOo
  try :
   oOOO ( Ii1IOOO0oOo00o0 , OooO0 , ooOoOoo0O )
  except :
   II . ok ( 'ERROR IN BUILD ZIP' , 'Please contact the build author, there are errors in this zip file that has caused the install process to fail. Most likely cause is it contains files with special characters in the name.' )
   return
   if 39 - 39: ooOo / i11iIiiIii
  time . sleep ( 1 )
  if 46 - 46: i11iIiiIii . I1ii11iIi11i
  if ooOOO == 1 :
   oOOO ( O00oo , Ooo , ooOoOoo0O )
   if 11 - 11: iIIi1i1
   if OO0ooOo != 1 :
    shutil . rmtree ( O00O0oOO00O00 )
    if 36 - 36: OoO0O00 % iIii1I11I1II1 - I1ii11iIi11i - i1IIi % o0oOOo0O0Ooo
  iIio00O000ooOO = open ( O0O , mode = 'w+' )
  iIio00O000ooOO . write ( IIIiI1iiiIIIi )
  iIio00O000ooOO . close ( )
  try :
   os . rename ( iIi1ii1I1 , o0 )
   if 54 - 54: I1I1i - II111iiii . iIIi1i1 + I1iii
  except :
   print "NO GUISETTINGS DOWNLOADED"
   if 45 - 45: ooOo + II111iiii . IiiI11Iiiii / I1ii11iIi11i
  time . sleep ( 1 )
  Oo0oO00 = open ( OOoOO0oo0ooO , mode = 'r' )
  iii = Oo0oO00 . read ( )
  Oo0oO00 . close ( )
  Ii1i = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( iii )
  IiI1 = Ii1i [ 0 ] if ( len ( Ii1i ) > 0 ) else ''
  ooooOoOooo00Oo = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( iii )
  Iii1IIII1Iii = ooooOoOooo00Oo [ 0 ] if ( len ( ooooOoOooo00Oo ) > 0 ) else ''
  ooo00O0OOo = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( iii )
  OO = ooo00O0OOo [ 0 ] if ( len ( ooo00O0OOo ) > 0 ) else ''
  if 76 - 76: I1iii + IiiI11Iiiii - I1I1i * iIii1I11I1II1 % i1IIi
  try :
   OooO0O0Ooo = open ( o0 , mode = 'r' )
   oO0O = OooO0O0Ooo . read ( )
   OooO0O0Ooo . close ( )
   o0ooo = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( oO0O )
   iiiI1 = o0ooo [ 0 ] if ( len ( o0ooo ) > 0 ) else ''
   o0oo00O = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( oO0O )
   O00oooO00oo = o0oo00O [ 0 ] if ( len ( o0oo00O ) > 0 ) else ''
   IIIIII1iI1II = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( oO0O )
   Ii111III1i11I = IIIIII1iI1II [ 0 ] if ( len ( IIIIII1iI1II ) > 0 ) else ''
   iiIiIiII = iii . replace ( IiI1 , iiiI1 ) . replace ( OO , Ii111III1i11I ) . replace ( Iii1IIII1Iii , O00oooO00oo )
   iiiiiIIi = open ( OOoOO0oo0ooO , mode = 'w+' )
   iiiiiIIi . write ( str ( iiIiIiII ) )
   iiiiiIIi . close ( )
   if 72 - 72: iIIi1i1 + II111iiii . O0 - IiiI11Iiiii / OoooooooOO . oOOOoo0O0OoO
  except :
   print "NO GUISETTINGS DOWNLOADED"
   if 28 - 28: iIii1I11I1II1 . O0
  if os . path . exists ( iIi1ii1I1 ) :
   os . remove ( iIi1ii1I1 )
   if 32 - 32: OoooooooOO
  os . rename ( OOoOO0oo0ooO , iIi1ii1I1 )
  try :
   os . remove ( o0 )
   if 29 - 29: I1ii11iIi11i
  except :
   pass
   if 41 - 41: I1iii
  os . makedirs ( O0o0O00Oo0o0 )
  time . sleep ( 1 )
  IiIIIi ( )
  if 49 - 49: I1iii % II111iiii . I1iii - o0oOOo0O0Ooo - OO0oo0oOO * I1I1i
  if 47 - 47: O0 . o0oOOo0O0Ooo / I1iii * IiiI11Iiiii
  if 63 - 63: oOOOoo0O0OoO - ooOo - IiiI11Iiiii - iIIi1i1 / ooOo + OoO0O00
  if 94 - 94: I1I1i / I1IiiI . II111iiii
  if 32 - 32: ooOo . Oo % Oo . OoOoOO00
  if 37 - 37: Oo + O0 + Oo . IiiI11Iiiii . o0oOOo0O0Ooo
  if 78 - 78: I1IiiI / OO0oo0oOO + o0oOOo0O0Ooo . Oo0Ooo / O0
  if 49 - 49: I1ii11iIi11i
  if 66 - 66: o0oOOo0O0Ooo . I1ii11iIi11i
  if 18 - 18: Oo0Ooo + I1I1i
  if 79 - 79: OoO0O00 - O0 + II111iiii % I1iii . I1IiiI
  if 43 - 43: I1IiiI % I1ii11iIi11i * I1iii
  if 31 - 31: I1iii / IiiI11Iiiii
  if 3 - 3: I1I1i
  if 37 - 37: I1iii * OoooooooOO * OO0oo0oOO + Oo0Ooo . I1IiiI
  if 61 - 61: Oo . Oo
  if 17 - 17: II111iiii / iIIi1i1
  if 80 - 80: Oo * OoO0O00 + I1iii
  if 62 - 62: OoooooooOO . O0 % Oo0Ooo
def iiIi1I ( ) :
 III1II1i ( )
 OOOOo00oOOO00 = xbmcgui . Dialog ( ) . browse ( 1 , 'Select the guisettings zip file you want to restore' , 'files' , '.zip' , False , False , Ooo0OO0oOO )
 if 13 - 13: I1ii11iIi11i / OoO0O00 * i11iIiiIii % OoO0O00 % OoO0O00 * II111iiii
 if OOOOo00oOOO00 == '' :
  return
  if 17 - 17: OO0oo0oOO . O0 * i1IIi - OoOoOO00 % i1IIi
 else :
  I1Ii1IIi = 1
  i1ooO ( OOOOo00oOOO00 , I1Ii1IIi )
  if 35 - 35: I1iii + I1ii11iIi11i . ooOo * Oo0Ooo
  if 27 - 27: iIii1I11I1II1 / I1iii - I1I1i - Oo0Ooo
def O0iIIii1 ( url , name ) :
 iIi1IiI = xbmcgui . Dialog ( ) . yesno ( 'Full Wipe And New Install' , 'This is a great option for first time install or if you\'re encountering any issues with your device. This will wipe all your Kodi settings, do you wish to continue?' , nolabel = 'Cancel' , yeslabel = 'Accept' )
 if iIi1IiI == 0 :
  return
  if 12 - 12: OO0oo0oOO . I1iii + OO0oo0oOO - Oo * IiiI11Iiiii - O0
 elif iIi1IiI == 1 :
  IiiI1Ii1IIi = '/storage/.restore/'
  iI1i1IiIIIIi = os . path . join ( IiiI1Ii1IIi , '20141128094249.tar' )
  if not os . path . exists ( IiiI1Ii1IIi ) :
   try :
    os . makedirs ( IiiI1Ii1IIi )
   except :
    pass
  downloader . download ( url , iI1i1IiIIIIi )
  time . sleep ( 2 )
  if 8 - 8: Oo % IiiI11Iiiii . ooOo
  OOo = 'http://120.24.252.100/TI/Community_Builds/downloadcount.php?id=%s' % ( name )
  try :
   ooI1111i ( OOo )
  except :
   pass
   if 39 - 39: I1IiiI . ooOo
  II . ok ( "Download Complete - Press OK To Reboot" , 'Once you press OK your device will attempt to reboot, if it hasn\'t rebooted within 30 seconds please pull the power to manually shutdown. When booting you may see lines of text, don\'t worry this is normal update behaviour!' )
  xbmc . executebuiltin ( 'Reboot' )
  if 4 - 4: i1IIi % o0oOOo0O0Ooo % ooOo . i1IIi
  if 85 - 85: I1I1i . I1iii * o0oOOo0O0Ooo % Oo0Ooo % II111iiii + oOOOoo0O0OoO
def oo00iiIIiIi1Ii1 ( ) :
 I1i1I1i1Ii = 0
 iIi1IiI = xbmcgui . Dialog ( ) . yesno ( 'Full Wipe And New Install' , 'This is a great option if you\'re encountering any issues with your device. This will wipe all your Kodi settings and restore with whatever is in the backup, do you wish to continue?' , nolabel = 'Cancel' , yeslabel = 'Accept' )
 if iIi1IiI == 0 :
  return
  if 76 - 76: i1IIi % iIii1I11I1II1 - o0oOOo0O0Ooo + I1I1i - OO0oo0oOO
 elif iIi1IiI == 1 :
  Ii1IOOO0oOo00o0 = xbmcgui . Dialog ( ) . browse ( 1 , 'Select the backup file you want to restore' , 'files' , '.tar' , False , False , ooOooo000oOO )
  if Ii1IOOO0oOo00o0 == '' :
   I1i1I1i1Ii = 1
   if 81 - 81: I1ii11iIi11i + OoooooooOO - Oo * O0
  if I1i1I1i1Ii == 1 :
   print "### No file selected, quitting restore process ###"
   return
  iI1i1IiIIIIi = os . path . join ( Oo0oOOo , '20141128094249.tar' )
  if not os . path . exists ( Oo0oOOo ) :
   try :
    os . makedirs ( Oo0oOOo )
   except :
    pass
  ooOoOoo0O . create ( 'Copying File To Restore Folder' , '' , 'Please wait...' )
  shutil . copyfile ( Ii1IOOO0oOo00o0 , iI1i1IiIIIIi )
  xbmc . executebuiltin ( 'Reboot' )
  if 100 - 100: iIii1I11I1II1 - OoOoOO00
  if 28 - 28: Oo0Ooo . O0 . OO0oo0oOO
def Ooo00O ( ) :
 oOO0o0oo0 ( )
 if I1IIIIiii1i ( ) :
  OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue]Restore a locally stored OpenELEC Backup[/COLOR]' , '' , 'restore_local_OE' , 'Restore.png' , '' , '' , 'Restore A Full OE System Backup' )
  if 60 - 60: i1IIi
 OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue]Restore A Locally stored build[/COLOR]' , 'local' , 'restore_local_CB' , 'Restore.png' , '' , '' , 'Restore A Full System Backup' )
 OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue]Restore Local guisettings file[/COLOR]' , 'url' , 'LocalGUIDialog' , 'Restore.png' , '' , '' , 'Back Up Your Full System' )
 if 57 - 57: iIIi1i1
 if os . path . exists ( os . path . join ( Ooo0OO0oOO , 'addons.zip' ) ) :
  OOo0oO00ooO00 ( '' , 'Restore Your Addons' , 'addons' , 'restore_zip' , 'Restore.png' , '' , '' , 'Restore Your Addons' )
  if 99 - 99: Oo0Ooo + oOOOoo0O0OoO % iIIi1i1 - o0oOOo0O0Ooo
 if os . path . exists ( os . path . join ( Ooo0OO0oOO , 'addon_data.zip' ) ) :
  OOo0oO00ooO00 ( '' , 'Restore Your Addon UserData' , 'addon_data' , 'restore_zip' , 'Restore.png' , '' , '' , 'Restore Your Addon UserData' )
  if 52 - 52: I1ii11iIi11i
 if os . path . exists ( os . path . join ( Ooo0OO0oOO , 'guisettings.xml' ) ) :
  OOo0oO00ooO00 ( '' , 'Restore Guisettings.xml' , iIi1ii1I1 , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your guisettings.xml' )
  if 93 - 93: IiiI11Iiiii . i11iIiiIii
 if os . path . exists ( os . path . join ( Ooo0OO0oOO , 'favourites.xml' ) ) :
  OOo0oO00ooO00 ( '' , 'Restore Favourites.xml' , o00oOO0 , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your favourites.xml' )
  if 24 - 24: Oo . OoO0O00 + oOOOoo0O0OoO . ooOo - I1ii11iIi11i % IiiI11Iiiii
 if os . path . exists ( os . path . join ( Ooo0OO0oOO , 'sources.xml' ) ) :
  OOo0oO00ooO00 ( '' , 'Restore Source.xml' , oOoo , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your sources.xml' )
  if 49 - 49: O0 . Oo0Ooo / I1iii
 if os . path . exists ( os . path . join ( Ooo0OO0oOO , 'advancedsettings.xml' ) ) :
  OOo0oO00ooO00 ( '' , 'Restore Advancedsettings.xml' , iIii11I , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your advancedsettings.xml' )
  if 29 - 29: I1ii11iIi11i / ooOo * O0 - i11iIiiIii - OoO0O00 + I1iii
 if os . path . exists ( os . path . join ( Ooo0OO0oOO , 'keyboard.xml' ) ) :
  OOo0oO00ooO00 ( '' , 'Restore Advancedsettings.xml' , iiii11I , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your keyboard.xml' )
  if 86 - 86: I1IiiI / I1ii11iIi11i * I1iii % i11iIiiIii
 if os . path . exists ( os . path . join ( Ooo0OO0oOO , 'RssFeeds.xml' ) ) :
  OOo0oO00ooO00 ( '' , 'Restore RssFeeds.xml' , Iii111II , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your RssFeeds.xml' )
  if 20 - 20: IiiI11Iiiii . OoooooooOO + IiiI11Iiiii + iIIi1i1 * I1ii11iIi11i
  if 44 - 44: i11iIiiIii
def o0OooO0ooo00o ( url ) :
 III1II1i ( )
 if 'addons' in url :
  IiI1I1II = xbmc . translatePath ( os . path . join ( Ooo0OO0oOO , 'addons.zip' ) )
  IIIiiIIIiI1 = Oo00OOOOO
  if 53 - 53: o0oOOo0O0Ooo - iIii1I11I1II1 - Oo - ooOo
 else :
  IiI1I1II = xbmc . translatePath ( os . path . join ( Ooo0OO0oOO , 'addon_data.zip' ) )
  IIIiiIIIiI1 = OO0o
  if 79 - 79: i11iIiiIii
 if 'Backup' in I1ii1 :
  oOo00oOO ( )
  ooOoOoo0O . create ( "Creating Backup" , "Backing Up" , '' , 'Please Wait' )
  Ii1II11II1iii = zipfile . ZipFile ( IiI1I1II , 'w' , zipfile . ZIP_DEFLATED )
  o0oOO0ooOoO = len ( IIIiiIIIiI1 )
  ooO0000o00O = [ ]
  O0Ooo = [ ]
  for o0iIiiIiiIi , i1iiIIIi , Oo0o in os . walk ( IIIiiIIIiI1 ) :
   for file in Oo0o :
    O0Ooo . append ( file )
  Ooo0oO0 = len ( O0Ooo )
  for o0iIiiIiiIi , i1iiIIIi , Oo0o in os . walk ( IIIiiIIIiI1 ) :
   for file in Oo0o :
    ooO0000o00O . append ( file )
    ii1I1I111 = len ( ooO0000o00O ) / float ( Ooo0oO0 ) * 100
    ooOoOoo0O . update ( int ( ii1I1I111 ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
    Ii1Ii = os . path . join ( o0iIiiIiiIi , file )
    if not 'temp' in i1iiIIIi :
     if not I1IiI in i1iiIIIi :
      import time
      iIiIii1I1II = '01/01/1980'
      O0Oooo = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( Ii1Ii ) ) )
      if O0Oooo > iIiIii1I1II :
       Ii1II11II1iii . write ( Ii1Ii , Ii1Ii [ o0oOO0ooOoO : ] )
  Ii1II11II1iii . close ( )
  ooOoOoo0O . close ( )
  II . ok ( "Backup Complete" , "You Are Now Backed Up" , '' , '' )
  if 81 - 81: IiiI11Iiiii + I1I1i - i11iIiiIii
 else :
  ooOoOoo0O . create ( "Extracting Zip" , "Checking " , '' , 'Please Wait' )
  ooOoOoo0O . update ( 0 , "" , "Extracting Zip Please Wait" )
  oOOO ( IiI1I1II , IIIiiIIIiI1 , ooOoOoo0O )
  time . sleep ( 1 )
  xbmc . executebuiltin ( 'UpdateLocalAddons ' )
  xbmc . executebuiltin ( "UpdateAddonRepos" )
  if 60 - 60: oOOOoo0O0OoO
  if 'Backup' in I1ii1 :
   II . ok ( "Install Complete" , 'To ensure the skin settings are set correctly Kodi will now close. If Kodi doesn\'t close please force close (pull power or force close in your OS - [COLOR=lime]DO NOT exit via Kodi menu[/COLOR])' )
   IiIIIi ( )
   if 14 - 14: Oo0Ooo % ooOo * IiiI11Iiiii - i11iIiiIii / I1ii11iIi11i * i11iIiiIii
  else :
   II . ok ( "SUCCESS!" , "You Are Now Restored" , '' , '' )
   if 95 - 95: iIii1I11I1II1 + OoOoOO00 . I1IiiI + OoOoOO00 * OO0oo0oOO + Oo
   if 14 - 14: I1iii - O0
def OoOO0Ooo ( url ) :
 xbmc . executebuiltin ( 'RunAddon(' + url + ')' )
 if 95 - 95: OoO0O00 - I1I1i % oOOOoo0O0OoO
 if 27 - 27: iIii1I11I1II1 / I1IiiI % OoOoOO00 / I1IiiI * I1iii
def I11II1I ( title ) :
 I1IO0 = ''
 oooOO = xbmc . Keyboard ( I1IO0 , title )
 oooOO . doModal ( )
 if oooOO . isConfirmed ( ) :
  I1IO0 = oooOO . getText ( ) . replace ( ' ' , '%20' )
  if I1IO0 == None :
   return False
 return I1IO0
 if 7 - 7: I1I1i * iIIi1i1 + OoOoOO00
 if 22 - 22: IiiI11Iiiii
def iIiOo ( url ) :
 IiI1Iii1 = Ooooo ( heading = "Search for add-ons" )
 if 53 - 53: OoooooooOO % OO0oo0oOO % iIii1I11I1II1 / Oo0Ooo + oOOOoo0O0OoO * I1iii
 if ( not IiI1Iii1 ) : return False , 0
 if 38 - 38: Oo0Ooo . Oo - oOOOoo0O0OoO
 if 10 - 10: ooOo * I1I1i * IiiI11Iiiii . O0
 ooOoOii1iII = urllib . quote_plus ( IiI1Iii1 )
 url += ooOoOii1iII
 i1iI1IIi1I ( url )
 if 19 - 19: I1I1i
 if 75 - 75: I1iii % O0
def ooi1 ( url ) :
 IiI1Iii1 = Ooooo ( heading = "Search for content" )
 if 26 - 26: O0 * I1iii - I1IiiI - IiiI11Iiiii / iIii1I11I1II1
 if 57 - 57: I1ii11iIi11i - OoO0O00 * iIii1I11I1II1
 if ( not IiI1Iii1 ) : return False , 0
 if 26 - 26: OoO0O00 % iIIi1i1 % o0oOOo0O0Ooo % OoOoOO00 . IiiI11Iiiii % O0
 if 91 - 91: II111iiii . Oo0Ooo . ooOo - OoooooooOO / OoOoOO00
 ooOoOii1iII = urllib . quote_plus ( IiI1Iii1 )
 url += ooOoOii1iII
 i1Iii ( url )
 if 30 - 30: OO0oo0oOO % o0oOOo0O0Ooo + i1IIi * OoooooooOO * OoO0O00 - II111iiii
 if 55 - 55: OoO0O00
def I111II1ii11I1 ( url ) :
 Oo0O00O000 = 'http://120.24.252.100/TI/Community_Builds/community_builds.php?id=%s' % ( url )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0oO = re . compile ( 'name="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i11I = re . compile ( 'author="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IIo0Oo0oO0oOO00 = re . compile ( 'version="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1ii1 = oo0oO [ 0 ] if ( len ( oo0oO ) > 0 ) else ''
 I11II1i1 = i11I [ 0 ] if ( len ( i11I ) > 0 ) else ''
 IiIiIi = IIo0Oo0oO0oOO00 [ 0 ] if ( len ( IIo0Oo0oO0oOO00 ) > 0 ) else ''
 II . ok ( I1ii1 , 'Author: [COLOR=dodgerblue]' + I11II1i1 + '[/COLOR]      Latest Version: [COLOR=dodgerblue]' + IiIiIi + '[/COLOR]' , '' , 'Click OK to view the build page.' )
 try :
  I1oo ( url + '&visibility=homepage' , url )
 except :
  return
  print "### Could not find build No. " + url
  II . ok ( 'Build Not Found' , 'Sorry we couldn\'t find the build, it may be it\'s marked as private. Please try manually searching via the Community Builds section' )
  if 41 - 41: i11iIiiIii
  if 34 - 34: II111iiii + Oo0Ooo . ooOo
def iii1II ( url ) :
 II . ok ( "This build is not complete" , 'The guisettings.xml file was not copied over during the last install process. Click OK to go to the build page and complete Install Step 2 (guisettings fix).' )
 if 34 - 34: OoOoOO00 . OO0oo0oOO % ooOo - O0 * O0
 try :
  I1oo ( url + '&visibility=homepage' , url )
  if 11 - 11: O0 * i11iIiiIii * II111iiii / Oo * O0
 except :
  return
  print "### Could not find build No. " + url
  II . ok ( 'Build Not Found' , 'Sorry we couldn\'t find the build, it may be it\'s marked as private. Please try manually searching via the Community Builds section' )
  if 71 - 71: OO0oo0oOO . Oo0Ooo
  if 24 - 24: Oo * OoooooooOO . O0 . OoO0O00 . I1IiiI
def OooO00ooo0o0 ( ) :
 Oo0O00O000 = 'http://120.24.252.100/TI/login/login_details.php?user=%s&pass=%s' % ( Oo0oO0ooo , o0oOoO00o )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OoOOoo0O00 = re . compile ( 'posts="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o00OOoo0 = re . compile ( 'messages="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i1I11i = re . compile ( 'unread="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OOOO00oOO = re . compile ( 'email="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OOO00O0oOOoOo = o00OOoo0 [ 0 ] if ( len ( o00OOoo0 ) > 0 ) else ''
 IIIII11i = i1I11i [ 0 ] if ( len ( i1I11i ) > 0 ) else ''
 Oo0oOo0 = OOOO00oOO [ 0 ] if ( len ( OOOO00oOO ) > 0 ) else ''
 OOoO0OooO = OoOOoo0O00 [ 0 ] if ( len ( OoOOoo0O00 ) > 0 ) else ''
 II . ok ( '[COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR]' , 'Username:  ' + Oo0oO0ooo , 'Email: ' + Oo0oOo0 , 'Unread Messages: ' + IIIII11i + '/' + OOO00O0oOOoOo + '[CR]Posts: ' + OOoO0OooO )
 if 38 - 38: I1IiiI . ooOo / O0 % Oo0Ooo / I1I1i / OoooooooOO
 if 11 - 11: O0 / oOOOoo0O0OoO / iIii1I11I1II1 % I1iii
def I1iiii ( url , type ) :
 if type == 'communitybuilds' :
  I1iI1Ii1I1Iii1 = 'grab_builds'
  if url . endswith ( "visibility=premium" ) :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , '&reseller=' + urllib . quote ( O0oo0OO0 ) + '&token=' + I1i1iiI1 + '&visibility=premium' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
  if url . endswith ( "visibility=reseller_private" ) :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , '&reseller=' + urllib . quote ( O0oo0OO0 ) + '&token=' + I1i1iiI1 + '&visibility=reseller_private' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
  if url . endswith ( "visibility=public" ) :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , '&visibility=public' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
  if url . endswith ( "visibility=private" ) :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , '&visibility=private' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
 if type == 'tutorials' :
  I1iI1Ii1I1Iii1 = 'grab_tutorials'
 if type == 'hardware' :
  I1iI1Ii1I1Iii1 = 'grab_hardware'
 if type == 'addons' :
  I1iI1Ii1I1Iii1 = 'grab_addons'
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Sort by Most Popular[/COLOR]' , str ( url ) + '&sortx=downloads&orderx=DESC' , I1iI1Ii1I1Iii1 , 'Popular.png' , '' , '' , '' )
 if type == 'hardware' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=lime]Filter Results[/COLOR]' , url , 'hardware_filter_menu' , 'Filter.png' , '' , '' , '' )
 if type != 'addons' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Sort by Most Popular[/COLOR]' , str ( url ) + '&sortx=downloadcount&orderx=DESC' , I1iI1Ii1I1Iii1 , 'Popular.png' , '' , '' , '' )
 if type == 'tutorials' or type == 'hardware' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Sort by Newest[/COLOR]' , str ( url ) + '&sortx=Added&orderx=DESC' , I1iI1Ii1I1Iii1 , 'Latest.png' , '' , '' , '' )
 else :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Sort by Newest[/COLOR]' , str ( url ) + '&sortx=created&orderx=DESC' , I1iI1Ii1I1Iii1 , 'Latest.png' , '' , '' , '' )
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Sort by Recently Updated[/COLOR]' , str ( url ) + '&sortx=updated&orderx=DESC' , I1iI1Ii1I1Iii1 , 'Recently_Updated.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Sort by A-Z[/COLOR]' , str ( url ) + '&sortx=name&orderx=ASC' , I1iI1Ii1I1Iii1 , 'AtoZ.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Sort by Z-A[/COLOR]' , str ( url ) + '&sortx=name&orderx=DESC' , I1iI1Ii1I1Iii1 , 'ZtoA.png' , '' , '' , '' )
 if type == 'public_CB' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Sort by Genre[/COLOR]' , url , 'genres' , 'Search_Genre.png' , '' , '' , '' )
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Sort by Country/Language[/COLOR]' , url , 'countries' , 'Search_Country.png' , '' , '' , '' )
  if 9 - 9: iIii1I11I1II1 / II111iiii * Oo
  if 96 - 96: I1iii + I1ii11iIi11i * OoOoOO00 * I1I1i * I1ii11iIi11i . I1ii11iIi11i
def i1I11iIIiIIiIi ( ) :
 IiI1IiI1iiI1 ( 'Speed Test Instructions' , '[COLOR=blue][B]What file should I use: [/B][/COLOR][CR]This function will download a file and will work out your speed based on how long it took to download. You will then be notified of '
 'what quality streams you can expect to stream without buffering. You can choose to download a 10MB, 16MB, 32MB, 64MB or 128MB file to use with the test. Using the larger files will give you a better '
 'indication of how reliable your speeds are but obviously if you have a limited amount of bandwidth allowance you may want to opt for a smaller file.'
 '[CR][CR][COLOR=blue][B]How accurate is this speed test:[/B][/COLOR][CR]Not very accurate at all! As this test is based on downloading a file from a server it\'s reliant on the server not having a go-slow day '
 'but the servers used should be pretty reliable. The 10MB file is hosted on a different server to the others so if you\'re not getting the results expected please try another file. If you have a fast fiber '
 'connection the chances are your speed will show as considerably slower than your real download speed due to the server not being able to send the file as fast as your download speed allows. Essentially the '
 'test results will be limited by the speed of the server but you will at least be able to see if it\'s your connection that\'s causing buffering or if it\'s the host you\'re trying to stream from'
 '[CR][CR][COLOR=blue][B]What is the differnce between Live Streams and Online Video:[/COLOR][/B][CR]When you run the test you\'ll see results based on your speeds and these let you know the quality you should expect to '
 'be able stream with your connection. Live Streams as the title suggests are like traditional TV channels, they are being streamed live so for example if you wanted to watch CNN this would fall into this category. '
 'Online Videos relates to movies, tv shows, youtube clips etc. Basically anything that isn\'t live - if you\'re new to the world of streaming then think of it as On Demand content, this is content that\'s been recorded and stored on the web.'
 '[CR][CR][COLOR=blue][B]Why am I still getting buffering:[/COLOR][/B][CR]The results you get from this test are strictly based on your download speed, there are many other factors that can cause buffering and contrary to popular belief '
 'having a massively fast internet connection will not make any difference to your buffering issues if the server you\'re trying to get the content from is unable to send it fast enough. This can often happen and is usually '
 'down to heavy traffic (too many users accessing the same server). A 10 Mb/s connection should be plenty fast enough for almost all content as it\'s very rare a server can send it any quicker than that.'
 '[CR][CR][COLOR=blue][B]What\'s the difference between MB/s and Mb/s:[/COLOR][/B][CR]A lot of people think the speed they see advertised by their ISP is Megabytes (MB/S) per second - this is not true. Speeds are usually shown as Mb/s '
 'which is Megabit per second - there are 8 of these to a megabyte so if you want to work out how many megabytes per second you\'re getting you need to divide the speed by 8. It may sound sneaky but really it\'s just the unit that has always been used.'
 '[CR][CR]A direct link to the buffering thread explaining what you can do to improve your viewing experience can be found at [COLOR=yellow]http://bit.ly/bufferingfix[/COLOR]'
 '[CR][CR]Thank you, [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] Team.' )
 if 45 - 45: I1IiiI
def IiI1i11i ( ) :
 OOo0oO00ooO00 ( '' , '[COLOR=blue]Instructions - Read me first[/COLOR]' , 'none' , 'speed_instructions' , 'howto.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Download 16MB file   - [COLOR=lime]Server 1[/COLOR]' , 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/16MB.txt' , 'runtest' , 'Download16.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Download 32MB file   - [COLOR=lime]Server 1[/COLOR]' , 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/32MB.txt' , 'runtest' , 'Download32.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Download 64MB file   - [COLOR=lime]Server 1[/COLOR]' , 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/64MB.txt' , 'runtest' , 'Download64.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Download 128MB file - [COLOR=lime]Server 1[/COLOR]' , 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/128MB.txt' , 'runtest' , 'Download128.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Download 10MB file   - [COLOR=yellow]Server 2[/COLOR]' , 'http://www.wswd.net/testdownloadfiles/10MB.zip' , 'runtest' , 'Download10.png' , '' , '' , '' )
 if 36 - 36: o0oOOo0O0Ooo % OO0oo0oOO * I1ii11iIi11i % I1iii + i1IIi - Oo0Ooo
 if 56 - 56: I1ii11iIi11i
def IiI1IiI1iiI1 ( heading , anounce ) :
 class II1iIii1Ii ( ) :
  WINDOW = 10147
  CONTROL_LABEL = 1
  CONTROL_TEXTBOX = 5
  def __init__ ( self , * args , ** kwargs ) :
   xbmc . executebuiltin ( "ActivateWindow(%d)" % ( self . WINDOW , ) )
   self . win = xbmcgui . Window ( self . WINDOW )
   xbmc . sleep ( 500 )
   self . setControls ( )
  def setControls ( self ) :
   self . win . getControl ( self . CONTROL_LABEL ) . setLabel ( heading )
   try : ooOo0O0o0 = open ( anounce ) ; OoOO0OO00 = ooOo0O0o0 . read ( )
   except : OoOO0OO00 = anounce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( OoOO0OO00 ) )
   return
 II1iIii1Ii ( )
 while xbmc . getCondVisibility ( 'Window.IsVisible(textviewer)' ) :
  xbmc . sleep ( 500 )
  if 28 - 28: O0 / o0oOOo0O0Ooo . I1iii / O0 . ooOo - o0oOOo0O0Ooo
  if 63 - 63: Oo / II111iiii . OoOoOO00 / i1IIi / OO0oo0oOO . o0oOOo0O0Ooo
def iIIiiiIiiii11 ( name , url ) :
 IiI1IiI1iiI1 ( name , url )
 if 22 - 22: OO0oo0oOO
 if 50 - 50: I1I1i . OO0oo0oOO / I1iii . O0 . i11iIiiIii + II111iiii
def o00oO ( ) :
 II1i1II1iIi = time . time ( )
 iII = time . localtime ( II1i1II1iIi )
 return time . strftime ( '%Y%m%d%H%M%S' , iII )
 if 89 - 89: OoOoOO00 % ooOo + OoooooooOO * o0oOOo0O0Ooo % iIii1I11I1II1
 if 79 - 79: OO0oo0oOO * IiiI11Iiiii
def iI1iIIII11 ( ) :
 OOo0oO00ooO00 ( '' , '[COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] Keyword Install' , IIIi1I1IIii1II , 'keywords' , 'Keywords.png' , '' , '' , '' )
 if I1IIIIiii1i ( ) :
  OOo0oO00ooO00 ( '' , '[COLOR=darkcyan]Wi-Fi Settings[/COLOR]' , '' , 'openelec_settings' , 'Wi-Fi.png' , '' , '' , '' )
  if 91 - 91: I1I1i % OO0oo0oOO + oOOOoo0O0OoO
  if 9 - 9: Oo0Ooo + II111iiii / II111iiii % Oo
  if 45 - 45: Oo * OoooooooOO - i1IIi
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Add-on Maintenance/Fixes[/COLOR]' , 'none' , 'addonfixes' , 'Addon_Fixes.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Backup/Restore My Content[/COLOR]' , 'none' , 'backup_restore' , 'Backup.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Clean/Wipe Options[/COLOR]' , 'none' , 'wipetools' , 'Addon_Fixes.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Check My IP Address' , 'none' , 'ipcheck' , 'Check_IP.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Check XBMC/Kodi Version' , 'none' , 'xbmcversion' , 'Version_Check.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Convert Physical Paths To Special' , OooO0 , 'fix_special' , 'Special_Paths.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Force Close Kodi' , 'url' , 'kill_xbmc' , 'Kill_XBMC.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Test My Download Speed' , 'none' , 'speedtest_menu' , 'Speed_Test.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Upload Log' , 'none' , 'uploadlog' , 'Log_File.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'View My Log' , 'none' , 'log' , 'View_Log.png' , '' , '' , '' )
 if 42 - 42: ooOo
 if 38 - 38: OoooooooOO . I1I1i . iIii1I11I1II1
def iIi1 ( url ) :
 OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow]1. Add-on Maintenance[/COLOR]' , str ( url ) + '&type=Maintenance' , 'grab_tutorials' , 'Maintenance.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Audio Add-ons' , str ( url ) + '&type=Audio' , 'grab_tutorials' , 'Audio.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Picture Add-ons' , str ( url ) + '&type=Pictures' , 'grab_tutorials' , 'Pictures.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Program Add-ons' , str ( url ) + '&type=Programs' , 'grab_tutorials' , 'Programs.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Video Add-ons' , str ( url ) + '&type=Video' , 'grab_tutorials' , 'Video.png' , '' , '' , '' )
 if 35 - 35: II111iiii % Oo . ooOo * iIIi1i1
 if 54 - 54: iIIi1i1 * OO0oo0oOO - oOOOoo0O0OoO
def i1iI1iii111 ( url ) :
 OOo = 'http://totalxbmc.com/TI/TutorialPortal/downloadcount.php?id=%s' % ( url )
 ooI1111i ( OOo )
 Oo0O00O000 = 'http://totalxbmc.com/TI/TutorialPortal/tutorialdetails.php?id=%s' % ( url )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0oO = re . compile ( 'name="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i11I = re . compile ( 'author="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiIIiI11II1 = re . compile ( 'video_guide1="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oooOo = re . compile ( 'video_guide2="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oOoO0Oo0 = re . compile ( 'video_guide3="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i11i11i = re . compile ( 'video_guide4="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiI1iI = re . compile ( 'video_guide5="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Ooo00O0 = re . compile ( 'video_label1="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OoO0OOoO0 = re . compile ( 'video_label2="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiI11i = re . compile ( 'video_label3="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0Oo = re . compile ( 'video_label4="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiI1i = re . compile ( 'video_label5="(.+?)"' ) . findall ( i11I1IiII1i1i )
 ooOooo = re . compile ( 'about="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Oo00 = re . compile ( 'step1="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0OO00 = re . compile ( 'step2="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oOO00 = re . compile ( 'step3="(.+?)"' ) . findall ( i11I1IiII1i1i )
 II1IiII1I1II = re . compile ( 'step4="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oooOII111iiI1Ii1 = re . compile ( 'step5="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oo0oO0oO00oO = re . compile ( 'step6="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0OOo000ooo0o = re . compile ( 'step7="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oo00oO0o000 = re . compile ( 'step8="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iIi1ii = re . compile ( 'step9="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1I11I1iIIiI1i = re . compile ( 'step10="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O0oOOOOooOo0 = re . compile ( 'step11="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0000o0OOOo = re . compile ( 'step12="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiiiiI1iii11 = re . compile ( 'step13="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IIIi11iiIIi = re . compile ( 'step14="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oOo000O00O = re . compile ( 'step15="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1IIiIi = re . compile ( 'screenshot1="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OOOOoOoO = re . compile ( 'screenshot2="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OO000 = re . compile ( 'screenshot3="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0oOoo0o = re . compile ( 'screenshot4="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IiiIiIIi = re . compile ( 'screenshot5="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O00Oo = re . compile ( 'screenshot6="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oOOoooo0O0 = re . compile ( 'screenshot7="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Ii111Ii11 = re . compile ( 'screenshot8="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Ii1II = re . compile ( 'screenshot9="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IIiII = re . compile ( 'screenshot10="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iII11 = re . compile ( 'screenshot11="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O00OO00OOOoO = re . compile ( 'screenshot12="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IiI11Ii1iI = re . compile ( 'screenshot13="(.+?)"' ) . findall ( i11I1IiII1i1i )
 ooOo0 = re . compile ( 'screenshot14="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OooO = re . compile ( 'screenshot15="(.+?)"' ) . findall ( i11I1IiII1i1i )
 if 78 - 78: OoooooooOO % ooOo - i11iIiiIii
 I1ii1 = oo0oO [ 0 ] if ( len ( oo0oO ) > 0 ) else ''
 I11II1i1 = i11I [ 0 ] if ( len ( i11I ) > 0 ) else ''
 I1I = iiIIiI11II1 [ 0 ] if ( len ( iiIIiI11II1 ) > 0 ) else 'None'
 ooooo = oooOo [ 0 ] if ( len ( oooOo ) > 0 ) else 'None'
 i11IIIiI1I = oOoO0Oo0 [ 0 ] if ( len ( oOoO0Oo0 ) > 0 ) else 'None'
 o0iiiI1I1iIIIi1 = i11i11i [ 0 ] if ( len ( i11i11i ) > 0 ) else 'None'
 Iii = iiI1iI [ 0 ] if ( len ( iiI1iI ) > 0 ) else 'None'
 O0Oo0o000oO = Ooo00O0 [ 0 ] if ( len ( Ooo00O0 ) > 0 ) else 'None'
 oO0o00oOOooO0 = OoO0OOoO0 [ 0 ] if ( len ( OoO0OOoO0 ) > 0 ) else 'None'
 OOOoO000 = iiI11i [ 0 ] if ( len ( iiI11i ) > 0 ) else 'None'
 oOOOO = o0Oo [ 0 ] if ( len ( o0Oo ) > 0 ) else 'None'
 IiIi1ii111i1 = iiI1i [ 0 ] if ( len ( iiI1i ) > 0 ) else 'None'
 iIiI1I1 = ooOooo [ 0 ] if ( len ( ooOooo ) > 0 ) else ''
 i111iiII1I = '[CR][CR][COLOR=dodgerblue]Step 1:[/COLOR][CR]' + Oo00 [ 0 ] if ( len ( Oo00 ) > 0 ) else ''
 iiiI1iIi1IiIi = '[CR][CR][COLOR=dodgerblue]Step 2:[/COLOR][CR]' + o0OO00 [ 0 ] if ( len ( o0OO00 ) > 0 ) else ''
 I1i11Iii1I1I1 = '[CR][CR][COLOR=dodgerblue]Step 3:[/COLOR][CR]' + oOO00 [ 0 ] if ( len ( oOO00 ) > 0 ) else ''
 IIi1ii1i1i1 = '[CR][CR][COLOR=dodgerblue]Step 4:[/COLOR][CR]' + II1IiII1I1II [ 0 ] if ( len ( II1IiII1I1II ) > 0 ) else ''
 O0o0O00O0 = '[CR][CR][COLOR=dodgerblue]Step 5:[/COLOR][CR]' + oooOII111iiI1Ii1 [ 0 ] if ( len ( oooOII111iiI1Ii1 ) > 0 ) else ''
 Oo0OO0O0oO0o = '[CR][CR][COLOR=dodgerblue]Step 6:[/COLOR][CR]' + oo0oO0oO00oO [ 0 ] if ( len ( oo0oO0oO00oO ) > 0 ) else ''
 O0oOOo0 = '[CR][CR][COLOR=dodgerblue]Step 7:[/COLOR][CR]' + o0OOo000ooo0o [ 0 ] if ( len ( o0OOo000ooo0o ) > 0 ) else ''
 iIi1OooOoOOo0 = '[CR][CR][COLOR=dodgerblue]Step 8:[/COLOR][CR]' + oo00oO0o000 [ 0 ] if ( len ( oo00oO0o000 ) > 0 ) else ''
 oOOo00ooO00 = '[CR][CR][COLOR=dodgerblue]Step 9:[/COLOR][CR]' + iIi1ii [ 0 ] if ( len ( iIi1ii ) > 0 ) else ''
 o0oO0OO = '[CR][CR][COLOR=dodgerblue]Step 10:[/COLOR][CR]' + I1I11I1iIIiI1i [ 0 ] if ( len ( I1I11I1iIIiI1i ) > 0 ) else ''
 I1IiIiIiiiI = '[CR][CR][COLOR=dodgerblue]Step 11:[/COLOR][CR]' + O0oOOOOooOo0 [ 0 ] if ( len ( O0oOOOOooOo0 ) > 0 ) else ''
 iIi1ii1I1IIIIII = '[CR][CR][COLOR=dodgerblue]Step 12:[/COLOR][CR]' + o0000o0OOOo [ 0 ] if ( len ( o0000o0OOOo ) > 0 ) else ''
 iIiI1iI = '[CR][CR][COLOR=dodgerblue]Step 13:[/COLOR][CR]' + iiiiiI1iii11 [ 0 ] if ( len ( iiiiiI1iii11 ) > 0 ) else ''
 o00OOOO000000 = '[CR][CR][COLOR=dodgerblue]Step 14:[/COLOR][CR]' + IIIi11iiIIi [ 0 ] if ( len ( IIIi11iiIIi ) > 0 ) else ''
 i1iI1Iiiiii11 = '[CR][CR][COLOR=dodgerblue]Step 15:[/COLOR][CR]' + oOo000O00O [ 0 ] if ( len ( oOo000O00O ) > 0 ) else ''
 OOoOo = I1IIiIi [ 0 ] if ( len ( I1IIiIi ) > 0 ) else ''
 Iiiiiii11IIiI = OOOOoOoO [ 0 ] if ( len ( OOOOoOoO ) > 0 ) else ''
 oOOO0o = OO000 [ 0 ] if ( len ( OO000 ) > 0 ) else ''
 Oo00O = o0oOoo0o [ 0 ] if ( len ( o0oOoo0o ) > 0 ) else ''
 o0OoII = IiiIiIIi [ 0 ] if ( len ( IiiIiIIi ) > 0 ) else ''
 i1i1IIi = O00Oo [ 0 ] if ( len ( O00Oo ) > 0 ) else ''
 o0oo0Ooo0 = oOOoooo0O0 [ 0 ] if ( len ( oOOoooo0O0 ) > 0 ) else ''
 o0OOoO = Ii111Ii11 [ 0 ] if ( len ( Ii111Ii11 ) > 0 ) else ''
 I1iII1II1I1ii = Ii1II [ 0 ] if ( len ( Ii1II ) > 0 ) else ''
 oo0OO0O = IIiII [ 0 ] if ( len ( IIiII ) > 0 ) else ''
 OO0OooOOoO00OO00 = iII11 [ 0 ] if ( len ( iII11 ) > 0 ) else ''
 ii11ii1iIiI1 = O00OO00OOOoO [ 0 ] if ( len ( O00OO00OOOoO ) > 0 ) else ''
 OoOo0oO0 = IiI11Ii1iI [ 0 ] if ( len ( IiI11Ii1iI ) > 0 ) else ''
 i111iIi1i1 = ooOo0 [ 0 ] if ( len ( ooOo0 ) > 0 ) else ''
 iII1I1iIIIiII = OooO [ 0 ] if ( len ( OooO ) > 0 ) else ''
 I1iiioO0o0O0Ooo0o = str ( '[COLOR=orange]Author: [/COLOR]' + I11II1i1 + '[CR][CR][COLOR=lime]About: [/COLOR]' + iIiI1I1 + i111iiII1I + iiiI1iIi1IiIi + I1i11Iii1I1I1 + IIi1ii1i1i1 + O0o0O00O0 + Oo0OO0O0oO0o + O0oOOo0 + iIi1OooOoOOo0 + oOOo00ooO00 + o0oO0OO + I1IiIiIiiiI + iIi1ii1I1IIIIII + iIiI1iI + o00OOOO000000 + i1iI1Iiiiii11 )
 if 41 - 41: oOOOoo0O0OoO - O0 * Oo0Ooo % I1IiiI
 if i111iiII1I != '' :
  OOo0oO00ooO00 ( '' , '[COLOR=yellow][Text Guide][/COLOR]  ' + I1ii1 , I1iiioO0o0O0Ooo0o , 'text_guide' , 'How_To.png' , O00o0OO , iIiI1I1 , '' )
 if I1I != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + O0Oo0o000oO , I1I , 'play_video' , 'Video_Guide.png' , O00o0OO , '' , '' )
 if ooooo != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + oO0o00oOOooO0 , ooooo , 'play_video' , 'Video_Guide.png' , O00o0OO , '' , '' )
 if i11IIIiI1I != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + OOOoO000 , i11IIIiI1I , 'play_video' , 'Video_Guide.png' , O00o0OO , '' , '' )
 if o0iiiI1I1iIIIi1 != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + oOOOO , o0iiiI1I1iIIIi1 , 'play_video' , 'Video_Guide.png' , O00o0OO , '' , '' )
 if Iii != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + IiIi1ii111i1 , Iii , 'play_video' , 'Video_Guide.png' , O00o0OO , '' , '' )
  if 70 - 70: I1I1i
  if 4 - 4: Oo + i11iIiiIii + OO0oo0oOO
def O0OoOOo0o ( ) :
 if o0O . getSetting ( 'tutorial_manual_search' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , 'tutorials' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_all' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=lime]All Guides[/COLOR] Everything in one place' , '' , 'grab_tutorials' , 'All.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_kodi' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=lime]XBMC / Kodi[/COLOR] Specific' , '' , 'xbmc_menu' , 'XBMC.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_xbmc4xbox' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=lime]XBMC4Xbox[/COLOR] Specific' , '&platform=XBMC4Xbox' , 'xbmc_menu' , 'XBMC4Xbox.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_android' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=orange][Platform][/COLOR] Android' , '&platform=Android' , 'platform_menu' , 'Android.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_atv' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=orange][Platform][/COLOR] Apple TV' , '&platform=ATV' , 'platform_menu' , 'ATV.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_ios' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=orange][Platform][/COLOR] ATV2 & iOS' , '&platform=iOS' , 'platform_menu' , 'iOS.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_linux' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=orange][Platform][/COLOR] Linux' , '&platform=Linux' , 'platform_menu' , 'Linux.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_pure_linux' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=orange][Platform][/COLOR] Pure Linux' , '&platform=Custom_Linux' , 'platform_menu' , 'Custom_Linux.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_openelec' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=orange][Platform][/COLOR] OpenELEC' , '&platform=OpenELEC' , 'platform_menu' , 'OpenELEC.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_osmc' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=orange][Platform][/COLOR] OSMC' , '&platform=OSMC' , 'platform_menu' , 'OSMC.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_osx' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=orange][Platform][/COLOR] OSX' , '&platform=OSX' , 'platform_menu' , 'OSX.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_raspbmc' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=orange][Platform][/COLOR] Raspbmc' , '&platform=Raspbmc' , 'platform_menu' , 'Raspbmc.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_windows' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=orange][Platform][/COLOR] Windows' , '&platform=Windows' , 'platform_menu' , 'Windows.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_allwinner' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Allwinner Devices' , '&hardware=Allwinner' , 'platform_menu' , 'Allwinner.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_aftv' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Amazon Fire TV' , '&hardware=AFTV' , 'platform_menu' , 'AFTV.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_amlogic' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] AMLogic Devices' , '&hardware=AMLogic' , 'platform_menu' , 'AMLogic.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_boxee' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Boxee' , '&hardware=Boxee' , 'platform_menu' , 'Boxee.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_intel' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Intel Devices' , '&hardware=Intel' , 'platform_menu' , 'Intel.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_rpi' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Raspberry Pi' , '&hardware=RaspberryPi' , 'platform_menu' , 'RaspberryPi.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_rockchip' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Rockchip Devices' , '&hardware=Rockchip' , 'platform_menu' , 'Rockchip.png' , '' , '' , '' )
 if o0O . getSetting ( 'tutorial_xbox' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][Hardware][/COLOR] Xbox' , '&hardware=Xbox' , 'platform_menu' , 'Xbox_Original.png' , '' , '' , '' )
  if 21 - 21: OO0oo0oOO - I1IiiI / OoooooooOO . i1IIi + II111iiii
  if 99 - 99: oOOOoo0O0OoO - I1ii11iIi11i - I1IiiI - oOOOoo0O0OoO + OoO0O00 + II111iiii
def i11iii1II1I1 ( ) :
 II = xbmcgui . Dialog ( )
 if II . yesno ( "Make Add-on Passwords Visible?" , "This will make all your add-on passwords visible in the add-on settings. Are you sure you wish to continue?" ) :
  for ii1OO0 , i1iiIIIi , Oo0o in os . walk ( Oo00OOOOO ) :
   for ooOo0O0o0 in Oo0o :
    if ooOo0O0o0 == 'settings.xml' :
     OOO = open ( os . path . join ( ii1OO0 , ooOo0O0o0 ) ) . read ( )
     I111i1I1 = re . compile ( '<setting id=(.+?)>' ) . findall ( OOO )
     for O0iiii in I111i1I1 :
      if 'pass' in O0iiii :
       if 'option="hidden"' in O0iiii :
        try :
         oOOOOOoOOoo0 = O0iiii . replace ( ' option="hidden"' , '' )
         ooOo0O0o0 = open ( os . path . join ( ii1OO0 , ooOo0O0o0 ) , mode = 'w' )
         ooOo0O0o0 . write ( str ( OOO ) . replace ( O0iiii , oOOOOOoOOoo0 ) )
         ooOo0O0o0 . close ( )
        except :
         pass
  II . ok ( "Passwords Are now visible" , "Your passwords will now be visible in your add-on settings. If you want to undo this please use the option to hide passwords." )
  if 25 - 25: II111iiii * i1IIi + I1I1i * o0oOOo0O0Ooo / Oo
  if 66 - 66: i11iIiiIii . OoO0O00 / OoOoOO00 - oOOOoo0O0OoO
def O0O0oooo ( ) :
 if o0O . getSetting ( 'email' ) == '' :
  II = xbmcgui . Dialog ( )
  II . ok ( "No Email Address Set" , "A new window will Now open for you to enter your Email address. The logfile will be sent here" )
  o0O . openSettings ( )
 xbmc . executebuiltin ( 'XBMC.RunScript(special://home/addons/' + I1IiI + '/uploadLog.py)' )
 if 90 - 90: Oo . OoOoOO00 . I1IiiI . I1I1i
 if 52 - 52: I1iii - Oo0Ooo
def IiiiiIi1iII1 ( localbuildcheck , localversioncheck , localidcheck ) :
 if oOOoo00O0O == 'true' :
  Oo0O00O000 = 'http://120.24.252.100/TI/login/login_details.php?user=%s&pass=%s' % ( Oo0oO0ooo , o0oOoO00o )
 else : Oo0O00O000 = 'http://120.24.252.100/TI/login/login_details.php?user=%s&pass=%s' % ( '' , '' )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 Iii1I1 = re . compile ( 'login_msg="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OoOO00OO0 = Iii1I1 [ 0 ] if ( len ( Iii1I1 ) > 0 ) else ''
 if 93 - 93: II111iiii * II111iiii + I1IiiI / Oo0Ooo
 if 9 - 9: Oo0Ooo - I1I1i
 if not 'REGISTER FOR FREE' in OoOO00OO0 :
  iiiiiIIi = open ( o00OO00OoO , mode = 'w+' )
  iiiiiIIi . write ( 'd="' + o00oO ( ) + '"\nlogin_msg="' + OoOO00OO0 + '"' )
  iiiiiIIi . close ( )
  if 30 - 30: OoooooooOO % Oo
 ooo0oo ( localbuildcheck , localversioncheck , localidcheck , OoOO00OO0 )
 if 14 - 14: OoOoOO00 / OoO0O00 / i11iIiiIii - OoOoOO00 / o0oOOo0O0Ooo - Oo
 if 81 - 81: IiiI11Iiiii % I1iii . iIIi1i1
def IIIii1I ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 xbmcgui . Dialog ( ) . ok ( 'Force Refresh Started Successfully' , 'Depending on the speed of your device it could take a few minutes for the update to take effect.' )
 return
 if 66 - 66: I1ii11iIi11i * I1iii / OoooooooOO * O0 % Oo
 if 49 - 49: II111iiii . I1IiiI * O0 * I1iii / oOOOoo0O0OoO * OoooooooOO
def OOo00 ( ) :
 Oo0O = 1
 try :
  ooI1111i ( 'http://google.com' )
 except :
  try :
   ooI1111i ( 'http://google.com' )
  except :
   try :
    ooI1111i ( 'http://google.com' )
   except :
    try :
     ooI1111i ( 'http://google.cn' )
    except :
     try :
      ooI1111i ( 'http://google.cn' )
     except :
      II . ok ( "NO INTERNET CONNECTION" , 'It looks like this device isn\'t connected to the internet. Only some of the maintenance options will work until you fix the connectivity problem.' )
      ooo0oo ( '' , '' , '' , '[COLOR=orange]NO INTERNET CONNECTION[/COLOR]' )
      Oo0O = 0
 if Oo0O == 1 :
  iI1IiiI ( )
  if 7 - 7: OoO0O00 % oOOOoo0O0OoO + I1I1i . OoOoOO00 . ooOo
  if 76 - 76: O0 * II111iiii
def iI1IiiI ( ) :
 ooo0OoO = 'None'
 ooO0 = '0'
 if 38 - 38: oOOOoo0O0OoO
 if 18 - 18: I1iii - IiiI11Iiiii
 Oo0oO00 = open ( IIIii1II1II , mode = 'r' )
 iii = Oo0oO00 . read ( )
 Oo0oO00 . close ( )
 if 18 - 18: II111iiii
 OOI111iIii1i1 = re . compile ( 'date="(.+?)"' ) . findall ( iii )
 I1i1I1i1I1 = OOI111iIii1i1 [ 0 ] if ( len ( OOI111iIii1i1 ) > 0 ) else ''
 oOooO0 = re . compile ( 'version="(.+?)"' ) . findall ( iii )
 III1iII1I1ii = oOooO0 [ 0 ] if ( len ( oOooO0 ) > 0 ) else ''
 if 33 - 33: I1iii . ooOo
 OooO0O0Ooo = open ( oo0OooOOo0 , mode = 'r' )
 oO0O = OooO0O0Ooo . read ( )
 OooO0O0Ooo . close ( )
 if 87 - 87: Oo0Ooo . o0oOOo0O0Ooo - OoooooooOO * ooOo % I1I1i + O0
 Ooo0Oo0oo0 = re . compile ( 'id="(.+?)"' ) . findall ( oO0O )
 II111i1ii1iII = re . compile ( 'name="(.+?)"' ) . findall ( oO0O )
 ooO0 = Ooo0Oo0oo0 [ 0 ] if ( len ( Ooo0Oo0oo0 ) > 0 ) else 'None'
 ooo0OoO = II111i1ii1iII [ 0 ] if ( len ( II111i1ii1iII ) > 0 ) else ''
 if 16 - 16: I1ii11iIi11i % Oo0Ooo % II111iiii % II111iiii
 if 51 - 51: OoOoOO00 * OoOoOO00 - O0 % iIii1I11I1II1 / O0
 if oo0o0O00 == 'true' :
  try :
   i11I1IiII1i1i = ooI1111i ( oO ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
   Ii11I11i11i11 = re . compile ( 'date="(.+?)"' ) . findall ( i11I1IiII1i1i )
   I1IIIIiII11 = re . compile ( 'video="https://www.youtube.com/watch\?v=(.+?)"' ) . findall ( i11I1IiII1i1i )
   i11IiIiii = Ii11I11i11i11 [ 0 ] if ( len ( Ii11I11i11i11 ) > 0 ) else ''
   i111 = I1IIIIiII11 [ 0 ] if ( len ( I1IIIIiII11 ) > 0 ) else ''
   if 25 - 25: i11iIiiIii / iIii1I11I1II1 * OoooooooOO . Oo
   if 69 - 69: Oo0Ooo * iIIi1i1
   if int ( I1i1I1i1I1 ) < int ( i11IiIiii ) :
    iiIiIiII = iii . replace ( I1i1I1i1I1 , i11IiIiii )
    iiiiiIIi = open ( IIIii1II1II , mode = 'w' )
    iiiiiIIi . write ( str ( iiIiIiII ) )
    iiiiiIIi . close ( )
    if 91 - 91: o0oOOo0O0Ooo . iIIi1i1 / OoO0O00 / i11iIiiIii * o0oOOo0O0Ooo
   yt . PlayVideo ( i111 , forcePlayer = True )
   xbmc . sleep ( 500 )
   while xbmc . Player ( ) . isPlaying ( ) :
    xbmc . sleep ( 500 )
  except : pass
 if not os . path . exists ( o00OO00OoO ) :
  print "### First login check ###"
  IiiiiIi1iII1 ( ooo0OoO , III1iII1I1ii , ooO0 )
  if 52 - 52: I1IiiI - i11iIiiIii / I1I1i . ooOo
  if 38 - 38: ooOo + OoooooooOO * OoOoOO00 % ooOo
 else :
  oo0Oooo0O = open ( o00OO00OoO , mode = 'r' )
  ooO0Oo = oo0Oooo0O . read ( )
  oo0Oooo0O . close ( )
  if 81 - 81: Oo
  OooOooo00OOO0o = re . compile ( 'd="(.+?)"' ) . findall ( ooO0Oo )
  II1iIIiIII = re . compile ( 'login_msg="(.+?)"' ) . findall ( ooO0Oo )
  O000O = OooOooo00OOO0o [ 0 ] if ( len ( OooOooo00OOO0o ) > 0 ) else '0'
  OoOO00OO0 = II1iIIiIII [ 0 ] if ( len ( II1iIIiIII ) > 0 ) else ''
  if 10 - 10: Oo . I1iii
  if int ( O000O ) + 2000000 > int ( o00oO ( ) ) :
   print "### Login successful ###"
   ooo0oo ( ooo0OoO , III1iII1I1ii , ooO0 , OoOO00OO0 )
  else :
   print "### Checking login ###"
   IiiiiIi1iII1 ( ooo0OoO , III1iII1I1ii , ooO0 )
   if 5 - 5: I1I1i - OO0oo0oOO
   if 16 - 16: I1I1i . IiiI11Iiiii . Oo0Ooo % Oo / I1I1i
def OooO0OOo ( ) :
 OOO0oo0ooOoo = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( OOO0oo0ooOoo ) == True :
  for ii1OO0 , i1iiIIIi , Oo0o in os . walk ( OOO0oo0ooOoo ) :
   OoOoO00OOoOOOo0 = 0
   OoOoO00OOoOOOo0 += len ( Oo0o )
   if OoOoO00OOoOOOo0 > 0 :
    for ooOo0O0o0 in Oo0o :
     try :
      os . unlink ( os . path . join ( ii1OO0 , ooOo0O0o0 ) )
     except :
      pass
    for ii1iIIiii1 in i1iiIIIi :
     try :
      shutil . rmtree ( os . path . join ( ii1OO0 , ii1iIIiii1 ) )
     except :
      pass
 ii1i11III1I1 = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'temp' )
 if os . path . exists ( ii1i11III1I1 ) == True :
  for ii1OO0 , i1iiIIIi , Oo0o in os . walk ( ii1i11III1I1 ) :
   OoOoO00OOoOOOo0 = 0
   OoOoO00OOoOOOo0 += len ( Oo0o )
   if OoOoO00OOoOOOo0 > 0 :
    for ooOo0O0o0 in Oo0o :
     try :
      os . unlink ( os . path . join ( ii1OO0 , ooOo0O0o0 ) )
     except :
      pass
    for ii1iIIiii1 in i1iiIIIi :
     try :
      shutil . rmtree ( os . path . join ( ii1OO0 , ii1iIIiii1 ) )
     except :
      pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  O000o = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  for ii1OO0 , i1iiIIIi , Oo0o in os . walk ( O000o ) :
   OoOoO00OOoOOOo0 = 0
   OoOoO00OOoOOOo0 += len ( Oo0o )
   if OoOoO00OOoOOOo0 > 0 :
    for ooOo0O0o0 in Oo0o :
     os . unlink ( os . path . join ( ii1OO0 , ooOo0O0o0 ) )
    for ii1iIIiii1 in i1iiIIIi :
     shutil . rmtree ( os . path . join ( ii1OO0 , ii1iIIiii1 ) )
  iiI1I = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  for ii1OO0 , i1iiIIIi , Oo0o in os . walk ( iiI1I ) :
   OoOoO00OOoOOOo0 = 0
   OoOoO00OOoOOOo0 += len ( Oo0o )
   if OoOoO00OOoOOOo0 > 0 :
    for ooOo0O0o0 in Oo0o :
     os . unlink ( os . path . join ( ii1OO0 , ooOo0O0o0 ) )
    for ii1iIIiii1 in i1iiIIIi :
     shutil . rmtree ( os . path . join ( ii1OO0 , ii1iIIiii1 ) )
     if 15 - 15: OoooooooOO
 iII1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( iII1i ) == True :
  for ii1OO0 , i1iiIIIi , Oo0o in os . walk ( iII1i ) :
   OoOoO00OOoOOOo0 = 0
   OoOoO00OOoOOOo0 += len ( Oo0o )
   if OoOoO00OOoOOOo0 > 0 :
    for ooOo0O0o0 in Oo0o :
     os . unlink ( os . path . join ( ii1OO0 , ooOo0O0o0 ) )
    for ii1iIIiii1 in i1iiIIIi :
     shutil . rmtree ( os . path . join ( ii1OO0 , ii1iIIiii1 ) )
     if 74 - 74: I1ii11iIi11i * I1I1i * I1I1i . IiiI11Iiiii + ooOo + iIIi1i1
 Ii1I1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.image.music.slideshow/cache' ) , '' )
 if os . path . exists ( Ii1I1 ) == True :
  for ii1OO0 , i1iiIIIi , Oo0o in os . walk ( Ii1I1 ) :
   OoOoO00OOoOOOo0 = 0
   OoOoO00OOoOOOo0 += len ( Oo0o )
   if OoOoO00OOoOOOo0 > 0 :
    for ooOo0O0o0 in Oo0o :
     os . unlink ( os . path . join ( ii1OO0 , ooOo0O0o0 ) )
    for ii1iIIiii1 in i1iiIIIi :
     shutil . rmtree ( os . path . join ( ii1OO0 , ii1iIIiii1 ) )
     if 43 - 43: Oo
 i1OO0o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( i1OO0o ) == True :
  for ii1OO0 , i1iiIIIi , Oo0o in os . walk ( i1OO0o ) :
   OoOoO00OOoOOOo0 = 0
   OoOoO00OOoOOOo0 += len ( Oo0o )
   if OoOoO00OOoOOOo0 > 0 :
    for ooOo0O0o0 in Oo0o :
     os . unlink ( os . path . join ( ii1OO0 , ooOo0O0o0 ) )
    for ii1iIIiii1 in i1iiIIIi :
     shutil . rmtree ( os . path . join ( ii1OO0 , ii1iIIiii1 ) )
     if 64 - 64: i1IIi / o0oOOo0O0Ooo
 IIiI1i11iIII1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( IIiI1i11iIII1 ) == True :
  for ii1OO0 , i1iiIIIi , Oo0o in os . walk ( IIiI1i11iIII1 ) :
   OoOoO00OOoOOOo0 = 0
   OoOoO00OOoOOOo0 += len ( Oo0o )
   if OoOoO00OOoOOOo0 > 0 :
    for ooOo0O0o0 in Oo0o :
     os . unlink ( os . path . join ( ii1OO0 , ooOo0O0o0 ) )
    for ii1iIIiii1 in i1iiIIIi :
     shutil . rmtree ( os . path . join ( ii1OO0 , ii1iIIiii1 ) )
     if 76 - 76: OoooooooOO * I1I1i - o0oOOo0O0Ooo * Oo * i1IIi * IiiI11Iiiii
 II11111i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.navi-x/cache' ) , '' )
 if os . path . exists ( II11111i ) == True :
  for ii1OO0 , i1iiIIIi , Oo0o in os . walk ( II11111i ) :
   OoOoO00OOoOOOo0 = 0
   OoOoO00OOoOOOo0 += len ( Oo0o )
   if OoOoO00OOoOOOo0 > 0 :
    for ooOo0O0o0 in Oo0o :
     os . unlink ( os . path . join ( ii1OO0 , ooOo0O0o0 ) )
    for ii1iIIiii1 in i1iiIIIi :
     shutil . rmtree ( os . path . join ( ii1OO0 , ii1iIIiii1 ) )
     if 46 - 46: iIIi1i1 - iIii1I11I1II1
 o0ooOoOO0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( o0ooOoOO0 ) == True :
  for ii1OO0 , i1iiIIIi , Oo0o in os . walk ( o0ooOoOO0 ) :
   OoOoO00OOoOOOo0 = 0
   OoOoO00OOoOOOo0 += len ( Oo0o )
   if OoOoO00OOoOOOo0 > 0 :
    for ooOo0O0o0 in Oo0o :
     os . unlink ( os . path . join ( ii1OO0 , ooOo0O0o0 ) )
    for ii1iIIiii1 in i1iiIIIi :
     shutil . rmtree ( os . path . join ( ii1OO0 , ii1iIIiii1 ) )
     if 35 - 35: OO0oo0oOO % O0
 I1i1IIIIIII = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.audio.ramfm/cache' ) , '' )
 if os . path . exists ( I1i1IIIIIII ) == True :
  for ii1OO0 , i1iiIIIi , Oo0o in os . walk ( I1i1IIIIIII ) :
   OoOoO00OOoOOOo0 = 0
   OoOoO00OOoOOOo0 += len ( Oo0o )
   if OoOoO00OOoOOOo0 > 0 :
    for ooOo0O0o0 in Oo0o :
     os . unlink ( os . path . join ( ii1OO0 , ooOo0O0o0 ) )
    for ii1iIIiii1 in i1iiIIIi :
     shutil . rmtree ( os . path . join ( ii1OO0 , ii1iIIiii1 ) )
     if 1 - 1: iIii1I11I1II1 - II111iiii - ooOo % OoO0O00 + OoOoOO00 + o0oOOo0O0Ooo
 I1IIiIiOoOO0OOo0Oo = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( I1IIiIiOoOO0OOo0Oo ) == True :
  for ii1OO0 , i1iiIIIi , Oo0o in os . walk ( I1IIiIiOoOO0OOo0Oo ) :
   OoOoO00OOoOOOo0 = 0
   OoOoO00OOoOOOo0 += len ( Oo0o )
   if OoOoO00OOoOOOo0 > 0 :
    for ooOo0O0o0 in Oo0o :
     os . unlink ( os . path . join ( ii1OO0 , ooOo0O0o0 ) )
    for ii1iIIiii1 in i1iiIIIi :
     shutil . rmtree ( os . path . join ( ii1OO0 , ii1iIIiii1 ) )
     if 33 - 33: I1ii11iIi11i - I1I1i
 try :
  i1IiIii1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.genesis' ) , 'cache.db' )
  oo0oO0o00Oo0 = database . connect ( i1IiIii1i )
  i1I1I = oo0oO0o00Oo0 . cursor ( )
  i1I1I . execute ( "DROP TABLE IF EXISTS rel_list" )
  i1I1I . execute ( "VACUUM" )
  oo0oO0o00Oo0 . commit ( )
  i1I1I . execute ( "DROP TABLE IF EXISTS rel_lib" )
  i1I1I . execute ( "VACUUM" )
  oo0oO0o00Oo0 . commit ( )
 except :
  pass
  if 27 - 27: OoO0O00 % iIIi1i1 - O0
  if 44 - 44: I1ii11iIi11i + I1ii11iIi11i - Oo / II111iiii
def OOo0 ( mode ) :
 if zip == '' :
  II . ok ( 'Please set your backup location before proceeding' , 'You have not set your backup storage folder.\nPlease update the addon settings and try again.' )
  o0O . openSettings ( sys . argv [ 0 ] )
  IIiI111i = o0O . getSetting ( 'zip' )
  if IIiI111i == '' :
   OOo0 ( mode )
 IIIIi11111 = xbmc . translatePath ( os . path . join ( Ooo0OO0oOO , 'Community Builds' , 'My Builds' ) )
 if not os . path . exists ( IIIIi11111 ) :
  os . makedirs ( IIIIi11111 )
 iIi1IiI = xbmcgui . Dialog ( ) . yesno ( "ABSOLUTELY CERTAIN?!!!" , 'Are you absolutely certain you want to wipe?' , '' , 'All addons and settings will be completely wiped!' , yeslabel = 'Yes' , nolabel = 'No' )
 if 47 - 47: oOOOoo0O0OoO + I1IiiI
 if iIi1IiI == 1 :
  if oO0 != "skin.confluence" :
   II . ok ( 'Default Confluence Skin Required' , 'Please switch to the default Confluence skin before performing a wipe.' )
   xbmc . executebuiltin ( "ActivateWindow(appearancesettings,return)" )
   return
  else :
   if 40 - 40: iIii1I11I1II1 % I1iii + II111iiii - I1IiiI
   iIi1IiI = xbmcgui . Dialog ( ) . yesno ( "VERY IMPORTANT" , 'This will completely wipe your install.' , 'Would you like to create a backup before proceeding?' , '' , yeslabel = 'No' , nolabel = 'Yes' )
   if iIi1IiI == 0 :
    if not os . path . exists ( IIIIi11111 ) :
     os . makedirs ( IIIIi11111 )
    IiI1Iii1 = Ooooo ( heading = "Enter a name for this backup" )
    if ( not IiI1Iii1 ) : return False , 0
    ooOoOii1iII = urllib . quote_plus ( IiI1Iii1 )
    O00oo = xbmc . translatePath ( os . path . join ( IIIIi11111 , ooOoOii1iII + '.zip' ) )
    OoOoooO000OO = [ 'plugin.program.totalinstaller' , 'plugin.program.tbs' ]
    O00Oooi1 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , '.gitignore' ]
    OOoooOoO0Oo = "Creating full backup of existing build"
    Oo000 = "Archiving..."
    iiIiII11i1 = ""
    oOo00Ooo0o0 = "Please Wait"
    o0O0OO ( OooO0 , O00oo , OOoooOoO0Oo , Oo000 , iiIiII11i1 , oOo00Ooo0o0 , OoOoooO000OO , O00Oooi1 )
    if 80 - 80: ooOo
    if 81 - 81: OoooooooOO / iIIi1i1 * iIii1I11I1II1 . Oo0Ooo + ooOo / O0
   ooOoOoo0O . create ( "Wiping Existing Content" , '' , 'Please wait...' , '' )
   for ii1OO0 , i1iiIIIi , Oo0o in os . walk ( OooO0 , topdown = True ) :
    i1iiIIIi [ : ] = [ ii1iIIiii1 for ii1iIIiii1 in i1iiIIIi if ii1iIIiii1 not in O0ii1ii1ii ]
    for I1ii1 in Oo0o :
     try :
      ooOoOoo0O . update ( 0 , "Removing [COLOR=yellow]" + I1ii1 + '[/COLOR]' , '' , 'Please wait...' )
      os . unlink ( os . path . join ( ii1OO0 , I1ii1 ) )
      os . remove ( os . path . join ( ii1OO0 , I1ii1 ) )
      os . rmdir ( os . path . join ( ii1OO0 , I1ii1 ) )
     except : print "Failed to remove file: " + I1ii1
     if 84 - 84: II111iiii - o0oOOo0O0Ooo
   oOoOoO0OoOO0 = [ I1ii1 for I1ii1 in os . listdir ( II11iiii1Ii ) if os . path . isdir ( os . path . join ( II11iiii1Ii , I1ii1 ) ) ]
   try :
    for I1ii1 in oOoOoO0OoOO0 :
     try :
      if I1ii1 not in O0ii1ii1ii :
       ooOoOoo0O . update ( 0 , "Cleaning Directory: [COLOR=yellow]" + I1ii1 + ' [/COLOR]' , '' , 'Please wait...' )
       shutil . rmtree ( os . path . join ( II11iiii1Ii , I1ii1 ) )
     except : print "Failed to remove: " + I1ii1
   except : pass
   if 75 - 75: I1IiiI
   for ii1OO0 , i1iiIIIi , Oo0o in os . walk ( II11iiii1Ii , topdown = True ) :
    i1iiIIIi [ : ] = [ ii1iIIiii1 for ii1iIIiii1 in i1iiIIIi if ii1iIIiii1 not in O0ii1ii1ii ]
    for I1ii1 in Oo0o :
     try :
      ooOoOoo0O . update ( 0 , "Removing [COLOR=yellow]" + I1ii1 + '[/COLOR]' , '' , 'Please wait...' )
      os . unlink ( os . path . join ( ii1OO0 , I1ii1 ) )
      os . remove ( os . path . join ( ii1OO0 , I1ii1 ) )
     except : print "Failed to remove file: " + I1ii1
     if 99 - 99: iIIi1i1 . I1iii
   o000 = [ I1ii1 for I1ii1 in os . listdir ( Oo00OOOOO ) if os . path . isdir ( os . path . join ( Oo00OOOOO , I1ii1 ) ) ]
   try :
    for I1ii1 in o000 :
     try :
      if oo00 == 'true' :
       if I1ii1 not in O0ii1ii1ii and not 'repo' in I1ii1 :
        ooOoOoo0O . update ( 0 , "Removing Add-on: [COLOR=yellow]" + I1ii1 + ' [/COLOR]' , '' , 'Please wait...' )
        shutil . rmtree ( os . path . join ( Oo00OOOOO , I1ii1 ) )
      else :
       if I1ii1 not in O0ii1ii1ii :
        ooOoOoo0O . update ( 0 , "Removing Add-on: [COLOR=yellow]" + I1ii1 + ' [/COLOR]' , '' , 'Please wait...' )
        shutil . rmtree ( os . path . join ( Oo00OOOOO , I1ii1 ) )
     except : print "Failed to remove: " + I1ii1
   except : pass
   if 41 - 41: I1ii11iIi11i * i11iIiiIii - Oo0Ooo * II111iiii
   OOO0 = [ I1ii1 for I1ii1 in os . listdir ( OO0o ) if os . path . isdir ( os . path . join ( OO0o , I1ii1 ) ) ]
   try :
    for I1ii1 in OOO0 :
     try :
      if I1ii1 not in O0ii1ii1ii :
       ooOoOoo0O . update ( 0 , "Removing Add-on Data: [COLOR=yellow]" + I1ii1 + ' [/COLOR]' , '' , 'Please wait...' )
       shutil . rmtree ( os . path . join ( OO0o , I1ii1 ) )
     except : print "Failed to remove: " + I1ii1
   except : pass
   if 100 - 100: o0oOOo0O0Ooo - OO0oo0oOO + i11iIiiIii
   iIii1I = [ I1ii1 for I1ii1 in os . listdir ( OooO0 ) if os . path . isdir ( os . path . join ( OooO0 , I1ii1 ) ) ]
   try :
    for I1ii1 in iIii1I :
     try :
      if I1ii1 not in O0ii1ii1ii :
       ooOoOoo0O . update ( 0 , "Cleaning Directory: [COLOR=yellow]" + I1ii1 + ' [/COLOR]' , '' , 'Please wait...' )
       shutil . rmtree ( os . path . join ( OooO0 , I1ii1 ) )
     except : print "Failed to remove: " + I1ii1
   except : pass
  if mode != 'CB' :
   II . ok ( 'Wipe Complete' , 'Kodi will now close.' , 'When you next load up Kodi it should boot into the default Confluence skin and you should have a fresh install.' )
   xbmc . executebuiltin ( 'quit' )
  try :
   os . remove ( IIIii1II1II )
  except : print "### Failed to remove startup.xml"
  try :
   os . remove ( oo0OooOOo0 )
  except : print "### Failed to remove id.xml"
 else : return
 if 89 - 89: i1IIi
 if 92 - 92: iIii1I11I1II1 * I1ii11iIi11i
def i1I11Iiii ( ) :
 OOo0oO00ooO00 ( '' , 'Clear Cache' , 'url' , 'clear_cache' , 'Clear_Cache.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Clear My Cached Artwork' , 'none' , 'remove_textures' , 'Delete_Cached_Artwork.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Delete Addon_Data' , 'url' , 'remove_addon_data' , 'Delete_Addon_Data.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Delete Old Builds/Zips From Device' , 'url' , 'remove_build' , 'Delete_Builds.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Delete Old Crash Logs' , 'url' , 'remove_crash_logs' , 'Delete_Crash_Logs.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Delete Packages Folder' , 'url' , 'remove_packages' , 'Delete_Packages.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Wipe My Install (Fresh Start)' , 'none' , 'wipe_xbmc' , 'Fresh_Start.png' , '' , '' , '' )
 if 78 - 78: oOOOoo0O0OoO
 if 62 - 62: I1IiiI + OoooooooOO + oOOOoo0O0OoO
def IiIII ( url ) :
 OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow]1. Install[/COLOR]' , str ( url ) + '&tags=Install&XBMC=1' , 'grab_tutorials' , 'Install.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=lime]2. Settings[/COLOR]' , str ( url ) + '&tags=Settings' , 'grab_tutorials' , 'Settings.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=orange]3. Add-ons[/COLOR]' , str ( url ) , 'tutorial_addon_menu' , 'Addons.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Audio' , str ( url ) + '&tags=Audio' , 'grab_tutorials' , 'Audio.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Errors' , str ( url ) + '&tags=Errors' , 'grab_tutorials' , 'Errors.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Gaming' , str ( url ) + '&tags=Gaming' , 'grab_tutorials' , 'gaming_portal.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  LiveTV' , str ( url ) + '&tags=LiveTV' , 'grab_tutorials' , 'LiveTV.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Maintenance' , str ( url ) + '&tags=Maintenance' , 'grab_tutorials' , 'Maintenance.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Pictures' , str ( url ) + '&tags=Pictures' , 'grab_tutorials' , 'Pictures.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Profiles' , str ( url ) + '&tags=Profiles' , 'grab_tutorials' , 'Profiles.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Skins' , str ( url ) + '&tags=Skins' , 'grab_tutorials' , 'Skin.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Video' , str ( url ) + '&tags=Video' , 'grab_tutorials' , 'Video.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][XBMC/Kodi][/COLOR]  Weather' , str ( url ) + '&tags=Weather' , 'grab_tutorials' , 'Weather.png' , '' , '' , '' )
 if 3 - 3: Oo0Ooo + Oo - I1IiiI
 if 60 - 60: O0 / i1IIi % i11iIiiIii / IiiI11Iiiii
def ooo00o0OO0 ( url ) :
 IIIIiI11I = xbmc . getInfoLabel ( "System.BuildVersion" )
 IiIiIi = float ( IIIIiI11I [ : 4 ] )
 if IiIiIi < 14 :
  oO0OOOo0OO = 'You are running XBMC'
 else :
  oO0OOOo0OO = 'You are running Kodi'
 II = xbmcgui . Dialog ( )
 II . ok ( oO0OOOo0OO , "Your version is: %s" % IiIiIi )
 if 25 - 25: Oo / OoooooooOO - I1ii11iIi11i
 if 31 - 31: OO0oo0oOO + OoO0O00 / I1IiiI * O0 + O0
 if 34 - 34: I1I1i
 if 5 - 5: OoO0O00 . I1IiiI
 if 48 - 48: Oo0Ooo - OoO0O00 . OO0oo0oOO - iIii1I11I1II1 % I1iii
 if 47 - 47: IiiI11Iiiii / OoooooooOO - II111iiii
 if 91 - 91: OoOoOO00 + o0oOOo0O0Ooo
 if 23 - 23: i1IIi
 if 9 - 9: i1IIi % oOOOoo0O0OoO - OoO0O00 * OoOoOO00 . o0oOOo0O0Ooo
 if 18 - 18: I1iii . OoOoOO00 + IiiI11Iiiii . I1IiiI + OoooooooOO . OoO0O00
 if 31 - 31: oOOOoo0O0OoO - OO0oo0oOO
 if 49 - 49: iIii1I11I1II1 - iIii1I11I1II1 - OoOoOO00 + I1I1i / OoOoOO00
 if 74 - 74: OoooooooOO + I1ii11iIi11i % O0
 if 32 - 32: I1ii11iIi11i + I1ii11iIi11i
 if 89 - 89: iIIi1i1 + ooOo + I1iii - Oo
 if 12 - 12: OoOoOO00 - o0oOOo0O0Ooo - oOOOoo0O0OoO / OO0oo0oOO
 if 17 - 17: OoO0O00 - oOOOoo0O0OoO - II111iiii / oOOOoo0O0OoO / I1iii
 if 30 - 30: Oo * I1ii11iIi11i % I1ii11iIi11i + IiiI11Iiiii * I1I1i
 if 33 - 33: o0oOOo0O0Ooo + OO0oo0oOO * O0 * OoO0O00 . I1ii11iIi11i
 if 74 - 74: IiiI11Iiiii * IiiI11Iiiii * o0oOOo0O0Ooo / ooOo
 if 91 - 91: i11iIiiIii . I1ii11iIi11i / II111iiii
 if 97 - 97: I1iii % i1IIi % I1I1i + Oo0Ooo - O0 - OO0oo0oOO
iiI1ii1IIiI = oo0O0oOOO0o ( )
Oo0o0000OOoO = None
OoOo0OO0oooo = None
iIIi1 = None
I11II1i1 = None
o00ooo0O = None
OoOO = None
I1iiioO0o0O0Ooo0o = None
Oo0oOo0 = None
O0oOOo0o = None
IiIIIIIi = None
I1IIiI = None
i11I1IiII1i1i = None
I1Ii1IIi = None
OOO00O0oOOoOo = None
oO0o0O00O00O = None
I1ii1 = None
OOoO0OooO = None
o0Ooo0o0Oo = None
IiIi1I1ii111 = None
O0OoO0ooOO0o = None
o00oo0oO00O000 = None
I1i1iI = None
ii1iOO00Oooo000 = None
ooOoOii1iII = None
IIiI1 = None
IIIII11i = None
I1I1i1I1I1I1 = None
IiIiIi = None
ooO0oOOooOo0 = None
I1iI1I1ii1 = None
OoOO00OO0 = None
I1ii1I11iIi = None
IiO00oo0o0ooO = 'maintenance'
if 70 - 70: Oo0Ooo + oOOOoo0O0OoO + Oo . I1ii11iIi11i - I1ii11iIi11i
try : Oo0o0000OOoO = urllib . unquote_plus ( iiI1ii1IIiI [ "addon_id" ] )
except : pass
try : iI1 = urllib . unquote_plus ( iiI1ii1IIiI [ "adult" ] )
except : pass
try : OoOo0OO0oooo = urllib . unquote_plus ( iiI1ii1IIiI [ "artpack" ] )
except : pass
try : iIIi1 = urllib . unquote_plus ( iiI1ii1IIiI [ "audioaddons" ] )
except : pass
try : I11II1i1 = urllib . unquote_plus ( iiI1ii1IIiI [ "author" ] )
except : pass
try : o00ooo0O = urllib . unquote_plus ( iiI1ii1IIiI [ "buildname" ] )
except : pass
try : OoOO = urllib . unquote_plus ( iiI1ii1IIiI [ "data_path" ] )
except : pass
try : I1iiioO0o0O0Ooo0o = urllib . unquote_plus ( iiI1ii1IIiI [ "description" ] )
except : pass
try : Oo0oOo0 = urllib . unquote_plus ( iiI1ii1IIiI [ "email" ] )
except : pass
try : O0oOOo0o = urllib . unquote_plus ( iiI1ii1IIiI [ "fanart" ] )
except : pass
try : IiIIIIIi = urllib . unquote_plus ( iiI1ii1IIiI [ "forum" ] )
except : pass
try : ii111iiIii = urllib . unquote_plus ( iiI1ii1IIiI [ "guisettingslink" ] )
except : pass
try : I1IIiI = urllib . unquote_plus ( iiI1ii1IIiI [ "iconimage" ] )
except : pass
try : i11I1IiII1i1i = urllib . unquote_plus ( iiI1ii1IIiI [ "link" ] )
except : pass
try : I1Ii1IIi = urllib . unquote_plus ( iiI1ii1IIiI [ "local" ] )
except : pass
try : OOO00O0oOOoOo = urllib . unquote_plus ( iiI1ii1IIiI [ "messages" ] )
except : pass
try : oO0o0O00O00O = str ( iiI1ii1IIiI [ "mode" ] )
except : pass
try : I1ii1 = urllib . unquote_plus ( iiI1ii1IIiI [ "name" ] )
except : pass
try : oo00ooooOOo00 = urllib . unquote_plus ( iiI1ii1IIiI [ "pictureaddons" ] )
except : pass
try : OOoO0OooO = urllib . unquote_plus ( iiI1ii1IIiI [ "posts" ] )
except : pass
try : o0Ooo0o0Oo = urllib . unquote_plus ( iiI1ii1IIiI [ "programaddons" ] )
except : pass
try : IiIi1I1ii111 = urllib . unquote_plus ( iiI1ii1IIiI [ "provider_name" ] )
except : pass
try : o00oo0oO00O000 = urllib . unquote_plus ( iiI1ii1IIiI [ "repo_link" ] )
except : pass
try : O0OoO0ooOO0o = urllib . unquote_plus ( iiI1ii1IIiI [ "repo_id" ] )
except : pass
try : I1i1iI = urllib . unquote_plus ( iiI1ii1IIiI [ "skins" ] )
except : pass
try : ii1iOO00Oooo000 = urllib . unquote_plus ( iiI1ii1IIiI [ "sources" ] )
except : pass
try : ooOoOii1iII = urllib . unquote_plus ( iiI1ii1IIiI [ "title" ] )
except : pass
try : IIiI1 = urllib . unquote_plus ( iiI1ii1IIiI [ "updated" ] )
except : pass
try : IIIII11i = urllib . unquote_plus ( iiI1ii1IIiI [ "unread" ] )
except : pass
try : I1I1i1I1I1I1 = urllib . unquote_plus ( iiI1ii1IIiI [ "url" ] )
except : pass
try : IiIiIi = urllib . unquote_plus ( iiI1ii1IIiI [ "version" ] )
except : pass
try : ooO0oOOooOo0 = urllib . unquote_plus ( iiI1ii1IIiI [ "video" ] )
except : pass
try : I1iI1I1ii1 = urllib . unquote_plus ( iiI1ii1IIiI [ "videoaddons" ] )
except : pass
try : OoOO00OO0 = urllib . unquote_plus ( iiI1ii1IIiI [ "welcometext" ] )
except : pass
try : I1ii1I11iIi = urllib . unquote_plus ( iiI1ii1IIiI [ "zip_link" ] )
except : pass
if 21 - 21: OO0oo0oOO - ooOo
if not os . path . exists ( OOO00O ) :
 os . makedirs ( OOO00O )
 if 55 - 55: IiiI11Iiiii * Oo0Ooo + OoOoOO00 * Oo / IiiI11Iiiii * i1IIi
if not os . path . exists ( IIIii1II1II ) :
 Oo0oO00 = open ( IIIii1II1II , mode = 'w+' )
 Oo0oO00 . write ( 'date="01011001"\nversion="0.0"' )
 Oo0oO00 . close ( )
 if 49 - 49: I1I1i + iIii1I11I1II1
if not os . path . exists ( oo0OooOOo0 ) :
 Oo0oO00 = open ( oo0OooOOo0 , mode = 'w+' )
 Oo0oO00 . write ( 'id="None"\nname="None"' )
 Oo0oO00 . close ( )
 if 30 - 30: i11iIiiIii % o0oOOo0O0Ooo . i1IIi
if os . path . exists ( o0OO00oO ) :
 try :
  shutil . rmtree ( o0OO00oO )
 except : pass
 if 49 - 49: o0oOOo0O0Ooo * I1iii + Oo0Ooo
if os . path . exists ( I11i1I1I ) :
 try :
  shutil . rmtree ( I11i1I1I )
 except : pass
 if 1 - 1: o0oOOo0O0Ooo / II111iiii + OO0oo0oOO . i11iIiiIii + iIIi1i1 . OoOoOO00
if os . path . exists ( oO0Oo ) :
 try :
  shutil . rmtree ( oO0Oo )
 except : pass
 if 95 - 95: o0oOOo0O0Ooo / oOOOoo0O0OoO % II111iiii + iIIi1i1
oOo0ooOO0O = binascii . unhexlify ( '6164646f6e2e786d6c' )
i1iiI = xbmc . translatePath ( os . path . join ( Oo00OOOOO , I1IiI , oOo0ooOO0O ) )
IIIII11IIi = open ( i1iiI , mode = 'r' )
iii = file . read ( IIIII11IIi )
file . close ( IIIII11IIi )
i11I1iiI1iI = re . compile ( '<ref>(.+?)</ref>' ) . findall ( iii )
i1i11 = i11I1iiI1iI [ 0 ] if ( len ( i11I1iiI1iI ) > 0 ) else ''
OoOO0o000000 = hashlib . md5 ( open ( O0Oo000ooO00 , 'rb' ) . read ( ) ) . hexdigest ( )
if i1i11 != OoOO0o000000 :
 os . remove ( O0Oo000ooO00 )
 if 84 - 84: I1iii % I1IiiI . o0oOOo0O0Ooo / O0 - OoOoOO00
if oO0o0O00O00O == None : OOo00 ( )
elif oO0o0O00O00O == 'addon_final_menu' : iIiIi11iI ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'addon_categories' : oo ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'addon_countries' : iiIiI1i1 ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'addon_genres' : III ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'addon_install' : Ii1iI11iI1 ( I1ii1 , I1ii1I11iIi , o00oo0oO00O000 , O0OoO0ooOO0o , Oo0o0000OOoO , IiIi1I1ii111 , IiIIIIIi , OoOO )
elif oO0o0O00O00O == 'addon_install_badzip' : I1I1 ( I1ii1 , I1ii1I11iIi , o00oo0oO00O000 , O0OoO0ooOO0o , Oo0o0000OOoO , IiIi1I1ii111 , IiIIIIIi , OoOO )
elif oO0o0O00O00O == 'addon_install_na' : iIiI1 ( I1ii1 , I1ii1I11iIi , o00oo0oO00O000 , O0OoO0ooOO0o , Oo0o0000OOoO , IiIi1I1ii111 , IiIIIIIi , OoOO )
elif oO0o0O00O00O == 'addon_install_zero' : OoooO0o ( I1ii1 , I1ii1I11iIi , o00oo0oO00O000 , O0OoO0ooOO0o , Oo0o0000OOoO , IiIi1I1ii111 , IiIIIIIi , OoOO )
elif oO0o0O00O00O == 'addon_loop' : I11Ii1iI11iI1 ( )
elif oO0o0O00O00O == 'addon_removal_menu' : oo00IIIIIIIiI ( )
elif oO0o0O00O00O == 'addonfix' : oOoo0OO0 ( )
elif oO0o0O00O00O == 'addonfixes' : oo00ooOoo ( )
elif oO0o0O00O00O == 'addonmenu' : IiiiI1 ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'addon_settings' : OOoO ( )
elif oO0o0O00O00O == 'backup' : BACKUP ( )
elif oO0o0O00O00O == 'backup_option' : OOoO00ooO ( )
elif oO0o0O00O00O == 'backup_restore' : i11IiIIi11I ( )
elif oO0o0O00O00O == 'browse_repos' : iIiIi1ii ( )
elif oO0o0O00O00O == 'check_storage' : checkPath . check ( IiO00oo0o0ooO )
elif oO0o0O00O00O == 'check_updates' : IiI ( )
elif oO0o0O00O00O == 'clear_cache' : Iiii111 ( )
elif oO0o0O00O00O == 'cb_test_loop' : I11Ii1iI11iI1 ( )
elif oO0o0O00O00O == 'CB_Menu' : oOOoo0 ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'community' : i1I1i1i ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'community_backup' : OoO0 ( )
elif oO0o0O00O00O == 'community_backup_2' : ii1II1II ( )
elif oO0o0O00O00O == 'community_menu' : I1oo ( I1I1i1I1I1I1 , ooO0oOOooOo0 )
elif oO0o0O00O00O == 'countries' : i1I11 ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'description' : oooOo00000 ( I1ii1 , I1I1i1I1I1I1 , o00ooo0O , I11II1i1 , IiIiIi , I1iiioO0o0O0Ooo0o , IIiI1 , I1i1iI , I1iI1I1ii1 , iIIi1 , o0Ooo0o0Oo , oo00ooooOOo00 , ii1iOO00Oooo000 , iI1 )
elif oO0o0O00O00O == 'fix_special' : Iiii1 ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'full_backup' : Oooo0ooOoo0 ( )
elif oO0o0O00O00O == 'genres' : Oo0o0ooOoO ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'gotham' : oOoo0oO ( )
elif oO0o0O00O00O == 'grab_addons' : i1iI1IIi1I ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'grab_builds' : i1Iii ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'grab_builds_premium' : Grab_Builds_Premium ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'grab_hardware' : III1I1ii ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'grab_news' : i11111 ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'grab_tutorials' : iII1iiiiI1i ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'guisettingsfix' : i1ooO ( I1I1i1I1I1I1 , I1Ii1IIi )
elif oO0o0O00O00O == 'hardware_filter_menu' : oo0O0O ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'hardware_final_menu' : Ii111I ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'hardware_root_menu' : iiII1II11i ( )
elif oO0o0O00O00O == 'helix' : ii1iI11IiIIi ( )
elif oO0o0O00O00O == 'hide_passwords' : I11II ( )
elif oO0o0O00O00O == 'ipcheck' : O0OOoO ( )
elif oO0o0O00O00O == 'install_content' : o0oo0oOOOo00 ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'install_from_zip' : Oo0O0oOoO0o0 ( )
elif oO0o0O00O00O == 'instructions' : ooOOOo0 ( )
elif oO0o0O00O00O == 'instructions_1' : iIIiiiIIi1111 ( )
elif oO0o0O00O00O == 'instructions_2' : I1OoO00o00 ( )
elif oO0o0O00O00O == 'instructions_3' : O00O0ooo00OO0 ( )
elif oO0o0O00O00O == 'instructions_4' : Instructions_4 ( )
elif oO0o0O00O00O == 'instructions_5' : Instructions_5 ( )
elif oO0o0O00O00O == 'instructions_6' : Instructions_6 ( )
elif oO0o0O00O00O == 'keywords' : iII1 ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'kill_xbmc' : IiIIIi ( )
elif oO0o0O00O00O == 'kodi_settings' : oOo0ooO0O0oo ( )
elif oO0o0O00O00O == 'local_backup' : iiI1ii ( )
elif oO0o0O00O00O == 'LocalGUIDialog' : IIi1IiIii ( )
elif oO0o0O00O00O == 'log' : i1II1i1iiI1 ( )
elif oO0o0O00O00O == 'manual_search' : Oooo000 ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'manual_search_builds' : Manual_Search_Builds ( )
elif oO0o0O00O00O == 'news_root_menu' : Ii11II1IIIIIi ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'news_menu' : II1I1Ii11 ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'notify_msg' : oooO00oOOooO ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'open_system_info' : i11I111I1 ( )
elif oO0o0O00O00O == 'open_filemanager' : iII11IiIIII ( )
elif oO0o0O00O00O == 'openelec_backup' : oO0oOo ( )
elif oO0o0O00O00O == 'openelec_settings' : iiii1ii1 ( )
elif oO0o0O00O00O == 'OSS' : oO0IIi11IiiiI11i ( I1ii1 , I1I1i1I1I1I1 , I1IIiI , I1iiioO0o0O0Ooo0o )
elif oO0o0O00O00O == 'play_video' : yt . PlayVideo ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'platform_menu' : IIi1Ii ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'popular' : OOooO0o ( )
elif oO0o0O00O00O == 'popularwizard' : o00oO00 ( I1ii1 , I1I1i1I1I1I1 , I1IIiI , I1iiioO0o0O0Ooo0o )
elif oO0o0O00O00O == 'register' : Iii1I ( )
elif oO0o0O00O00O == 'remove_addon_data' : oO0OO ( )
elif oO0o0O00O00O == 'remove_addons' : o0OO000ooOo ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'remove_build' : ii111I1IiiI1i ( )
elif oO0o0O00O00O == 'remove_crash_logs' : IiiiiI ( )
elif oO0o0O00O00O == 'remove_packages' : oOoOo000Ooooo ( )
elif oO0o0O00O00O == 'remove_textures' : OooOoooo0000 ( )
elif oO0o0O00O00O == 'restore' : RESTORE ( )
elif oO0o0O00O00O == 'restore_backup' : o00oIiIiIiiI ( I1ii1 , I1I1i1I1I1I1 , I1iiioO0o0O0Ooo0o )
elif oO0o0O00O00O == 'restore_community' : i1iIIi ( I1ii1 , I1I1i1I1I1I1 , ooO0oOOooOo0 , I1iiioO0o0O0Ooo0o , I1i1iI , ii111iiIii , OoOo0OO0oooo )
elif oO0o0O00O00O == 'restore_local_CB' : oo0O0 ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'restore_local_gui' : iiIi1I ( )
elif oO0o0O00O00O == 'restore_local_OE' : oo00iiIIiIi1Ii1 ( )
elif oO0o0O00O00O == 'restore_openelec' : O0iIIii1 ( I1I1i1I1I1I1 , I1iiioO0o0O0Ooo0o )
elif oO0o0O00O00O == 'restore_option' : Ooo00O ( )
elif oO0o0O00O00O == 'restore_zip' : o0OooO0ooo00o ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'run_addon' : OoOO0Ooo ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'runtest' : speedtest . runtest ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'search_addons' : iIiOo ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'search_builds' : ooi1 ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'Search_Private' : Private_Search ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'showinfo' : I111II1ii11I1 ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'showinfo2' : iii1II ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'SortBy' : I1iiii ( BuildURL , type )
elif oO0o0O00O00O == 'speed_instructions' : i1I11iIIiIIiIi ( )
elif oO0o0O00O00O == 'speedtest_menu' : IiI1i11i ( )
elif oO0o0O00O00O == 'text_guide' : iIIiiiIiiii11 ( I1ii1 , I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'tools' : iI1iIIII11 ( )
elif oO0o0O00O00O == 'tutorial_final_menu' : i1iI1iii111 ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'tutorial_addon_menu' : iIi1 ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'tutorial_root_menu' : O0OoOOo0o ( )
elif oO0o0O00O00O == 'unhide_passwords' : i11iii1II1I1 ( )
elif oO0o0O00O00O == 'update' : IIIii1I ( )
elif oO0o0O00O00O == 'uploadlog' : O0O0oooo ( )
elif oO0o0O00O00O == 'user_info' : OooO00ooo0o0 ( )
elif oO0o0O00O00O == 'wipetools' : i1I11Iiii ( )
elif oO0o0O00O00O == 'xbmc_menu' : IiIII ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'xbmcversion' : ooo00o0OO0 ( I1I1i1I1I1I1 )
elif oO0o0O00O00O == 'wipe_xbmc' : OOo0 ( oO0o0O00O00O )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
