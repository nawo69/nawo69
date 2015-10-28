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
O0oo0OO0 = o0O . getSetting ( 'favourites' )
I1i1iiI1 = o0O . getSetting ( 'sources' )
iiIIIII1i1iI = o0O . getSetting ( 'repositories' )
o0oO0 = o0O . getSetting ( 'enablekeyword' )
oo00 = o0O . getSetting ( 'keywordpath' )
o00 = o0O . getSetting ( 'keywordname' )
Oo0oO0ooo = o0O . getSetting ( 'mastercopy' )
o0oOoO00o = o0O . getSetting ( 'username' ) . replace ( ' ' , '%20' )
i1 = o0O . getSetting ( 'password' )
oOOoo00O0O = o0O . getSetting ( 'versionoverride' )
i1111 = o0O . getSetting ( 'login' )
i11 = o0O . getSetting ( 'addonportal' )
I11 = o0O . getSetting ( 'maintenance' )
Oo0o0000o0o0 = o0O . getSetting ( 'hardwareportal' )
oOo0oooo00o = o0O . getSetting ( 'maintenance' )
oO0o0o0ooO0oO = o0O . getSetting ( 'latestnews' )
oo0o0O00 = o0O . getSetting ( 'tutorialportal' )
oO = o0O . getSetting ( 'startupvideo' )
i1iiIIiiI111 = o0O . getSetting ( 'startupvideopath' )
oooOOOOO = o0O . getSetting ( 'wizard' )
i1iiIII111ii = o0O . getSetting ( 'wizardurl1' )
i1iIIi1 = o0O . getSetting ( 'wizardname1' )
ii11iIi1I = o0O . getSetting ( 'wizardurl2' )
iI111I11I1I1 = o0O . getSetting ( 'wizardname2' )
OOooO0OOoo = o0O . getSetting ( 'wizardurl3' )
iIii1 = o0O . getSetting ( 'wizardname3' )
oOOoO0 = o0O . getSetting ( 'wizardurl4' )
O0OoO000O0OO = o0O . getSetting ( 'wizardname4' )
iiI1IiI = o0O . getSetting ( 'wizardurl5' )
II = o0O . getSetting ( 'wizardname5' )
ooOoOoo0O = o0O . getSetting ( 'trcheck' )
OooO0 = xbmcgui . Dialog ( )
II11iiii1Ii = xbmcgui . DialogProgress ( )
OO0o = xbmc . translatePath ( 'special://home/' )
Ooo = xbmc . translatePath ( os . path . join ( 'special://home/userdata' , '' ) )
O0o0Oo = xbmc . translatePath ( os . path . join ( Ooo , 'addon_data' ) )
Oo00OOOOO = xbmc . translatePath ( os . path . join ( Ooo , 'Database' ) )
O0O = xbmc . translatePath ( os . path . join ( Ooo , 'Thumbnails' ) )
O00o0OO = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' , '' ) )
I11i1 = xbmc . translatePath ( os . path . join ( O00o0OO , I1IiI , 'default.py' ) )
iIi1ii1I1 = xbmc . translatePath ( os . path . join ( O00o0OO , I1IiI , 'fanart.jpg' ) )
o0 = xbmc . translatePath ( os . path . join ( O00o0OO , I1IiI , 'resources' , 'addonxml' ) )
I11II1i = xbmc . translatePath ( os . path . join ( Ooo , 'guisettings.xml' ) )
IIIII = xbmc . translatePath ( os . path . join ( Ooo , 'guifix.xml' ) )
if 75 - 75: iii % OoO0
Ooooo = xbmc . translatePath ( os . path . join ( O00o0OO , I1IiI , 'icon_menu.png' ) )
I1I1i = xbmc . translatePath ( os . path . join ( Ooo , 'favourites.xml' ) )
oOOOoo0O0OoO = xbmc . translatePath ( os . path . join ( Ooo , 'sources.xml' ) )
ii1i1I1i = xbmc . translatePath ( os . path . join ( Ooo , 'advancedsettings.xml' ) )
o00oOO0 = xbmc . translatePath ( os . path . join ( Ooo , 'profiles.xml' ) )
oOoo = xbmc . translatePath ( os . path . join ( Ooo , 'RssFeeds.xml' ) )
iIii11I = xbmc . translatePath ( os . path . join ( Ooo , 'keymaps' , 'keyboard.xml' ) )
OOO0OOO00oo = xbmc . translatePath ( os . path . join ( zip ) )
Iii111II = xbmc . translatePath ( os . path . join ( OOO0OOO00oo , 'Community Builds' , '' ) )
iiii11I = xbmc . translatePath ( os . path . join ( O0o0Oo , I1IiI , 'startup.xml' ) )
Ooo0OO0oOO = xbmc . translatePath ( os . path . join ( O0o0Oo , I1IiI , 'temp.xml' ) )
ii11i1 = xbmc . translatePath ( os . path . join ( O0o0Oo , I1IiI , 'id.xml' ) )
IIIii1II1II = xbmc . translatePath ( os . path . join ( O00o0OO , 'repository.totalinstaller' ) )
i1I1iI = xbmc . translatePath ( os . path . join ( O00o0OO , 'repository.totalrevolution' ) )
oo0OooOOo0 = xbmc . translatePath ( os . path . join ( O00o0OO , 'plugin.program.totalrevolution' ) )
o0OO00oO = xbmc . translatePath ( os . path . join ( O0o0Oo , I1IiI , 'idtemp.xml' ) )
I11i1I1I = xbmc . translatePath ( os . path . join ( O0o0Oo , I1IiI , 'temp' ) )
oO0Oo = xbmc . translatePath ( os . path . join ( O00o0OO , I1IiI , 'resources/' ) )
oOOoo0Oo = xbmc . translatePath ( os . path . join ( O00o0OO , I1IiI , 'default.py' ) )
o00OO00OoO = xbmc . getSkinDir ( )
OOOO0OOoO0O0 = xbmc . translatePath ( 'special://logpath/' )
O0Oo000ooO00 = '/storage/backup'
oO0 = '/storage/.restore/'
Ii1iIiII1ii1 = Net ( )
ooOooo000oOO = xbmc . translatePath ( os . path . join ( O0o0Oo , I1IiI ) )
Oo0oOOo = xbmc . translatePath ( os . path . join ( ooOooo000oOO , 'guinew.xml' ) )
Oo0OoO00oOO0o = xbmc . translatePath ( os . path . join ( ooOooo000oOO , 'guitemp' , '' ) )
OOO00O = xbmc . translatePath ( os . path . join ( OOO0OOO00oo , 'Database' ) )
OOoOO0oo0ooO = os . path . join ( O00o0OO , 'packages' )
O0o0O00Oo0o0 = os . path . join ( Ooo , 'addontemp' )
O00O0oOO00O00 = xbmc . translatePath ( os . path . join ( Ooo , '.cbcfg' ) )
i1Oo00 = [ 'firstrun' , 'plugin.program.tbs' , 'plugin.program.totalinstaller' , 'script.module.addon.common' , 'addons' , 'addon_data' , 'userdata' , 'sources.xml' , 'favourites.xml' ]
i1i = 0.0
iiI111I1iIiI = 0.0
IIIi1I1IIii1II = '0'
O0ii1ii1ii = [ '/storage/.kodi' , '/storage/.cache' , '/storage/.config' , '/storage/.ssh' ]
oooooOoo0ooo = '1889903'
if 6 - 6: oOoO0o00OO0 - iI1iiIiiII . OOo00O0 / iIII % O0
if 43 - 43: OoooooooOO + O0 * O0 % O0
if 74 - 74: I1ii11iIi11i - I1IiiI - Oo0Ooo . OoO0 - iI1iiIiiII
class OOOoOoo0O ( xbmcgui . WindowXMLDialog ) :
 if 77 - 77: oOoO0o00OO0 % oOoO0o00OO0 * ooOo - i11iIiiIii
 def __init__ ( self , * args , ** kwargs ) :
  self . shut = kwargs [ 'close_time' ]
  xbmc . executebuiltin ( "Skin.Reset(AnimeWindowXMLDialogClose)" )
  xbmc . executebuiltin ( "Skin.SetBool(AnimeWindowXMLDialogClose)" )
  if 93 - 93: OoooooooOO / I1IiiI % i11iIiiIii + I1ii11iIi11i * OoO0O00
 def onFocus ( self , controlID ) :
  pass
  if 15 - 15: iii . OoO0O00 / Oo0Ooo + iii
 def onClick ( self , controlID ) :
  if controlID == 12 :
   xbmc . Player ( ) . stop ( )
   self . _close_dialog ( )
   if 78 - 78: O0 . ooOo . II111iiii % Oo
 def onAction ( self , action ) :
  if action in [ 5 , 6 , 7 , 9 , 10 , 92 , 117 ] or action . getButtonCode ( ) in [ 275 , 257 , 261 ] :
   xbmc . Player ( ) . stop ( )
   self . _close_dialog ( )
   if 49 - 49: OoO0 / OoO0O00 . II111iiii
 def _close_dialog ( self ) :
  xbmc . executebuiltin ( "Skin.Reset(AnimeWindowXMLDialogClose)" )
  time . sleep ( .4 )
  self . close ( )
  if 68 - 68: i11iIiiIii % I1ii11iIi11i + i11iIiiIii
  if 31 - 31: II111iiii . I1IiiI
def II1I ( name , url , mode , iconimage , fanart , video , description , skins , guisettingslink , artpack ) :
 O0i1II1Iiii1I11 = sys . argv [ 0 ]
 O0i1II1Iiii1I11 += "?url=" + urllib . quote_plus ( url )
 O0i1II1Iiii1I11 += "&mode=" + str ( mode )
 O0i1II1Iiii1I11 += "&name=" + urllib . quote_plus ( name )
 O0i1II1Iiii1I11 += "&iconimage=" + urllib . quote_plus ( iconimage )
 O0i1II1Iiii1I11 += "&fanart=" + urllib . quote_plus ( fanart )
 O0i1II1Iiii1I11 += "&video=" + urllib . quote_plus ( video )
 O0i1II1Iiii1I11 += "&description=" + urllib . quote_plus ( description )
 O0i1II1Iiii1I11 += "&skins=" + urllib . quote_plus ( skins )
 O0i1II1Iiii1I11 += "&guisettingslink=" + urllib . quote_plus ( guisettingslink )
 O0i1II1Iiii1I11 += "&artpack=" + urllib . quote_plus ( artpack )
 if 9 - 9: I1ii11iIi11i / Oo0Ooo - I1IiiI / OoooooooOO / iIii1I11I1II1 - o0oOOo0O0Ooo
 o00oooO0Oo = True
 o0O0OOO0Ooo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if 45 - 45: O0 / o0oOOo0O0Ooo
 o0O0OOO0Ooo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0O0OOO0Ooo . setProperty ( "Fanart_Image" , fanart )
 o0O0OOO0Ooo . setProperty ( "Build.Video" , video )
 if 32 - 32: oOoO0o00OO0 . iI1iiIiiII . iI1iiIiiII
 if ( mode == None ) or ( mode == 'restore_option' ) or ( mode == 'backup_option' ) or ( mode == 'cb_root_menu' ) or ( mode == 'genres' ) or ( mode == 'grab_builds' ) or ( mode == 'community_menu' ) or ( mode == 'instructions' ) or ( mode == 'countries' ) or ( mode == 'update_build' ) or ( url == None ) or ( len ( url ) < 1 ) :
  if 62 - 62: I1ii11iIi11i + iI1iiIiiII % oOoO0o00OO0 + Oo
  o00oooO0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0i1II1Iiii1I11 , listitem = o0O0OOO0Ooo , isFolder = True )
  if 33 - 33: O0 . iI1iiIiiII . I1IiiI
 else :
  o00oooO0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0i1II1Iiii1I11 , listitem = o0O0OOO0Ooo , isFolder = False )
  if 72 - 72: i1IIi / OoO0O00 + OoooooooOO - Oo0Ooo
 return o00oooO0Oo
 if 29 - 29: I1ii11iIi11i + ooOo % O0
 if 10 - 10: iii / OOo00O0 - I1IiiI * iIii1I11I1II1 - I1IiiI
def OO0oO0 ( handle , url , listitem , isFolder ) :
 xbmcplugin . addDirectoryItem ( handle , url , listitem , isFolder )
 if 82 - 82: iii % o0oOOo0O0Ooo % OoO0O00 - Oo0Ooo + OoooooooOO
 if 22 - 22: i1IIi + O0 . iIii1I11I1II1 * oOoO0o00OO0 % i11iIiiIii * I1IiiI
def oo000o ( name , url , mode , iconimage , fanart , buildname , author , version , description , updated , skins , videoaddons , audioaddons , programaddons , pictureaddons , sources , adult ) :
 if 44 - 44: i1IIi % II111iiii + iii
 iconimage = Ooooo
 if 45 - 45: oOoO0o00OO0 / oOoO0o00OO0 + OOo00O0 + iIII
 O0i1II1Iiii1I11 = sys . argv [ 0 ]
 O0i1II1Iiii1I11 += "?url=" + urllib . quote_plus ( url )
 O0i1II1Iiii1I11 += "&mode=" + str ( mode )
 O0i1II1Iiii1I11 += "&name=" + urllib . quote_plus ( name )
 O0i1II1Iiii1I11 += "&iconimage=" + urllib . quote_plus ( iconimage )
 O0i1II1Iiii1I11 += "&fanart=" + urllib . quote_plus ( fanart )
 O0i1II1Iiii1I11 += "&author=" + urllib . quote_plus ( author )
 O0i1II1Iiii1I11 += "&description=" + urllib . quote_plus ( description )
 O0i1II1Iiii1I11 += "&version=" + urllib . quote_plus ( version )
 O0i1II1Iiii1I11 += "&buildname=" + urllib . quote_plus ( buildname )
 O0i1II1Iiii1I11 += "&updated=" + urllib . quote_plus ( updated )
 O0i1II1Iiii1I11 += "&skins=" + urllib . quote_plus ( skins )
 O0i1II1Iiii1I11 += "&videoaddons=" + urllib . quote_plus ( videoaddons )
 O0i1II1Iiii1I11 += "&audioaddons=" + urllib . quote_plus ( audioaddons )
 O0i1II1Iiii1I11 += "&buildname=" + urllib . quote_plus ( buildname )
 O0i1II1Iiii1I11 += "&programaddons=" + urllib . quote_plus ( programaddons )
 O0i1II1Iiii1I11 += "&pictureaddons=" + urllib . quote_plus ( pictureaddons )
 O0i1II1Iiii1I11 += "&sources=" + urllib . quote_plus ( sources )
 O0i1II1Iiii1I11 += "&adult=" + urllib . quote_plus ( adult )
 if 47 - 47: o0oOOo0O0Ooo + iIII
 o00oooO0Oo = True
 o0O0OOO0Ooo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if 82 - 82: II111iiii . iI1iiIiiII - iIii1I11I1II1 - iI1iiIiiII * II111iiii
 o0O0OOO0Ooo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0O0OOO0Ooo . setProperty ( "Fanart_Image" , fanart )
 o0O0OOO0Ooo . setProperty ( "Build.Video" , ooO0oOOooOo0 )
 if 38 - 38: OOo00O0
 o00oooO0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0i1II1Iiii1I11 , listitem = o0O0OOO0Ooo , isFolder = False )
 if 84 - 84: iIii1I11I1II1 % oOoO0o00OO0 / iIii1I11I1II1 % iii
 return o00oooO0Oo
 if 45 - 45: O0
def I1IiiiiI ( title , name , url , mode , iconimage = '' , fanart = '' , video = '' , description = '' , zip_link = '' , repo_link = '' , repo_id = '' , addon_id = '' , provider_name = '' , forum = '' , data_path = '' ) :
 if len ( iconimage ) > 0 :
  if 80 - 80: OOo00O0 . i11iIiiIii - o0oOOo0O0Ooo
  iconimage = Ooooo
 else :
  iconimage = 'DefaultFolder.png'
  if 25 - 25: OoO0O00
 if fanart == '' :
  fanart = iIi1ii1I1
  if 62 - 62: Oo + O0
 O0i1II1Iiii1I11 = sys . argv [ 0 ]
 O0i1II1Iiii1I11 += "?url=" + urllib . quote_plus ( url )
 O0i1II1Iiii1I11 += "&zip_link=" + urllib . quote_plus ( zip_link )
 O0i1II1Iiii1I11 += "&repo_link=" + urllib . quote_plus ( repo_link )
 O0i1II1Iiii1I11 += "&data_path=" + urllib . quote_plus ( data_path )
 O0i1II1Iiii1I11 += "&provider_name=" + str ( provider_name )
 O0i1II1Iiii1I11 += "&forum=" + str ( forum )
 O0i1II1Iiii1I11 += "&repo_id=" + str ( repo_id )
 O0i1II1Iiii1I11 += "&addon_id=" + str ( addon_id )
 O0i1II1Iiii1I11 += "&mode=" + str ( mode )
 O0i1II1Iiii1I11 += "&name=" + urllib . quote_plus ( name )
 O0i1II1Iiii1I11 += "&fanart=" + urllib . quote_plus ( fanart )
 O0i1II1Iiii1I11 += "&video=" + urllib . quote_plus ( video )
 O0i1II1Iiii1I11 += "&description=" + urllib . quote_plus ( description )
 if 98 - 98: o0oOOo0O0Ooo
 o00oooO0Oo = True
 o0O0OOO0Ooo = xbmcgui . ListItem ( title , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if 51 - 51: Oo0Ooo - ooOo + II111iiii * OoO0 . iii + ooOo
 o0O0OOO0Ooo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0O0OOO0Ooo . setProperty ( "Fanart_Image" , fanart )
 o0O0OOO0Ooo . setProperty ( "Build.Video" , video )
 if 78 - 78: i11iIiiIii / oOoO0o00OO0 - OoO0 / Oo + ooOo
 OO0oO0 ( handle = int ( sys . argv [ 1 ] ) , url = O0i1II1Iiii1I11 , listitem = o0O0OOO0Ooo , isFolder = False )
 if 82 - 82: OoO0
 if 46 - 46: OoooooooOO . i11iIiiIii
def OOo0oO00ooO00 ( type , name , url , mode , iconimage = '' , fanart = '' , video = '' , description = '' ) :
 if type != 'folder2' and type != 'addon' :
  if 90 - 90: OoOoOO00 * OOo00O0 + o0oOOo0O0Ooo
  if 81 - 81: ooOo . o0oOOo0O0Ooo % O0 / I1IiiI - ooOo
  if 43 - 43: i11iIiiIii + Oo0Ooo * II111iiii * OOo00O0 * O0
  if 64 - 64: Oo % iIii1I11I1II1 * ooOo
  if 79 - 79: O0
  if 78 - 78: I1ii11iIi11i + Oo - OOo00O0
  iconimage = Ooooo
 if type == 'addon' :
  if 38 - 38: o0oOOo0O0Ooo - ooOo + iIii1I11I1II1 / OoOoOO00 % Oo0Ooo
  if len ( iconimage ) > 0 :
   iconimage = iconimage
  else :
   iconimage = 'DefaultFolder.png'
   if 57 - 57: OoO0O00 / iIII
   if 29 - 29: iIii1I11I1II1 + OoOoOO00 * OoO0O00 * Oo . I1IiiI * I1IiiI
   if 7 - 7: iI1iiIiiII * OOo00O0 % OoO0 - o0oOOo0O0Ooo
 if fanart == '' :
  fanart = iIi1ii1I1
  if 13 - 13: OoO0 . i11iIiiIii
 O0i1II1Iiii1I11 = sys . argv [ 0 ]
 O0i1II1Iiii1I11 += "?url=" + urllib . quote_plus ( url )
 O0i1II1Iiii1I11 += "&mode=" + str ( mode )
 O0i1II1Iiii1I11 += "&name=" + urllib . quote_plus ( name )
 O0i1II1Iiii1I11 += "&fanart=" + urllib . quote_plus ( fanart )
 O0i1II1Iiii1I11 += "&video=" + urllib . quote_plus ( video )
 O0i1II1Iiii1I11 += "&description=" + urllib . quote_plus ( description )
 if 56 - 56: I1ii11iIi11i % O0 - I1IiiI
 o00oooO0Oo = True
 o0O0OOO0Ooo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 if 100 - 100: OoO0 - O0 % ooOo * Oo + I1IiiI
 o0O0OOO0Ooo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : description } )
 o0O0OOO0Ooo . setProperty ( "Fanart_Image" , fanart )
 o0O0OOO0Ooo . setProperty ( "Build.Video" , video )
 if 88 - 88: OoooooooOO - OoO0O00 * O0 * OoooooooOO . OoooooooOO
 if ( type == 'folder' ) or ( type == 'folder2' ) or ( type == 'tutorial_folder' ) or ( type == 'news_folder' ) :
  o00oooO0Oo = OO0oO0 ( handle = int ( sys . argv [ 1 ] ) , url = O0i1II1Iiii1I11 , listitem = o0O0OOO0Ooo , isFolder = True )
  if 33 - 33: OOo00O0 + oOoO0o00OO0 * ooOo / iIii1I11I1II1 - I1IiiI
 else :
  o00oooO0Oo = OO0oO0 ( handle = int ( sys . argv [ 1 ] ) , url = O0i1II1Iiii1I11 , listitem = o0O0OOO0Ooo , isFolder = False )
  if 54 - 54: OOo00O0 / Oo . ooOo % oOoO0o00OO0
 return o00oooO0Oo
 if 57 - 57: i11iIiiIii . I1ii11iIi11i - OoO0 - ooOo + OoOoOO00
 if 63 - 63: OoOoOO00 * oOoO0o00OO0
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
 if 44 - 44: ooOo / iii / iii
 if 87 - 87: Oo0Ooo . I1IiiI - II111iiii + O0 / Oo0Ooo / ooOo
def IiI ( ) :
 IIIii1I ( )
 xbmc . executebuiltin ( 'ActivateWindow(10040,"addons://outdated/",return)' )
 if 97 - 97: O0 + OoOoOO00
 if 89 - 89: o0oOOo0O0Ooo + OoO0O00 * iii * OoO0
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
 if 69 - 69: iIII
 if 40 - 40: OOo00O0 + OoooooooOO % o0oOOo0O0Ooo - iIii1I11I1II1 . I1IiiI
def iIiIi11iI ( url ) :
 Oo0O00O000 = 'http://noobsandnerds.com/TI/AddonPortal/addondetails.php?id=%s' % ( url )
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
 if 47 - 47: Oo0Ooo % iii % i11iIiiIii - O0 + iIII
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
 if 78 - 78: oOoO0o00OO0 + iii . iIII - oOoO0o00OO0 . OoO0
 if 30 - 30: I1IiiI + OoO0O00 % OoO0 * oOoO0o00OO0 / Oo0Ooo - iii
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
 if 98 - 98: iIii1I11I1II1 * I1ii11iIi11i * Oo + iIII % i11iIiiIii % O0
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
 o00OO00OoO = IIIIiIiIi1 [ 0 ] if ( len ( IIIIiIiIi1 ) > 0 ) else ''
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
 if 86 - 86: II111iiii % i11iIiiIii + OoO0 % i11iIiiIii
 if iII111Ii != '' :
  Ooo0o0OOO = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR][COLOR=red]This add-on is depreciated, it\'s no longer available.[/COLOR]'
  if 35 - 35: Oo + oOoO0o00OO0
 elif i1ii1II1ii == '' and o0o0oOoOO0O == '' and Ii == '' :
  Ooo0o0OOO = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR][COLOR=lime]No reported problems[/COLOR]'
  if 40 - 40: o0oOOo0O0Ooo
 elif i1ii1II1ii == '' and o0o0oOoOO0O == '' and Ii != '' and iII111Ii == '' :
  Ooo0o0OOO = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR][COLOR=orange]Although there have been no reported problems there may be issues with this add-on, see below.[/COLOR]'
  if 67 - 67: ooOo + II111iiii - O0 . ooOo * II111iiii * iii
 elif i1ii1II1ii == '' and o0o0oOoOO0O != '' :
  Ooo0o0OOO = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR]Marked as broken by the add-on developer.[CR][COLOR=dodgerblue]Developer Comments: [/COLOR]' + o0o0oOoOO0O
  if 90 - 90: OoO0 . iI1iiIiiII
 elif i1ii1II1ii != '' and o0o0oOoOO0O == '' :
  Ooo0o0OOO = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR]Marked as broken by a member of the community at [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR][CR][COLOR=dodgerblue]User Comments: [/COLOR]' + i1ii1II1ii
  if 81 - 81: Oo - iii % iIII - OoO0O00 / Oo0Ooo
 elif i1ii1II1ii != '' and o0o0oOoOO0O != '' :
  Ooo0o0OOO = '[CR][CR][COLOR=dodgerblue]Status: [/COLOR]Marked as broken by both the add-on developer and a member of the community at [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR][CR][COLOR=dodgerblue]Developer Comments: [/COLOR]' + o0o0oOoOO0O + '[CR][COLOR=dodgerblue]User Comments: [/COLOR]' + i1ii1II1ii
  if 4 - 4: OoooooooOO - i1IIi % OoO0 - Oo * o0oOOo0O0Ooo
  if 85 - 85: OoooooooOO * iIii1I11I1II1 . oOoO0o00OO0 / OoooooooOO % I1IiiI % O0
 I1iii = str ( '[COLOR=orange]Name: [/COLOR]' + I1ii1 + '[COLOR=orange]     Author(s): [/COLOR]' + IiIi1I1ii111 + '[COLOR=orange][CR][CR]Version: [/COLOR]' + IiIiIi + '[COLOR=orange]     Created: [/COLOR]' + IIIII1 + '[COLOR=orange]     Updated: [/COLOR]' + IIiI1 + '[COLOR=orange][CR][CR]Repository: [/COLOR]' + O0OoO0ooOO0o + OoOo0oOooOoOO + '[COLOR=orange]     Add-on Type(s): [/COLOR]' + iIi1Ii1i1iI + O0Oo00OoOo + Ooo0o0OOO + iII111Ii + Ii + IiIIIIIi + OooO0oo + Ooo00OoOOO )
 if 86 - 86: I1ii11iIi11i * O0 * iI1iiIiiII
 if 51 - 51: II111iiii + iI1iiIiiII . i1IIi . I1ii11iIi11i + OoOoOO00 * I1IiiI
 if os . path . exists ( os . path . join ( O00o0OO , Oo0o0000OOoO ) ) :
  if 'script.module' in Oo0o0000OOoO or 'repo' in Oo0o0000OOoO :
   OOo0oO00ooO00 ( '' , '[COLOR=orange]Already installed[/COLOR]' , '' , '' , i11111I1I , '' , '' , '' )
  else :
   OOo0oO00ooO00 ( '' , '[COLOR=orange]Already installed -[/COLOR] Click here to run the add-on' , Oo0o0000OOoO , 'run_addon' , i11111I1I , '' , '' , '' )
   if 72 - 72: ooOo + ooOo / II111iiii . OoooooooOO % OoO0
   if 49 - 49: ooOo . OoO0O00 - Oo0Ooo * OoooooooOO . Oo0Ooo
 if I1ii1 == '' :
  OOo0oO00ooO00 ( '' , '[COLOR=yellow]Sorry request failed due to high traffic on server, please try again[/COLOR]' , '' , '' , i11111I1I , '' , '' , '' )
  if 2 - 2: OoooooooOO % Oo
  if 63 - 63: I1IiiI % iIii1I11I1II1
 elif I1ii1 != '' :
  if 39 - 39: oOoO0o00OO0 / II111iiii / I1ii11iIi11i % I1IiiI
  if ( i1ii1II1ii == '' ) and ( o0o0oOoOO0O == '' ) and ( iII111Ii == '' ) and ( Ii == '' ) :
   OOo0oO00ooO00 ( 'addon' , '[COLOR=yellow][FULL DETAILS][/COLOR] No problems reported' , I1iii , 'text_guide' , i11111I1I , '' , '' , I1iii )
   if 89 - 89: OOo00O0 + OoooooooOO + OOo00O0 * i1IIi + iIii1I11I1II1 % iii
  if ( i1ii1II1ii != '' and iII111Ii == '' ) or ( o0o0oOoOO0O != '' and iII111Ii == '' ) or ( Ii != '' and iII111Ii == '' ) :
   OOo0oO00ooO00 ( 'addon' , '[COLOR=yellow][FULL DETAILS][/COLOR][COLOR=orange] Possbile problems reported[/COLOR]' , I1iii , 'text_guide' , i11111I1I , '' , '' , I1iii )
   if 59 - 59: Oo + i11iIiiIii
  if iII111Ii != '' :
   OOo0oO00ooO00 ( 'addon' , '[COLOR=yellow][FULL DETAILS][/COLOR][COLOR=red] Add-on now depreciated[/COLOR]' , I1iii , 'text_guide' , i11111I1I , '' , '' , I1iii )
   if 88 - 88: i11iIiiIii - iIII
   if 67 - 67: Oo . Oo0Ooo + OoOoOO00 - OoooooooOO
  if iII111Ii == '' :
   if 70 - 70: Oo / II111iiii - iIii1I11I1II1 - oOoO0o00OO0
   if O0OoO0ooOO0o != '' and 'superrepo' not in O0OoO0ooOO0o :
    I1IiiiiI ( '[COLOR=lime][INSTALL - Recommended] [/COLOR]' + I1ii1 , I1ii1 , '' , 'addon_install_zero' , 'Install.png' , '' , '' , OooO0oo , iI , i1OO0oOOoo , O0OoO0ooOO0o , Oo0o0000OOoO , IiIi1I1ii111 , IiIi1iIIi1 , oOOO00o000o )
    I1IiiiiI ( '[COLOR=lime][INSTALL - Backup Option] [/COLOR]' + I1ii1 , I1ii1 , '' , 'addon_install' , 'Install.png' , '' , '' , OooO0oo , iIi11i1 , i1OO0oOOoo , O0OoO0ooOO0o , Oo0o0000OOoO , IiIi1I1ii111 , IiIi1iIIi1 , oOOO00o000o )
    if 11 - 11: iIii1I11I1II1 . OoooooooOO . II111iiii / i1IIi - iii
   if O0OoO0ooOO0o == '' or 'superrepo' in O0OoO0ooOO0o :
    I1IiiiiI ( '[COLOR=lime][INSTALL] [/COLOR]' + I1ii1 + ' - THIS IS NOT IN A SELF UPDATING REPO' , I1ii1 , '' , 'addon_install' , 'Install.png' , '' , '' , OooO0oo , iIi11i1 , i1OO0oOOoo , O0OoO0ooOO0o , Oo0o0000OOoO , IiIi1I1ii111 , IiIi1iIIi1 , oOOO00o000o )
    if 30 - 30: OoOoOO00
    if 21 - 21: i11iIiiIii / OOo00O0 % Oo * O0 . iii - iIii1I11I1II1
  if ii1Oo0000oOo != 'None' :
   OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  Preview' , I1I , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 26 - 26: II111iiii * OoOoOO00
  if I1I != 'None' :
   OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + O0Oo0o000oO , I1I , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 10 - 10: II111iiii . oOoO0o00OO0
  if ooooo != 'None' :
   OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + oO0o00oOOooO0 , ooooo , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 32 - 32: OoO0 . iI1iiIiiII . OoooooooOO - OoO0O00 + ooOo
  if i11IIIiI1I != 'None' :
   OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + OOOoO000 , i11IIIiI1I , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 88 - 88: oOoO0o00OO0
  if o0iiiI1I1iIIIi1 != 'None' :
   OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + oOOOO , o0iiiI1I1iIIIi1 , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 19 - 19: II111iiii * iI1iiIiiII + OoO0
  if Iii != 'None' :
   OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + IiIi1ii111i1 , Iii , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 65 - 65: Oo . OOo00O0 . OoO0O00 . oOoO0o00OO0 - Oo
  if I1iiiiI1iI != 'None' :
   OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + i1i1i1I , I1iiiiI1iI , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 19 - 19: i11iIiiIii + oOoO0o00OO0 % iIII
  if iIiiiii1i != 'None' :
   OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + oOoo000 , iIiiiii1i , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 14 - 14: OoO0O00 . II111iiii . iii / OoO0 % I1ii11iIi11i - iIII
  if iiIi1IIiI != 'None' :
   OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + OooOo00o , iiIi1IIiI , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 67 - 67: iii - Oo . i1IIi
  if i1oO0OO0 != 'None' :
   OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][VIDEO][/COLOR]  ' + IiI11i1IIiiI , i1oO0OO0 , 'play_video' , 'Video_Guide.png' , '' , '' , '' )
   if 35 - 35: oOoO0o00OO0 + iIII - ooOo . oOoO0o00OO0 . iI1iiIiiII
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
 O0000 = xbmc . translatePath ( os . path . join ( O00o0OO , addon_id ) )
 if 64 - 64: II111iiii - I1IiiI
 if os . path . exists ( O0000 ) :
  O0O0ooOOO = 1
  if 67 - 67: oOoO0o00OO0 % oOoO0o00OO0 / oOoO0o00OO0
 else :
  O0O0ooOOO = 0
  if 53 - 53: iIii1I11I1II1
 oooo00o0o0o = xbmc . translatePath ( os . path . join ( OOoOO0oo0ooO , name + '.zip' ) )
 O0Oo00oO0O00 = xbmc . translatePath ( os . path . join ( O00o0OO , addon_id ) )
 if 32 - 32: II111iiii . OoO0 - oOoO0o00OO0 * OOo00O0
 II11iiii1Ii . create ( "Installing Addon" , "Please wait whilst your addon is installed" , '' , '' )
 if 71 - 71: o0oOOo0O0Ooo % OoO0 - II111iiii * OoooooooOO
 try :
  downloader . download ( repo_link , oooo00o0o0o , II11iiii1Ii )
  oOOO ( oooo00o0o0o , O00o0OO , II11iiii1Ii )
  if 56 - 56: I1ii11iIi11i
 except :
  if 26 - 26: OoooooooOO % OoooooooOO
  try :
   downloader . download ( zip_link , oooo00o0o0o , II11iiii1Ii )
   oOOO ( oooo00o0o0o , O00o0OO , II11iiii1Ii )
   if 33 - 33: OOo00O0
  except :
   if 62 - 62: I1ii11iIi11i + OoO0 + i1IIi / OoooooooOO
   try :
    if not os . path . exists ( O0Oo00oO0O00 ) :
     os . makedirs ( O0Oo00oO0O00 )
     if 7 - 7: o0oOOo0O0Ooo + i1IIi . I1IiiI / Oo0Ooo
    i11I1IiII1i1i = ooI1111i ( data_path ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
    I111i1I1 = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( i11I1IiII1i1i )
    if 62 - 62: Oo * OOo00O0 / Oo0Ooo * o0oOOo0O0Ooo
    for II1Ii1iI1i1 in I111i1I1 :
     o0OoO000O = xbmc . translatePath ( os . path . join ( O0Oo00oO0O00 , II1Ii1iI1i1 ) )
     if 94 - 94: OoOoOO00 . O0 / OoO0 . I1ii11iIi11i - i1IIi
     if addon_id not in II1Ii1iI1i1 and '/' not in II1Ii1iI1i1 :
      if 26 - 26: OoO0O00 - Oo . o0oOOo0O0Ooo
      try :
       II11iiii1Ii . update ( 0 , "Downloading [COLOR=yellow]" + II1Ii1iI1i1 + '[/COLOR]' , '' , 'Please wait...' )
       downloader . download ( data_path + II1Ii1iI1i1 , o0OoO000O , II11iiii1Ii )
       if 65 - 65: I1ii11iIi11i % O0 % iIii1I11I1II1 * OoO0
      except :
       print "failed to install" + II1Ii1iI1i1
       if 31 - 31: OoO0
     if '/' in II1Ii1iI1i1 and '..' not in II1Ii1iI1i1 and 'http' not in II1Ii1iI1i1 :
      iIIiI1I1i = data_path + II1Ii1iI1i1
      O0O0OOooOO0 ( o0OoO000O , iIIiI1I1i )
      if 31 - 31: I1IiiI * ooOo + OoooooooOO - oOoO0o00OO0 / OoooooooOO
   except :
    OooO0 . ok ( "Error downloading add-on" , 'There was an error downloading [COLOR=yellow]' + name , '[/COLOR]Please consider updating the add-on portal with details or report the error on the forum at [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR]' )
    i11I1II = 0
    if 19 - 19: iI1iiIiiII * iIII * o0oOOo0O0Ooo + O0 / O0
 if i11I1II == 1 :
  time . sleep ( 1 )
  II11iiii1Ii . update ( 0 , "[COLOR=yellow]" + name + '[/COLOR]  [COLOR=lime]Successfully Installed[/COLOR]' , '' , 'Now installing repository' )
  time . sleep ( 1 )
  ooOoO = xbmc . translatePath ( os . path . join ( O00o0OO , repo_id ) )
  if 91 - 91: ooOo + I1IiiI
  if ( repo_id != 'repository.xbmc.org' ) and not ( os . path . exists ( ooOoO ) ) and ( repo_id != '' ) and ( 'superrepo' not in repo_id ) :
   OoOooo ( repo_id )
   if 74 - 74: iIii1I11I1II1 * iI1iiIiiII % OoOoOO00
  xbmc . sleep ( 2000 )
  if 36 - 36: OoooooooOO - ooOo
  if os . path . exists ( O0000 ) and O0O0ooOOO == 0 :
   OOo = 'http://noobsandnerds.com/TI/AddonPortal/downloadcount.php?id=%s' % ( addon_id )
   ooI1111i ( OOo )
   if 89 - 89: O0
  IIIII1I1Ii11iI ( name , addon_id )
  xbmc . executebuiltin ( 'UpdateLocalAddons' )
  xbmc . sleep ( 1000 )
  xbmc . executebuiltin ( 'UpdateAddonRepos' )
  if 52 - 52: Oo - oOoO0o00OO0 * ooOo
  if OO0OOO0oOOo00O == 0 :
   OooO0 . ok ( name + " Install Complete" , 'The add-on has been successfully installed but' , 'there was an error installing the repository.' , 'This will mean the add-on fails to update' )
   if 17 - 17: OoooooooOO + Oo * iii * OoOoOO00
  if OO0oIII111i11IiI == 0 :
   OooO0 . ok ( name + " Install Complete" , 'The add-on has been successfully installed but' , 'there was an error installing modules.' , 'This could result in errors with the add-on.' )
   if 36 - 36: O0 + Oo0Ooo
  if OO0oIII111i11IiI != 0 and OO0OOO0oOOo00O != 0 and forum != 'None' :
   OooO0 . ok ( name + " Install Complete" , 'Please support the developer(s) [COLOR=dodgerblue]' + provider_name , '[/COLOR]Support for this add-on can be found at [COLOR=yellow]' + forum , '[/COLOR][CR]Visit [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR] for all your Kodi needs.' )
   if 5 - 5: Oo0Ooo * OoOoOO00
  if OO0oIII111i11IiI != 0 and OO0OOO0oOOo00O != 0 and forum == 'None' :
   OooO0 . ok ( name + " Install Complete" , 'Please support the developer(s) [COLOR=dodgerblue]' + provider_name , '[/COLOR]No details of forum support have been given.' )
   if 46 - 46: iIII
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 33 - 33: oOoO0o00OO0 - II111iiii * OoooooooOO - Oo0Ooo - Oo
 if 84 - 84: OOo00O0 + Oo0Ooo - OoOoOO00 * OoOoOO00
def OoooO0o ( name , contenttypes , repo_link , repo_id , addon_id , provider_name , forum , data_path ) :
 O0000 = xbmc . translatePath ( os . path . join ( O00o0OO , addon_id ) )
 forum = str ( forum )
 if 24 - 24: OoOoOO00 % i1IIi + oOoO0o00OO0 . i11iIiiIii . I1ii11iIi11i
 if not os . path . exists ( O0000 ) :
  IIi1II = 1
  if 2 - 2: II111iiii - OoO0O00 . iI1iiIiiII * oOoO0o00OO0 / ooOo
 else :
  IIi1II = 0
  if 80 - 80: Oo / iii / OoOoOO00 + i1IIi - Oo0Ooo
 repo_id = str ( repo_id )
 ooOoO = xbmc . translatePath ( os . path . join ( O00o0OO , repo_id ) )
 if 11 - 11: o0oOOo0O0Ooo * OoO0O00
 if os . path . exists ( O0000 ) :
  O0O0ooOOO = 1
  iIi1IiI = OooO0 . yesno ( 'Add-on Already Installed' , 'This add-on has already been detected on your system. Would you like to remove the old version and re-install? There should be no need for this unless you\'ve manually opened up the add-on code and edited in a text editor.' )
  if 14 - 14: iI1iiIiiII % ooOo % Oo0Ooo - i11iIiiIii
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
   if 31 - 31: iii % Oo * iii
  IiII1i1iii1Ii = os . path . join ( O00o0OO , addon_id , 'addon.xml' )
  iIO0O00OOo = os . path . join ( O00o0OO , addon_id , 'default.py' )
  if 66 - 66: i11iIiiIii / o0oOOo0O0Ooo - OoooooooOO / i1IIi . i11iIiiIii
  shutil . copyfile ( o0 , IiII1i1iii1Ii )
  if 16 - 16: Oo0Ooo % I1ii11iIi11i + iii - O0 . oOoO0o00OO0 / OOo00O0
  IIi1I = open ( os . path . join ( IiII1i1iii1Ii ) , mode = 'r' )
  iiiO00O00O000OOO = IIi1I . read ( )
  IIi1I . close ( )
  if 3 - 3: O0
  if 64 - 64: i1IIi % iIII / i11iIiiIii - i1IIi % Oo . oOoO0o00OO0
  II1i111 = re . compile ( 'testid[\s\S]*?' ) . findall ( iiiO00O00O000OOO )
  Ooo0OOoOoO0 = II1i111 [ 0 ] if ( len ( II1i111 ) > 0 ) else 'None'
  i1iiiIii11 = re . compile ( 'testname[\s\S]*?' ) . findall ( iiiO00O00O000OOO )
  oo0oO = i1iiiIii11 [ 0 ] if ( len ( i1iiiIii11 ) > 0 ) else 'None'
  OOoOOO000O0 = re . compile ( 'testprovider[\s\S]*?' ) . findall ( iiiO00O00O000OOO )
  oOo0 = OOoOOO000O0 [ 0 ] if ( len ( OOoOOO000O0 ) > 0 ) else 'None'
  II1i11I1 = re . compile ( 'testprovides[\s\S]*?' ) . findall ( iiiO00O00O000OOO )
  iiIiIiII = II1i11I1 [ 0 ] if ( len ( II1i11I1 ) > 0 ) else 'None'
  i1I1 = iiiO00O00O000OOO . replace ( Ooo0OOoOoO0 , addon_id ) . replace ( oo0oO , name ) . replace ( oOo0 , provider_name ) . replace ( iiIiIiII , contenttypes )
  if 28 - 28: I1ii11iIi11i . i1IIi
  iIIiooO00O00oOO = open ( IiII1i1iii1Ii , mode = 'w+' )
  iIIiooO00O00oOO . write ( str ( i1I1 ) )
  iIIiooO00O00oOO . close ( )
  if 40 - 40: oOoO0o00OO0 . ooOo + I1IiiI + I1ii11iIi11i + OOo00O0
  i11Ii1I1I11I = open ( iIO0O00OOo , mode = 'w' )
  i11Ii1I1I11I . write ( 'import xbmcplugin,xbmcgui,xbmc,xbmcaddon,os,sys\nAddonID="' + addon_id + '"\nAddonName="' + name + '"\ndialog=xbmcgui.Dialog()\nxbmc.executebuiltin("UpdateLocalAddons")\nxbmc.executebuiltin("UpdateAddonRepos")\nchoice=dialog.yesno(AddonName+" Add-on Requires Update","This add-on may still be in the process of the updating. We recommend waiting but if you\'ve already tried that and it\'s not updating you can try re-installing via the CP backup method.",yeslabel="Install Option 2", nolabel="Wait...")\nif choice == 1: xbmc.executebuiltin(\'ActivateWindow(10001,"plugin://plugin.program.totalinstaller/?mode=grab_addons&url=%26redirect%26addonid%3d\'+AddonID+\'")\')\nxbmcplugin.endOfDirectory(int(sys.argv[1]))' )
  i11Ii1I1I11I . close ( )
  if 29 - 29: OoooooooOO . I1IiiI % I1ii11iIi11i - oOoO0o00OO0
  xbmc . sleep ( 1000 )
  if 8 - 8: i1IIi
  if os . path . exists ( O0000 ) and O0O0ooOOO == 0 :
   OOo = 'http://noobsandnerds.com/TI/AddonPortal/downloadcount.php?id=%s' % ( addon_id )
   ooI1111i ( OOo )
   if 32 - 32: ooOo / II111iiii
  xbmc . executebuiltin ( 'UpdateLocalAddons' )
  xbmc . executebuiltin ( 'UpdateAddonRepos' )
  OooO0 . ok ( name + " Install Complete" , '[COLOR=dodgerblue]' + name + '[/COLOR] has now been installed, please allow a few moments for Kodi to update the add-on and it\'s dependencies.' )
  if 45 - 45: I1ii11iIi11i + OoO0O00 * i11iIiiIii / Oo % iii * O0
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 17 - 17: O0
 if 88 - 88: Oo0Ooo . O0 % OoooooooOO / Oo
def ooOoo0oO0OoO0 ( name , contenttypes , repo_link , repo_id , addon_id , provider_name , forum , data_path ) :
 ooOoO = xbmc . translatePath ( os . path . join ( O00o0OO , repo_id ) )
 O0000 = xbmc . translatePath ( os . path . join ( O00o0OO , addon_id ) )
 if 70 - 70: ooOo - ooOo
 if os . path . exists ( O0000 ) :
  if 57 - 57: I1IiiI - o0oOOo0O0Ooo + OoO0O00 % Oo0Ooo
  iIi1IiI = OooO0 . yesno ( 'Add-on Already Installed' , 'This add-on has already been detected on your system. Would you like to remove the old version and re-install? There should be no need for this unless you\'ve manually opened up the add-on code and edited in a text editor.' )
  if 26 - 26: oOoO0o00OO0 . oOoO0o00OO0
  if iIi1IiI == 1 :
   o0OO000ooOo ( O0000 )
   if 35 - 35: OOo00O0 . OoOoOO00 * i11iIiiIii
 if os . path . exists ( ooOoO ) :
  if 44 - 44: i11iIiiIii / Oo0Ooo
  if os . path . exists ( O0000 ) :
   O0O0ooOOO = 1
   if 42 - 42: OoooooooOO + Oo0Ooo % II111iiii + OoO0O00
  else :
   O0O0ooOOO = 0
   if 24 - 24: oOoO0o00OO0 * II111iiii % oOoO0o00OO0 % iI1iiIiiII + OoooooooOO
  iIi1IiI = OooO0 . yesno ( 'WARNING!' , '[COLOR=orange]This Add-on may be unlawful in your region.[/COLOR][CR]The repository required for installation of this add-on has been detected on your system. Would you like to continue to the Kodi addon browser to install?' )
  if 29 - 29: II111iiii - OoooooooOO - i11iIiiIii . o0oOOo0O0Ooo
  if iIi1IiI == 1 :
   if 19 - 19: II111iiii
   if 'video' in contenttypes :
    xbmc . executebuiltin ( 'ActivateWindow(10040,"addons://' + repo_id + '/xbmc.addon.video/?",return)' )
    if 72 - 72: OoooooooOO / I1IiiI + OoO0 / OoOoOO00 * OoO0
   elif 'executable' in contenttypes :
    xbmc . executebuiltin ( 'ActivateWindow(10040,"addons://' + repo_id + '/xbmc.addon.executable/?",return)' )
    if 34 - 34: O0 * O0 % OoooooooOO + oOoO0o00OO0 * iIii1I11I1II1 % OoO0
   elif 'audio' in contenttypes :
    xbmc . executebuiltin ( 'ActivateWindow(10040,"addons://' + repo_id + '/xbmc.addon.audio/?",return)' )
    if 25 - 25: iii + OoOoOO00 . o0oOOo0O0Ooo % OoOoOO00 * Oo
  xbmc . sleep ( 2000 )
  if 32 - 32: i11iIiiIii - OOo00O0
  if os . path . exists ( O0000 ) and O0O0ooOOO == 0 :
   OOo = 'http://noobsandnerds.com/TI/AddonPortal/downloadcount.php?id=%s' % ( addon_id )
   ooI1111i ( OOo )
   if 53 - 53: OoooooooOO - iI1iiIiiII
 else :
  OooO0 . ok ( 'WARNING!' , '[COLOR=orange]This add-on may possibly be unlawful in your region.[/COLOR][CR]If you\'ve investigated the legality of it and are happy to install then you must have the following repository installed: [COLOR=dodgerblue]' + repo_id + '[/COLOR]' )
  if 87 - 87: ooOo . I1IiiI
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 17 - 17: OoO0 . i11iIiiIii
 if 5 - 5: I1ii11iIi11i + O0 + O0 . OOo00O0 - iIII
def o00oo0000 ( name , contenttypes , repo_link , repo_id , addon_id , provider_name , forum , data_path ) :
 OooO0 . ok ( 'Add-on Not Approved' , 'Sorry there are no repository details for this add-on and it\'s been marked as potentially giving access to unlawful content. The most likely cause for this is the add-on has only been released via social media groups.' )
 if 44 - 44: Oo0Ooo % iIii1I11I1II1
 if 90 - 90: II111iiii + OoooooooOO % OoooooooOO
def I11Ii ( ) :
 OOo0oO00ooO00 ( '' , o0OOO + ' Storage Folder Check' , 'url' , 'check_storage' , 'Check_Download.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Completely remove an add-on (inc. passwords)' , 'plugin' , 'addon_removal_menu' , 'Remove_Addon.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Make Add-ons Gotham/Helix Compatible' , 'none' , 'gotham' , 'Gotham_Compatible.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Make Skins Kodi (Helix) Compatible' , 'none' , 'helix' , 'Kodi_Compatible.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Hide my add-on passwords' , 'none' , 'hide_passwords' , 'Hide_Passwords.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Test My Download Speed' , 'none' , 'speedtest_menu' , 'Speed_Test.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Unhide my add-on passwords' , 'none' , 'unhide_passwords' , 'Unhide_Passwords.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Update My Add-ons (Force Refresh)' , 'none' , 'update' , 'Update_Addons.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Wipe All Add-on Settings (addon_data)' , 'url' , 'remove_addon_data' , 'Delete_Addon_Data.png' , '' , '' , '' )
 if 16 - 16: Oo0Ooo / i11iIiiIii
 if 64 - 64: i11iIiiIii / OoO0 * i1IIi
def OOOOOOoO ( sign ) :
 OOo0oO00ooO00 ( 'folder' , '[COLOR=darkcyan][Manual Search][/COLOR] Search By Name' , 'name=' , 'search_addons' , 'Search_Addons.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=darkcyan][Manual Search][/COLOR] Search By Author' , 'author=' , 'search_addons' , 'Search_Addons.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=darkcyan][Manual Search][/COLOR] Search In Description' , 'desc=' , 'search_addons' , 'Search_Addons.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=darkcyan][Manual Search][/COLOR] Search By Add-on ID' , 'addonid=' , 'search_addons' , 'Search_Addons.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][Filter Results][/COLOR] By Genres' , 'p' , 'addon_genres' , 'Search_Genre.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][Filter Results][/COLOR] By Countries' , 'p' , 'addon_countries' , 'Search_Country.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue][Filter Results][/COLOR] By Kodi Categories' , 'p' , 'addon_categories' , 'Search_Category.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=orange][Kodi Add-on Browser][/COLOR] Install From Zip' , '' , 'install_from_zip' , 'Search_Addons.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=orange][Kodi Add-on Browser][/COLOR] Browse My Repositories' , '' , 'browse_repos' , 'Search_Addons.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=orange][Kodi Add-on Browser][/COLOR] Check For Add-on Updates' , '' , 'check_updates' , 'Search_Addons.png' , '' , '' , '' )
 if 12 - 12: oOoO0o00OO0 . iI1iiIiiII . OoOoOO00 / O0
 if 58 - 58: o0oOOo0O0Ooo - II111iiii % ooOo + OOo00O0 . OoOoOO00 / iI1iiIiiII
def IIo00ooo ( ) :
 for file in glob . glob ( os . path . join ( O00o0OO , '*' ) ) :
  I1ii1 = str ( file ) . replace ( O00o0OO , '[COLOR=red]REMOVE [/COLOR]' ) . replace ( 'plugin.' , '[COLOR=dodgerblue](PLUGIN) [/COLOR]' ) . replace ( 'audio.' , '' ) . replace ( 'video.' , '' ) . replace ( 'skin.' , '[COLOR=yellow](SKIN) [/COLOR]' ) . replace ( 'repository.' , '[COLOR=orange](REPOSITORY) [/COLOR]' ) . replace ( 'script.' , '[COLOR=cyan](SCRIPT) [/COLOR]' ) . replace ( 'metadata.' , '[COLOR=orange](METADATA) [/COLOR]' ) . replace ( 'service.' , '[COLOR=pink](SERVICE) [/COLOR]' ) . replace ( 'weather.' , '[COLOR=green](WEATHER) [/COLOR]' ) . replace ( 'module.' , '[COLOR=orange](MODULE) [/COLOR]' )
  Ii1IiIiIi1IiI = ( os . path . join ( file , 'icon.png' ) )
  i1iiIIi1I = ( os . path . join ( file , 'fanart.jpg' ) )
  OOo0oO00ooO00 ( '' , I1ii1 , file , 'remove_addons' , Ii1IiIiIi1IiI , i1iiIIi1I , '' , '' )
  if 36 - 36: I1IiiI * Oo0Ooo
  if 77 - 77: ooOo % i1IIi - OoO0
def oOO00OO0ooo0o ( ) :
 o0O . openSettings ( sys . argv [ 0 ] )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 83 - 83: I1ii11iIi11i / OOo00O0 - i11iIiiIii . iIii1I11I1II1 + Oo0Ooo
 if 59 - 59: O0 % Oo0Ooo
def O0o00O0Oo0 ( sourcefile , destfile , message_header , message1 , message2 , message3 , exclude_dirs , exclude_files ) :
 o0I11iII = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 IiiIiI = len ( sourcefile )
 iIIIIiiIii = [ ]
 ooO0oo = [ ]
 if 56 - 56: OoooooooOO - iii - i1IIi
 II11iiii1Ii . create ( message_header , message1 , message2 , message3 )
 if 8 - 8: OOo00O0 / Oo . I1IiiI + I1ii11iIi11i / i11iIiiIii
 for I1Iii1iI1 , o0Oo0oOooOoOo , I1i in os . walk ( sourcefile ) :
  if 59 - 59: OoooooooOO . OoO0 / O0 - Oo
  for file in I1i :
   ooO0oo . append ( file )
   if 1 - 1: iI1iiIiiII / iI1iiIiiII - i11iIiiIii
 OO0oIiII1iiI = len ( ooO0oo )
 if 34 - 34: I1IiiI . ooOo + i1IIi
 for I1Iii1iI1 , o0Oo0oOooOoOo , I1i in os . walk ( sourcefile ) :
  if 98 - 98: ooOo % iI1iiIiiII * i11iIiiIii % I1ii11iIi11i
  o0Oo0oOooOoOo [ : ] = [ iIiI1IIiii11 for iIiI1IIiii11 in o0Oo0oOooOoOo if iIiI1IIiii11 not in exclude_dirs ]
  I1i [ : ] = [ IiI1 for IiI1 in I1i if IiI1 not in exclude_files and not 'crashlog' in IiI1 and not 'stacktrace' in IiI1 ]
  if 87 - 87: o0oOOo0O0Ooo % iIii1I11I1II1
  for file in I1i :
   if 100 - 100: OOo00O0 . I1IiiI * OOo00O0 - I1IiiI . iii * OoO0
   try :
    iIIIIiiIii . append ( file )
    oO000o = len ( iIIIIiiIii ) / float ( OO0oIiII1iiI ) * 100
    II11iiii1Ii . update ( 0 , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % iIiI1IIiii11 , 'Please Wait' )
    o0Oo = os . path . join ( I1Iii1iI1 , file )
    if 57 - 57: Oo / Oo0Ooo
   except :
    print "Unable to backup file: " + file
    if 69 - 69: ooOo - Oo0Ooo % iI1iiIiiII
   if not 'temp' in o0Oo0oOooOoOo :
    if 50 - 50: OoooooooOO
    if not I1IiI in o0Oo0oOooOoOo :
     if 4 - 4: II111iiii . iii + OoO0 * OOo00O0 . iIII
     try :
      oOoOo = '01/01/1980'
      oO0OO = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( o0Oo ) ) )
      if 88 - 88: OoOoOO00 - i11iIiiIii % o0oOOo0O0Ooo * iii + I1ii11iIi11i
      if oO0OO > oOoOo :
       o0I11iII . write ( o0Oo , o0Oo [ IiiIiI : ] )
       if 52 - 52: II111iiii . I1IiiI + OoOoOO00 % OoO0O00
     except :
      print "Unable to backup file: " + file
      if 62 - 62: o0oOOo0O0Ooo
 o0I11iII . close ( )
 II11iiii1Ii . close ( )
 if 15 - 15: iii + OoO0 . Oo * OoO0O00 . OoOoOO00
 if 18 - 18: i1IIi % II111iiii + OOo00O0 % OoO0
def oOO ( sourcefile , destfile ) :
 o0I11iII = zipfile . ZipFile ( destfile , 'w' , zipfile . ZIP_DEFLATED )
 IiiIiI = len ( sourcefile )
 iIIIIiiIii = [ ]
 ooO0oo = [ ]
 if 53 - 53: o0oOOo0O0Ooo % Oo0Ooo * Oo0Ooo
 II11iiii1Ii . create ( "Backing Up Files" , "Archiving..." , '' , 'Please Wait' )
 if 77 - 77: Oo - iI1iiIiiII . iii / I1IiiI + OoO0O00 % ooOo
 for I1Iii1iI1 , o0Oo0oOooOoOo , I1i in os . walk ( sourcefile ) :
  if 12 - 12: i1IIi
  for file in I1i :
   ooO0oo . append ( file )
   if 63 - 63: iI1iiIiiII + o0oOOo0O0Ooo
 OO0oIiII1iiI = len ( ooO0oo )
 if 1 - 1: I1ii11iIi11i / OoO0O00 + ooOo . o0oOOo0O0Ooo / I1ii11iIi11i - oOoO0o00OO0
 for I1Iii1iI1 , o0Oo0oOooOoOo , I1i in os . walk ( sourcefile ) :
  if 5 - 5: Oo
  for file in I1i :
   iIIIIiiIii . append ( file )
   oO000o = len ( iIIIIiiIii ) / float ( OO0oIiII1iiI ) * 100
   II11iiii1Ii . update ( int ( oO000o ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
   o0Oo = os . path . join ( I1Iii1iI1 , file )
   if 4 - 4: oOoO0o00OO0 % OOo00O0 / OoO0O00 . Oo / Oo - I1ii11iIi11i
   if not 'temp' in o0Oo0oOooOoOo :
    if 79 - 79: I1ii11iIi11i + OOo00O0
    if not I1IiI in o0Oo0oOooOoOo :
     if 10 - 10: Oo0Ooo + O0
     import time
     oOoOo = '01/01/1980'
     oO0OO = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( o0Oo ) ) )
     if 43 - 43: iIii1I11I1II1 / II111iiii % o0oOOo0O0Ooo - Oo
     if oO0OO > oOoOo :
      o0I11iII . write ( o0Oo , o0Oo [ IiiIiI : ] )
 o0I11iII . close ( )
 II11iiii1Ii . close ( )
 if 62 - 62: iii
 if 63 - 63: Oo + iIII * ooOo / o0oOOo0O0Ooo / Oo0Ooo * iIii1I11I1II1
def OOoO00ooO ( ) :
 OOo0oO00ooO00 ( '' , '[COLOR=orange][INSTRUCTIONS][/COLOR] How to create and share my build' , '' , 'instructions_1' , 'Backup.png' , '' , '' , 'Back Up Your Full System' )
 OOo0oO00ooO00 ( '' , '[COLOR=gold]Create My Own [/COLOR][COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] [COLOR=gold]Community Build[/COLOR]' , 'url' , 'community_backup' , 'Backup.png' , '' , '' , 'Back Up Your Full System' )
 if I1IIIIiii1i ( ) :
  OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue]Create OpenELEC Backup[/COLOR] (full backup can only be used on OpenELEC)' , 'none' , 'openelec_backup' , 'Backup.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue]Create My Own Universal Build[/COLOR] (For copying to other devices)' , 'none' , 'community_backup_2' , 'Backup.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue]Create My Own Full Backup[/COLOR] (will only work on THIS device)' , 'local' , 'local_backup' , 'Backup.png' , '' , '' , 'Back Up Your Full System' )
 OOo0oO00ooO00 ( '' , 'Backup Addons Only' , 'addons' , 'restore_zip' , 'Backup.png' , '' , '' , 'Back Up Your Addons' )
 OOo0oO00ooO00 ( '' , 'Backup Addon Data Only' , 'addon_data' , 'restore_zip' , 'Backup.png' , '' , '' , 'Back Up Your Addon Userdata' )
 OOo0oO00ooO00 ( '' , 'Backup Guisettings.xml' , I11II1i , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your guisettings.xml' )
 if 51 - 51: Oo . I1IiiI
 if os . path . exists ( I1I1i ) :
  OOo0oO00ooO00 ( '' , 'Backup Favourites.xml' , I1I1i , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your favourites.xml' )
  if 73 - 73: OoooooooOO . I1IiiI / OOo00O0 % OoO0
 if os . path . exists ( oOOOoo0O0OoO ) :
  OOo0oO00ooO00 ( '' , 'Backup Source.xml' , oOOOoo0O0OoO , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your sources.xml' )
  if 65 - 65: iI1iiIiiII - I1IiiI - OoO0
 if os . path . exists ( ii1i1I1i ) :
  OOo0oO00ooO00 ( '' , 'Backup Advancedsettings.xml' , ii1i1I1i , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your advancedsettings.xml' )
  if 42 - 42: II111iiii * I1IiiI % i1IIi - OoO0 % iI1iiIiiII
 if os . path . exists ( iIii11I ) :
  OOo0oO00ooO00 ( '' , 'Backup Advancedsettings.xml' , iIii11I , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your keyboard.xml' )
  if 36 - 36: i11iIiiIii / ooOo * I1ii11iIi11i * I1ii11iIi11i + OoO0 * iii
 if os . path . exists ( oOoo ) :
  OOo0oO00ooO00 ( '' , 'Backup RssFeeds.xml' , oOoo , 'restore_backup' , 'Backup.png' , '' , '' , 'Back Up Your RssFeeds.xml' )
  if 32 - 32: OoO0O00
  if 50 - 50: iIII + i1IIi
def i11IiIIi11I ( ) :
 OOo0oO00ooO00 ( 'folder' , 'Backup My Content' , 'none' , 'backup_option' , 'Backup.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Restore My Content' , 'none' , 'restore_option' , 'Restore.png' , '' , '' , '' )
 if 78 - 78: iI1iiIiiII
 if 83 - 83: iIii1I11I1II1 % OoOoOO00 % o0oOOo0O0Ooo % OOo00O0 . I1ii11iIi11i % O0
def iIiIi1ii ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(10040,"addons://repos/",return)' )
 if 28 - 28: iIii1I11I1II1 + iIii1I11I1II1
 if 28 - 28: ooOo
def ooo0oo ( localbuildcheck , localversioncheck , id , welcometext ) :
 if ( o0oOoO00o . replace ( '%20' , ' ' ) in welcometext ) and ( 'elc' in welcometext ) :
  OOo0oO00ooO00 ( '' , welcometext , 'show' , 'user_info' , 'noobsandnerds.png' , '' , '' , '' )
  if 8 - 8: OoO0O00 + OoOoOO00 . iIii1I11I1II1 % O0
  if id != 'None' :
   if 43 - 43: I1ii11iIi11i - oOoO0o00OO0
   if id != 'Local' :
    O000O = Oo00OO0 ( localbuildcheck , localversioncheck , id )
    if 72 - 72: i1IIi / ooOo * OOo00O0
    if O000O == True :
     if 40 - 40: OoO0 - OoOoOO00 * OoOoOO00 . OoOoOO00 + OoooooooOO
     if not 'Partially installed' in localbuildcheck :
      OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]' + localbuildcheck + ':[/COLOR] [COLOR=lime]NEW VERSION AVAILABLE[/COLOR]' , id , 'showinfo' , 'noobsandnerds.png' , '' , '' , '' )
      if 77 - 77: iIii1I11I1II1 . OoO0 % ooOo / OoO0
     if '(Partially installed)' in localbuildcheck :
      OOo0oO00ooO00 ( 'folder' , '[COLOR=lime]Current Build Installed: [/COLOR][COLOR=dodgerblue]' + localbuildcheck + '[/COLOR]' , id , 'showinfo2' , 'noobsandnerds.png' , '' , '' , '' )
    else :
     OOo0oO00ooO00 ( 'folder' , '[COLOR=lime]Current Build Installed: [/COLOR][COLOR=dodgerblue]' + localbuildcheck + '[/COLOR]' , id , 'showinfo' , 'noobsandnerds.png' , '' , '' , '' )
     if 54 - 54: ooOo + iIII - Oo0Ooo
   else :
    if 35 - 35: OoO0 - OoO0 + i1IIi - O0 - OOo00O0
    if localbuildcheck == 'Incomplete' :
     OOo0oO00ooO00 ( '' , '[COLOR=lime]Your last restore is not yet completed[/COLOR]' , 'url' , oOO0o0oo0 ( ) , 'noobsandnerds.png' , '' , '' , '' )
     if 78 - 78: Oo + oOoO0o00OO0 . iI1iiIiiII
    else :
     OOo0oO00ooO00 ( '' , '[COLOR=lime]Current Build Installed: [/COLOR][COLOR=dodgerblue]Local Build (' + localbuildcheck + ')[/COLOR]' , 'noobsandnerds.png' , '' , '' , '' , '' , '' )
  OOo0oO00ooO00 ( '' , '[COLOR=orange]---------------------------------------[/COLOR]' , 'None' , '' , 'noobsandnerds.png' , '' , '' , '' )
  if 91 - 91: iIii1I11I1II1 . o0oOOo0O0Ooo . I1ii11iIi11i + OoooooooOO
 if o0oOoO00o != '' and i1 != '' and not 'elc' in welcometext :
  OOo0oO00ooO00 ( '' , '[COLOR=lime]Unable to login, please check your details[/COLOR]' , 'None' , 'addon_settings' , 'noobsandnerds.png' , '' , '' , '' )
  if 69 - 69: OOo00O0 - I1IiiI
 if not 'elc' in welcometext :
  OOo0oO00ooO00 ( '' , welcometext , 'None' , 'register' , 'noobsandnerds.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=yellow]Settings[/COLOR]' , 'settings' , 'addon_settings' , 'SETTINGS.png' , '' , '' , '' )
 if 95 - 95: I1IiiI * i11iIiiIii . iIII
 if 41 - 41: II111iiii
 if 37 - 37: iii . Oo0Ooo % iI1iiIiiII * i1IIi
 if 71 - 71: Oo0Ooo / o0oOOo0O0Ooo + Oo
 if 48 - 48: OOo00O0 + oOoO0o00OO0
 if 16 - 16: iIii1I11I1II1 % i11iIiiIii . OoOoOO00 % iIII + ooOo . OoO0O00
 if 46 - 46: OoO0O00 - o0oOOo0O0Ooo / OoOoOO00 - OoooooooOO + ooOo
 OOo0oO00ooO00 ( 'folder' , 'Install Content' , welcometext , 'install_content' , 'Search_Addons.png' , '' , '' , '' )
 if 58 - 58: o0oOOo0O0Ooo / o0oOOo0O0Ooo + iIII + iii - OoOoOO00 . Oo
 if Oo0o0000o0o0 == 'true' :
  OOo0oO00ooO00 ( 'folder' , 'Hardware Reviews' , 'none' , 'hardware_root_menu' , 'hardware.png' , '' , '' , '' )
  if 15 - 15: iIII * OoOoOO00 % iI1iiIiiII . OoOoOO00 . iii
 if oO0o0o0ooO0oO == 'true' :
  OOo0oO00ooO00 ( 'folder' , 'Latest News' , 'none' , 'news_root_menu' , 'LatestNews.png' , '' , '' , '' )
  if 97 - 97: ooOo
 if oo0o0O00 == 'true' :
  OOo0oO00ooO00 ( 'folder' , 'Tutorials' , '' , 'tutorial_root_menu' , 'Tutorials.png' , '' , '' , '' )
  if 80 - 80: I1IiiI . OoO0
 if oOo0oooo00o == 'true' :
  OOo0oO00ooO00 ( 'folder' , 'Maintenance' , 'none' , 'tools' , 'Additional_Tools.png' , '' , '' , '' )
  if 47 - 47: iii + iIII + II111iiii % i11iIiiIii
  if 93 - 93: I1ii11iIi11i % OoOoOO00 . O0 / oOoO0o00OO0 * ooOo
def i1iii1ii ( ) :
 II1 = 'defaultskindependecycheck'
 if os . path . exists ( O0o0O00Oo0o0 ) :
  shutil . rmtree ( O0o0O00Oo0o0 )
  if 27 - 27: OoO0 + I1IiiI * iIii1I11I1II1 . OoooooooOO * OoOoOO00
 if not os . path . exists ( O0o0O00Oo0o0 ) :
  os . makedirs ( O0o0O00Oo0o0 )
  if 100 - 100: OoO0O00 / i1IIi - I1IiiI % OoO0 - iIii1I11I1II1
  if 17 - 17: iii / o0oOOo0O0Ooo % Oo0Ooo
  if 71 - 71: iI1iiIiiII . OOo00O0 . OoO0O00
 if o00OO00OoO != 'skin.confluence' :
  Oo0O0O00Oo = os . path . join ( O00o0OO , o00OO00OoO , 'addon.xml' )
  I111Ii = open ( Oo0O0O00Oo , mode = 'r' )
  II11 = I111Ii . read ( )
  I111Ii . close ( )
  if 2 - 2: iIii1I11I1II1
  iiii1 = re . compile ( '<requires[\s\S]*?\/requires' ) . findall ( II11 )
  II1 = iiii1 [ 0 ] if ( len ( iiii1 ) > 0 ) else 'None'
  if 66 - 66: ooOo * iIii1I11I1II1 % iIii1I11I1II1 * iI1iiIiiII - iIII - iI1iiIiiII
 o0O0oO0 = ooI1111i ( 'http://noobsandnerds.com/TI/AddonPortal/approved.php' )
 if 77 - 77: O0 . OoO0
 II11iiii1Ii . create ( 'Backing Up Add-ons' , '' , 'Please Wait...' )
 if 39 - 39: iIII . II111iiii
 for I1ii1 in os . listdir ( O00o0OO ) :
  if 45 - 45: ooOo * OoOoOO00 / iIii1I11I1II1
  if 77 - 77: OOo00O0 - iii
  if not 'totalinstaller' in I1ii1 and not 'plugin.program.tbs' in I1ii1 and not 'packages' in I1ii1 and os . path . isdir ( os . path . join ( O00o0OO , I1ii1 ) ) :
   if 11 - 11: I1ii11iIi11i
   if 26 - 26: iIii1I11I1II1 * OOo00O0 - Oo
   if I1ii1 in o0O0oO0 and not I1ii1 in II1 and not 'script.' in I1ii1 and not 'repo.' in I1ii1 and not 'repository.' in I1ii1 and os . path . isdir ( os . path . join ( O00o0OO , I1ii1 ) ) :
    if 27 - 27: I1ii11iIi11i * OOo00O0 - OoO0O00 + OoO0 * OoO0
    if 55 - 55: iIII
    if not 'service.xbmc.versioncheck' in I1ii1 and not 'packages' in I1ii1 and os . path . isdir ( os . path . join ( O00o0OO , I1ii1 ) ) :
     if 82 - 82: OOo00O0 - Oo + OoO0O00
     try :
      II11iiii1Ii . update ( 0 , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % I1ii1 , 'Please Wait...' )
      os . makedirs ( os . path . join ( O0o0O00Oo0o0 , I1ii1 ) )
      if 64 - 64: o0oOOo0O0Ooo . O0 * OoO0 + OoooooooOO - Oo0Ooo . OoooooooOO
      IiII1i1iii1Ii = os . path . join ( O0o0O00Oo0o0 , I1ii1 , 'addon.xml' )
      iIO0O00OOo = os . path . join ( O0o0O00Oo0o0 , I1ii1 , 'default.py' )
      IIi1I = open ( os . path . join ( O00o0OO , I1ii1 , 'addon.xml' ) , mode = 'r' )
      iiiO00O00O000OOO = IIi1I . read ( )
      IIi1I . close ( )
      if 70 - 70: Oo0Ooo - ooOo . iIii1I11I1II1 % iii / OoOoOO00 - O0
      i1iiiIii11 = re . compile ( ' name="(.+?)"' ) . findall ( iiiO00O00O000OOO )
      OOoOOO000O0 = re . compile ( 'provider-name="(.+?)"' ) . findall ( iiiO00O00O000OOO )
      o0O0oo0o = re . compile ( '<addon[\s\S]*?">' ) . findall ( iiiO00O00O000OOO )
      II11iI1iiI = re . compile ( '<description[\s\S]*?<\/description>' ) . findall ( iiiO00O00O000OOO )
      oo0oO = i1iiiIii11 [ 0 ] if ( len ( i1iiiIii11 ) > 0 ) else 'None'
      oOo0OOoO0 = OOoOOO000O0 [ 0 ] if ( len ( OOoOOO000O0 ) > 0 ) else 'Anonymous'
      I1 = o0O0oo0o [ 0 ] if ( len ( o0O0oo0o ) > 0 ) else 'None'
      i1i1iI1iiiI = II11iI1iiI [ 0 ] if ( len ( II11iI1iiI ) > 0 ) else 'None'
      if 14 - 14: I1IiiI . OoO0
      i1iI1i1I1 = '<addon id="' + I1ii1 + '" name="' + oo0oO + '" version="0" provider-name="' + oOo0OOoO0 + '">'
      I1iii = '<description>If you\'re seeing this message it means the add-on is still updating, please wait for the update process to complete.</description>'
      if 99 - 99: iIII / iIii1I11I1II1 - OoO0 * I1ii11iIi11i % I1IiiI
      if I1 != 'None' :
       i1I1 = iiiO00O00O000OOO . replace ( i1i1iI1iiiI , I1iii ) . replace ( I1 , i1iI1i1I1 )
       if 13 - 13: OoO0O00
      else :
       i1I1 = iiiO00O00O000OOO . replace ( i1i1iI1iiiI , I1iii )
       if 70 - 70: OOo00O0 + O0 . ooOo * OoO0
      iIIiooO00O00oOO = open ( IiII1i1iii1Ii , mode = 'w+' )
      iIIiooO00O00oOO . write ( str ( i1I1 ) )
      iIIiooO00O00oOO . close ( )
      i11Ii1I1I11I = open ( iIO0O00OOo , mode = 'w+' )
      i11Ii1I1I11I . write ( 'import xbmcplugin,xbmcgui,xbmc,xbmcaddon,os,sys\nAddonID="' + I1ii1 + '"\nAddonName="' + oo0oO + '"\ndialog=xbmcgui.Dialog()\ndialog.ok(AddonName+" Add-on Requires Update","This add-on may still be in the process of the updating so we recommend waiting a few minutes to see if it updates naturally. If it hasn\'t updated after 5mins please try reinstalling via the Community Portal add-on")\nxbmcplugin.endOfDirectory(int(sys.argv[1]))' )
      i11Ii1I1I11I . close ( )
      if 2 - 2: OoooooooOO . Oo . iI1iiIiiII
     except :
      print "### Failed to backup: " + I1ii1
      if 42 - 42: Oo % ooOo / OoO0O00 - ooOo * i11iIiiIii
      if 19 - 19: ooOo * I1IiiI % i11iIiiIii
   else :
    shutil . copytree ( os . path . join ( O00o0OO , I1ii1 ) , os . path . join ( O0o0O00Oo0o0 , I1ii1 ) )
    if 24 - 24: o0oOOo0O0Ooo
 II11iiii1Ii . close ( )
 if 10 - 10: o0oOOo0O0Ooo % OoO0 / Oo
 i11Ii1iIiII = "Creating Backup"
 O0oOo00Ooo0o0 = "Archiving..."
 i1IiII1i1I = ""
 iI1ii1ii1I = "Please Wait"
 if 18 - 18: ooOo * ooOo % ooOo
 O0o00O0Oo0 ( O0o0O00Oo0o0 , O00O0oOO00O00 , i11Ii1iIiII , O0oOo00Ooo0o0 , i1IiII1i1I , iI1ii1ii1I , '' , '' )
 if 17 - 17: O0 * OoOoOO00 * I1ii11iIi11i * II111iiii * iii % i1IIi
 try :
  shutil . rmtree ( O0o0O00Oo0o0 )
  if 33 - 33: I1ii11iIi11i * I1ii11iIi11i . iIII . i11iIiiIii
 except :
  print "### COMMUNITY BUILDS: Failed to remove temp addons folder - manual delete required ###"
  if 48 - 48: o0oOOo0O0Ooo . OoO0 + OoOoOO00 % I1ii11iIi11i / i11iIiiIii
  if 74 - 74: II111iiii . O0 - I1IiiI + iI1iiIiiII % i11iIiiIii % OoOoOO00
def O0OOO0 ( url ) :
 II11iiii1Ii . create ( 'Cleaning Temp Paths' , '' , 'Please wait...' )
 if os . path . exists ( O0o0O00Oo0o0 ) :
  shutil . rmtree ( O0o0O00Oo0o0 )
  if 8 - 8: i11iIiiIii / II111iiii + o0oOOo0O0Ooo * OoO0 % iI1iiIiiII . iii
 if not os . path . exists ( O0o0O00Oo0o0 ) :
  os . makedirs ( O0o0O00Oo0o0 )
  if 6 - 6: iI1iiIiiII % Oo0Ooo . Oo0Ooo - I1ii11iIi11i / iii . i1IIi
 oOOO ( O00O0oOO00O00 , O0o0O00Oo0o0 )
 if 99 - 99: OoOoOO00 . OOo00O0
 for I1ii1 in os . listdir ( O0o0O00Oo0o0 ) :
  if 59 - 59: iii / Oo0Ooo / Oo / O0 / OoOoOO00 + o0oOOo0O0Ooo
  if not 'totalinstaller' in I1ii1 and not 'plugin.program.tbs' in I1ii1 :
   if not os . path . exists ( os . path . join ( O00o0OO , I1ii1 ) ) :
    os . rename ( os . path . join ( O0o0O00Oo0o0 , I1ii1 ) , os . path . join ( O00o0OO , I1ii1 ) )
    II11iiii1Ii . update ( 0 , "Installing: [COLOR=yellow]" + I1ii1 + '[/COLOR]' , '' , 'Please wait...' )
    print "### Successfully installed: " + I1ii1
    if 13 - 13: o0oOOo0O0Ooo % ooOo / OOo00O0 % OOo00O0 % O0
   else :
    print "### " + I1ii1 + " Already exists on system"
    if 90 - 90: iI1iiIiiII . iIII / iIii1I11I1II1
    if 28 - 28: iI1iiIiiII + ooOo - iIII / iIii1I11I1II1 - I1IiiI
def Ii1i1 ( welcometext ) :
 oOoO00 ( 'disclaimer.xml' )
 if ooOoOoo0O == 'true' :
  OOo0oO00ooO00 ( 'folder' , 'I have read and understand the disclaimer.' , welcometext , 'CB_Menu' , 'Community_Builds.png' , '' , '' , '' )
 else :
  OOo0oO00ooO00 ( 'folder' , 'I have read and understand the disclaimer.' , 'welcome' , 'CB_Menu' , 'Community_Builds.png' , '' , '' , '' )
  if 45 - 45: OoO0 . OoooooooOO
  if 27 - 27: OoO0 * Oo0Ooo . OoOoOO00
def Ii111Iiiii ( welcometext ) :
 iIii = xbmc . getInfoLabel ( "System.BuildVersion" )
 iii1IIiI = float ( iIii [ : 2 ] )
 IiIiIi = int ( iii1IIiI )
 print "#### Welcome: " + welcometext
 if iI1Ii11111iIi == 'true' :
  if 33 - 33: iii
  if i1i1II == 'true' :
   oOo00OoO0O ( 'yes' )
   if 69 - 69: iIii1I11I1II1 * I1IiiI - oOoO0o00OO0 + O0 + O0
  if i1i1II == 'false' :
   oOo00OoO0O ( 'no' )
   if 65 - 65: OOo00O0 / i11iIiiIii / OoO0O00 - Oo
 if not 'elc' in welcometext :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]To access community builds you must be logged in[/COLOR]' , 'settings' , 'addon_settings' , 'noobsandnerds.png' , '' , '' , 'Register at [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR]' )
  if 9 - 9: I1IiiI / OOo00O0 - Oo0Ooo * iIii1I11I1II1
 if IiII == 'true' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Show My Private List[/COLOR]' , '&visibility=private' , 'grab_builds' , 'Private_builds.png' , '' , '' , '' )
  if 86 - 86: II111iiii + iIII + iI1iiIiiII
 if ( ( o0oOoO00o . replace ( '%20' , ' ' ) in welcometext ) and ( 'elc' in welcometext ) ) :
  if 9 - 9: iIII + II111iiii % iIII % iI1iiIiiII + iIii1I11I1II1
  if ( IiIiIi < 14 ) or ( oOOoo00O0O == 'true' ) :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Show All Gotham Compatible Builds[/COLOR]' , '&xbmc=gotham&visibility=public' , 'grab_builds' , 'TRCOMMUNITYGOTHAMBUILDS.png' , '' , '' , '' )
   if 59 - 59: i1IIi
  if ( IiIiIi == 14 ) or ( oOOoo00O0O == 'true' ) :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Show All Helix Compatible Builds[/COLOR]' , '&xbmc=helix&visibility=public' , 'grab_builds' , 'TRCOMMUNITYHELIXBUILDS.png' , '' , '' , '' )
   if 48 - 48: O0 * OoO0 * OoO0O00 . OoO0O00 * iii - OoO0
  if ( IiIiIi == 15 ) or ( oOOoo00O0O == 'true' ) :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Show All Isengard Compatible Builds[/COLOR]' , '&xbmc=isengard&visibility=public' , 'grab_builds' , 'TRCOMMUNITYHELIXBUILDS.png' , '' , '' , '' )
   if 14 - 14: I1ii11iIi11i + i11iIiiIii
   if 83 - 83: I1ii11iIi11i / i11iIiiIii + II111iiii . oOoO0o00OO0 * Oo + iI1iiIiiII
   if 42 - 42: i1IIi % II111iiii . iIII
  if oooOOOOO == 'false' :
   OOo0oO00ooO00 ( '' , '[COLOR=gold]How to fix builds broken on other wizards![/COLOR]' , '' , 'instructions_5' , 'TRCOMMUNITYGOTHAMBUILDS.png' , '' , '' , '' )
  if i1iiIII111ii != '' and oooOOOOO == 'true' :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=darkcyan]Show ' + i1iIIi1 + ' Builds[/COLOR]' , '&id=1' , 'grab_builds' , 'TRCOMMUNITYGOTHAMBUILDS.png' , '' , '' , '' )
  if ii11iIi1I != '' and oooOOOOO == 'true' :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=darkcyan]Show ' + iI111I11I1I1 + ' Builds[/COLOR]' , '&id=2' , 'grab_builds' , 'TRCOMMUNITYGOTHAMBUILDS.png' , '' , '' , '' )
  if OOooO0OOoo != '' and oooOOOOO == 'true' :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=darkcyan]Show ' + iIii1 + ' Builds[/COLOR]' , '&id=3' , 'grab_builds' , 'TRCOMMUNITYGOTHAMBUILDS.png' , '' , '' , '' )
  if oOOoO0 != '' and oooOOOOO == 'true' :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=darkcyan]Show ' + O0OoO000O0OO + ' Builds[/COLOR]' , '&id=4' , 'grab_builds' , 'TRCOMMUNITYGOTHAMBUILDS.png' , '' , '' , '' )
  if iiI1IiI != '' and oooOOOOO == 'true' :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=darkcyan]Show ' + II + ' Builds[/COLOR]' , '&id=5' , 'grab_builds' , 'TRCOMMUNITYGOTHAMBUILDS.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Create My Own Community Build' , 'url' , 'backup_option' , 'Backup.png' , '' , '' , 'Back Up Your Full System' )
 if 7 - 7: I1ii11iIi11i - ooOo * Oo + o0oOOo0O0Ooo . I1ii11iIi11i
 if 85 - 85: O0
def IiiIiI1I1 ( skin ) :
 iI111i11iI1 = '<onleft>%s</onleft>'
 III1ii = '<onright>%s</onright>'
 iI1III1iIi11 = '<onup>%s</onup>'
 i11I1I = '<ondown>%s</ondown>'
 oo0ooooo00o = '<control type="button" id="%s">'
 if 78 - 78: iIii1I11I1II1 . o0oOOo0O0Ooo % iIii1I11I1II1 . O0 / Oo
 if 76 - 76: i1IIi * OoooooooOO * O0 + OOo00O0 * OOo00O0
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
 if 20 - 20: o0oOOo0O0Ooo * iIII
 for i1III1iI , ii1ii1IiiiiIi1I in i1iIiIii :
  ooo0O0o0OoOO = open ( skin ) . read ( )
  iIi11i = ooo0O0o0OoOO . replace ( oo0ooooo00o % i1III1iI , oo0ooooo00o % ii1ii1IiiiiIi1I ) . replace ( iI111i11iI1 % i1III1iI , iI111i11iI1 % ii1ii1IiiiiIi1I ) . replace ( III1ii % i1III1iI , III1ii % ii1ii1IiiiiIi1I ) . replace ( iI1III1iIi11 % i1III1iI , iI1III1iIi11 % ii1ii1IiiiiIi1I ) . replace ( i11I1I % i1III1iI , i11I1I % ii1ii1IiiiiIi1I )
  IiI1 = open ( skin , mode = 'w' )
  IiI1 . write ( iIi11i )
  IiI1 . close ( )
  if 98 - 98: iIII - oOoO0o00OO0 . iii
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
 IiI1 = open ( skin , mode = 'w' )
 IiI1 . write ( iIi11i )
 IiI1 . close ( )
 if 87 - 87: OoOoOO00 % iIii1I11I1II1
 if 72 - 72: Oo . Oo - I1ii11iIi11i
def III1II1i ( ) :
 iI1i1IiIIIIi = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if 65 - 65: O0 * I1IiiI / I1IiiI . OoOoOO00
 if not os . path . exists ( zip ) :
  OooO0 . ok ( 'Download/Storage Path Check' , 'The download location you have stored does not exist .\nPlease update the addon settings and try again.' )
  o0O . openSettings ( sys . argv [ 0 ] )
  if 87 - 87: II111iiii * I1ii11iIi11i % Oo0Ooo * Oo0Ooo
  if 58 - 58: Oo . o0oOOo0O0Ooo + I1IiiI % Oo0Ooo - OoO0O00
def Oo00OO0 ( localbuildcheck , localversioncheck , id ) :
 Oo0O00O000 = 'http://120.24.252.100/TI/Community_Builds/buildupdate.php?id=%s' % ( id )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 50 - 50: oOoO0o00OO0 % II111iiii - iIII . i1IIi + O0 % oOoO0o00OO0
 if id != 'None' :
  i1iIi1IIiIII1 = re . compile ( 'version="(.+?)"' ) . findall ( i11I1IiII1i1i )
  i1Ii11I1II = i1iIi1IIiIII1 [ 0 ] if ( len ( i1iIi1IIiIII1 ) > 0 ) else ''
  if 77 - 77: ooOo - Oo0Ooo - iIii1I11I1II1
  if localversioncheck < i1Ii11I1II :
   return True
   if 16 - 16: OoO0O00 / oOoO0o00OO0 / i1IIi . oOoO0o00OO0 + ooOo
 else :
  return False
  if 26 - 26: iIii1I11I1II1 + i1IIi / OoOoOO00 % I1ii11iIi11i
  if 44 - 44: OoooooooOO . II111iiii . Oo % OoooooooOO
def oOO0o0oo0 ( ) :
 Oo0oO00 = open ( ii11i1 , mode = 'r' )
 iiiO00O00O000OOO = Oo0oO00 . read ( )
 Oo0oO00 . close ( )
 if 41 - 41: O0 - iii * iIii1I11I1II1
 II111i1ii1iII = re . compile ( 'name="(.+?)"' ) . findall ( iiiO00O00O000OOO )
 ooo0OoO = II111i1ii1iII [ 0 ] if ( len ( II111i1ii1iII ) > 0 ) else ''
 if 50 - 50: I1IiiI * Oo + iIII
 if ooo0OoO == "Incomplete" :
  iIi1IiI = xbmcgui . Dialog ( ) . yesno ( "Finish Restore Process" , 'If you\'re certain the correct skin has now been set click OK' , 'to finish the install process, once complete XBMC/Kodi will' , ' then close. Do you want to finish the install process?' , yeslabel = 'Yes' , nolabel = 'No' )
  if 88 - 88: iii + i11iIiiIii % ooOo * Oo * Oo * OoO0
  if iIi1IiI == 1 :
   I1I1iO0O0oo ( )
   if 83 - 83: iI1iiIiiII / OOo00O0
  elif iIi1IiI == 0 :
   return
   if 64 - 64: OoO0O00 % iI1iiIiiII . OOo00O0 % OoO0O00 + iii * iI1iiIiiII
def OOOO00OooO ( ) :
 iI1i1IiIIIIi = xbmc . translatePath ( os . path . join ( zip , 'testCBFolder' ) )
 if 64 - 64: OoO0O00 . I1IiiI - OoooooooOO . iIII - oOoO0o00OO0
 try :
  os . makedirs ( iI1i1IiIIIIi )
  os . removedirs ( iI1i1IiIIIIi )
  OooO0 . ok ( '[COLOR=lime]SUCCESS[/COLOR]' , 'Great news, the path you chose is writeable.' , 'Some of these builds are rather big, we recommend a minimum of 1GB storage space.' )
  if 77 - 77: OoO0 % OoOoOO00 / II111iiii % oOoO0o00OO0 % OoooooooOO % OoO0O00
 except :
  OooO0 . ok ( '[COLOR=red]CANNOT WRITE TO PATH[/COLOR]' , 'Kodi cannot write to the path you\'ve chosen. Please click OK in the settings menu to save the path then try again. Some devices give false results, we recommend using a USB stick as the backup path.' )
  if 19 - 19: iI1iiIiiII * OOo00O0 / ooOo * OOo00O0 - OoooooooOO * iii
  if 17 - 17: II111iiii + Oo0Ooo . OOo00O0
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
 if 15 - 15: ooOo / OOo00O0
def Iiii111 ( ) :
 iIi1IiI = xbmcgui . Dialog ( ) . yesno ( 'Clear All Known Cache?' , 'This will clear all known cache files and can help if you\'re encountering kick-outs during playback as well as other random issues. There is no harm in using this.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if 71 - 71: O0 / I1IiiI . OOo00O0 / OOo00O0 * iIII
 if iIi1IiI == 1 :
  OooO0OOo ( )
  OooOoooo0000 ( )
  if 29 - 29: OoO0 - I1IiiI / I1IiiI * OoO0 * iI1iiIiiII . Oo
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
 if 5 - 5: OoOoOO00 % oOoO0o00OO0 + iI1iiIiiII
 if 13 - 13: iI1iiIiiII
def ii1II1II ( ) :
 i11i11II11i = 1
 III1II1i ( )
 II1Ii1I1i = xbmc . translatePath ( os . path . join ( OOO0OOO00oo , 'Community Builds' , 'My Builds' , '' ) )
 OOooOooo0OOo0 = xbmc . translatePath ( os . path . join ( OOO0OOO00oo , 'Community Builds' , 'My Builds' , 'my_full_backup.zip' ) )
 oo0o0OoOO0o0 = xbmc . translatePath ( os . path . join ( OOO0OOO00oo , 'Community Builds' , 'My Builds' , 'my_full_backup_GUI_Settings.zip' ) )
 if 14 - 14: o0oOOo0O0Ooo % iI1iiIiiII + I1ii11iIi11i + OoO0O00
 if not os . path . exists ( II1Ii1I1i ) :
  os . makedirs ( II1Ii1I1i )
  if 76 - 76: OoO0O00 - i11iIiiIii + OoOoOO00 + Oo / OoooooooOO
 IiI1Iii1 = OooooiIiiiIiIi ( heading = "Enter a name for this backup" )
 if ( not IiI1Iii1 ) :
  return False , 0
  if 19 - 19: iI1iiIiiII . I1ii11iIi11i / OoOoOO00
 O00oo = urllib . quote_plus ( IiI1Iii1 )
 OoOoooO000OO = xbmc . translatePath ( os . path . join ( II1Ii1I1i , O00oo + '.zip' ) )
 O00Oooi1 = [ I1IiI ]
 oOOO0ooOO = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'Thumbs.db' , '.gitignore' ]
 i11IiI1iiI11 = [ I1IiI , 'cache' , 'system' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' ]
 OOoOOOO00 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' , 'Thumbs.db' , '.gitignore' ]
 i11Ii1iIiII = "Creating full backup of existing build"
 IIii1III = "Creating Community Build"
 O0oOo00Ooo0o0 = "Archiving..."
 i1IiII1i1I = ""
 iI1ii1ii1I = "Please Wait"
 if 94 - 94: i11iIiiIii % OoooooooOO / I1IiiI
 if Oo0oO0ooo == 'true' :
  O0o00O0Oo0 ( OO0o , OOooOooo0OOo0 , i11Ii1iIiII , O0oOo00Ooo0o0 , i1IiII1i1I , iI1ii1ii1I , O00Oooi1 , oOOO0ooOO )
  if 24 - 24: I1IiiI * ooOo
 iIi1IiI = xbmcgui . Dialog ( ) . yesno ( "Do you want to include your addon_data folder?" , 'This contains ALL addon settings including passwords but may also contain important information such as skin shortcuts. We recommend MANUALLY removing the addon_data folders that aren\'t required.' , yeslabel = 'Yes' , nolabel = 'No' )
 if 85 - 85: II111iiii . iIII % Oo % iii
 if iIi1IiI == 0 :
  i11IiI1iiI11 = [ I1IiI , 'cache' , 'system' , 'peripheral_data' , 'library' , 'keymaps' , 'addon_data' , 'Thumbnails' ]
  if 80 - 80: ooOo * iii / iIii1I11I1II1 % ooOo / iIii1I11I1II1
 elif iIi1IiI == 1 :
  pass
  if 42 - 42: i1IIi / i11iIiiIii . Oo0Ooo * oOoO0o00OO0 . i11iIiiIii * O0
 Iiii1 ( OO0o )
 O0o00O0Oo0 ( OO0o , OoOoooO000OO , IIii1III , O0oOo00Ooo0o0 , i1IiII1i1I , iI1ii1ii1I , i11IiI1iiI11 , OOoOOOO00 )
 time . sleep ( 1 )
 if 27 - 27: Oo
 O0OO0ooO00 = xbmc . translatePath ( os . path . join ( II1Ii1I1i , O00oo + '_guisettings.zip' ) )
 oO0oOO0o = zipfile . ZipFile ( O0OO0ooO00 , mode = 'w' )
 if 65 - 65: oOoO0o00OO0 . OoO0O00 + OoO0
 try :
  oO0oOO0o . write ( I11II1i , 'guisettings.xml' , zipfile . ZIP_DEFLATED )
 except : i11i11II11i = 0
 if 25 - 25: o0oOOo0O0Ooo + Oo0Ooo . Oo0Ooo % OoooooooOO - OoO0
 try :
  oO0oOO0o . write ( xbmc . translatePath ( os . path . join ( OO0o , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
 except : pass
 if 43 - 43: OoO0O00 % OoO0O00
 oO0oOO0o . close ( )
 if 46 - 46: Oo0Ooo % iIii1I11I1II1 . oOoO0o00OO0 . O0 * iIII / OoooooooOO
 if Oo0oO0ooo == 'true' :
  II1iI1IIi = zipfile . ZipFile ( oo0o0OoOO0o0 , mode = 'w' )
  try :
   II1iI1IIi . write ( I11II1i , 'guisettings.xml' , zipfile . ZIP_DEFLATED )
  except : i11i11II11i = 0
  if 41 - 41: I1IiiI - OOo00O0 % II111iiii . OOo00O0 - iii
  try :
   II1iI1IIi . write ( xbmc . translatePath ( os . path . join ( OO0o , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
  except : pass
  II1iI1IIi . close ( )
  if 45 - 45: OoO0 - Oo
  if i11i11II11i == 0 :
   OooO0 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your system, please reboot and try again.' , '' , '' )
   if 70 - 70: OoO0O00 % I1IiiI / I1IiiI . iii % iIII . II111iiii
  else :
   OooO0 . ok ( "SUCCESS!" , 'You Are Now Backed Up and can share this build with the community.' )
   if 10 - 10: OoO0 - i11iIiiIii . I1ii11iIi11i % i1IIi
   if Oo0oO0ooo == 'true' :
    OooO0 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=dodgerblue]' + OOooOooo0OOo0 , '[/COLOR]Universal Backup: [COLOR=dodgerblue]' + OoOoooO000OO + '[/COLOR]' )
    if 78 - 78: iIii1I11I1II1 * Oo0Ooo . Oo0Ooo - Oo . iIii1I11I1II1
   else :
    OooO0 . ok ( "Build Location" , 'Universal Backup:[CR][COLOR=dodgerblue]' + OoOoooO000OO + '[/COLOR]' )
    if 30 - 30: iIII + iIII % iI1iiIiiII - o0oOOo0O0Ooo - I1ii11iIi11i
    if 36 - 36: iii % Oo
def OoO0i1ii1IIIII ( ) :
 III1II1i ( )
 iIi1IiI = OooO0 . yesno ( '[COLOR=gold]Create[/COLOR] [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] [COLOR=gold]Build[/COLOR]' , 'This backup will only work if you share your build on the [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] portal with the rest of the community. It will not work with any other installer/wizard, do you wish to continue?' )
 if 52 - 52: OoOoOO00 / OoO0O00 + OOo00O0
 if iIi1IiI == 1 :
  i11i11II11i = 1
  II1Ii1I1i = xbmc . translatePath ( os . path . join ( OOO0OOO00oo , 'Community Builds' , 'My Builds' , '' ) )
  OOooOooo0OOo0 = xbmc . translatePath ( os . path . join ( OOO0OOO00oo , 'Community Builds' , 'My Builds' , 'my_full_backup.zip' ) )
  oo0o0OoOO0o0 = xbmc . translatePath ( os . path . join ( OOO0OOO00oo , 'Community Builds' , 'My Builds' , 'my_full_backup_GUI_Settings.zip' ) )
  if 49 - 49: iIii1I11I1II1 % iii . iii . iIii1I11I1II1 * OoOoOO00 / iii
  if not os . path . exists ( II1Ii1I1i ) :
   os . makedirs ( II1Ii1I1i )
   if 95 - 95: ooOo * iIii1I11I1II1 + I1ii11iIi11i
  IiI1Iii1 = OooooiIiiiIiIi ( heading = "Enter a name for this backup" )
  if 5 - 5: Oo0Ooo
  if ( not IiI1Iii1 ) :
   return False , 0
   if 100 - 100: OoO0 + iIii1I11I1II1
  O00oo = urllib . quote_plus ( IiI1Iii1 )
  OoOoooO000OO = xbmc . translatePath ( os . path . join ( II1Ii1I1i , O00oo + '.zip' ) )
  if 59 - 59: iI1iiIiiII
  if 89 - 89: OoOoOO00 % iIii1I11I1II1
  O00Oooi1 = [ I1IiI ]
  oOOO0ooOO = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'Thumbs.db' , '.gitignore' ]
  i11IiI1iiI11 = [ I1IiI , 'cache' , 'system' , 'addons' , 'Thumbnails' , "peripheral_data" , 'library' , 'keymaps' , 'script.module.metahandler' , 'script.artistslideshow' , 'ArtistSlideshow' ]
  OOoOOOO00 = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , "Textures13.db" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'advancedsettings.xml' , 'Thumbs.db' , '.gitignore' ]
  i11Ii1iIiII = "Creating full backup of existing build"
  IIii1III = "Creating Community Build"
  O0oOo00Ooo0o0 = "Archiving..."
  i1IiII1i1I = ""
  iI1ii1ii1I = "Please Wait"
  if 35 - 35: I1ii11iIi11i + OOo00O0 - OoOoOO00 % ooOo % o0oOOo0O0Ooo % OoOoOO00
  if 45 - 45: I1IiiI * Oo % OoO0O00
  if Oo0oO0ooo == 'true' :
   O0o00O0Oo0 ( OO0o , OOooOooo0OOo0 , i11Ii1iIiII , O0oOo00Ooo0o0 , i1IiII1i1I , iI1ii1ii1I , O00Oooi1 , oOOO0ooOO )
   if 24 - 24: iIII - iii * ooOo
  iIi1IiI = xbmcgui . Dialog ( ) . yesno ( "Do you want to include your addon_data folder?" , 'This contains ALL addon settings including passwords but may also contain important information such as skin shortcuts. We recommend MANUALLY removing the addon_data folders that aren\'t required.' , yeslabel = 'Yes' , nolabel = 'No' )
  if 87 - 87: OoO0 - I1ii11iIi11i % I1ii11iIi11i . ooOo / I1ii11iIi11i
  if 6 - 6: OoOoOO00 / iIii1I11I1II1 * OoooooooOO * i11iIiiIii
  if iIi1IiI == 0 :
   i11IiI1iiI11 = [ I1IiI , 'cache' , 'system' , 'addons' , 'peripheral_data' , 'library' , 'keymaps' , 'addon_data' , 'Thumbnails' ]
   if 79 - 79: iI1iiIiiII % OoO0O00
  elif iIi1IiI == 1 :
   pass
   if 81 - 81: i11iIiiIii + i11iIiiIii * OoO0O00 + iI1iiIiiII
   if 32 - 32: O0 . OoooooooOO
  i1iii1ii ( )
  Iiii1 ( OO0o )
  O0o00O0Oo0 ( OO0o , OoOoooO000OO , IIii1III , O0oOo00Ooo0o0 , i1IiII1i1I , iI1ii1ii1I , i11IiI1iiI11 , OOoOOOO00 )
  if 15 - 15: I1IiiI . OoO0O00
  if 17 - 17: i11iIiiIii / Oo0Ooo . OoO0O00 / I1IiiI
  try :
   os . remove ( O00O0oOO00O00 )
  except :
   pass
   if 38 - 38: i1IIi . I1ii11iIi11i % OoO0 + iIii1I11I1II1 + O0
  try :
   os . remove ( O0o0O00Oo0o0 )
  except :
   pass
   if 47 - 47: OoO0O00 + iI1iiIiiII / II111iiii
  time . sleep ( 1 )
  if 97 - 97: I1ii11iIi11i / I1IiiI % O0 + i1IIi - iIII
  if 38 - 38: o0oOOo0O0Ooo % OOo00O0 + i11iIiiIii + oOoO0o00OO0 + iIII / i11iIiiIii
  O0OO0ooO00 = xbmc . translatePath ( os . path . join ( II1Ii1I1i , O00oo + '_guisettings.zip' ) )
  oO0oOO0o = zipfile . ZipFile ( O0OO0ooO00 , mode = 'w' )
  if 94 - 94: oOoO0o00OO0 - Oo0Ooo + ooOo
  try :
   oO0oOO0o . write ( I11II1i , 'guisettings.xml' , zipfile . ZIP_DEFLATED )
   if 59 - 59: iii . I1IiiI - iIii1I11I1II1 + iIii1I11I1II1
  except :
   i11i11II11i = 0
   if 56 - 56: ooOo + iIII
  try :
   oO0oOO0o . write ( xbmc . translatePath ( os . path . join ( OO0o , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
   if 32 - 32: II111iiii + OoOoOO00 % iIII / OoOoOO00 + I1ii11iIi11i
  except :
   pass
   if 2 - 2: i11iIiiIii - OOo00O0 + OoO0O00 % iii * OoO0
  oO0oOO0o . close ( )
  if 54 - 54: O0 - oOoO0o00OO0 . Oo % oOoO0o00OO0 + oOoO0o00OO0
  if 36 - 36: Oo % i11iIiiIii
  if Oo0oO0ooo == 'true' :
   II1iI1IIi = zipfile . ZipFile ( oo0o0OoOO0o0 , mode = 'w' )
   if 47 - 47: i1IIi + II111iiii . Oo0Ooo * ooOo . iii / i1IIi
   try :
    II1iI1IIi . write ( I11II1i , 'guisettings.xml' , zipfile . ZIP_DEFLATED )
    if 50 - 50: OOo00O0 / i1IIi % OoooooooOO
   except :
    i11i11II11i = 0
    if 83 - 83: I1ii11iIi11i * I1ii11iIi11i + Oo
   try :
    II1iI1IIi . write ( xbmc . translatePath ( os . path . join ( OO0o , 'userdata' , 'profiles.xml' ) ) , 'profiles.xml' , zipfile . ZIP_DEFLATED )
    if 57 - 57: O0 - O0 . I1ii11iIi11i / o0oOOo0O0Ooo / OoO0
   except :
    pass
    if 20 - 20: Oo * II111iiii - OoOoOO00 - ooOo * OOo00O0
   II1iI1IIi . close ( )
   if 6 - 6: iIII + Oo / Oo0Ooo + iI1iiIiiII % II111iiii / OoO0O00
  if i11i11II11i == 0 :
   OooO0 . ok ( "FAILED!" , 'The guisettings.xml file could not be found on your system, please reboot and try again.' , '' , '' )
   if 45 - 45: OoooooooOO
  else :
   OooO0 . ok ( "SUCCESS!" , 'You Are Now Backed Up and can share this build with the community.' )
   if 9 - 9: iii . OoO0O00 * i1IIi . OoooooooOO
   if Oo0oO0ooo == 'true' :
    OooO0 . ok ( "Build Locations" , 'Full Backup (only used to restore on this device): [COLOR=dodgerblue]' + OOooOooo0OOo0 , '[/COLOR]Universal Backup (this will ONLY work for sharing on the [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] portal):[CR][COLOR=dodgerblue]' + OoOoooO000OO + '[/COLOR]' )
    if 32 - 32: OoOoOO00 . I1ii11iIi11i % I1IiiI - II111iiii
   else :
    OooO0 . ok ( "Build Location" , 'Universal Backup (this will ONLY work for sharing on the [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] portal):[CR][COLOR=dodgerblue]' + OoOoooO000OO + '[/COLOR]' )
    if 11 - 11: O0 + I1IiiI
    if 80 - 80: ooOo % ooOo % O0 - i11iIiiIii . oOoO0o00OO0 / O0
def IiIi1Ii ( url , video ) :
 Oo0O00O000 = 'http://120.24.252.100/TI/Community_Builds/community_builds_premium.php?id=%s' % ( url )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIIiI11II1 = re . compile ( 'path="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oooOo = re . compile ( 'myart="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oOoO0Oo0 = re . compile ( 'artpack="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oOIIiIi = re . compile ( 'videopreview="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i11i11i = re . compile ( 'videoguide1="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiI1iI = re . compile ( 'videoguide2="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Ooo00O0 = re . compile ( 'videoguide3="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OoO0OOoO0 = re . compile ( 'videoguide4="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiI11i = re . compile ( 'videoguide5="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0OoiiI1i = re . compile ( 'videolabel1="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i11I = re . compile ( 'videolabel2="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0oO0o0oo0O0 = re . compile ( 'videolabel3="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O0oo00oOOO0o = re . compile ( 'videolabel4="(.+?)"' ) . findall ( i11I1IiII1i1i )
 II1i = re . compile ( 'videolabel5="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oo0oO = re . compile ( 'name="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I111iiIIiI1I = re . compile ( 'author="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IIo0Oo0oO0oOO00 = re . compile ( 'version="(.+?)"' ) . findall ( i11I1IiII1i1i )
 II11iI1iiI = re . compile ( 'description="(.+?)"' ) . findall ( i11I1IiII1i1i )
 ooO00Oo = re . compile ( 'DownloadURL="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Iiii1Ii1I = re . compile ( 'UpdateURL="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oooOOOOOi1iIii = re . compile ( 'UpdateDate="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0O0ooooooo00 = re . compile ( 'UpdateDesc="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oooO = re . compile ( 'updated="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1111ii11IIII = re . compile ( 'defaultskin="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IiIi1II111I = re . compile ( 'skins="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o00o = re . compile ( 'videoaddons="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IIi1i1 = re . compile ( 'audioaddons="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0O0Ooo = re . compile ( 'programaddons="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O0o = re . compile ( 'pictureaddons="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O00oOOooO = re . compile ( 'sources="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IiIIii1iiI = re . compile ( 'adult="(.+?)"' ) . findall ( i11I1IiII1i1i )
 ii1IiiII = re . compile ( 'guisettings="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IiiI1II1II1i = re . compile ( 'thumb="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iIO0OO0o0O00oO = re . compile ( 'fanart="(.+?)"' ) . findall ( i11I1IiII1i1i )
 if 81 - 81: iI1iiIiiII / iii
 III1 = oooOo [ 0 ] if ( len ( oooOo ) > 0 ) else ''
 IIi11 = oOoO0Oo0 [ 0 ] if ( len ( oOoO0Oo0 ) > 0 ) else ''
 iI1i1IiIIIIi = iiIIiI11II1 [ 0 ] if ( len ( iiIIiI11II1 ) > 0 ) else ''
 I1ii1 = oo0oO [ 0 ] if ( len ( oo0oO ) > 0 ) else ''
 o0O0oo0 = I111iiIIiI1I [ 0 ] if ( len ( I111iiIIiI1I ) > 0 ) else ''
 IiIiIi = IIo0Oo0oO0oOO00 [ 0 ] if ( len ( IIo0Oo0oO0oOO00 ) > 0 ) else ''
 I1iii = II11iI1iiI [ 0 ] if ( len ( II11iI1iiI ) > 0 ) else 'No information available'
 IIiI1 = oooO [ 0 ] if ( len ( oooO ) > 0 ) else ''
 iIIi1 = I1111ii11IIII [ 0 ] if ( len ( I1111ii11IIII ) > 0 ) else ''
 o0Ooo0o0Oo = IiIi1II111I [ 0 ] if ( len ( IiIi1II111I ) > 0 ) else ''
 oo00ooooOOo00 = o00o [ 0 ] if ( len ( o00o ) > 0 ) else ''
 ii1iOO00Oooo000 = IIi1i1 [ 0 ] if ( len ( IIi1i1 ) > 0 ) else ''
 iI1 = o0O0Ooo [ 0 ] if ( len ( o0O0Ooo ) > 0 ) else ''
 ii111iiIii = O0o [ 0 ] if ( len ( O0o ) > 0 ) else ''
 oO0o = O00oOOooO [ 0 ] if ( len ( O00oOOooO ) > 0 ) else ''
 iIiI = IiIIii1iiI [ 0 ] if ( len ( IiIIii1iiI ) > 0 ) else ''
 iIIiiiI1iI1 = ii1IiiII [ 0 ] if ( len ( ii1IiiII ) > 0 ) else 'None'
 oO00000oO0o0O = ooO00Oo [ 0 ] if ( len ( ooO00Oo ) > 0 ) else 'None'
 IIIiI1iI1 = Iiii1Ii1I [ 0 ] if ( len ( Iiii1Ii1I ) > 0 ) else 'None'
 IIiIiiii1I1 = oooOOOOOi1iIii [ 0 ] if ( len ( oooOOOOOi1iIii ) > 0 ) else 'None'
 oO0O0 = o0O0ooooooo00 [ 0 ] if ( len ( o0O0ooooooo00 ) > 0 ) else 'None'
 ii1Oo0000oOo = oOIIiIi [ 0 ] if ( len ( oOIIiIi ) > 0 ) else 'None'
 I1I = i11i11i [ 0 ] if ( len ( i11i11i ) > 0 ) else 'None'
 ooooo = iiI1iI [ 0 ] if ( len ( iiI1iI ) > 0 ) else 'None'
 i11IIIiI1I = Ooo00O0 [ 0 ] if ( len ( Ooo00O0 ) > 0 ) else 'None'
 o0iiiI1I1iIIIi1 = OoO0OOoO0 [ 0 ] if ( len ( OoO0OOoO0 ) > 0 ) else 'None'
 Iii = iiI11i [ 0 ] if ( len ( iiI11i ) > 0 ) else 'None'
 O0Oo0o000oO = o0OoiiI1i [ 0 ] if ( len ( o0OoiiI1i ) > 0 ) else 'None'
 oO0o00oOOooO0 = i11I [ 0 ] if ( len ( i11I ) > 0 ) else 'None'
 OOOoO000 = o0oO0o0oo0O0 [ 0 ] if ( len ( o0oO0o0oo0O0 ) > 0 ) else 'None'
 oOOOO = O0oo00oOOO0o [ 0 ] if ( len ( O0oo00oOOO0o ) > 0 ) else 'None'
 IiIi1ii111i1 = II1i [ 0 ] if ( len ( II1i ) > 0 ) else 'None'
 Ii1IiIiIi1IiI = IiiI1II1II1i [ 0 ] if ( len ( IiiI1II1II1i ) > 0 ) else 'None'
 i1iiIIi1I = iIO0OO0o0O00oO [ 0 ] if ( len ( iIO0OO0o0O00oO ) > 0 ) else 'None'
 if 65 - 65: oOoO0o00OO0 . I1IiiI
 Oo0oO00 = open ( Ooo0OO0oOO , mode = 'w+' )
 Oo0oO00 . write ( 'id="' + str ( video ) + '"\nname="' + I1ii1 + '"\nversion="' + IiIiIi + '"' )
 Oo0oO00 . close ( )
 if 25 - 25: Oo * Oo / ooOo % Oo0Ooo
 i1iiiiI11ii = open ( ii11i1 , mode = 'r' )
 oooooOOo0o = i1iiiiI11ii . read ( )
 i1iiiiI11ii . close ( )
 if 98 - 98: OoO0O00 / iii - OoO0
 II1i111 = re . compile ( 'id="(.+?)"' ) . findall ( oooooOOo0o )
 OO = II1i111 [ 0 ] if ( len ( II1i111 ) > 0 ) else 'None'
 OOo0oOOOOooOo = re . compile ( 'version="(.+?)"' ) . findall ( oooooOOo0o )
 IIIi1I1IIii1II = OOo0oOOOOooOo [ 0 ] if ( len ( OOo0oOOOOooOo ) > 0 ) else 'None'
 i1I111II , Oo0OOo , i1II11I11ii1 = url . partition ( '&' )
 OOo0oO00ooO00 ( '' , '[COLOR=yellow]IMPORTANT:[/COLOR] Install Instructions' , '' , 'instructions_2' , 'noobsandnerds.png' , '' , '' , '' )
 oo000o ( '[COLOR=yellow]Description:[/COLOR] This contains important info from the build author' , 'None' , 'description' , 'BUILDDETAILS.png' , i1iiIIi1I , I1ii1 , o0O0oo0 , IiIiIi , I1iii , IIiI1 , o0Ooo0o0Oo , oo00ooooOOo00 , ii1iOO00Oooo000 , iI1 , ii111iiIii , oO0o , iIiI )
 if 64 - 64: ooOo % OoOoOO00 / II111iiii % iIII - oOoO0o00OO0
 if OO == i1I111II and IIIi1I1IIii1II != IiIiIi :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]----------------- UPDATE AVAILABLE ------------------[/COLOR]' , 'None' , '' , 'noobsandnerds.png' , '' , '' , '' )
  II1I ( '[COLOR=dodgerblue]1. Update:[/COLOR] Overwrite My Current Setup & Install New Build' , oO00000oO0o0O , 'restore_community' , Ii1IiIiIi1IiI , '' , 'update' , I1ii1 , iIIi1 , iIIiiiI1iI1 , IIi11 )
  II1I ( '[COLOR=dodgerblue]2. Update:[/COLOR] Keep My Library & Profiles' , oO00000oO0o0O , 'restore_community' , Ii1IiIiIi1IiI , '' , 'updatelibprofile' , I1ii1 , iIIi1 , iIIiiiI1iI1 , IIi11 )
  II1I ( '[COLOR=dodgerblue]3. Update:[/COLOR] Keep My Library Only' , oO00000oO0o0O , 'restore_community' , Ii1IiIiIi1IiI , '' , 'updatelibrary' , I1ii1 , iIIi1 , iIIiiiI1iI1 , IIi11 )
  II1I ( '[COLOR=dodgerblue]4. Update:[/COLOR] Keep My Profiles Only' , oO00000oO0o0O , 'restore_community' , Ii1IiIiIi1IiI , '' , 'updateprofiles' , I1ii1 , iIIi1 , iIIiiiI1iI1 , IIi11 )
  if 2 - 2: OOo00O0 - I1ii11iIi11i + o0oOOo0O0Ooo * OoO0O00 / oOoO0o00OO0
 if ii1Oo0000oOo != 'None' or I1I != 'None' or ooooo != 'None' or i11IIIiI1I != 'None' or o0iiiI1I1iIIIi1 != 'None' or Iii != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]------------------ VIDEO GUIDES -----------------[/COLOR]' , 'None' , '' , 'noobsandnerds.png' , '' , '' , '' )
  if 26 - 26: Oo * Oo0Ooo
 if ii1Oo0000oOo != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] Preview[/COLOR]' , ii1Oo0000oOo , 'play_video' , 'Video_Preview.png' , i1iiIIi1I , '' , '' )
  if 31 - 31: iii * ooOo . OoO0
 if I1I != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + O0Oo0o000oO + '[/COLOR]' , I1I , 'play_video' , 'Video_Guide.png' , i1iiIIi1I , '' , '' )
  if 35 - 35: iii
 if ooooo != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + oO0o00oOOooO0 + '[/COLOR]' , ooooo , 'play_video' , 'Video_Guide.png' , i1iiIIi1I , '' , '' )
  if 94 - 94: iIII / i11iIiiIii % O0
 if i11IIIiI1I != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + OOOoO000 + '[/COLOR]' , i11IIIiI1I , 'play_video' , 'Video_Guide.png' , i1iiIIi1I , '' , '' )
  if 70 - 70: iii - Oo0Ooo / OoooooooOO % OoooooooOO
 if o0iiiI1I1iIIIi1 != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + oOOOO + '[/COLOR]' , o0iiiI1I1iIIIi1 , 'play_video' , 'Video_Guide.png' , i1iiIIi1I , '' , '' )
  if 95 - 95: OoooooooOO % OoooooooOO . OoO0
 if Iii != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]Video:[/COLOR][COLOR=white] ' + IiIi1ii111i1 + '[/COLOR]' , Iii , 'play_video' , 'Video_Guide.png' , i1iiIIi1I , '' , '' )
  if 26 - 26: ooOo + iI1iiIiiII - II111iiii . II111iiii + I1ii11iIi11i + OoOoOO00
 if OO != i1I111II :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]------------------ INSTALL OPTIONS ------------------[/COLOR]' , 'None' , '' , 'noobsandnerds.png' , '' , '' , '' )
  if 68 - 68: O0
 if oO00000oO0o0O == 'None' :
  II1I ( '[COLOR=orange]Sorry this build is currently unavailable[/COLOR]' , '' , '' , '' , '' , '' , '' , '' , '' , '' )
  if 76 - 76: I1ii11iIi11i
 if OO != i1I111II :
  if 99 - 99: o0oOOo0O0Ooo
  if 1 - 1: OoO0 * OoOoOO00 * OoO0O00 + Oo0Ooo
  if 90 - 90: OOo00O0 % Oo0Ooo - Oo0Ooo . iIii1I11I1II1 / Oo + iii
  if 89 - 89: ooOo
  II1I ( '[COLOR=dodgerblue]1. Install:[/COLOR] Overwrite My Current Setup & Install New Build' , oO00000oO0o0O , 'restore_community' , Ii1IiIiIi1IiI , i1iiIIi1I , 'merge' , I1ii1 , iIIi1 , iIIiiiI1iI1 , IIi11 )
  II1I ( '[COLOR=dodgerblue]2. Install:[/COLOR] Keep My Library & Profiles' , oO00000oO0o0O , 'restore_community' , Ii1IiIiIi1IiI , i1iiIIi1I , 'libprofile' , I1ii1 , iIIi1 , iIIiiiI1iI1 , IIi11 )
  II1I ( '[COLOR=dodgerblue]3. Install:[/COLOR] Keep My Library Only' , oO00000oO0o0O , 'restore_community' , Ii1IiIiIi1IiI , i1iiIIi1I , 'library' , I1ii1 , iIIi1 , iIIiiiI1iI1 , IIi11 )
  II1I ( '[COLOR=dodgerblue]4. Install:[/COLOR] Keep My Profiles Only' , oO00000oO0o0O , 'restore_community' , Ii1IiIiIi1IiI , i1iiIIi1I , 'profiles' , I1ii1 , iIIi1 , iIIiiiI1iI1 , IIi11 )
  if 87 - 87: oOoO0o00OO0 % Oo0Ooo
 if iIIiiiI1iI1 != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]---------- (OPTIONAL) Guisettings Fix ----------[/COLOR]' , 'None' , '' , 'noobsandnerds.png' , '' , '' , '' )
  OOo0oO00ooO00 ( '' , '[COLOR=orange]Install Step 2:[/COLOR] Apply guisettings.xml fix' , iIIiiiI1iI1 , 'guisettingsfix' , 'Fix_My_Build.png' , i1iiIIi1I , '' , '' )
  if 62 - 62: OoO0O00 + iIII / oOoO0o00OO0 * i11iIiiIii
  if 37 - 37: oOoO0o00OO0
def iIIiI1111 ( ) :
 OooOO = xbmcgui . Dialog ( ) . browse ( 3 , 'Select the folder you want to store this file in' , 'files' , '' , False , False )
 IiI1Iii1 = OooooiIiiiIiIi ( heading = "Enter a name for this keyword" )
 if 86 - 86: OoO0 . Oo / iI1iiIiiII - OoooooooOO
 if ( not IiI1Iii1 ) :
  return False , 0
  if 45 - 45: Oo
 O00oo = urllib . quote_plus ( IiI1Iii1 )
 II11iiii1Ii . create ( 'Backing Up Addons & Repositories' , '' , 'Please Wait...' )
 if 25 - 25: Oo % O0
 if not os . path . exists ( O0o0O00Oo0o0 ) :
  os . makedirs ( O0o0O00Oo0o0 )
  if 44 - 44: OOo00O0 . OoO0 * II111iiii / iI1iiIiiII + iIii1I11I1II1
 o0O0oO0 = ooI1111i ( 'http://noobsandnerds.com/TI/AddonPortal/approved.php' )
 if 14 - 14: O0 % iI1iiIiiII % OoO0 * ooOo
 if 65 - 65: iii % ooOo + I1ii11iIi11i
 for I1ii1 in os . listdir ( O00o0OO ) :
  if not 'metadata' in I1ii1 and not 'module' in I1ii1 and not 'script.common' in I1ii1 and not 'packages' in I1ii1 and not 'service.xbmc.versioncheck' in I1ii1 and os . path . isdir ( os . path . join ( O00o0OO , I1ii1 ) ) :
   try :
    II11iiii1Ii . update ( 0 , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % I1ii1 , 'Please Wait...' )
    if 86 - 86: iIii1I11I1II1 / O0 . OOo00O0 % iIii1I11I1II1 % Oo0Ooo
    if 86 - 86: i11iIiiIii - o0oOOo0O0Ooo . iIII * Oo0Ooo / OoO0 % o0oOOo0O0Ooo
    if I1ii1 in o0O0oO0 :
     if 61 - 61: o0oOOo0O0Ooo + OoOoOO00
     if not os . path . exists ( os . path . join ( O0o0O00Oo0o0 , 'addons' , I1ii1 ) ) :
      os . makedirs ( os . path . join ( O0o0O00Oo0o0 , 'addons' , I1ii1 ) )
     shutil . copyfile ( os . path . join ( O00o0OO , I1ii1 , 'addon.xml' ) , os . path . join ( O0o0O00Oo0o0 , 'addons' , I1ii1 , 'addon.xml' ) )
    if not I1ii1 in o0O0oO0 :
     shutil . copytree ( os . path . join ( O00o0OO , I1ii1 ) , os . path . join ( O0o0O00Oo0o0 , 'addons' , I1ii1 ) )
     if 15 - 15: OoOoOO00 * ooOo + Oo . iii % I1IiiI - iIII
    II1I1I1i1i = os . path . join ( O0o0O00Oo0o0 , 'addons' , I1ii1 , 'addon.xml' )
    if 74 - 74: O0 % OoooooooOO * Oo0Ooo + Oo * oOoO0o00OO0
    if 100 - 100: Oo + OoO0 * o0oOOo0O0Ooo + II111iiii
    if 70 - 70: Oo0Ooo * iIii1I11I1II1
    O00Ooo0ooo0 = open ( II1I1I1i1i , mode = 'r' )
    iiiO00O00O000OOO = O00Ooo0ooo0 . read ( )
    O00Ooo0ooo0 . close ( )
    if 74 - 74: iii
    if 58 - 58: iIii1I11I1II1 * OoO0O00 * OOo00O0 * iIII . OoooooooOO
    o0O0oo0o = re . compile ( '<addon[\s\S]*?">' ) . findall ( iiiO00O00O000OOO )
    I1 = o0O0oo0o [ 0 ] if ( len ( o0O0oo0o ) > 0 ) else 'None'
    II1IIiiI1 = re . compile ( 'version="[\s\S]*?"' ) . findall ( I1 )
    O00O00 = II1IIiiI1 [ 0 ] if ( len ( II1IIiiI1 ) > 0 ) else '0'
    if 66 - 66: Oo0Ooo - iIii1I11I1II1
    if 9 - 9: o0oOOo0O0Ooo % I1ii11iIi11i . I1ii11iIi11i
    IiIIIIii11i = str ( I1 ) . replace ( O00O00 , 'version="0.0.0.1"' )
    i1I1 = iiiO00O00O000OOO . replace ( I1 , IiIIIIii11i )
    if 82 - 82: I1ii11iIi11i
    i11Ii1I1I11I = open ( II1I1I1i1i , mode = 'w' )
    i11Ii1I1I11I . write ( str ( i1I1 ) )
    i11Ii1I1I11I . close ( )
    if 54 - 54: o0oOOo0O0Ooo + iii - iIii1I11I1II1 % iIII % iI1iiIiiII
   except :
    print "### Failed to create: " + I1ii1 + ' ###'
    if 19 - 19: I1ii11iIi11i / iIii1I11I1II1 % i1IIi . OoooooooOO
 i11IiI1iiI11 = [ '.svn' , '.git' ]
 OOoOOOO00 = [ '.DS_Store' , 'Thumbs.db' , '.gitignore' ]
 O0oO0oo0O0 = os . path . join ( OooOO , O00oo + '.zip' )
 O0o00O0Oo0 ( O0o0O00Oo0o0 , O0oO0oo0O0 , 'Creating Keyword' , '' , '' , '' , i11IiI1iiI11 , OOoOOOO00 )
 try :
  shutil . rmtree ( O0o0O00Oo0o0 )
 except : pass
 OooO0 . ok ( 'New Keyword Created' , 'Please read the instructions on how to share this keyword with the community. Your zip file can be found at:' , '[COLOR=dodgerblue]' + O0oO0oo0O0 + '[/COLOR]' )
 if 66 - 66: Oo - iIII - Oo0Ooo
 if 54 - 54: oOoO0o00OO0 . i1IIi
def i1IiIiIiiI1 ( ) :
 print '############################################################       DELETING USERDATA             ###############################################################'
 iI1Ii = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data' , '' ) )
 if 74 - 74: OoooooooOO % Oo + ooOo % OoooooooOO + OoO0O00 * i11iIiiIii
 for ooO , o0Oo0oOooOoOo , I1i in os . walk ( iI1Ii ) :
  IIi1ii = 0
  IIi1ii += len ( I1i )
  if 38 - 38: iIii1I11I1II1 + OoooooooOO * I1IiiI % OoOoOO00 % iii - iI1iiIiiII
  if IIi1ii >= 0 :
   if 56 - 56: OoooooooOO * Oo0Ooo * iii + iIII
   for IiI1 in I1i :
    os . unlink ( os . path . join ( ooO , IiI1 ) )
    if 54 - 54: OoOoOO00 * i11iIiiIii . OoooooooOO - iIii1I11I1II1
   for iIiI1IIiii11 in o0Oo0oOooOoOo :
    shutil . rmtree ( os . path . join ( ooO , iIiI1IIiii11 ) )
    if 38 - 38: iii . iii * ooOo / OoooooooOO % iIII
    if 80 - 80: OoO0O00 / iI1iiIiiII * I1IiiI % iI1iiIiiII
def ooo00 ( ) :
 for iII11II1II in glob . glob ( os . path . join ( OOOO0OOoO0O0 , 'xbmc_crashlog*.*' ) ) :
  OOO00000o0 = iII11II1II
  os . remove ( iII11II1II )
  OooO0 = xbmcgui . Dialog ( )
  OooO0 . ok ( "Crash Logs Deleted" , "Your old crash logs have now been deleted." )
  if 96 - 96: o0oOOo0O0Ooo * ooOo - Oo * o0oOOo0O0Ooo * i1IIi
  if 8 - 8: iIII - Oo0Ooo + iIii1I11I1II1 + i1IIi * OoO0 - iIii1I11I1II1
def i1Ii ( ) :
 print '############################################################       DELETING PACKAGES             ###############################################################'
 I1iIIIIIi = xbmc . translatePath ( os . path . join ( 'special://home/addons/packages' , '' ) )
 if 36 - 36: iI1iiIiiII
 for ooO , o0Oo0oOooOoOo , I1i in os . walk ( I1iIIIIIi ) :
  IIi1ii = 0
  IIi1ii += len ( I1i )
  if 19 - 19: OoOoOO00 . o0oOOo0O0Ooo . OoooooooOO
  if IIi1ii > 0 :
   if 13 - 13: Oo . Oo0Ooo / II111iiii
   for IiI1 in I1i :
    os . unlink ( os . path . join ( ooO , IiI1 ) )
    if 43 - 43: iIii1I11I1II1 % OoO0O00
   for iIiI1IIiii11 in o0Oo0oOooOoOo :
    shutil . rmtree ( os . path . join ( ooO , iIiI1IIiii11 ) )
    if 84 - 84: Oo0Ooo
    if 44 - 44: OoooooooOO * i11iIiiIii / Oo0Ooo
def OoOoO00o00 ( ) :
 print '############################################################       DELETING USERDATA             ###############################################################'
 iI1Ii = xbmc . translatePath ( os . path . join ( 'special://home/userdata/addon_data' , '' ) )
 if 51 - 51: Oo0Ooo * iIii1I11I1II1 . OoooooooOO . OoO0 - Oo / I1IiiI
 for ooO , o0Oo0oOooOoOo , I1i in os . walk ( iI1Ii ) :
  IIi1ii = 0
  IIi1ii += len ( I1i )
  if 98 - 98: II111iiii + OoO0 + OoooooooOO / i1IIi - OoO0
  if IIi1ii >= 0 :
   if 87 - 87: oOoO0o00OO0 / iii / iii % OoooooooOO - I1ii11iIi11i * ooOo
   for IiI1 in I1i :
    os . unlink ( os . path . join ( ooO , IiI1 ) )
    if 23 - 23: i11iIiiIii
   for iIiI1IIiii11 in o0Oo0oOooOoOo :
    shutil . rmtree ( os . path . join ( ooO , iIiI1IIiii11 ) )
    if 100 - 100: ooOo + O0 . I1IiiI + i1IIi - OoOoOO00 + o0oOOo0O0Ooo
    if 65 - 65: II111iiii / Oo0Ooo
def IIIII1I1Ii11iI ( name , addon_id ) :
 OO0oIII111i11IiI = 1
 i11I1II = 1
 iiII1i = xbmc . translatePath ( os . path . join ( O00o0OO , addon_id , 'addon.xml' ) )
 IiiiI1 = open ( iiII1i , mode = 'r' )
 I1IIIi = IiiiI1 . read ( )
 IiiiI1 . close ( )
 I1iOo00oOO00 = re . compile ( 'import addon="(.+?)"' ) . findall ( I1IIIi )
 if 21 - 21: OoooooooOO . II111iiii - iI1iiIiiII * iIII * iI1iiIiiII
 for O0Oo00OoOo in I1iOo00oOO00 :
  if 45 - 45: O0 * OOo00O0 + i11iIiiIii - Oo - iIii1I11I1II1
  if not 'xbmc.python' in O0Oo00OoOo :
   print 'Script Requires --- ' + O0Oo00OoOo
   I11I111i1I1 = xbmc . translatePath ( os . path . join ( O00o0OO , O0Oo00OoOo ) )
   if 41 - 41: OoooooooOO / i1IIi
   if not os . path . exists ( I11I111i1I1 ) :
    Oo0O00O000 = 'http://noobsandnerds.com/TI/AddonPortal/dependencyinstall.php?id=%s' % ( O0Oo00OoOo )
    i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
    oo0oO = re . compile ( 'name="(.+?)"' ) . findall ( i11I1IiII1i1i )
    IIo0Oo0oO0oOO00 = re . compile ( 'version="(.+?)"' ) . findall ( i11I1IiII1i1i )
    ooO000OO0O00O = re . compile ( 'repo_url="(.+?)"' ) . findall ( i11I1IiII1i1i )
    OOOoOO0o = re . compile ( 'data_url="(.+?)"' ) . findall ( i11I1IiII1i1i )
    i1II1 = re . compile ( 'zip_url="(.+?)"' ) . findall ( i11I1IiII1i1i )
    oo00oO0o = re . compile ( 'repo_id="(.+?)"' ) . findall ( i11I1IiII1i1i )
    OO0Ooo0Oooo = oo0oO [ 0 ] if ( len ( oo0oO ) > 0 ) else ''
    IiIiIi = IIo0Oo0oO0oOO00 [ 0 ] if ( len ( IIo0Oo0oO0oOO00 ) > 0 ) else ''
    i1i1Ii1IiIII = ooO000OO0O00O [ 0 ] if ( len ( ooO000OO0O00O ) > 0 ) else ''
    I1IIii11 = OOOoOO0o [ 0 ] if ( len ( OOOoOO0o ) > 0 ) else ''
    I1I1 = i1II1 [ 0 ] if ( len ( i1II1 ) > 0 ) else ''
    O0OOO0ooO00o = oo00oO0o [ 0 ] if ( len ( oo00oO0o ) > 0 ) else ''
    I1iii1 = xbmc . translatePath ( os . path . join ( OOoOO0oo0ooO , OO0Ooo0Oooo + '.zip' ) )
    if 19 - 19: ooOo % OoooooooOO . OoooooooOO
    try :
     downloader . download ( i1i1Ii1IiIII , I1iii1 , II11iiii1Ii )
     oOOO ( I1iii1 , O00o0OO , II11iiii1Ii )
     if 40 - 40: O0 . OOo00O0 / iIii1I11I1II1 * o0oOOo0O0Ooo
    except :
     if 73 - 73: Oo0Ooo - oOoO0o00OO0 . ooOo % i1IIi . O0
     try :
      downloader . download ( I1I1 , I1iii1 , II11iiii1Ii )
      oOOO ( I1iii1 , O00o0OO , II11iiii1Ii )
      if 15 - 15: iIII . iIii1I11I1II1 * I1IiiI % iii
     except :
      if 21 - 21: OoO0O00 - I1IiiI . OoooooooOO
      try :
       if 6 - 6: iIii1I11I1II1 - iIii1I11I1II1 % o0oOOo0O0Ooo / iIii1I11I1II1 * OOo00O0
       if not os . path . exists ( I11I111i1I1 ) :
        os . makedirs ( I11I111i1I1 )
        if 3 - 3: Oo . iI1iiIiiII / Oo0Ooo
       i11I1IiII1i1i = ooI1111i ( I1IIii11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
       I111i1I1 = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( i11I1IiII1i1i )
       if 89 - 89: OoooooooOO . iIii1I11I1II1 . Oo0Ooo * iIii1I11I1II1 - OOo00O0
       for II1Ii1iI1i1 in I111i1I1 :
        o0OoO000O = xbmc . translatePath ( os . path . join ( I11I111i1I1 , II1Ii1iI1i1 ) )
        if 92 - 92: OoooooooOO - I1ii11iIi11i - OoooooooOO % I1IiiI % I1IiiI % iIii1I11I1II1
        if addon_id not in II1Ii1iI1i1 and '/' not in II1Ii1iI1i1 :
         if 92 - 92: oOoO0o00OO0 * O0 % OOo00O0 . iIii1I11I1II1
         try :
          II11iiii1Ii . update ( 0 , "Downloading [COLOR=yellow]" + II1Ii1iI1i1 + '[/COLOR]' , '' , 'Please wait...' )
          downloader . download ( I1IIii11 + II1Ii1iI1i1 , o0OoO000O , II11iiii1Ii )
          if 66 - 66: iii + OoO0
         except :
          print "failed to install" + II1Ii1iI1i1
          if 48 - 48: I1ii11iIi11i
        if '/' in II1Ii1iI1i1 and '..' not in II1Ii1iI1i1 and 'http' not in II1Ii1iI1i1 :
         iIIiI1I1i = I1IIii11 + II1Ii1iI1i1
         O0O0OOooOO0 ( o0OoO000O , iIIiI1I1i )
         if 96 - 96: iIII . OoooooooOO
      except :
       OooO0 . ok ( "Error downloading dependency" , 'There was an error downloading [COLOR=dodgerblue]' + OO0Ooo0Oooo + '[/COLOR]. Please consider updating the add-on portal with details or report the error on the forum at [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR]' )
       i11I1II = 0
       OO0oIII111i11IiI = 0
       if 39 - 39: Oo + OoO0O00
    if i11I1II == 1 :
     time . sleep ( 1 )
     II11iiii1Ii . update ( 0 , "[COLOR=yellow]" + OO0Ooo0Oooo + '[/COLOR]  [COLOR=lime]Successfully Installed[/COLOR]' , '' , 'Please wait...' )
     time . sleep ( 1 )
     OOo = 'http://noobsandnerds.com/TI/AddonPortal/downloadcount.php?id=%s' % ( O0Oo00OoOo )
     ooI1111i ( OOo )
 II11iiii1Ii . close ( )
 time . sleep ( 1 )
 if 80 - 80: Oo % OoO0O00 / OoOoOO00
 if 54 - 54: Oo0Ooo % OoO0O00 - Oo - iii
def o0I1iI111ii111i ( name , url , buildname , author , version , description , updated , skins , videoaddons , audioaddons , programaddons , pictureaddons , sources , adult ) :
 o00iI1Ii11iIiiI1 ( buildname + '     v.' + version , '[COLOR=yellow][B]Author:   [/B][/COLOR]' + author + '[COLOR=yellow][B]               Last Updated:   [/B][/COLOR]' + updated + '[COLOR=yellow][B]               Adult Content:   [/B][/COLOR]' + adult + '[CR][CR][COLOR=yellow][B]Description:[CR][/B][/COLOR]' + description +
 '[CR][CR][COLOR=blue][B]Skins:   [/B][/COLOR]' + skins + '[CR][CR][COLOR=blue][B]Video Addons:   [/B][/COLOR]' + videoaddons + '[CR][CR][COLOR=blue][B]Audio Addons:   [/B][/COLOR]' + audioaddons +
 '[CR][CR][COLOR=blue][B]Program Addons:   [/B][/COLOR]' + programaddons + '[CR][CR][COLOR=blue][B]Picture Addons:   [/B][/COLOR]' + pictureaddons + '[CR][CR][COLOR=blue][B]Sources:   [/B][/COLOR]' + sources +
 '[CR][CR][COLOR=orange]Disclaimer: [/COLOR]These are community builds and they may overwrite some of your existing settings, '
 'It\'s purely the responsibility of the user to choose whether or not they wish to install these builds, the individual who uploads the build should state what\'s included and then it\'s the users decision to decide whether or not that content is suitable for them.' )
 if 15 - 15: iii % Oo
 if 30 - 30: OoO0 + II111iiii % OoooooooOO
def oOo000O00O0 ( path ) :
 II11iiii1Ii . create ( "[COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR]" , "Wiping..." , '' , 'Please Wait' )
 shutil . rmtree ( path , ignore_errors = True )
 if 43 - 43: iIII
 if 53 - 53: i1IIi . i1IIi - iii / oOoO0o00OO0 - OoOoOO00 % I1IiiI
def oOOO ( _in , _out , dp = None ) :
 if dp :
  return O0OiI ( _in , _out , dp )
  if 85 - 85: II111iiii
 return o0oOOoo0O ( _in , _out )
 if 57 - 57: I1IiiI . i11iIiiIii * II111iiii + OoooooooOO + OoO0
 if 73 - 73: O0 % iii + oOoO0o00OO0 . I1ii11iIi11i . I1ii11iIi11i + iI1iiIiiII
def o0oOOoo0O ( _in , _out ) :
 try :
  i1i111I = zipfile . ZipFile ( _in , 'r' )
  i1i111I . extractall ( _out )
  if 77 - 77: iIII
 except Exception , O0O0OO0O0 :
  print str ( O0O0OO0O0 )
  return False
  if 78 - 78: ooOo / OoooooooOO . ooOo
 return True
 if 50 - 50: iI1iiIiiII . iIII - O0 % I1IiiI . OOo00O0
 if 17 - 17: O0 + OoooooooOO
def O0OiI ( _in , _out , dp ) :
 i1i111I = zipfile . ZipFile ( _in , 'r' )
 oo0OooO = float ( len ( i1i111I . infolist ( ) ) )
 I11iI1 = 0
 if 96 - 96: o0oOOo0O0Ooo % iI1iiIiiII / Oo
 try :
  if 63 - 63: i1IIi % i11iIiiIii % II111iiii * OoooooooOO
  for iIiII1 in i1i111I . infolist ( ) :
   I11iI1 += 1
   i111iii1I1 = I11iI1 / oo0OooO * 100
   dp . update ( int ( i111iii1I1 ) )
   i1i111I . extract ( iIiII1 , _out )
   if 48 - 48: OoooooooOO . OoOoOO00
 except Exception , O0O0OO0O0 :
  print str ( O0O0OO0O0 )
  return False
  if 65 - 65: ooOo . Oo0Ooo
 return True
 if 94 - 94: OoOoOO00 + iI1iiIiiII . iIII
def I1I1iO0O0oo ( ) :
 os . remove ( ii11i1 )
 os . rename ( o0OO00oO , ii11i1 )
 xbmc . executebuiltin ( 'UnloadSkin' )
 xbmc . executebuiltin ( "ReloadSkin" )
 OooO0 . ok ( "Local Restore Complete" , 'XBMC/Kodi will now close.' , '' , '' )
 xbmc . executebuiltin ( "Quit" )
 if 69 - 69: O0 - O0
 if 41 - 41: iI1iiIiiII % o0oOOo0O0Ooo
def Iiii1 ( url ) :
 II11iiii1Ii . create ( "Changing Physical Paths To Special" , "Renaming paths..." , '' , 'Please Wait' )
 if 67 - 67: O0 % OOo00O0
 for ooO , o0Oo0oOooOoOo , I1i in os . walk ( url ) :
  if 35 - 35: I1IiiI . OoOoOO00 + OoooooooOO % Oo0Ooo % Oo
  for file in I1i :
   if 39 - 39: OoO0
   if file . endswith ( ".xml" ) :
    II11iiii1Ii . update ( 0 , "Fixing" , file , 'Please Wait' )
    ooo0O0o0OoOO = open ( ( os . path . join ( ooO , file ) ) ) . read ( )
    oOo0000ooO = ooo0O0o0OoOO . replace ( OO0o , 'special://home/' )
    IiI1 = open ( ( os . path . join ( ooO , file ) ) , mode = 'w' )
    IiI1 . write ( str ( oOo0000ooO ) )
    IiI1 . close ( )
    if 15 - 15: iIII . o0oOOo0O0Ooo + OoOoOO00 . iIii1I11I1II1 % iIII + O0
    if 22 - 22: o0oOOo0O0Ooo + Oo0Ooo . iIII + I1ii11iIi11i * oOoO0o00OO0 . i11iIiiIii
def O0OOOOOO0ooO ( ) :
 II11IiI1 = 'http://noobsandnerds.com/TI/AddonPortal/Addon_Fix/addonfix.txt'
 i11I1IiII1i1i = ooI1111i ( II11IiI1 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I111i1I1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11I1IiII1i1i )
 if 86 - 86: iIii1I11I1II1 % ooOo - OoOoOO00 + OOo00O0 % OoO0O00 . I1ii11iIi11i
 for I1ii1 , iiIIiIi , Ii1IiIiIi1IiI , i1iiIIi1I , I1iii in I111i1I1 :
  OOo0oO00ooO00 ( '' , I1ii1 , iiIIiIi , 'OSS' , Ii1IiIiIi1IiI , i1iiIIi1I , '' , I1iii )
  if 97 - 97: oOoO0o00OO0 + iii % Oo0Ooo . II111iiii / II111iiii * oOoO0o00OO0
  if 80 - 80: OOo00O0 / i11iIiiIii + OoooooooOO
def III11i1iI11 ( ) :
 O00Oooi1 = [ ]
 oOOO0ooOO = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , '.gitignore' ]
 i11Ii1iIiII = "Creating full backup of existing build"
 IIii1III = "Creating Community Build"
 O0oOo00Ooo0o0 = "Archiving..."
 i1IiII1i1I = ""
 iI1ii1ii1I = "Please Wait"
 if 58 - 58: ooOo
 O0o00O0Oo0 ( OO0o , myfullbackup , i11Ii1iIiII , O0oOo00Ooo0o0 , i1IiII1i1I , iI1ii1ii1I , O00Oooi1 , oOOO0ooOO )
 if 98 - 98: o0oOOo0O0Ooo * OoO0O00
 if 10 - 10: ooOo - oOoO0o00OO0 % II111iiii - OOo00O0 - i1IIi
def iIi11iI1i ( url ) :
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
 if 46 - 46: i1IIi + II111iiii * i1IIi - OoO0
 if o0O . getSetting ( 'adult' ) == 'true' :
  OOo0oO00ooO00 ( 'folder' , 'XXX' , str ( url ) + '&genre=adult' , 'grab_builds' , 'adult.png' , '' , '' , '' )
  if 79 - 79: II111iiii - ooOo * I1ii11iIi11i - OoOoOO00 . I1ii11iIi11i
def OooooiIiiiIiIi ( default = "" , heading = "" , hidden = False ) :
 iiII1IIii1i1 = xbmc . Keyboard ( default , heading , hidden )
 if 38 - 38: oOoO0o00OO0 * OoooooooOO
 iiII1IIii1i1 . doModal ( )
 if ( iiII1IIii1i1 . isConfirmed ( ) ) :
  return unicode ( iiII1IIii1i1 . getText ( ) , "utf-8" )
 return default
 if 2 - 2: ooOo - i11iIiiIii
 if 98 - 98: ooOo + OoooooooOO - OOo00O0 % i11iIiiIii / o0oOOo0O0Ooo . OoooooooOO
def ooo0 ( ) :
 o0OOo0O = [ ]
 oo00i1i11I1I1 = sys . argv [ 2 ]
 if len ( oo00i1i11I1I1 ) >= 2 :
  OOOOOoooO = sys . argv [ 2 ]
  oO0Oooo0OoO = OOOOOoooO . replace ( '?' , '' )
  if ( OOOOOoooO [ len ( OOOOOoooO ) - 1 ] == '/' ) :
   OOOOOoooO = OOOOOoooO [ 0 : len ( OOOOOoooO ) - 2 ]
  Iiii1IIIIiiI11 = oO0Oooo0OoO . split ( '&' )
  o0OOo0O = { }
  for I1iii1I in range ( len ( Iiii1IIIIiiI11 ) ) :
   ooo = { }
   ooo = Iiii1IIIIiiI11 [ I1iii1I ] . split ( '=' )
   if ( len ( ooo ) ) == 2 :
    o0OOo0O [ ooo [ 0 ] ] = ooo [ 1 ]
    if 39 - 39: ooOo / iIII * II111iiii * oOoO0o00OO0
 return o0OOo0O
 if 41 - 41: i11iIiiIii * O0 - oOoO0o00OO0 . II111iiii % OoO0O00 % I1ii11iIi11i
def I1I11i ( ) :
 iI1i1IiIIIIi = xbmc . translatePath ( os . path . join ( 'special://home' , 'addons' ) )
 II11iiii1Ii = xbmcgui . DialogProgress ( )
 II11iiii1Ii . create ( "Gotham Addon Fix" , "Please wait whilst your addons" , '' , 'are being made Gotham compatible.' )
 if 38 - 38: i11iIiiIii . iIii1I11I1II1 . Oo / OoO0O00
 for iII11II1II in glob . glob ( os . path . join ( iI1i1IiIIIIi , '*.*' ) ) :
  if 18 - 18: Oo0Ooo * OOo00O0
  for file in glob . glob ( os . path . join ( iII11II1II , '*.*' ) ) :
   if 99 - 99: II111iiii * iIii1I11I1II1 % O0 * ooOo / II111iiii % OoooooooOO
   if 'addon.xml' in file :
    II11iiii1Ii . update ( 0 , "Fixing" , file , 'Please Wait' )
    ooo0O0o0OoOO = open ( file ) . read ( )
    oOo0000ooO = ooo0O0o0OoOO . replace ( 'addon="xbmc.python" version="1.0"' , 'addon="xbmc.python" version="2.1.0"' ) . replace ( 'addon="xbmc.python" version="2.0"' , 'addon="xbmc.python" version="2.1.0"' )
    IiI1 = open ( file , mode = 'w' )
    IiI1 . write ( str ( oOo0000ooO ) )
    IiI1 . close ( )
    if 14 - 14: iI1iiIiiII . iI1iiIiiII % iIII
 OooO0 = xbmcgui . Dialog ( )
 OooO0 . ok ( "Your addons have now been made compatible" , "If you still find you have addons that aren't working please run the addon so it throws up a script error, upload a log and post details on the relevant support forum." )
 if 42 - 42: o0oOOo0O0Ooo . Oo - iIII
 if 33 - 33: II111iiii / O0 / iI1iiIiiII - iii - i1IIi
def IiIiiI ( ) :
 OooO0 = xbmcgui . Dialog ( )
 OoOoO0oO00O = xbmcgui . Dialog ( ) . yesno ( 'Convert Addons To Gotham' , 'This will edit your addon.xml files so they show as Gotham compatible. It\'s doubtful this will have any effect on whether or not they work but it will get rid of the annoying incompatible pop-up message. Do you wish to continue?' )
 if 79 - 79: OoooooooOO / I1IiiI
 if OoOoO0oO00O == 1 :
  I1I11i ( )
  if 87 - 87: iI1iiIiiII . i1IIi % OoooooooOO * i11iIiiIii
  if 67 - 67: OOo00O0 / OoO0O00 . OoooooooOO
def OoIIiIIIII1I ( url ) :
 global oooooOoo0ooo
 if 96 - 96: i11iIiiIii . II111iiii
 if o0O . getSetting ( 'adult' ) == 'true' :
  iIiI = 'yes'
  if 7 - 7: i1IIi
 else :
  iIiI = 'no'
  if 63 - 63: iIii1I11I1II1 + iI1iiIiiII % i1IIi / I1IiiI % II111iiii
 OO0iiiii1iiIIii = 'http://noobsandnerds.com/TI/AddonPortal/sortby_new.php?sortx=name&user=%s&adult=%s&%s' % ( o0oOoO00o , iIiI , url )
 i11I1IiII1i1i = ooI1111i ( OO0iiiii1iiIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 8 - 8: I1ii11iIi11i * I1ii11iIi11i * i1IIi + oOoO0o00OO0 . I1ii11iIi11i
 I111i1I1 = re . compile ( 'name="(.+?)"  <br> downloads="(.+?)"  <br> icon="(.+?)"  <br> broken="(.+?)"  <br> UID="(.+?)"  <br>' , re . DOTALL ) . findall ( i11I1IiII1i1i )
 if I111i1I1 == [ ] :
  if 100 - 100: OoooooooOO - O0 . iii / iii + II111iiii * OoOoOO00
  I111i1I1 = re . compile ( 'name="(.+?)" <br> downloads="(.+?)" <br> icon="(.+?)" <br> broken="(.+?)" <br> UID="(.+?)" <br>' , re . DOTALL ) . findall ( i11I1IiII1i1i )
 print I111i1I1
 if 37 - 37: Oo0Ooo
 if I111i1I1 != [ ] :
  O00Oo00o00O ( OO0iiiii1iiIIii , 'addons' )
  if 15 - 15: iii / Oo0Ooo * iii
  for I1ii1 , i1iI1 , i11111I1I , i1ii1II1ii , I1111I1Ii in I111i1I1 :
   if 68 - 68: OoO0O00 + I1IiiI * o0oOOo0O0Ooo . ooOo + OoOoOO00 + iIII
   if i1ii1II1ii == '0' :
    OOo0oO00ooO00 ( 'folder2' , I1ii1 + '[COLOR=lime] [' + i1iI1 + ' downloads][/COLOR]' , I1111I1Ii , 'addon_final_menu' , i11111I1I , '' , '' )
    if 80 - 80: OoOoOO00 * Oo
   if i1ii1II1ii == '1' :
    OOo0oO00ooO00 ( 'folder2' , '[COLOR=red]' + I1ii1 + ' [REPORTED AS BROKEN][/COLOR]' , I1111I1Ii , 'addon_final_menu' , i11111I1I , '' , '' )
    if 47 - 47: iIII
 elif '&redirect' in url :
  iIi1IiI = OooO0 . yesno ( 'No Content Found' , 'This add-on cannot be found on the Add-on Portal.' , '' , 'Would you like to remove this item from your setup?' )
  if 63 - 63: II111iiii / i11iIiiIii % II111iiii . I1ii11iIi11i
  if iIi1IiI == 1 : print "remove"
  if 6 - 6: Oo + i11iIiiIii
 else :
  OooO0 . ok ( 'No Content Found' , 'Sorry no content can be found that matches' , 'your search criteria.' , '' )
  if 26 - 26: iI1iiIiiII / OoO0 - OoooooooOO
  if 9 - 9: OoooooooOO * I1ii11iIi11i
def iI1II1i ( url ) :
 if zip == '' :
  OooO0 . ok ( 'Storage/Download Folder Not Set' , 'You have not set your backup storage folder.\nPlease update the addon settings and try again.' , '' , '' )
  o0O . openSettings ( sys . argv [ 0 ] )
  if 27 - 27: I1ii11iIi11i / Oo
 if o0O . getSetting ( 'adult' ) == 'true' :
  iIiI = ''
  if 33 - 33: OoooooooOO % I1ii11iIi11i . O0 / I1ii11iIi11i
 else :
  iIiI = 'no'
  if 63 - 63: iI1iiIiiII + iIii1I11I1II1 + I1IiiI + OOo00O0
 if not 'id=' in url :
  OO0iiiii1iiIIii = 'http://120.24.252.100/TI/Community_Builds/sortby.php?sortx=name&orderx=ASC&adult=%s&%s' % ( iIiI , url )
  i11I1IiII1i1i = ooI1111i ( OO0iiiii1iiIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
  if 72 - 72: OoO0O00 + i11iIiiIii + I1ii11iIi11i
  I111i1I1 = re . compile ( 'name="(.+?)"  <br> id="(.+?)"  <br> Thumbnail="(.+?)"  <br> Fanart="(.+?)"  <br> downloads="(.+?)"  <br> <br>' , re . DOTALL ) . findall ( i11I1IiII1i1i )
  if I111i1I1 == [ ] :
   if 96 - 96: ooOo % i1IIi / o0oOOo0O0Ooo
   I111i1I1 = re . compile ( 'name="(.+?)" <br> id="(.+?)" <br> Thumbnail="(.+?)" <br> Fanart="(.+?)" <br> downloads="(.+?)" <br> <br>' , re . DOTALL ) . findall ( i11I1IiII1i1i )
  O00Oo00o00O ( url , 'communitybuilds' )
  if 13 - 13: II111iiii - Oo0Ooo % i11iIiiIii + oOoO0o00OO0
  for I1ii1 , id , ooOooOoo , Oooo0Oo00o , i1iI1 in I111i1I1 :
   II1I ( I1ii1 + '[COLOR=lime] (' + i1iI1 + ' downloads)[/COLOR]' , id + url , 'community_menu' , ooOooOoo , Oooo0Oo00o , id , '' , '' , '' , '' )
   if 32 - 32: OoOoOO00 . iIii1I11I1II1 % ooOo . O0 . OoOoOO00 / oOoO0o00OO0
 if 'id=1' in url : OO0iiiii1iiIIii = i1iiIII111ii
 if 'id=2' in url : OO0iiiii1iiIIii = ii11iIi1I
 if 'id=3' in url : OO0iiiii1iiIIii = OOooO0OOoo
 if 'id=4' in url : OO0iiiii1iiIIii = oOOoO0
 if 'id=5' in url : OO0iiiii1iiIIii = iiI1IiI
 if 45 - 45: iIii1I11I1II1
 i11I1IiII1i1i = ooI1111i ( OO0iiiii1iiIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I111i1I1 = re . compile ( 'name="(.+?)".+?rl="(.+?)".+?mg="(.+?)".+?anart="(.+?)".+?escription="(.+?)"' ) . findall ( i11I1IiII1i1i )
 if 41 - 41: oOoO0o00OO0 % oOoO0o00OO0 - iI1iiIiiII % OoO0O00 - OoooooooOO - oOoO0o00OO0
 for I1ii1 , url , Ii1IiIiIi1IiI , i1iiIIi1I , I1iii in I111i1I1 :
  if not 'viewport' in I1ii1 :
   OOo0oO00ooO00 ( 'addon' , I1ii1 , url , 'restore_local_CB' , Ii1IiIiIi1IiI , i1iiIIi1I , I1iii , '' )
   if 66 - 66: o0oOOo0O0Ooo % OoOoOO00
   if 30 - 30: OoOoOO00 * Oo0Ooo % iIii1I11I1II1 % OoO0O00 + i11iIiiIii
def IiOo00O0o0O ( url ) :
 OO0iiiii1iiIIii = 'http://noobsandnerds.com/TI/HardwarePortal/sortby.php?sortx=Added&orderx=DESC&%s' % ( url )
 i11I1IiII1i1i = ooI1111i ( OO0iiiii1iiIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 86 - 86: iii + O0 + Oo0Ooo - iii
 I111i1I1 = re . compile ( 'name="(.+?)"  <br> id="(.+?)"  <br> thumb="(.+?)"  <br><br>' , re . DOTALL ) . findall ( i11I1IiII1i1i )
 if I111i1I1 == [ ] :
  if 34 - 34: II111iiii % I1IiiI % OOo00O0 + Oo0Ooo - OoOoOO00
  I111i1I1 = re . compile ( 'name="(.+?)" <br> id="(.+?)" <br> thumb="(.+?)" <br><br>' , re . DOTALL ) . findall ( i11I1IiII1i1i )
 O00Oo00o00O ( OO0iiiii1iiIIii , 'hardware' )
 if 66 - 66: OoO0 * iIii1I11I1II1 - iIII / I1IiiI
 for I1ii1 , id , o0i1I in I111i1I1 :
  OOo0oO00ooO00 ( 'folder2' , I1ii1 , id , 'hardware_final_menu' , o0i1I , '' , '' )
  if 76 - 76: iii % iI1iiIiiII / iI1iiIiiII / OoO0O00 % ooOo . iIii1I11I1II1
  if 85 - 85: OoO0
def Oo0O0OooOooo0 ( url ) :
 OO0iiiii1iiIIii = 'http://noobsandnerds.com/TI/LatestNews/sortby.php?sortx=item_date&orderx=DESC&%s' % ( url )
 i11I1IiII1i1i = ooI1111i ( OO0iiiii1iiIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 81 - 81: ooOo - Oo
 I111i1I1 = re . compile ( 'name="(.+?)"  <br> date="(.+?)"  <br> source="(.+?)"  <br> id="(.+?)"  <br><br>' , re . DOTALL ) . findall ( i11I1IiII1i1i )
 if I111i1I1 == [ ] :
  if 21 - 21: Oo0Ooo * o0oOOo0O0Ooo + OoooooooOO . OOo00O0 % ooOo
  I111i1I1 = re . compile ( 'name="(.+?)" <br> date="(.+?)" <br> source="(.+?)" <br> id="(.+?)" <br><br>' , re . DOTALL ) . findall ( i11I1IiII1i1i )
 for I1ii1 , IIIIIiiI , i1iIii , id in I111i1I1 :
  if 95 - 95: iii / iI1iiIiiII . O0 * iI1iiIiiII - o0oOOo0O0Ooo * Oo0Ooo
  if "OpenELEC" in i1iIii :
   OOo0oO00ooO00 ( '' , I1ii1 + '  (' + IIIIIiiI + ')' , id , 'news_menu' , 'OpenELEC.png' , '' , '' )
   if 6 - 6: OoOoOO00 . II111iiii * I1IiiI . I1IiiI / OoO0
  if "Official" in i1iIii :
   OOo0oO00ooO00 ( '' , I1ii1 + '  (' + IIIIIiiI + ')' , id , 'news_menu' , 'XBMC.png' , '' , '' )
   if 14 - 14: OOo00O0 % iI1iiIiiII - O0 / OOo00O0
  if "Raspbmc" in i1iIii :
   OOo0oO00ooO00 ( '' , I1ii1 + '  (' + IIIIIiiI + ')' , id , 'news_menu' , 'Raspbmc.png' , '' , '' )
   if 91 - 91: i11iIiiIii % OOo00O0 * ooOo - I1ii11iIi11i . OOo00O0
  if "XBMC4Xbox" in i1iIii :
   OOo0oO00ooO00 ( '' , I1ii1 + '  (' + IIIIIiiI + ')' , id , 'news_menu' , 'XBMC4Xbox.png' , '' , '' )
   if 28 - 28: i11iIiiIii
  if "noobsandnerds" in i1iIii :
   OOo0oO00ooO00 ( '' , I1ii1 + '  (' + IIIIIiiI + ')' , id , 'news_menu' , 'noobsandnerds.png' , '' , '' )
   if 51 - 51: I1IiiI + iIII * O0 . OoO0
   if 82 - 82: Oo * I1ii11iIi11i % OoO0 . Oo
def iI1oOoo ( url ) :
 OO0iiiii1iiIIii = 'http://noobsandnerds.com/TI/TutorialPortal/sortby.php?sortx=Name&orderx=ASC&%s' % ( url )
 i11I1IiII1i1i = ooI1111i ( OO0iiiii1iiIIii ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 if 59 - 59: iI1iiIiiII % OoO0
 I111i1I1 = re . compile ( 'name="(.+?)"  <br> about="(.+?)"  <br> id="(.+?)"  <br><br>' , re . DOTALL ) . findall ( i11I1IiII1i1i )
 if I111i1I1 == [ ] :
  if 57 - 57: iii . O0 % OoooooooOO . I1IiiI . i1IIi - II111iiii
  I111i1I1 = re . compile ( 'name="(.+?)" <br> about="(.+?)" <br> id="(.+?)" <br><br>' , re . DOTALL ) . findall ( i11I1IiII1i1i )
 O00Oo00o00O ( OO0iiiii1iiIIii , 'tutorials' )
 if 61 - 61: O0 . o0oOOo0O0Ooo / OoOoOO00
 for I1ii1 , oo000oOOo0Oo , id in I111i1I1 :
  OOo0oO00ooO00 ( 'folder' , I1ii1 , id , 'tutorial_final_menu' , 'Tutorials.png' , '' , oo000oOOo0Oo )
  if 91 - 91: II111iiii - iIii1I11I1II1 / i1IIi * i1IIi % Oo0Ooo
  if 82 - 82: iIII
def OoOooO0 ( url , local ) :
 III1II1i ( )
 iIi1IiI = xbmcgui . Dialog ( ) . yesno ( I1ii1 , 'This will over-write your existing guisettings.xml.' , 'Are you sure this is the build you have installed?' , '' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Fix' )
 if 9 - 9: OoOoOO00 - iI1iiIiiII
 if iIi1IiI == 1 :
  iiIi ( url , local )
  if 31 - 31: i11iIiiIii + iI1iiIiiII - OOo00O0 * oOoO0o00OO0
  if 60 - 60: oOoO0o00OO0 + OoO0O00 + iii % iIii1I11I1II1 . Oo0Ooo
def iiIi ( url , local ) :
 O0OOOOoO00oo = False
 OoOiII11IiIi = 0
 iII1I1i = 1
 if 6 - 6: ooOo / O0 / OoO0 / iI1iiIiiII / ooOo . iIii1I11I1II1
 if os . path . exists ( Oo0oOOo ) :
  os . remove ( Oo0oOOo )
  if 62 - 62: iIii1I11I1II1
 if os . path . exists ( IIIII ) :
  os . remove ( IIIII )
  if 4 - 4: I1ii11iIi11i * iii . iii . II111iiii / Oo
 if os . path . exists ( o00oOO0 ) :
  os . remove ( o00oOO0 )
  if 86 - 86: ooOo % O0 + OoO0O00
 if not os . path . exists ( Oo0OoO00oOO0o ) :
  os . makedirs ( Oo0OoO00oOO0o )
  if 52 - 52: Oo0Ooo / oOoO0o00OO0
  if 42 - 42: iIii1I11I1II1 * OoO0 / OoO0O00 + Oo
 try :
  shutil . copyfile ( I11II1i , Oo0oOOo )
  if 48 - 48: OoooooooOO - OOo00O0 . i11iIiiIii * oOoO0o00OO0 - OoO0 - o0oOOo0O0Ooo
 except :
  print "No guisettings found, most likely due to a previously failed attempt at install"
  if 59 - 59: oOoO0o00OO0 / iii . Oo0Ooo
 if local != 1 :
  o0III11IiI = os . path . join ( OOO0OOO00oo , 'guifix.zip' )
  if 53 - 53: oOoO0o00OO0 / i1IIi / i1IIi
 else :
  o0III11IiI = xbmc . translatePath ( url )
  if 77 - 77: iii + i1IIi . iii
  if 89 - 89: o0oOOo0O0Ooo + Oo * ooOo
 i1iI1IIi = str ( os . path . getsize ( o0III11IiI ) )
 II11iiii1Ii . create ( "Installing Skin Fix" , "Checking " , '' , 'Please Wait' )
 II11iiii1Ii . update ( 0 , "" , "Extracting Zip Please Wait" )
 oOOO ( o0III11IiI , Oo0OoO00oOO0o , II11iiii1Ii )
 if 27 - 27: O0 / OoO0O00
 if local != 'library' or local != 'updatelibrary' or local != 'fresh' :
  if 99 - 99: OoO0 - iI1iiIiiII * iIii1I11I1II1 . II111iiii
  try :
   O00Ooo0ooo0 = open ( Oo0OoO00oOO0o + 'profiles.xml' , mode = 'r' )
   OooO00o000 = O00Ooo0ooo0 . read ( )
   O00Ooo0ooo0 . close ( )
   if 36 - 36: iii - iI1iiIiiII . iI1iiIiiII
   if os . path . exists ( Oo0OoO00oOO0o + 'profiles.xml' ) :
    if 60 - 60: i11iIiiIii * Oo0Ooo % OoO0O00 + OoO0O00
    if local == None :
     iIi1IiI = xbmcgui . Dialog ( ) . yesno ( "PROFILES DETECTED" , 'This build has profiles included, would you like to overwrite your existing profiles or keep the ones you have?' , '' , '' , nolabel = 'Keep my profiles' , yeslabel = 'Use new profiles' )
     if 84 - 84: iIii1I11I1II1 + OoooooooOO
    if local != None :
     iIi1IiI = 1
     if 77 - 77: O0 * I1ii11iIi11i * ooOo + OoO0O00 + I1ii11iIi11i - OOo00O0
    if iIi1IiI == 1 :
     iIIiooO00O00oOO = open ( o00oOO0 , mode = 'w' )
     time . sleep ( 1 )
     iIIiooO00O00oOO . write ( OooO00o000 )
     time . sleep ( 1 )
     iIIiooO00O00oOO . close ( )
     iII1I1i = 0
     if 10 - 10: I1ii11iIi11i + iI1iiIiiII
  except :
   print "no profiles.xml file"
   if 58 - 58: I1IiiI + OoooooooOO / oOoO0o00OO0 . iIII % o0oOOo0O0Ooo / I1ii11iIi11i
   if 62 - 62: II111iiii
 os . rename ( Oo0OoO00oOO0o + 'guisettings.xml' , IIIII )
 if 12 - 12: iI1iiIiiII + II111iiii
 if local != 'fresh' :
  O0Ooo00o00O = OooO0 . yesno ( "Do You Want To Keep Your Kodi Settings?" , 'Would you like to keep your existing settings or would you rather erase them and install the ones associated with this latest build?' , nolabel = 'Keep my settings' , yeslabel = 'Replace my settings' )
  if 80 - 80: oOoO0o00OO0
 if local == 'fresh' :
  O0Ooo00o00O = 1
  if 3 - 3: I1ii11iIi11i * iii
 if O0Ooo00o00O == 1 :
  if 53 - 53: iIii1I11I1II1 / oOoO0o00OO0 % OoO0O00 + iI1iiIiiII / iIII
  if os . path . exists ( I11II1i ) :
   if 74 - 74: Oo0Ooo
   try :
    print "Attempting to remove guisettings"
    os . remove ( I11II1i )
    O0OOOOoO00oo = True
    if 8 - 8: I1IiiI % II111iiii - o0oOOo0O0Ooo - iii % I1IiiI
   except :
    print "Problem removing guisettings"
    O0OOOOoO00oo = False
    if 93 - 93: OoO0 * oOoO0o00OO0 / Oo
   try :
    print "Attempting to replace guisettings with new"
    os . rename ( IIIII , I11II1i )
    O0OOOOoO00oo = True
    if 88 - 88: ooOo
   except :
    print "Failed to replace guisettings with new"
    O0OOOOoO00oo = False
    if 1 - 1: Oo0Ooo
    if 95 - 95: OoooooooOO / iii % OoooooooOO / iIII * iI1iiIiiII
 if O0Ooo00o00O == 0 :
  Oo0oO00 = open ( Oo0oOOo , mode = 'r' )
  iiiO00O00O000OOO = Oo0oO00 . read ( )
  Oo0oO00 . close ( )
  if 75 - 75: O0
  oOoO = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( iiiO00O00O000OOO )
  OOooooO = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( iiiO00O00O000OOO )
  oOoo00 = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( iiiO00O00O000OOO )
  IIiIi = oOoO [ 0 ] if ( len ( oOoO ) > 0 ) else ''
  I1I1IIiiI1 = OOooooO [ 0 ] if ( len ( OOooooO ) > 0 ) else ''
  oooOOO0o0O0 = oOoo00 [ 0 ] if ( len ( oOoo00 ) > 0 ) else ''
  if 31 - 31: OoooooooOO - ooOo / OOo00O0
  if 62 - 62: i11iIiiIii - iii
  i1iiiiI11ii = open ( IIIII , mode = 'r' )
  oooooOOo0o = i1iiiiI11ii . read ( )
  i1iiiiI11ii . close ( )
  if 81 - 81: iii
  OOOOooO0 = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( oooooOOo0o )
  Iii11ii1iIIi = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( oooooOOo0o )
  iiii1Ii1iii = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( oooooOOo0o )
  Oo0Oo0 = OOOOooO0 [ 0 ] if ( len ( OOOOooO0 ) > 0 ) else ''
  oooOooooO = Iii11ii1iIIi [ 0 ] if ( len ( Iii11ii1iIIi ) > 0 ) else ''
  i1I = iiii1Ii1iii [ 0 ] if ( len ( iiii1Ii1iii ) > 0 ) else ''
  i1I1 = iiiO00O00O000OOO . replace ( IIiIi , Oo0Oo0 ) . replace ( oooOOO0o0O0 , i1I ) . replace ( I1I1IIiiI1 , oooOooooO )
  if 49 - 49: i1IIi - OoOoOO00 . Oo0Ooo + iIii1I11I1II1 - iIII / Oo0Ooo
  iIIiooO00O00oOO = open ( Oo0oOOo , mode = 'w+' )
  iIIiooO00O00oOO . write ( str ( i1I1 ) )
  iIIiooO00O00oOO . close ( )
  if 24 - 24: ooOo - oOoO0o00OO0 / iIII
  if 10 - 10: OoOoOO00 * i1IIi
  if os . path . exists ( I11II1i ) :
   if 15 - 15: iii + i1IIi - II111iiii % I1IiiI
   try :
    os . remove ( I11II1i )
    O0OOOOoO00oo = True
    if 34 - 34: I1IiiI
   except :
    O0OOOOoO00oo = False
    if 57 - 57: Oo . OoO0 % o0oOOo0O0Ooo
  try :
   os . rename ( Oo0oOOo , I11II1i )
   os . remove ( IIIII )
   O0OOOOoO00oo = True
   if 32 - 32: iii / iI1iiIiiII - O0 * iIii1I11I1II1
  except :
   O0OOOOoO00oo = False
   if 70 - 70: OoooooooOO % OoooooooOO % OoO0O00
   if 98 - 98: OoO0O00
 if O0OOOOoO00oo == True or local == None :
  if 18 - 18: iii + Oo0Ooo - OoO0O00 / OOo00O0 / Oo
  try :
   Oo0oO00 = open ( Ooo0OO0oOO , mode = 'r' )
   iiiO00O00O000OOO = Oo0oO00 . read ( )
   Oo0oO00 . close ( )
   if 53 - 53: Oo + o0oOOo0O0Ooo . ooOo / iii
   o0000oO = re . compile ( 'id="(.+?)"' ) . findall ( iiiO00O00O000OOO )
   ooo0ooOoOoO = re . compile ( 'name="(.+?)"' ) . findall ( iiiO00O00O000OOO )
   o0o00OoOO = re . compile ( 'version="(.+?)"' ) . findall ( iiiO00O00O000OOO )
   Iii1iii1I = o0000oO [ 0 ] if ( len ( o0000oO ) > 0 ) else ''
   oOo000Oo00o = ooo0ooOoOoO [ 0 ] if ( len ( ooo0ooOoOoO ) > 0 ) else ''
   i1Ii11I1II = o0o00OoOO [ 0 ] if ( len ( o0o00OoOO ) > 0 ) else ''
   if 81 - 81: OoooooooOO
   iIIiooO00O00oOO = open ( ii11i1 , mode = 'w+' )
   iIIiooO00O00oOO . write ( 'id="' + str ( Iii1iii1I ) + '"\nname="' + oOo000Oo00o + '"\nversion="' + i1Ii11I1II + '"\ngui="' + i1iI1IIi + '"' )
   iIIiooO00O00oOO . close ( )
   if 88 - 88: O0 * o0oOOo0O0Ooo
   Oo0oO00 = open ( iiii11I , mode = 'r' )
   iiiO00O00O000OOO = Oo0oO00 . read ( )
   Oo0oO00 . close ( )
   if 44 - 44: o0oOOo0O0Ooo / I1ii11iIi11i . Oo0Ooo + OoOoOO00
   O00O00 = re . compile ( 'version="(.+?)"' ) . findall ( iiiO00O00O000OOO )
   IIIi1I1IIii1II = O00O00 [ 0 ] if ( len ( O00O00 ) > 0 ) else ''
   i1I1 = iiiO00O00O000OOO . replace ( IIIi1I1IIii1II , i1Ii11I1II )
   if 32 - 32: iI1iiIiiII - iIII * oOoO0o00OO0 * iii
   iIIiooO00O00oOO = open ( iiii11I , mode = 'w' )
   iIIiooO00O00oOO . write ( str ( i1I1 ) )
   iIIiooO00O00oOO . close ( )
   os . remove ( Ooo0OO0oOO )
   if 84 - 84: OoO0 + I1ii11iIi11i % I1IiiI + i11iIiiIii
  except :
   iIIiooO00O00oOO = open ( ii11i1 , mode = 'w+' )
   iIIiooO00O00oOO . write ( 'id="None"\nname="Unknown"\nversion="Unknown"\ngui="' + i1iI1IIi + '"' )
   iIIiooO00O00oOO . close ( )
   if 37 - 37: iii % I1ii11iIi11i / iIII
   if 94 - 94: iii / OoO0O00 . o0oOOo0O0Ooo
 if os . path . exists ( Oo0OoO00oOO0o + 'profiles.xml' ) :
  os . remove ( Oo0OoO00oOO0o + 'profiles.xml' )
  time . sleep ( 1 )
  if 1 - 1: Oo0Ooo . II111iiii
 if os . path . exists ( Oo0OoO00oOO0o ) :
  os . removedirs ( Oo0OoO00oOO0o )
  if 93 - 93: II111iiii . i11iIiiIii + II111iiii % ooOo
 O00OOO000oo0 = xbmc . translatePath ( os . path . join ( O0o0Oo , I1IiI , 'notification.txt' ) )
 if 16 - 16: iIii1I11I1II1 * oOoO0o00OO0 + ooOo . O0 . o0oOOo0O0Ooo
 if os . path . exists ( O00OOO000oo0 ) :
  os . remove ( O00OOO000oo0 )
  if 99 - 99: i11iIiiIii - oOoO0o00OO0
 if O0OOOOoO00oo == True :
  o0O0O0O00o ( )
  OoOooOo00o ( )
  if 28 - 28: I1ii11iIi11i + I1ii11iIi11i % OoOoOO00
  if 12 - 12: iii
def I11iIi1i1I1i1 ( url ) :
 Oo0O00O000 = 'http://noobsandnerds.com/TI/HardwarePortal/hardwaredetails.php?id=%s' % ( url )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0oO = re . compile ( 'name="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiiiii1ii1 = re . compile ( 'manufacturer="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i11i11i = re . compile ( 'video_guide1="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiI1iI = re . compile ( 'video_guide2="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Ooo00O0 = re . compile ( 'video_guide3="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OoO0OOoO0 = re . compile ( 'video_guide4="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiI11i = re . compile ( 'video_guide5="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0OoiiI1i = re . compile ( 'video_label1="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i11I = re . compile ( 'video_label2="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0oO0o0oo0O0 = re . compile ( 'video_label3="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O0oo00oOOO0o = re . compile ( 'video_label4="(.+?)"' ) . findall ( i11I1IiII1i1i )
 II1i = re . compile ( 'video_label5="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iIIII1i1 = re . compile ( 'shops="(.+?)"' ) . findall ( i11I1IiII1i1i )
 II11iI1iiI = re . compile ( 'description="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1I1oO00o0oOoo = re . compile ( 'screenshot1="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oOOI1 = re . compile ( 'screenshot2="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OOI1i = re . compile ( 'screenshot3="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i1II1iII1 = re . compile ( 'screenshot4="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I11II11IiI11 = re . compile ( 'screenshot5="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O00o = re . compile ( 'screenshot6="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Ii11Iiii1iiii = re . compile ( 'screenshot7="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i1IIII1111 = re . compile ( 'screenshot8="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Ooo0o0000OO = re . compile ( 'screenshot9="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iIiI1II1I1 = re . compile ( 'screenshot10="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OooiIiI1i1Ii = re . compile ( 'screenshot11="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Oo0o00o = re . compile ( 'screenshot12="(.+?)"' ) . findall ( i11I1IiII1i1i )
 III1I1 = re . compile ( 'screenshot13="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iI1IIIIII = re . compile ( 'screenshot14="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OO0oO0Oo = re . compile ( 'added="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I11iIiI1I1i11 = re . compile ( 'platform="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OoooOO0 = re . compile ( 'chipset="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oo0OoO = re . compile ( 'official_guide="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iIIi1iii1 = re . compile ( 'official_preview="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IiiI1II1II1i = re . compile ( 'thumbnail="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o00o0 = re . compile ( 'stock_rom="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OOoOo0O0 = re . compile ( 'CPU="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1o0 = re . compile ( 'GPU="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1IiiiiI1i1I = re . compile ( 'RAM="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I11i1I1 = re . compile ( 'flash="(.+?)"' ) . findall ( i11I1IiII1i1i )
 ooOooO = re . compile ( 'wifi="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oooo = re . compile ( 'bluetooth="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IIIiI1iIIII = re . compile ( 'LAN="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0oo00OOOo = re . compile ( 'xbmc_version="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oo0oOi1i1IIi = re . compile ( 'pros="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0oo0Ooo0 = re . compile ( 'cons="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0OOoO = re . compile ( 'library_scan="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1iII1II1I1ii = re . compile ( '4k="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oo0OO0O = re . compile ( '1080="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OO0OooOOoO00OO00 = re . compile ( '720="(.+?)"' ) . findall ( i11I1IiII1i1i )
 ii11ii1iIiI1 = re . compile ( '3D="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OoOo0oO0 = re . compile ( 'DTS="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i111iIi1i1 = re . compile ( 'BootTime="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OOo00O0O = re . compile ( 'CopyFiles="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oooOoO = re . compile ( 'CopyVideo="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IiiIi1IiiiI = re . compile ( 'EthernetTest="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OO0oooOO = re . compile ( 'Slideshow="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IIIi1iiIIiiiI = re . compile ( 'total_review="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1IIiIi1iI = re . compile ( 'whufclee_review="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oOo0Iiii11 = re . compile ( 'CB_Premium="(.+?)"' ) . findall ( i11I1IiII1i1i )
 if 65 - 65: OOo00O0 + oOoO0o00OO0 * oOoO0o00OO0
 I1ii1 = oo0oO [ 0 ] if ( len ( oo0oO ) > 0 ) else ''
 OoOO = iiiiii1ii1 [ 0 ] if ( len ( iiiiii1ii1 ) > 0 ) else ''
 I1I = i11i11i [ 0 ] if ( len ( i11i11i ) > 0 ) else 'None'
 ooooo = iiI1iI [ 0 ] if ( len ( iiI1iI ) > 0 ) else 'None'
 i11IIIiI1I = Ooo00O0 [ 0 ] if ( len ( Ooo00O0 ) > 0 ) else 'None'
 o0iiiI1I1iIIIi1 = OoO0OOoO0 [ 0 ] if ( len ( OoO0OOoO0 ) > 0 ) else 'None'
 Iii = iiI11i [ 0 ] if ( len ( iiI11i ) > 0 ) else 'None'
 O0Oo0o000oO = o0OoiiI1i [ 0 ] if ( len ( o0OoiiI1i ) > 0 ) else 'None'
 oO0o00oOOooO0 = i11I [ 0 ] if ( len ( i11I ) > 0 ) else 'None'
 OOOoO000 = o0oO0o0oo0O0 [ 0 ] if ( len ( o0oO0o0oo0O0 ) > 0 ) else 'None'
 oOOOO = O0oo00oOOO0o [ 0 ] if ( len ( O0oo00oOOO0o ) > 0 ) else 'None'
 IiIi1ii111i1 = II1i [ 0 ] if ( len ( II1i ) > 0 ) else 'None'
 iIO0oOoo00Oo0O = iIIII1i1 [ 0 ] if ( len ( iIIII1i1 ) > 0 ) else ''
 I1iii = II11iI1iiI [ 0 ] if ( len ( II11iI1iiI ) > 0 ) else ''
 Iii1i1Ii = I1I1oO00o0oOoo [ 0 ] if ( len ( I1I1oO00o0oOoo ) > 0 ) else ''
 III1iIii = oOOI1 [ 0 ] if ( len ( oOOI1 ) > 0 ) else ''
 iiIII1i1 = OOI1i [ 0 ] if ( len ( OOI1i ) > 0 ) else ''
 oOOo0OOoOO0 = i1II1iII1 [ 0 ] if ( len ( i1II1iII1 ) > 0 ) else ''
 IiIi = I11II11IiI11 [ 0 ] if ( len ( I11II11IiI11 ) > 0 ) else ''
 IIi1IiiIi1III = O00o [ 0 ] if ( len ( O00o ) > 0 ) else ''
 IiIiIiiIIii = Ii11Iiii1iiii [ 0 ] if ( len ( Ii11Iiii1iiii ) > 0 ) else ''
 OOo00O00o0O0 = i1IIII1111 [ 0 ] if ( len ( i1IIII1111 ) > 0 ) else ''
 iI1III = Ooo0o0000OO [ 0 ] if ( len ( Ooo0o0000OO ) > 0 ) else ''
 I1I111 = iIiI1II1I1 [ 0 ] if ( len ( iIiI1II1I1 ) > 0 ) else ''
 I1iI = OooiIiI1i1Ii [ 0 ] if ( len ( OooiIiI1i1Ii ) > 0 ) else ''
 IIiiI = Oo0o00o [ 0 ] if ( len ( Oo0o00o ) > 0 ) else ''
 ooO0 = III1I1 [ 0 ] if ( len ( III1I1 ) > 0 ) else ''
 IIOoOOoOo = iI1IIIIII [ 0 ] if ( len ( iI1IIIIII ) > 0 ) else ''
 Ii1 = OO0oO0Oo [ 0 ] if ( len ( OO0oO0Oo ) > 0 ) else ''
 OoOo0oOooOoOO = I11iIiI1I1i11 [ 0 ] if ( len ( I11iIiI1I1i11 ) > 0 ) else ''
 Iiiiii = OoooOO0 [ 0 ] if ( len ( OoooOO0 ) > 0 ) else ''
 IiIii1i11i1 = oo0OoO [ 0 ] if ( len ( oo0OoO ) > 0 ) else 'None'
 ooOOo00o0ooO = iIIi1iii1 [ 0 ] if ( len ( iIIi1iii1 ) > 0 ) else 'None'
 o0i1I = IiiI1II1II1i [ 0 ] if ( len ( IiiI1II1II1i ) > 0 ) else ''
 iIOO = o00o0 [ 0 ] if ( len ( o00o0 ) > 0 ) else ''
 I1III1I11I1 = OOoOo0O0 [ 0 ] if ( len ( OOoOo0O0 ) > 0 ) else ''
 oO000OoO00OoO = I1o0 [ 0 ] if ( len ( I1o0 ) > 0 ) else ''
 I1IiIi1iiI = I1IiiiiI1i1I [ 0 ] if ( len ( I1IiiiiI1i1I ) > 0 ) else ''
 iiII1II11i = I11i1I1 [ 0 ] if ( len ( I11i1I1 ) > 0 ) else ''
 ooO0OoooooOo0oOo0 = ooOooO [ 0 ] if ( len ( ooOooO ) > 0 ) else ''
 II11II = oooo [ 0 ] if ( len ( oooo ) > 0 ) else ''
 i1ii11 = IIIiI1iIIII [ 0 ] if ( len ( IIIiI1iIIII ) > 0 ) else ''
 iIii = o0oo00OOOo [ 0 ] if ( len ( o0oo00OOOo ) > 0 ) else ''
 IIIo00O = oo0oOi1i1IIi [ 0 ] if ( len ( oo0oOi1i1IIi ) > 0 ) else ''
 ii1I1I1 = o0oo0Ooo0 [ 0 ] if ( len ( o0oo0Ooo0 ) > 0 ) else ''
 oo0oOOO0oOoo = o0OOoO [ 0 ] if ( len ( o0OOoO ) > 0 ) else ''
 Ii1o0OOOoo0000 = I1iII1II1I1ii [ 0 ] if ( len ( I1iII1II1I1ii ) > 0 ) else ''
 IiIIii1i1i11iII = oo0OO0O [ 0 ] if ( len ( oo0OO0O ) > 0 ) else ''
 o0II1 = OO0OooOOoO00OO00 [ 0 ] if ( len ( OO0OooOOoO00OO00 ) > 0 ) else ''
 OOO = ii11ii1iIiI1 [ 0 ] if ( len ( ii11ii1iIiI1 ) > 0 ) else ''
 iiIII1I11iii = OoOo0oO0 [ 0 ] if ( len ( OoOo0oO0 ) > 0 ) else ''
 ooIii = i111iIi1i1 [ 0 ] if ( len ( i111iIi1i1 ) > 0 ) else ''
 o0OO00oOOO0o0 = OOo00O0O [ 0 ] if ( len ( OOo00O0O ) > 0 ) else ''
 iiii = oooOoO [ 0 ] if ( len ( oooOoO ) > 0 ) else ''
 oOOOOOoOOoo0 = IiiIi1IiiiI [ 0 ] if ( len ( IiiIi1IiiiI ) > 0 ) else ''
 oo0OOO0OOoOO = OO0oooOO [ 0 ] if ( len ( OO0oooOO ) > 0 ) else ''
 oOoOII1i1 = IIIi1iiIIiiiI [ 0 ] if ( len ( IIIi1iiIIiiiI ) > 0 ) else ''
 o0o0oo0OOo0O0 = I1IIiIi1iI [ 0 ] if ( len ( I1IIiIi1iI ) > 0 ) else 'None'
 iIIiiII11i1I1 = oOo0Iiii11 [ 0 ] if ( len ( oOo0Iiii11 ) > 0 ) else ''
 Ii111Ii1iiIi1 = str ( '[COLOR=dodgerblue]Added: [/COLOR]' + Ii1 + '[CR][COLOR=dodgerblue]Manufacturer: [/COLOR]' + OoOO + '[CR][COLOR=dodgerblue]Supported Roms: [/COLOR]' + OoOo0oOooOoOO + '[CR][COLOR=dodgerblue]Chipset: [/COLOR]' + Iiiiii + '[CR][COLOR=dodgerblue]CPU: [/COLOR]' + I1III1I11I1 + '[CR][COLOR=dodgerblue]GPU: [/COLOR]' + oO000OoO00OoO + '[CR][COLOR=dodgerblue]RAM: [/COLOR]' + I1IiIi1iiI + '[CR][COLOR=dodgerblue]Flash: [/COLOR]' + iiII1II11i + '[CR][COLOR=dodgerblue]Wi-Fi: [/COLOR]' + ooO0OoooooOo0oOo0 + '[CR][COLOR=dodgerblue]Bluetooth: [/COLOR]' + II11II + '[CR][COLOR=dodgerblue]LAN: [/COLOR]' + i1ii11 + '[CR][CR][COLOR=yellow]About: [/COLOR]' + I1iii + '[CR][CR][COLOR=yellow]Summary:[/COLOR][CR][CR][COLOR=dodgerblue]Pros:[/COLOR]    ' + IIIo00O + '[CR][CR][COLOR=dodgerblue]Cons:[/COLOR]  ' + ii1I1I1 + '[CR][CR][COLOR=yellow]Benchmark Results:[/COLOR][CR][CR][COLOR=dodgerblue]Boot Time:[/COLOR][CR]' + ooIii + '[CR][CR][COLOR=dodgerblue]Time taken to scan 1,000 movies (local NFO files):[/COLOR][CR]' + oo0oOOO0oOoo + '[CR][CR][COLOR=dodgerblue]Copy 4,000 files (660.8MB) locally:[/COLOR][CR]' + o0OO00oOOO0o0 + '[CR][CR][COLOR=dodgerblue]Copy a MP4 file (339.4MB) locally:[/COLOR][CR]' + iiii + '[CR][CR][COLOR=dodgerblue]Ethernet Speed - Copy MP4 (339.4MB) from SMB share to device:[/COLOR][CR]' + oOOOOOoOOoo0 + '[CR][CR][COLOR=dodgerblue]4k Playback:[/COLOR][CR]' + Ii1o0OOOoo0000 + '[CR][CR][COLOR=dodgerblue]1080p Playback:[/COLOR][CR]' + IiIIii1i1i11iII + '[CR][CR][COLOR=dodgerblue]720p Playback:[/COLOR][CR]' + o0II1 + '[CR][CR][COLOR=dodgerblue]Audio Playback:[/COLOR][CR]' + iiIII1I11iii + '[CR][CR][COLOR=dodgerblue]Image Slideshow:[/COLOR][CR]' + oo0OOO0OOoOO )
 OOI11i1IIi1i1 = str ( '[COLOR=dodgerblue]Added: [/COLOR]' + Ii1 + '[CR][COLOR=dodgerblue]Manufacturer: [/COLOR]' + OoOO + '[CR][COLOR=dodgerblue]Supported Roms: [/COLOR]' + OoOo0oOooOoOO + '[CR][COLOR=dodgerblue]Chipset: [/COLOR]' + Iiiiii + '[CR][COLOR=dodgerblue]CPU: [/COLOR]' + I1III1I11I1 + '[CR][COLOR=dodgerblue]GPU: [/COLOR]' + oO000OoO00OoO + '[CR][COLOR=dodgerblue]RAM: [/COLOR]' + I1IiIi1iiI + '[CR][COLOR=dodgerblue]Flash: [/COLOR]' + iiII1II11i + '[CR][COLOR=dodgerblue]Wi-Fi: [/COLOR]' + ooO0OoooooOo0oOo0 + '[CR][COLOR=dodgerblue]Bluetooth: [/COLOR]' + II11II + '[CR][COLOR=dodgerblue]LAN: [/COLOR]' + i1ii11 + '[CR][CR][COLOR=yellow]About: [/COLOR]' + I1iii + '[CR][CR][COLOR=yellow]Summary:[/COLOR][CR][CR][COLOR=dodgerblue]Pros:[/COLOR]    ' + IIIo00O + '[CR][CR][COLOR=dodgerblue]Cons:[/COLOR]  ' + ii1I1I1 + '[CR][CR][COLOR=orange]4k Playback:[/COLOR]  ' + Ii1o0OOOoo0000 + '[CR][CR][COLOR=orange]1080p Playback:[/COLOR]  ' + IiIIii1i1i11iII + '[CR][CR][COLOR=orange]720p Playback:[/COLOR]  ' + o0II1 + '[CR][CR][COLOR=orange]DTS Compatibility:[/COLOR]  ' + iiIII1I11iii + '[CR][CR][COLOR=orange]Time taken to scan 100 movies:[/COLOR]  ' + oo0oOOO0oOoo )
 if 28 - 28: iii . OoooooooOO * Oo + i11iIiiIii % I1IiiI . iIii1I11I1II1
 if I1iii != '' and iIO0oOoo00Oo0O != '' :
  OOo0oO00ooO00 ( '' , '[COLOR=yellow][Text Guide][/COLOR]  Official Description' , Ii111Ii1iiIi1 , 'text_guide' , 'Tutorials.png' , iIi1ii1I1 , '' , '' )
 if I1iii != '' and iIO0oOoo00Oo0O == '' :
  OOo0oO00ooO00 ( '' , '[COLOR=yellow][Text Guide][/COLOR]  Official Description' , OOI11i1IIi1i1 , 'text_guide' , 'Tutorials.png' , iIi1ii1I1 , '' , '' )
 if o0o0oo0OOo0O0 != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]   Benchmark Review' , o0o0oo0OOo0O0 , 'play_video' , 'Video_Guide.png' , iIi1ii1I1 , '' , '' )
 if ooOOo00o0ooO != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]   Official Video Preview' , ooOOo00o0ooO , 'play_video' , 'Video_Guide.png' , iIi1ii1I1 , '' , '' )
 if IiIii1i11i1 != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]   Official Video Guide' , IiIii1i11i1 , 'play_video' , 'Video_Guide.png' , iIi1ii1I1 , '' , '' )
 if I1I != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + O0Oo0o000oO , I1I , 'play_video' , 'Video_Guide.png' , iIi1ii1I1 , '' , '' )
 if ooooo != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + oO0o00oOOooO0 , ooooo , 'play_video' , 'Video_Guide.png' , iIi1ii1I1 , '' , '' )
 if i11IIIiI1I != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + OOOoO000 , i11IIIiI1I , 'play_video' , 'Video_Guide.png' , iIi1ii1I1 , '' , '' )
 if o0iiiI1I1iIIIi1 != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + oOOOO , o0iiiI1I1iIIIi1 , 'play_video' , 'Video_Guide.png' , iIi1ii1I1 , '' , '' )
 if Iii != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + IiIi1ii111i1 , Iii , 'play_video' , 'Video_Guide.png' , iIi1ii1I1 , '' , '' )
  if 63 - 63: II111iiii - iii . OoOoOO00
  if 8 - 8: I1IiiI * iIII / iI1iiIiiII + OoOoOO00 . iI1iiIiiII - Oo
def Oo0O ( ) :
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
 if 60 - 60: Oo * iIII * OoO0O00
 if 64 - 64: iii / II111iiii / OoO0O00 - iIII * iIii1I11I1II1 . oOoO0o00OO0
def iIi11I1II ( url ) :
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
 if 93 - 93: I1ii11iIi11i - iIII % I1ii11iIi11i
 if 12 - 12: Oo + OoO0O00 * iii + OoO0 + iI1iiIiiII
 if 58 - 58: oOoO0o00OO0 * OoO0 - i11iIiiIii % I1ii11iIi11i
def I11O0O0o ( ) :
 o00OO00OoO = xbmc . getSkinDir ( )
 iI1i1IiIIIIi = xbmc . translatePath ( os . path . join ( O00o0OO , o00OO00OoO ) )
 if 45 - 45: OoOoOO00
 for ooO , o0Oo0oOooOoOo , I1i in os . walk ( iI1i1IiIIIIi ) :
  if 100 - 100: i1IIi % OoO0
  for IiI1 in I1i :
   if 55 - 55: I1IiiI + oOoO0o00OO0
   if 'DialogKeyboard.xml' in IiI1 :
    o00OO00OoO = os . path . join ( ooO , IiI1 )
    ooo0O0o0OoOO = open ( o00OO00OoO ) . read ( )
    iIi11i = ooo0O0o0OoOO . replace ( '<control type="label" id="310"' , '<control type="edit" id="312"' )
    IiI1 = open ( o00OO00OoO , mode = 'w' )
    IiI1 . write ( iIi11i )
    IiI1 . close ( )
    IiiIiI1I1 ( o00OO00OoO )
    if 85 - 85: ooOo + oOoO0o00OO0 % oOoO0o00OO0 / iii . I1IiiI - OoOoOO00
    for I1iii1I in range ( 48 , 58 ) :
     Ii1IIIII ( I1iii1I , o00OO00OoO )
     if 19 - 19: iii / oOoO0o00OO0 + iI1iiIiiII
 OooO0 = xbmcgui . Dialog ( )
 OooO0 . ok ( "Skin Changes Successful" , 'A BIG thank you to Mikey1234 for this fix. The code used for this function was ported from the Xunity Maintenance add-on' )
 xbmc . executebuiltin ( 'ReloadSkin()' )
 if 76 - 76: iIii1I11I1II1 / OOo00O0 - I1ii11iIi11i % o0oOOo0O0Ooo % Oo + OoooooooOO
def IIi1II1i111i ( ) :
 OooO0 = xbmcgui . Dialog ( )
 OoOoO0oO00O = xbmcgui . Dialog ( ) . yesno ( 'Convert This Skin To Kodi (Helix)?' , 'This will fix the problem with a blank on-screen keyboard showing in skins designed for Gotham (being run on Kodi). This will only affect the currently running skin.' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Fix' )
 if 58 - 58: iIII
 if OoOoO0oO00O == 1 :
  I11O0O0o ( )
  if 45 - 45: o0oOOo0O0Ooo
  if 67 - 67: oOoO0o00OO0 + iIII
def iiiiiI1II ( ) :
 if OooO0 . yesno ( "Hide Passwords" , "This will hide all your passwords in your" , "add-on settings, are you sure you wish to continue?" ) :
  for ooO , o0Oo0oOooOoOo , I1i in os . walk ( O00o0OO ) :
   for IiI1 in I1i :
    if IiI1 == 'settings.xml' :
     oOO000000oO0 = open ( os . path . join ( ooO , IiI1 ) ) . read ( )
     I111i1I1 = re . compile ( '<setting id=(.+?)>' ) . findall ( oOO000000oO0 )
     for o0o00o in I111i1I1 :
      if 'pass' in o0o00o :
       if not 'option="hidden"' in o0o00o :
        try :
         o0OOo0O00OO0O = o0o00o . replace ( '/' , ' option="hidden"/' )
         IiI1 = open ( os . path . join ( ooO , IiI1 ) , mode = 'w' )
         IiI1 . write ( str ( oOO000000oO0 ) . replace ( o0o00o , o0OOo0O00OO0O ) )
         IiI1 . close ( )
        except :
         pass
  OooO0 . ok ( "Passwords Hidden" , "Your passwords will now show as stars (hidden), if you want to undo this please use the option to unhide passwords." )
  if 58 - 58: ooOo
  if 50 - 50: OoooooooOO * I1ii11iIi11i - O0
def I1iO00O000oOO0oO ( url ) :
 Oo0O00O000 = 'http://noobsandnerds.com/IT/Community_Builds/guisettings.php?id=%s' % ( url )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 ii1IiiII = re . compile ( 'guisettings="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iIIiiiI1iI1 = ii1IiiII [ 0 ] if ( len ( ii1IiiII ) > 0 ) else 'None'
 if 88 - 88: o0oOOo0O0Ooo . I1IiiI % ooOo . Oo0Ooo % iIII . ooOo
 iiIi ( iIIiiiI1iI1 , OoO0ooOOoo )
 if 95 - 95: Oo0Ooo * Oo + I1IiiI . O0
 if 36 - 36: OoOoOO00 * OoO0O00 / iIII / I1IiiI - OoO0
def o0oOo0OoO ( path ) :
 I11iIiiI = xbmc . translatePath ( os . path . join ( Ooo , 'background_art' , '' ) )
 if 88 - 88: I1ii11iIi11i - iii * OoooooooOO * oOoO0o00OO0 . i11iIiiIii . o0oOOo0O0Ooo
 if os . path . exists ( I11iIiiI ) :
  oOo000O00O0 ( I11iIiiI )
  if 96 - 96: I1IiiI % I1IiiI / o0oOOo0O0Ooo / OoOoOO00 * iIII - OOo00O0
 time . sleep ( 1 )
 if 94 - 94: Oo0Ooo - iIii1I11I1II1 + I1IiiI - i1IIi + OoooooooOO % OoO0O00
 if not os . path . exists ( I11iIiiI ) :
  os . makedirs ( I11iIiiI )
  if 36 - 36: oOoO0o00OO0 * iii * O0 * Oo - o0oOOo0O0Ooo / I1ii11iIi11i
 try :
  II11iiii1Ii . create ( "Installing Artwork" , "Downloading artwork pack" , '' , 'Please Wait' )
  IIi11 = os . path . join ( OOO0OOO00oo , I1IiiI + '_artpack.zip' )
  downloader . download ( path , IIi11 , II11iiii1Ii )
  time . sleep ( 1 )
  II11iiii1Ii . create ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "Checking " , '' , 'Please Wait' )
  II11iiii1Ii . update ( 0 , "" , "Extracting Zip Please Wait" )
  oOOO ( IIi11 , I11iIiiI , II11iiii1Ii )
  if 54 - 54: i1IIi - OoO0O00 / OoooooooOO
 except :
  pass
  if 95 - 95: O0 + iIii1I11I1II1 . I1ii11iIi11i
  if 61 - 61: OoO0 * OoO0
def O0III1Iiii1i11 ( url ) :
 OOo0oO00ooO00 ( 'folder' , '[COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] Keywords' , '' , 'nan_menu' , 'Keywords.png' , '' , '' , '' )
 if 74 - 74: Oo0Ooo / OOo00O0 % OOo00O0 . iI1iiIiiII
 if o0oO0 == 'true' and oo00 != '' and o00 != '' :
  OOo0oO00ooO00 ( '' , 'Install ' + o00 + ' keyword' , oo00 , 'keywords' , 'Keywords.png' , '' , '' , '' )
  if 72 - 72: i1IIi
 if i11 == 'true' :
  OOo0oO00ooO00 ( 'folder' , 'Manage Add-ons' , oooooOoo0ooo , 'addonmenu' , 'Search_Addons.png' , '' , '' , '' )
  if 21 - 21: OOo00O0 . Oo / i11iIiiIii * i1IIi
 if I11 == 'true' :
  OOo0oO00ooO00 ( 'folder' , 'Community Builds' , url , 'community' , 'Community_Builds.png' , '' , '' , '' )
  if 82 - 82: iIII * Oo0Ooo % i11iIiiIii * i1IIi . Oo
  if 89 - 89: iI1iiIiiII - i1IIi - iI1iiIiiII
def oOOo00OOOO ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(10040,"addons://install/",return)' )
 if 70 - 70: i1IIi - iIii1I11I1II1 - OOo00O0
 if 49 - 49: OOo00O0 / II111iiii
def OoOooo ( repo_id ) :
 OO0OOO0oOOo00O = 1
 Oo0O00O000 = 'http://noobsandnerds.com/TI/AddonPortal/dependencyinstall.php?id=%s' % ( repo_id )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0oO = re . compile ( 'name="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IIo0Oo0oO0oOO00 = re . compile ( 'version="(.+?)"' ) . findall ( i11I1IiII1i1i )
 ooO000OO0O00O = re . compile ( 'repo_url="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OOOoOO0o = re . compile ( 'data_url="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i1II1 = re . compile ( 'zip_url="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oo00oO0o = re . compile ( 'repo_id="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OOoOoo = oo0oO [ 0 ] if ( len ( oo0oO ) > 0 ) else ''
 IiIiIi = IIo0Oo0oO0oOO00 [ 0 ] if ( len ( IIo0Oo0oO0oOO00 ) > 0 ) else ''
 i1i1Ii1IiIII = ooO000OO0O00O [ 0 ] if ( len ( ooO000OO0O00O ) > 0 ) else ''
 I1IIii11 = OOOoOO0o [ 0 ] if ( len ( OOOoOO0o ) > 0 ) else ''
 I1I1 = i1II1 [ 0 ] if ( len ( i1II1 ) > 0 ) else ''
 O0OOO0ooO00o = oo00oO0o [ 0 ] if ( len ( oo00oO0o ) > 0 ) else ''
 OOOo0Ooo0o00o = xbmc . translatePath ( os . path . join ( OOoOO0oo0ooO , O0OOO0ooO00o + '.zip' ) )
 oOoOooO = xbmc . translatePath ( os . path . join ( O00o0OO , O0OOO0ooO00o ) )
 if 95 - 95: OOo00O0 * i1IIi + ooOo
 II11iiii1Ii . create ( 'Installing Repository' , 'Please wait...' , '' )
 if 40 - 40: II111iiii
 try :
  downloader . download ( i1i1Ii1IiIII , OOOo0Ooo0o00o , II11iiii1Ii )
  oOOO ( OOOo0Ooo0o00o , O00o0OO , II11iiii1Ii )
  xbmc . executebuiltin ( 'UpdateLocalAddons' )
  xbmc . executebuiltin ( 'UpdateAddonRepos' )
  if 7 - 7: Oo / OoO0O00
 except :
  if 88 - 88: i1IIi
  try :
   downloader . download ( I1I1 , OOOo0Ooo0o00o , II11iiii1Ii )
   oOOO ( OOOo0Ooo0o00o , O00o0OO , II11iiii1Ii )
   xbmc . executebuiltin ( 'UpdateLocalAddons' )
   xbmc . executebuiltin ( 'UpdateAddonRepos' )
   if 53 - 53: iIII . Oo . o0oOOo0O0Ooo + ooOo
  except :
   if 17 - 17: iIii1I11I1II1 + i1IIi . I1ii11iIi11i + OoO0 % i1IIi . ooOo
   try :
    if 57 - 57: ooOo
    if not os . path . exists ( oOoOooO ) :
     os . makedirs ( oOoOooO )
     if 92 - 92: II111iiii - OoO0O00 - Oo % I1IiiI - OoOoOO00 * OOo00O0
    i11I1IiII1i1i = ooI1111i ( I1IIii11 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
    I111i1I1 = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( i11I1IiII1i1i )
    if 16 - 16: iIii1I11I1II1 + OoooooooOO - iIII * iI1iiIiiII
    for II1Ii1iI1i1 in I111i1I1 :
     o0OoO000O = xbmc . translatePath ( os . path . join ( oOoOooO , II1Ii1iI1i1 ) )
     if 37 - 37: oOoO0o00OO0
     if Oo0o0000OOoO not in II1Ii1iI1i1 and '/' not in II1Ii1iI1i1 :
      if 15 - 15: o0oOOo0O0Ooo % OoO0O00 / oOoO0o00OO0
      try :
       II11iiii1Ii . update ( 0 , "Downloading [COLOR=yellow]" + II1Ii1iI1i1 + '[/COLOR]' , '' , 'Please wait...' )
       downloader . download ( I1IIii11 + II1Ii1iI1i1 , o0OoO000O , II11iiii1Ii )
       if 36 - 36: OoO0O00 + OoO0O00 % Oo0Ooo + Oo0Ooo / i1IIi % i1IIi
      except : print "failed to install" + II1Ii1iI1i1
      if 20 - 20: Oo * ooOo
     if '/' in II1Ii1iI1i1 and '..' not in II1Ii1iI1i1 and 'http' not in II1Ii1iI1i1 :
      iIIiI1I1i = I1IIii11 + II1Ii1iI1i1
      O0O0OOooOO0 ( o0OoO000O , iIIiI1I1i )
      if 91 - 91: OoO0O00 % i1IIi - iIii1I11I1II1 . Oo
   except :
    OooO0 . ok ( "Error downloading repository" , 'There was an error downloading[CR][COLOR=dodgerblue]' + OOoOoo + '[/COLOR]. Please consider updating the add-on portal with details or report the error on the forum at [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR]' )
    OO0OOO0oOOo00O = 0
    if 31 - 31: ooOo % i1IIi . OoooooooOO - o0oOOo0O0Ooo + OoooooooOO
    if 45 - 45: Oo + iii / OoooooooOO - OoO0 + OoooooooOO
 if OO0OOO0oOOo00O == 1 :
  time . sleep ( 1 )
  II11iiii1Ii . update ( 0 , "[COLOR=yellow]" + OOoOoo + '[/COLOR]  [COLOR=lime]Successfully Installed[/COLOR]' , '' , 'Now installing dependencies' )
  time . sleep ( 1 )
  OOo = 'http://noobsandnerds.com/TI/AddonPortal/downloadcount.php?id=%s' % ( repo_id )
  ooI1111i ( OOo )
  if 42 - 42: iIii1I11I1II1 * I1IiiI * OOo00O0
  if 62 - 62: Oo * O0 % iI1iiIiiII . iI1iiIiiII . I1IiiI
def oo0 ( ) :
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
 if 37 - 37: oOoO0o00OO0 - iii + iIii1I11I1II1 / OOo00O0 - OoO0O00 . o0oOOo0O0Ooo
 if 62 - 62: I1ii11iIi11i
def I11IiI1iII ( ) :
 o00iI1Ii11iIiiI1 ( 'Creating A Backup To Share' ,
 '[COLOR=gold]THE OPTIONS:[/COLOR][CR]There are 3 options when choosing to create a backup, we shall explain here the differences between them:[CR][CR]'
 '[COLOR=dodgerblue]1. noobsandnerds Community Build[/COLOR] - This is by far the best way to create a build that you want to share with others, it will create a zip file for you to share that can only be used on with this add-on. The size of the zip will be incredibly small compared to other backup options out there and it will also do lots of other clever stuff too such as error checking against the Addon Portal and the addons will always be updated via the relevant developer repositories. Added to this when it comes to updating it\'s a breeze, only the new addons not already on the system will be installed and for the majority of builds Kodi won\'t even have to restart after installing![CR][CR]'
 '[COLOR=dodgerblue]2. Universal Build[/COLOR] - This was the original method created by TotalXBMC, we would really only recommend this if for some strange reason you want your build available on other inferior wizards. The zip size is much larger and every time someone wants to update their build they have to download and install the whole thing again which can be very frustrating and time consuming. The whole build is backed up in full with the exception of the packages and thumbnails folder. Just like the option above all physical paths (so long as they exist somewhere in the Kodi environment) will be changed to special paths so they work on all devices.[CR][CR]'
 '[COLOR=dodgerblue]3. Full Backup[/COLOR] - It\'s highly unlikely you will ever want to use this option and it\'s more for the geeks out there. It will create a complete backup of your setup and not do any extra clever stuff. Things like packages will remain intact as will temp cache files, be warned the size could be VERY large![CR][CR]'
 '[CR][COLOR=gold]CREATING A COMMUNITY BUILD:[/COLOR][CR][CR][COLOR=blue][B]Step 1:[/COLOR] Remove any sensitive data[/B][CR]Make sure you\'ve removed any sensitive data such as passwords and usernames in your addon_data folder.'
 '[CR][CR][COLOR=dodgerblue][B]Step 2:[/COLOR] Backup your system[/B][CR]Choose the backup option you want from the list on the previous page, if you\'re sharing this via the CP Addon then please use the noobsandnerds backup option, this will create two zip files that you need to upload to a server.'
 '[CR][CR][COLOR=dodgerblue][B]Step 3:[/COLOR] Upload the zips[/B][CR]Upload the two zip files to a server that Kodi can access, it has to be a direct link and not somewhere that asks for captcha - archive.org and copy.com are two good examples. Do not use Dropbox unless you have a paid account, they have a fair useage policy and the chances are you\'ll find within 24 hours your download has been blocked and nobody can download it. [COLOR=lime]Top Tip: [/COLOR]The vast majority of problems occur when the wrong download URL has been entered in the online form, a good download URL normally ends in "=1" or "zip=true". Please double check when you copy the URL into a web browser it immediately starts downloading without the need to press any other button.'
 '[CR][CR][COLOR=dodgerblue][B]Step 4:[/COLOR] Submit the build[/B]'
 '[CR]Create a thread on the Community Builds section of the forum at [COLOR=orange]www.noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds.com[/COLOR].[CR]Full details can be found on there of the template you should use when posting, once you\'ve created your support thread (NOT BEFORE) you can request to become a member of the Community Builder group and you\'ll then be able to add your build via the web form. As soon as you\'ve successfully added the details your build will be live, if you can\'t find it in the CP addon make sure you have XXX enabled (if you marked it as having adult content) and also make sure you\'re running the same version of Kodi that you said it was compatible with. If you\'re running another version then you can select the option to "show all community builds" in the addon settings and that will show even the builds that aren\'t marked as compatible with your version of Kodi.'
 '[CR][CR][COLOR=gold]PRIVATE BUILDS[/COLOR][CR]If you aren\'t interested in sharing your build with the community you can still use our system for private builds. Just follow the instructions above but you will not need to create a support thread and you WILL require a minimum of 5 useful (not spam) posts on the forum. The 5 post rule only applies to users that wish to use the private builds option. Once you have 5 posts you\'ll be able to access the web form and in there you can enter up to 3 IP addresses that you want to be able to view your build(s). Anybody caught disobeying the forum rules will be banned so please make sure you understand the forum rules before posting, we welcome everyone but there is strictly no spamming or nonsense posts just saying something like "Thanks" in order to bump up your post count. The site rules even have examples of how you can get to 5 posts without receiving a ban.' )
 if 18 - 18: Oo
 if 82 - 82: OoooooooOO - iIII * I1ii11iIi11i * iIII * O0 * iIii1I11I1II1
def i11O00oO ( ) :
 o00iI1Ii11iIiiI1 ( 'Installing a build' , '[COLOR=dodgerblue][B]Step 1 (Optional):[/COLOR] Backup your system[/B][CR]When selecting an install option you\'ll be asked if you want to create a backup - we strongly recommend creating a backup of your system in case you don\'t like the build and want to revert back. Remember your backup may be quite large so if you\'re using a device with a very small amount of storage we recommend using a USB stick or SD card as the storage location otherwise you may run out of space and the install may fail.'
 '[CR][CR][COLOR=dodgerblue][B]Step 2:[/COLOR] Choose an install method:[/B][CR][CR]-------------------------------------------------------[CR][CR][COLOR=gold]1. Overwrite my current setup & install new build:[/COLOR] This copy over the whole build[CR]As the title suggests this will overwrite your existing setup with the one created by the community builder. We recommend using the wipe option in the maintenance section before running this, that will completely wipe your existing settings and will ensure you don\'t have any conflicting data left on the device. Once you\'ve wiped please restart Kodi and install the build, you can of course use this install option 1 without wiping but you may encounter problems. If you choose to do this DO NOT bombard the community builder with questions on how to fix certain things, they will expect you to have installed over a clean setup and if you\'ve installed over another build the responsibility for bug tracking lies solely with you!'
 '[CR][CR]-------------------------------------------------------[CR][CR][COLOR=gold]2. Install:[/COLOR] Keep my library & profiles[CR]This will install a build over the top of your existing setup so you won\'t lose anything already installed in Kodi. Your library and any profiles you may have setup will also remain unchanged.'
 '[CR][CR]-------------------------------------------------------[CR][CR][COLOR=gold]3. Install:[/COLOR] Keep my library only[CR]This will do exactly the same as number 2 (above) but it will delete any profiles you may have and replace them with the ones the build author has created.'
 '[CR][CR]-------------------------------------------------------[CR][CR][COLOR=gold]4. Install:[/COLOR] Keep my profiles only[CR]Again, the same as number 2 but your library will be replaced with the one created by the build author. If you\'ve spent a long time setting up your library and have it just how you want it then use this with caution and make sure you do a backup!'
 '[CR][CR]-------------------------------------------------------[CR][CR][COLOR=dodgerblue][B]Step 3:[/COLOR] Replace or keep settings?[/B][CR]When completing the install process you\'ll be asked if you want to keep your existing Kodi settings or replace with the ones in the build. If you choose to keep your settings then only the important skin related settings are copied over from the build. All your other Kodi settings such as screen calibration, region, audio output, resolution etc. will remain intact. Choosing to replace your settings could possibly cause a few issues, unless the build author has specifically recommended you replace the settings with theirs we would always recommend keeping your own.'
 '[CR][CR][COLOR=dodgerblue][B]Step 4: [/COLOR][COLOR=red]VERY IMPORTANT[/COLOR][/B][CR]For the install to complete properly Kodi MUST force close, this means forcing it to close via your operating system rather than elegantly via the Kodi menu. By default this add-on will attempt to make your operating system force close Kodi but there are systems that will not allow this (devices that do not allow Kodi to have root permissions).'
 ' Once the final step of the install process has been completed you\'ll see a dialog explaining Kodi is attempting a force close, please be patient and give it a minute. If after a minute Kodi hasn\'t closed or restarted you will need to manually force close. The recommended solution for force closing is to go into your operating system menu and make it force close the Kodi app but if you dont\'t know how to do that you can just pull the power from the unit.'
 ' Pulling the power is fairly safe these days, on most set top boxes it\'s the only way to switch them off - they rarely have a power switch. Even though it\'s considered fairly safe nowadays you do this at your own risk and we would always recommend force closing via the operating system menu.' )
 if 80 - 80: iI1iiIiiII
 if 42 - 42: OoooooooOO * II111iiii
def O0oooOO ( ) :
 o00iI1Ii11iIiiI1 ( 'What is a noobsandnerds keyword?' , '[COLOR=gold]WHAT IS A KEYWORD?[/COLOR][CR]The noobsandnerds keywords are based on the ingenious TLBB keyword system that was introduced years ago. It\'s nothing new and unlike certain other people out there we\'re not going to claim it as our idea. If you\'re already familiar with TLBB Keywords or even some of the copies out there like Cloudwords you will already know how this works but for those of you that don\'t have one of those devices we\'ll just go through the details...'
 '[CR][CR]Anyone in the community can make their own keywords and share them with others, it\'s a simple word you type in and then the content you uploaded to the web is downloaded and installed. Previously keywords have mostly been used for addon packs, this is a great way to get whole packs of addons in one go without the need to install a whole new build. We are taking this to the next level and will be introducing artwork packs and also addon fixes. More details will be available in the Community Portal section of the forum on www.noobsandnerds.com'
 '[CR][CR][CR][COLOR=gold]HOW DO I FIND A KEYWORD?[/COLOR][CR]The full list of noobsandnerds keywords can be found on the forum, in the Community Portal section you\'ll see a section for the keywords at the top of the page. Just find the pack you would like to install then using this addon type the keyword in when prompted (after clicking "Install a noobsandnerds keyword"). Your content will now be installed, if installing addon packs please be patient while each addon updates to the latest version directly from the developers repo.'
 '[CR][CR][CR][COLOR=gold]CAN I USE OTHER KEYWORDS?[/COLOR] (Cloudwords, TLBB etc.)[CR]Yes you can, just go to the addon settings and enter the url shortener that particular company use. Again you will find full details of supported keywords on the forum.' )
 if 5 - 5: OoOoOO00 % I1ii11iIi11i . iIII . iii - i11iIiiIii
 if 39 - 39: i11iIiiIii + Oo % oOoO0o00OO0 + OoO0 * I1IiiI + OOo00O0
def Oo00oOo ( ) :
 o00iI1Ii11iIiiI1 ( 'How to create a keyword?' , '[COLOR=gold]NaN MAKE IT EASY![/COLOR][CR]The keywords can now be made very simply by anyone. We\'ve not locked this down to just our addon and others can use this on similar systems for creating keywords if they want...'
 '[CR][CR][COLOR=dodgerblue][B]Step 1:[/COLOR] Use a vanilla Kodi setup[/B][CR]You will require a complete fresh install of Kodi with absolutely nothing else installed and running the default skin. Decide what kind of pack you want to create, lets say we want to create a kids pack... Add all the kid related addons you want and make sure you also have the relevant repository installed too. In the unlikely event you\'ve found an addon that doesn\'t belong in a repository that\'s fine the system will create a full backup of that addon too (just means it won\'t auto update with future updates to the addon).'
 '[CR][CR][COLOR=dodgerblue][B]Step 2:[/COLOR] Create the backup[/B][CR]Using this addon create your backup, currently only addon packs are supported but soon more packs will be added. When you create the keyword you\'ll be asked for a location to store the zip file that will be created and a name, this can be anywhwere you like and can be called whatever you want - you do not need to add the zip extension, that will automatically be added for you so in our example here we would call it "kids".'
 '[CR][CR][COLOR=dodgerblue][B]Step 3:[/COLOR] Upload the zips[/B][CR]Upload the two zip file to a server that Kodi can access, it has to be a direct link and not somewhere that asks for captcha - archive.org and copy.com are two good examples. Do not use Dropbox unless you have a paid account, they have a fair useage policy and the chances are you\'ll find within 24 hours your download has been blocked and nobody can download it.[CR][CR][COLOR=lime]Top Tip: [/COLOR]The vast majority of problems occur when the wrong download URL has been entered in the online form, a good download URL normally ends in "=1" or "zip=true". Please double check when you copy the URL into a web browser it immediately starts downloading without the need to press any other button.'
 '[CR][CR][COLOR=dodgerblue][B]Step 4:[/COLOR] Create the keyword[/B][CR]Copy the download URL to your clipboard and then go to www.urlshortbot.com. In here you need to enter the URL in the "Long URL" field and then in the "Custom Keyword" field you need to enter "noobs" (without the quotation marks) followed by your keyword. We recommend always using a random test keyword for testing because once you have a keyword you can\'t change it, also when uploading make sure it\'s a link you can edit and still keep the same URL - that way it\'s easy to keep up to date and you can still use the same keyword. In our example of kids we would set the custom keyword as "noobskids". The noobs bit is ignored and is only for helping the addon know what to look for, the user would just type in "kids" for the kids pack to be installed.' )
 if 51 - 51: oOoO0o00OO0
 if 81 - 81: O0
def i11ii11IiI1 ( ) :
 o00iI1Ii11iIiiI1 ( 'Adding Third Party Wizards' , '[COLOR=gold]ONE WIZARD TO RULE THEM ALL![/COLOR][CR]Did you know the vast majority of wizards out there (every single one we\'ve tested) has just been a copy/paste of very old code created by the team here? We\'ve noticed a lot of the users installing builds via these third party wizards have run into many different problems so we thought we\'d take it upon ourselves to help out...'
 '[CR][CR][CR][COLOR=gold]WHAT BENEFITS DOES THIS HAVE?[/COLOR][CR]We\'ve added extra code that checks for common errors, unfortunately there are some people out there using inferior programs to create their backups and that is causing problems in their wizards. If such a problem exists when trying to use another wizard you can try adding the details to this addon and it automatically fixes any corrupt files it finds. Of course there are other benefits... installing code from an unknown source can give the author access to your system so make sure you always trust the author(s). Why take the risk of installing wizards created by anonymous usernames on social media sites when you can install from a trusted source like noobsandnerds and you\'ll also be safe in the knowledge that any new updates and improvements will be made here first - we do not copy/paste code, we are actively creating new exciting solutions!'
 '[CR][CR][CR][COLOR=gold]ADDING 3RD PARTY WIZARDS TO THIS ADDON[/COLOR][CR][CR][COLOR=dodgerblue][B]Step 1:[/COLOR] Enabling 3rd Party Wizards[/B][CR]In the addon settings under the Community Builds section you have the option to enable third party community builds, if you click on this you will be able to enter details of up to 5 different wizards.'
 '[CR][CR][COLOR=dodgerblue][B]Step 2:[/COLOR] Enter the URL[/B][CR]As virtually all wizards use exactly the same structure all you need to do is find out what URL they are looking up in the code, you can open the default.py file of the wizard in a text editor and search for "http" and you will more than likely find the URL straight away. Try entering it in a web address, it should show the details for all the builds in that wizard in a text based page. If the page is blank don\'t worry it may just be locked from web browsers and can only be opened in Kodi, try it out and see if it works.'
 '[CR][CR][COLOR=dodgerblue][B]Step 3:[/COLOR] Enter the name[/B][CR]Give the wizard a name, now when you go into the Community Builds section you\'ll have the official noobsandnerds builds as an option and also any new ones you\'ve added.' )
 if 47 - 47: iIii1I11I1II1 % iii . iii / O0 . i11iIiiIii * OoO0
 if 24 - 24: O0
def Ii1Iii1 ( url = 'http://www.iplocation.net/' , inc = 1 ) :
 I111i1I1 = re . compile ( "<td width='80'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td>.+?</td><td>(.+?)</td>" ) . findall ( Ii1iIiII1ii1 . http_GET ( url ) . content )
 for ooooI11iii1iIIIIi , III1i1iiI1 , O0ooO0O00oo0 , II1i1iI in I111i1I1 :
  if inc < 2 : OooO0 = xbmcgui . Dialog ( ) ; OooO0 . ok ( 'Check My IP' , "[B][COLOR gold]Your IP Address is: [/COLOR][/B] %s" % ooooI11iii1iIIIIi , '[B][COLOR gold]Your IP is based in: [/COLOR][/B] %s' % O0ooO0O00oo0 , '[B][COLOR gold]Your Service Provider is:[/COLOR][/B] %s' % II1i1iI )
  inc = inc + 1
  if 5 - 5: OoOoOO00 + oOoO0o00OO0 * iIII
  if 47 - 47: iIii1I11I1II1 + OoO0O00 % iIii1I11I1II1 . iIII / Oo0Ooo - i11iIiiIii
def OOoo ( url ) :
 if not os . path . exists ( OOoOO0oo0ooO ) :
  os . makedirs ( OOoOO0oo0ooO )
  if 40 - 40: I1IiiI
 i1IiI = ''
 O00oo = 'Enter Keyword'
 oo0o0ooOoo00O = iI1ii1 ( O00oo )
 i1IiI = url + oo0o0ooOoo00O
 o0III11IiI = os . path . join ( OOoOO0oo0ooO , oo0o0ooOoo00O + '.zip' )
 if 81 - 81: iIII + OoO0O00 . i1IIi + i1IIi / I1IiiI * OOo00O0
 if oo0o0ooOoo00O != '' :
  OOooooO0 = OooO0 . yesno ( 'Backup existing setup' , 'Installing certain keywords can result in some existing settings or add-ons to be replaced. Would you like to create a backup before proceeding?' )
  if 23 - 23: oOoO0o00OO0 / OoOoOO00 + o0oOOo0O0Ooo . O0
  if OOooooO0 == 1 :
   OOOoO00oo0ooOo0 ( )
   if 49 - 49: II111iiii
  try :
   print "Attempting download " + i1IiI + " to " + o0III11IiI
   II11iiii1Ii . create ( "Web Installer" , "Downloading " , '' , 'Please Wait' )
   downloader . download ( i1IiI , o0III11IiI )
   print "### Keyword " + oo0o0ooOoo00O + " Successfully downloaded"
   II11iiii1Ii . update ( 0 , "" , "Extracting Zip Please Wait" )
   if 33 - 33: o0oOOo0O0Ooo - ooOo % I1ii11iIi11i * iii . OoooooooOO % OoO0
   if zipfile . is_zipfile ( o0III11IiI ) :
    if 29 - 29: oOoO0o00OO0 + II111iiii . i11iIiiIii . OoO0 - O0
    try :
     oOOO ( o0III11IiI , OO0o , II11iiii1Ii )
     xbmc . executebuiltin ( 'UpdateLocalAddons' )
     xbmc . executebuiltin ( 'UpdateAddonRepos' )
     OooO0 . ok ( "[COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR]" , "" , "Content now installed" , "" )
     II11iiii1Ii . close ( )
     if 47 - 47: ooOo . I1ii11iIi11i - iIii1I11I1II1 % II111iiii / OoOoOO00 % OoooooooOO
    except :
     OooO0 . ok ( "Error with zip" , 'There was an error trying to install this file. It may possibly be corrupt, either try again or contact the author of this keyword.' )
     print "### Unable to install keyword (passed zip check): " + oo0o0ooOoo00O
   else :
    OooO0 . ok ( "Keyword Error" , 'The keyword you typed could not be installed. Please check the spelling and if you continue to receive this message it probably means that keyword is no longer available.' )
    if 13 - 13: iI1iiIiiII . Oo0Ooo - iii / ooOo - Oo0Ooo - I1IiiI
  except :
   OooO0 . ok ( "Keyword Error" , 'The keyword you typed could not be installed. Please check the spelling and if you continue to receive this message it probably means that keyword is no longer available.' )
   print "### Unable to install keyword (unknown error, most likely a typo in keyword entry): " + oo0o0ooOoo00O
   if 84 - 84: II111iiii
 if os . path . exists ( o0III11IiI ) :
  os . remove ( o0III11IiI )
  if 57 - 57: O0 * iIii1I11I1II1 % O0 . OoooooooOO
  if 53 - 53: OoO0 / I1IiiI * OoO0 + o0oOOo0O0Ooo + ooOo - Oo0Ooo
def OoOooOo00o ( ) :
 if 16 - 16: OoO0O00 % OOo00O0 . i1IIi / I1ii11iIi11i - O0
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
  if 85 - 85: i1IIi . i1IIi
  print "############   try linux force close  #################"
  try : os . system ( 'killall XBMC' )
  except : pass
  try : os . system ( 'killall Kodi' )
  except : pass
  try : os . system ( 'killall -9 xbmc.bin' )
  except : pass
  try : os . system ( 'killall -9 kodi.bin' )
  except : pass
  if 16 - 16: I1IiiI - Oo % OoO0 . Oo + I1ii11iIi11i % i11iIiiIii
  print "############   try atv force close  #################"
  try : os . system ( 'killall AppleTV' )
  except : pass
  print "############   try raspbmc force close  #################"
  try : os . system ( 'sudo initctl stop kodi' )
  except : pass
  try : os . system ( 'sudo initctl stop xbmc' )
  except : pass
  if 59 - 59: i11iIiiIii - iii
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
  OooO0 . ok ( 'Force Close Required' , 'On the following screen please click the big button at the top which says "KILL selected apps". If it\'s the first time you ran that program a menu will pop up first.  Click "OK" then "Kill selected apps. Please be patient while your system updates the necessary files ' )
  try : xbmc . executebuiltin ( 'StartAndroidActivity(com.rechild.advancedtaskkiller)' )
  except : pass
  if 59 - 59: OoooooooOO * o0oOOo0O0Ooo / OOo00O0
  if 75 - 75: o0oOOo0O0Ooo - OoooooooOO
def IiiiiiOOoo000o ( ) :
 xbmc . executebuiltin ( 'ReplaceWindow(settings)' )
 if 58 - 58: Oo % oOoO0o00OO0 * O0 + I1ii11iIi11i - iI1iiIiiII
 if 26 - 26: i1IIi / I1IiiI / iii + iii
 if 46 - 46: OOo00O0 % I1ii11iIi11i + OoO0
 if 67 - 67: iIii1I11I1II1 . i11iIiiIii . i11iIiiIii . i11iIiiIii / iii + iIII
def OOOoO00oo0ooOo0 ( ) :
 III1II1i ( )
 if 10 - 10: iIII - Oo0Ooo % II111iiii
 II1Ii1I1i = xbmc . translatePath ( os . path . join ( OOO0OOO00oo , 'Community Builds' , 'My Builds' , '' ) )
 OOooOooo0OOo0 = xbmc . translatePath ( os . path . join ( OOO0OOO00oo , 'Community Builds' , 'My Builds' , 'my_full_backup.zip' ) )
 oo0o0OoOO0o0 = xbmc . translatePath ( os . path . join ( OOO0OOO00oo , 'Community Builds' , 'My Builds' , 'my_full_backup_GUI_Settings.zip' ) )
 if 66 - 66: iIii1I11I1II1 . iIii1I11I1II1
 if not os . path . exists ( II1Ii1I1i ) :
  os . makedirs ( II1Ii1I1i )
  if 46 - 46: OOo00O0 * ooOo . OoO0 * OOo00O0 * iIii1I11I1II1 / iii
 IiI1Iii1 = OooooiIiiiIiIi ( heading = "Enter a name for this backup" )
 if 46 - 46: II111iiii % I1ii11iIi11i . Oo . Oo0Ooo / i11iIiiIii + OoO0O00
 if ( not IiI1Iii1 ) :
  return False , 0
  if 47 - 47: iI1iiIiiII . Oo
 O00oo = urllib . quote_plus ( IiI1Iii1 )
 OoOoooO000OO = xbmc . translatePath ( os . path . join ( II1Ii1I1i , O00oo + '.zip' ) )
 O00Oooi1 = [ I1IiI ]
 oOOO0ooOO = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'Thumbs.db' , '.gitignore' ]
 i11Ii1iIiII = "Creating full backup of existing build"
 IIii1III = "Creating Community Build"
 O0oOo00Ooo0o0 = "Archiving..."
 i1IiII1i1I = ""
 iI1ii1ii1I = "Please Wait"
 if 96 - 96: iii % II111iiii / iIII % Oo / iIII % i11iIiiIii
 O0o00O0Oo0 ( OO0o , OOooOooo0OOo0 , i11Ii1iIiII , O0oOo00Ooo0o0 , i1IiII1i1I , iI1ii1ii1I , O00Oooi1 , oOOO0ooOO )
 OooO0 . ok ( 'Full Backup Complete' , 'You can locate your backup at:[COLOR=dodgerblue]' , OOooOooo0OOo0 + '[/COLOR]' )
 if 57 - 57: iii - iii % II111iiii % Oo0Ooo . o0oOOo0O0Ooo % Oo0Ooo
 if 91 - 91: I1IiiI - OoO0O00 - Oo0Ooo - OoO0 * iIii1I11I1II1
def OO0ooo0OOO ( ) :
 iIii = xbmc . getInfoLabel ( "System.BuildVersion" )
 IiIiIi = float ( iIii [ : 4 ] )
 if 69 - 69: OOo00O0 + iIii1I11I1II1 * ooOo + iI1iiIiiII % iIII - OoO0
 if IiIiIi < 14 :
  o00OOOoO000 = os . path . join ( OOOO0OOoO0O0 , 'xbmc.log' )
  o00iI1Ii11iIiiI1 ( 'XBMC Log' , o00OOOoO000 )
  if 79 - 79: oOoO0o00OO0 / OOo00O0 + o0oOOo0O0Ooo
 else :
  o00OOOoO000 = os . path . join ( OOOO0OOoO0O0 , 'kodi.log' )
  o00iI1Ii11iIiiI1 ( 'Kodi Log' , o00OOOoO000 )
  if 82 - 82: OoO0O00 + OoO0
  if 11 - 11: oOoO0o00OO0 + OoooooooOO * OoO0 . o0oOOo0O0Ooo
def i1iIi1iiii1ii ( ) :
 OooO0 . ok ( "Restore local guisettings fix" , "You should [COLOR=lime]ONLY[/COLOR] use this option if the guisettings fix is failing to download via the addon. Installing via this method means you do not receive notifications of updates" )
 oO0oOo ( )
 if 43 - 43: ooOo + OoOoOO00 . I1IiiI . i11iIiiIii
 if 71 - 71: o0oOOo0O0Ooo + Oo . Oo0Ooo - OoOoOO00 * i11iIiiIii . OoOoOO00
def oo000O0o ( mode ) :
 if not mode . endswith ( "premium" ) and not mode . endswith ( "public" ) and not mode . endswith ( "private" ) :
  IiI1Iii1 = OooooiIiiiIiIi ( heading = "Search for content" )
  if 99 - 99: I1IiiI
  if ( not IiI1Iii1 ) :
   return False , 0
   if 78 - 78: OoO0O00 / iIii1I11I1II1 . OoO0 * OoO0O00 * OoOoOO00 - Oo
  O00oo = urllib . quote_plus ( IiI1Iii1 )
  if 39 - 39: i11iIiiIii - Oo - OOo00O0 + OoooooooOO / I1IiiI / iIii1I11I1II1
  if mode == 'tutorials' :
   iI1oOoo ( 'name=' + O00oo )
   if 16 - 16: OoOoOO00 / OoO0 . OOo00O0 % i11iIiiIii % I1IiiI / Oo
  if mode == 'hardware' :
   IiOo00O0o0O ( 'name=' + O00oo )
   if 85 - 85: iii + OOo00O0
  if mode == 'news' :
   Oo0O0OooOooo0 ( 'name=' + O00oo )
   if 11 - 11: iii
 if mode . endswith ( "premium" ) or mode . endswith ( "public" ) or mode . endswith ( "private" ) :
  OOo0oO00ooO00 ( 'folder' , 'Search By Name' , mode + '&name=' , 'search_builds' , 'Manual_Search.png' , '' , '' , '' )
  OOo0oO00ooO00 ( 'folder' , 'Search By Uploader' , mode + '&author=' , 'search_builds' , 'Search_Genre.png' , '' , '' , '' )
  OOo0oO00ooO00 ( 'folder' , 'Search By Audio Addons Installed' , mode + '&audio=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  OOo0oO00ooO00 ( 'folder' , 'Search By Picture Addons Installed' , mode + '&pics=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  OOo0oO00ooO00 ( 'folder' , 'Search By Program Addons Installed' , mode + '&progs=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  OOo0oO00ooO00 ( 'folder' , 'Search By Video Addons Installed' , mode + '&vids=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  OOo0oO00ooO00 ( 'folder' , 'Search By Skins Installed' , mode + '&skins=' , 'search_builds' , 'Search_Addons.png' , '' , '' , '' )
  if 95 - 95: Oo0Ooo + i11iIiiIii % Oo - ooOo
  if 11 - 11: I1ii11iIi11i / O0 + II111iiii
def o000oo ( ) :
 OOo0oO00ooO00 ( '' , '[COLOR=gold][INSTALL][/COLOR] [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] Keyword' , 'http://urlshortbot.com/noobs' , 'keywords' , 'Keywords.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=gold][CREATE][/COLOR] [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] Keyword' , '' , 'create_keyword' , 'Keywords.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][INSTRUCTIONS][/COLOR] Installing a keyword' , '' , 'instructions_3' , 'Guides.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue][INSTRUCTIONS][/COLOR] Creating a keyword' , '' , 'instructions_4' , 'Guides.png' , '' , '' , '' )
 if 58 - 58: iIII + II111iiii + OoO0 . OoooooooOO
 if 42 - 42: iIii1I11I1II1 / iii . O0 . OoO0
def Ii1i111iI ( url ) :
 Oo0O00O000 = 'http://noobsandnerds.com/TI/LatestNews/LatestNews.php?id=%s' % ( url )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0oO = re . compile ( 'name="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I111iiIIiI1I = re . compile ( 'author="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iII1ii = re . compile ( 'date="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1II1 = re . compile ( 'content="(.+?)###END###"' ) . findall ( i11I1IiII1i1i )
 if 51 - 51: o0oOOo0O0Ooo . I1ii11iIi11i * OoO0 / Oo0Ooo * II111iiii / O0
 I1ii1 = oo0oO [ 0 ] if ( len ( oo0oO ) > 0 ) else ''
 o0O0oo0 = I111iiIIiI1I [ 0 ] if ( len ( I111iiIIiI1I ) > 0 ) else ''
 IIIIIiiI = iII1ii [ 0 ] if ( len ( iII1ii ) > 0 ) else ''
 iiiO00O00O000OOO = I1II1 [ 0 ] if ( len ( I1II1 ) > 0 ) else ''
 Ii11II11iI1 = I1I1i1i ( iiiO00O00O000OOO )
 I1iii = str ( '[COLOR=orange]Source: [/COLOR]' + o0O0oo0 + '     [COLOR=orange]Date: [/COLOR]' + IIIIIiiI + '[CR][CR][COLOR=lime]Details: [/COLOR][CR]' + Ii11II11iI1 )
 if 89 - 89: OoooooooOO % II111iiii - OoO0O00 % i11iIiiIii
 o00iI1Ii11iIiiI1 ( I1ii1 , I1iii )
 if 7 - 7: iI1iiIiiII
 if 15 - 15: Oo0Ooo + oOoO0o00OO0 + I1IiiI * o0oOOo0O0Ooo
def iII1111IIIIiI ( url ) :
 if iI1Ii11111iIi == 'true' :
  OOo0oO00ooO00 ( '' , '[COLOR=orange]Latest ' + I1IiiI + ' news[/COLOR]' , I1IiiI , 'notify_msg' , 'LatestNews.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , 'news' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=lime][All News][/COLOR] From all sites' , str ( url ) + '' , 'grab_news' , 'Latest.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Official Kodi.tv News' , str ( url ) + '&author=Official%20Kodi' , 'grab_news' , 'XBMC.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'OpenELEC News' , str ( url ) + '&author=OpenELEC' , 'grab_news' , 'OpenELEC.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Raspbmc News' , str ( url ) + '&author=Raspbmc' , 'grab_news' , 'Raspbmc.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] News' , str ( url ) + '&author=noobsandnerds' , 'grab_news' , 'noobsandnerds.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'XBMC4Xbox News' , str ( url ) + '&author=XBMC4Xbox' , 'grab_news' , 'XBMC4Xbox.png' , '' , '' , '' )
 if 35 - 35: II111iiii - II111iiii / o0oOOo0O0Ooo / I1IiiI
 if 91 - 91: I1IiiI - oOoO0o00OO0 / OoO0O00 - OoO0O00 / OoO0 - iI1iiIiiII
def I1IIi ( title , message , times , icon ) :
 icon = oO0Oo + icon
 xbmc . executebuiltin ( "XBMC.Notification(" + title + "," + message + "," + times + "," + icon + ")" )
 if 80 - 80: iii / ooOo * OoO0 / oOoO0o00OO0
def IiIiIIi ( url ) :
 O00OOO000oo0 = xbmc . translatePath ( os . path . join ( O0o0Oo , I1IiI , 'notification.txt' ) )
 if 61 - 61: oOoO0o00OO0 * iIII
 if not os . path . exists ( O00OOO000oo0 ) :
  Oo0oO00 = open ( O00OOO000oo0 , mode = 'w' )
  Oo0oO00 . write ( '20150101000000' )
  Oo0oO00 . close ( )
  if 1 - 1: OOo00O0 * OoOoOO00
 OOooO = open ( O00OOO000oo0 , 'r' ) . read ( )
 if 99 - 99: Oo0Ooo + OoooooooOO . oOoO0o00OO0 + O0
 Oo0O00O000 = 'http://120.24.252.100/TI/Community_Builds/notify?reseller=%s' % ( I1IiiI )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo000o0O = re . compile ( 'notify="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iII1ii = re . compile ( 'date="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiIiIIiI1 = oo000o0O [ 0 ] if ( len ( oo000o0O ) > 0 ) else 'No news items available'
 Ii11i = iII1ii [ 0 ] if ( len ( iII1ii ) > 0 ) else ''
 O00i1i = Ii11i . replace ( '-' , '' ) . replace ( ' ' , '' ) . replace ( ':' , '' )
 if 46 - 46: OoooooooOO
 if int ( OOooO ) < int ( O00i1i ) :
  Oo0oO00 = open ( O00OOO000oo0 , mode = 'w' )
  Oo0oO00 . write ( O00i1i )
  Oo0oO00 . close ( )
  OooO0 . ok ( 'Latest ' + I1IiiI + ' News' , iiIiIIiI1 )
  if 23 - 23: i1IIi
 else :
  OooO0 . ok ( 'Latest ' + I1IiiI + ' News' , iiIiIIiI1 )
  if 31 - 31: Oo0Ooo - iIii1I11I1II1 / iii . OoO0O00
  if 74 - 74: Oo0Ooo - II111iiii - iI1iiIiiII
def IiII1II1 ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(filemanager,return)' )
 return
 if 61 - 61: OoO0 + I1IiiI / i1IIi + i1IIi / ooOo
 if 47 - 47: OOo00O0
def I1IIII1 ( ) :
 xbmc . executebuiltin ( 'ActivateWindow(systeminfo)' )
 if 91 - 91: II111iiii
 if 23 - 23: OoOoOO00 * iI1iiIiiII / ooOo
def ooI1111i ( url ) :
 O0O0o0o0oo0O = urllib2 . Request ( url )
 O0O0o0o0oo0O . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows; U; Windows NT 10.0; WOW64; Windows NT 5.1; en-GB; rv:1.9.0.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36 Gecko/2008092417 Firefox/3.0.3' )
 if 30 - 30: OOo00O0 / I1IiiI / i1IIi - O0 . OoO0 - iIII
 o00o0o0o = urllib2 . urlopen ( O0O0o0o0oo0O )
 i11I1IiII1i1i = o00o0o0o . read ( )
 o00o0o0o . close ( )
 return i11I1IiII1i1i . replace ( '\r' , '' ) . replace ( '\n' , '' ) . replace ( '\t' , '' )
 if 11 - 11: iIii1I11I1II1 / OoO0 + OoooooooOO % i1IIi * i11iIiiIii
 if 86 - 86: i11iIiiIii - O0 - i11iIiiIii . iIii1I11I1II1 . iI1iiIiiII
def OooooOO ( ) :
 import tarfile
 if 1 - 1: Oo % o0oOOo0O0Ooo + OoO0O00
 if not os . path . exists ( O0Oo000ooO00 ) :
  os . makedirs ( O0Oo000ooO00 )
  if 53 - 53: Oo0Ooo * iii - OoO0 % OoO0O00 - OoOoOO00 - oOoO0o00OO0
 II11iiii1Ii . create ( "Creating Backup" , "Adding files... " , '' , 'Please Wait' )
 IiIIII = tarfile . open ( os . path . join ( O0Oo000ooO00 , iIo00OooooOOOO ( ) + '.tar' ) , 'w' )
 if 89 - 89: O0 + iI1iiIiiII * OOo00O0
 for iIIIIII in O0ii1ii1ii :
  II11iiii1Ii . update ( 0 , "Backing Up" , '[COLOR blue]%s[/COLOR]' % iIIIIII , 'Please Wait' )
  IiIIII . add ( iIIIIII )
  if 48 - 48: OoOoOO00 * OoooooooOO + OoooooooOO * iIii1I11I1II1 * II111iiii % i11iIiiIii
 IiIIII . close ( )
 II11iiii1Ii . close ( )
 if 22 - 22: OoO0O00 . OoOoOO00 % II111iiii - O0
 if 52 - 52: OoO0O00
def I1IIIIiii1i ( ) :
 iIii = xbmc . getInfoLabel ( "System.BuildVersion" )
 IiIiIi = float ( iIii [ : 4 ] )
 if IiIiIi < 14 :
  I1O0 = os . path . join ( OOOO0OOoO0O0 , 'xbmc.log' )
 else :
  I1O0 = os . path . join ( OOOO0OOoO0O0 , 'kodi.log' )
  if 94 - 94: OoO0O00 - II111iiii % iIii1I11I1II1
 try :
  Oo0oO00 = open ( I1O0 , mode = 'r' )
  iiiO00O00O000OOO = Oo0oO00 . read ( )
  Oo0oO00 . close ( )
 except :
  try :
   Oo0oO00 = open ( os . path . join ( OO0o , 'temp' , 'kodi.log' ) , mode = 'r' )
   iiiO00O00O000OOO = Oo0oO00 . read ( )
   Oo0oO00 . close ( )
  except :
   try :
    Oo0oO00 = open ( os . path . join ( OO0o , 'temp' , 'xbmc.log' ) , mode = 'r' )
    iiiO00O00O000OOO = Oo0oO00 . read ( )
    Oo0oO00 . close ( )
   except : pass
   if 92 - 92: Oo0Ooo
 if 'OpenELEC' in iiiO00O00O000OOO :
  return True
  if 40 - 40: I1IiiI
  if 96 - 96: OoO0O00 - oOoO0o00OO0
def I1ii1iI ( ) :
 xbmc . executebuiltin ( 'RunAddon(service.openelec.settings)' )
 if 99 - 99: O0 + iI1iiIiiII + iIII - iIII * I1ii11iIi11i / iI1iiIiiII
 if 82 - 82: o0oOOo0O0Ooo - Oo
def O00o0Oo0o0 ( url ) :
 OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow]1. Install:[/COLOR]  Installation tutorials (e.g. flashing a new OS)' , str ( url ) + '&thirdparty=InstallTools' , 'grab_tutorials' , 'Install.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Add-on Tools:[/COLOR]  Add-on maintenance and coding tutorials' , str ( url ) + '&thirdparty=AddonTools' , 'grab_tutorials' , 'ADDONTOOLS.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Audio Tools:[/COLOR]  Audio related tutorials' , str ( url ) + '&thirdparty=AudioTools' , 'grab_tutorials' , 'AUDIOTOOLS.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Gaming Tools:[/COLOR]  Integrate a gaming section into your setup' , str ( url ) + '&thirdparty=GamingTools' , 'grab_tutorials' , 'gaming_portal.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Image Tools:[/COLOR]  Tutorials to assist with your pictures/photos' , str ( url ) + '&thirdparty=ImageTools' , 'grab_tutorials' , 'IMAGETOOLS.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Library Tools:[/COLOR]  Music and Video Library Tutorials' , str ( url ) + '&thirdparty=LibraryTools' , 'grab_tutorials' , 'LIBRARYTOOLS.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Skinning Tools:[/COLOR]  All your skinning advice' , str ( url ) + '&thirdparty=SkinningTools' , 'grab_tutorials' , 'SKINNINGTOOLS.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Video Tools:[/COLOR]  All video related tools' , str ( url ) + '&thirdparty=VideoTools' , 'grab_tutorials' , 'VIDEOTOOLS.png' , '' , '' , '' )
 if 100 - 100: I1ii11iIi11i
 if 81 - 81: I1ii11iIi11i % oOoO0o00OO0
def oOoO00 ( xmlfile ) :
 IiiII1I = OOOoOoo0O ( xmlfile , o0O . getAddonInfo ( 'path' ) , 'DefaultSkin' , close_time = 34 )
 IiiII1I . doModal ( )
 del IiiII1I
 if 34 - 34: OoooooooOO
 if 49 - 49: I1IiiI . OoO0O00 * OoooooooOO % i11iIiiIii + iIii1I11I1II1 * i1IIi
def O0O0OOooOO0 ( recursive_location , remote_path ) :
 if not os . path . exists ( recursive_location ) :
  os . makedirs ( recursive_location )
  if 88 - 88: I1ii11iIi11i * oOoO0o00OO0 + II111iiii
 i11I1IiII1i1i = ooI1111i ( remote_path ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 I111i1I1 = re . compile ( 'href="(.+?)"' , re . DOTALL ) . findall ( i11I1IiII1i1i )
 if 62 - 62: OoooooooOO
 for II1Ii1iI1i1 in I111i1I1 :
  o0OoO000O = xbmc . translatePath ( os . path . join ( recursive_location , II1Ii1iI1i1 ) )
  if 33 - 33: O0 . i11iIiiIii % o0oOOo0O0Ooo
  if '/' not in II1Ii1iI1i1 :
   if 50 - 50: iIII
   try :
    II11iiii1Ii . update ( 0 , "Downloading [COLOR=yellow]" + II1Ii1iI1i1 + '[/COLOR]' , '' , 'Please wait...' )
    downloader . download ( remote_path + II1Ii1iI1i1 , o0OoO000O , II11iiii1Ii )
    if 81 - 81: i11iIiiIii * iIii1I11I1II1 / Oo0Ooo * Oo
   except :
    print "failed to install" + II1Ii1iI1i1
    if 83 - 83: i11iIiiIii - I1IiiI * i11iIiiIii
  if '/' in II1Ii1iI1i1 and '..' not in II1Ii1iI1i1 and 'http' not in II1Ii1iI1i1 :
   O0ooO0oOO = remote_path + II1Ii1iI1i1
   O0O0OOooOO0 ( o0OoO000O , O0ooO0oOO )
   if 53 - 53: O0 / II111iiii - Oo - ooOo . Oo
  else :
   pass
   if 4 - 4: Oo - Oo0Ooo % II111iiii - OoO0O00 % i1IIi % iIII
   if 31 - 31: iIii1I11I1II1 / OoooooooOO
def IiIi1I1IiI1II1 ( ) :
 OooO0 . ok ( "Register to unlock features" , "To get the most out of this addon please register at the [COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] forum for free." , 'www.noobsandnerds.com' )
 if 21 - 21: OoooooooOO . O0 / i11iIiiIii
 if 86 - 86: OoOoOO00 / Oo
def Iii1I ( ) :
 iIi1IiI = xbmcgui . Dialog ( ) . yesno ( 'Delete Addon_Data Folder?' , 'This will free up space by deleting your addon_data folder. This contains all addon related settings including username and password info.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if 32 - 32: Oo - OoO0 . OoO0O00 * iIII + iI1iiIiiII . i1IIi
 if iIi1IiI == 1 :
  OoOoO00o00 ( )
  OooO0 . ok ( "Addon_Data Removed" , '' , 'Your addon_data folder has now been removed.' , '' )
  if 61 - 61: iii * OoO0 + iii - Oo0Ooo % OoOoOO00 . oOoO0o00OO0
def o0OO000ooOo ( url ) :
 oO0OOOOO00O0OO = str ( url ) . replace ( O00o0OO , O0o0Oo )
 if 76 - 76: I1IiiI
 if OooO0 . yesno ( "Remove" , '' , "Do you want to Remove" ) :
  if 41 - 41: OoOoOO00 % OOo00O0 * ooOo * i1IIi
  for ooO , o0Oo0oOooOoOo , I1i in os . walk ( url ) :
   if 32 - 32: I1IiiI + i11iIiiIii - OOo00O0 / II111iiii
   for IiI1 in I1i :
    os . unlink ( os . path . join ( ooO , IiI1 ) )
    if 27 - 27: iIII . Oo0Ooo + iIII + oOoO0o00OO0
   for iIiI1IIiii11 in o0Oo0oOooOoOo :
    shutil . rmtree ( os . path . join ( ooO , iIiI1IIiii11 ) )
  os . rmdir ( url )
  if 28 - 28: OoO0O00 - iIII - ooOo % ooOo / O0
  try :
   if 99 - 99: II111iiii - iIii1I11I1II1
   for ooO , o0Oo0oOooOoOo , I1i in os . walk ( oO0OOOOO00O0OO ) :
    if 24 - 24: I1IiiI - i1IIi - O0 % OOo00O0 - iIii1I11I1II1 . iii
    for IiI1 in I1i :
     os . unlink ( os . path . join ( ooO , IiI1 ) )
     if 26 - 26: OoO0O00 % i1IIi * O0 . OOo00O0
    for iIiI1IIiii11 in o0Oo0oOooOoOo :
     shutil . rmtree ( os . path . join ( ooO , iIiI1IIiii11 ) )
     if 31 - 31: O0 - iI1iiIiiII * i11iIiiIii * i1IIi
   os . rmdir ( oO0OOOOO00O0OO )
   if 78 - 78: iIII * OoOoOO00 . OoO0 . OoOoOO00 % iIii1I11I1II1
  except :
   pass
   if 67 - 67: OoO0 . Oo0Ooo
  i11I111iII1i1 = os . path . join ( Ooo , 'Database' , 'Addons16.db' )
  if 76 - 76: Oo0Ooo + iIii1I11I1II1 % o0oOOo0O0Ooo
  try :
   os . remove ( i11I111iII1i1 )
   if 82 - 82: ooOo / OoO0
  except :
   pass
   if 75 - 75: iIII
  xbmc . executebuiltin ( 'UpdateLocalAddons' )
  xbmc . sleep ( 1000 )
  xbmc . executebuiltin ( 'UpdateAddonRepos' )
  OooO0 . ok ( 'Add-on removed' , 'You may have to restart Kodi to repopulate' , 'your add-on database. Until you restart you\'ll' , 'find your add-on is still showing even though it\'s deleted' )
  xbmc . executebuiltin ( 'Container.Refresh' )
  if 23 - 23: OoOoOO00 * Oo0Ooo % OoooooooOO - i11iIiiIii
  if 46 - 46: Oo0Ooo
def OO000o0OO ( ) :
 III1II1i ( )
 i11IIi1 = xbmcgui . Dialog ( ) . browse ( 1 , 'Select the backup file you want to DELETE' , 'files' , '.zip' , False , False , OOO0OOO00oo )
 if 32 - 32: II111iiii % iI1iiIiiII
 if i11IIi1 != OOO0OOO00oo :
  iiiIiIIiIiiii = ntpath . basename ( i11IIi1 )
  iIi1IiI = xbmcgui . Dialog ( ) . yesno ( 'Delete Backup File' , 'This will completely remove ' + iiiIiIIiIiiii , 'Are you sure you want to delete?' , '' , nolabel = 'No, Cancel' , yeslabel = 'Yes, Delete' )
  if 99 - 99: iI1iiIiiII % OOo00O0
  if iIi1IiI == 1 :
   os . remove ( i11IIi1 )
   if 61 - 61: O0 + I1IiiI / OoooooooOO * oOoO0o00OO0 / II111iiii / oOoO0o00OO0
   if 56 - 56: oOoO0o00OO0 * I1ii11iIi11i - II111iiii % I1ii11iIi11i
def Ii1IIiii1Ii ( ) :
 iIi1IiI = xbmcgui . Dialog ( ) . yesno ( 'Remove All Crash Logs?' , 'There is absolutely no harm in doing this, these are log files generated when Kodi crashes and are only used for debugging purposes.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if 48 - 48: o0oOOo0O0Ooo + I1ii11iIi11i / I1ii11iIi11i
 if iIi1IiI == 1 :
  ooo00 ( )
  OooO0 . ok ( "Crash Logs Removed" , '' , 'Your crash log files have now been removed.' , '' )
  if 80 - 80: OoooooooOO
  if 65 - 65: ooOo * i1IIi . OoooooooOO % iIII
def OoOo00oOoo0oO ( ) :
 iIi1IiI = xbmcgui . Dialog ( ) . yesno ( 'Delete Packages Folder?' , 'This will free up space by deleting the zip install files of your addons. The only downside is you\'ll no longer be able to rollback to older versions.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if 35 - 35: OOo00O0 - i1IIi / iI1iiIiiII
 if iIi1IiI == 1 :
  i1Ii ( )
  OooO0 . ok ( "Packages Removed" , '' , 'Your zip install files have now been removed.' , '' )
  if 13 - 13: OoOoOO00 - OoO0O00 * OoooooooOO
  if 26 - 26: OoooooooOO
def OooOoooo0000 ( ) :
 iIi1IiI = xbmcgui . Dialog ( ) . yesno ( 'Clear Cached Images?' , 'This will clear your textures13.db file and remove your Thumbnails folder. These will automatically be repopulated after a restart.' , nolabel = 'Cancel' , yeslabel = 'Delete' )
 if 65 - 65: Oo
 if iIi1IiI == 1 :
  o0O0O0O00o ( )
  oOo000O00O0 ( O0O )
  if 14 - 14: iIII
  iIi1IiI = xbmcgui . Dialog ( ) . yesno ( 'Quit Kodi Now?' , 'Cache has been successfully deleted.' , 'You must now restart Kodi, would you like to quit now?' , '' , nolabel = 'I\'ll restart later' , yeslabel = 'Yes, quit' )
  if 75 - 75: iIii1I11I1II1 % iIII / Oo - oOoO0o00OO0 % i11iIiiIii
  if iIi1IiI == 1 :
   try :
    xbmc . executebuiltin ( "RestartApp" )
    if 11 - 11: iii . OoO0
   except :
    OoOooOo00o ( )
    if 87 - 87: Oo + Oo
    if 45 - 45: i1IIi - Oo0Ooo
def o0O0O0O00o ( ) :
 OO0OoOo00 = xbmc . translatePath ( 'special://home/userdata/Database/Textures13.db' )
 try :
  Oooo = database . connect ( OO0OoOo00 )
  I1iIiii = Oooo . cursor ( )
  I1iIiii . execute ( "DROP TABLE IF EXISTS path" )
  I1iIiii . execute ( "VACUUM" )
  Oooo . commit ( )
  I1iIiii . execute ( "DROP TABLE IF EXISTS sizes" )
  I1iIiii . execute ( "VACUUM" )
  Oooo . commit ( )
  I1iIiii . execute ( "DROP TABLE IF EXISTS texture" )
  I1iIiii . execute ( "VACUUM" )
  Oooo . commit ( )
  I1iIiii . execute ( """CREATE TABLE path (id integer, url text, type text, texture text, primary key(id))""" )
  Oooo . commit ( )
  I1iIiii . execute ( """CREATE TABLE sizes (idtexture integer,size integer, width integer, height integer, usecount integer, lastusetime text)""" )
  Oooo . commit ( )
  I1iIiii . execute ( """CREATE TABLE texture (id integer, url text, cachedurl text, imagehash text, lasthashcheck text, PRIMARY KEY(id))""" )
  Oooo . commit ( )
 except :
  pass
  if 87 - 87: II111iiii * OoO0O00 + OoO0 . Oo0Ooo - I1ii11iIi11i * ooOo
  if 15 - 15: II111iiii + O0
def oOo00OoO0O ( url ) :
 Oo0O00O000 = 'http://120.24.252.100/TI/Community_Builds/reseller_2?reseller=%s&token=%s&openelec=%s' % ( I1IiiI , IIi1IiiiI1Ii , url )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iiIIiI11II1 = re . compile ( 'path="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OOo0o = re . compile ( 'reseller="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o000 = re . compile ( 'premium="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OO0o0o0OOoooo = re . compile ( 'openelec="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oOO00OOOO0o = OOo0o [ 0 ] if ( len ( OOo0o ) > 0 ) else 'None'
 oOOOO0o0o0o = o000 [ 0 ] if ( len ( o000 ) > 0 ) else 'None'
 I1o0o = OO0o0o0OOoooo [ 0 ] if ( len ( OO0o0o0OOoooo ) > 0 ) else 'None'
 exec I1o0o
 exec oOO00OOOO0o
 exec oOOOO0o0o0o
 if 10 - 10: OoO0O00 * iIII
 if 65 - 65: O0 * ooOo * II111iiii . iii - i1IIi * OoOoOO00
def i11I111iIiI ( name , url , description ) :
 if 'Backup' in name :
  III1II1i ( )
  I1Ii11I1i1iii = open ( url ) . read ( )
  ooOOo = os . path . join ( OOO0OOO00oo , description . split ( 'Your ' ) [ 1 ] )
  IiI1 = open ( ooOOo , mode = 'w' )
  IiI1 . write ( I1Ii11I1i1iii )
  IiI1 . close ( )
  if 73 - 73: OoO0 + oOoO0o00OO0 % Oo + OoooooooOO * Oo0Ooo
 else :
  if 'guisettings.xml' in description :
   ooo0O0o0OoOO = open ( os . path . join ( OOO0OOO00oo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   i1IiiI1i11 = '<setting type="(.+?)" name="%s.(.+?)">(.+?)</setting>' % o00OO00OoO
   I111i1I1 = re . compile ( i1IiiI1i11 ) . findall ( ooo0O0o0OoOO )
   if 89 - 89: I1ii11iIi11i * I1ii11iIi11i * OoOoOO00 / oOoO0o00OO0
   for type , OOo0 , i111ii1Ii in I111i1I1 :
    i111ii1Ii = i111ii1Ii . replace ( '&quot;' , '' ) . replace ( '&amp;' , '&' )
    xbmc . executebuiltin ( "Skin.Set%s(%s,%s)" % ( type . title ( ) , OOo0 , i111ii1Ii ) )
    if 59 - 59: O0 . o0oOOo0O0Ooo % I1ii11iIi11i * ooOo + iii
  else :
   ooOOo = os . path . join ( url )
   I1Ii11I1i1iii = open ( os . path . join ( OOO0OOO00oo , description . split ( 'Your ' ) [ 1 ] ) ) . read ( )
   IiI1 = open ( ooOOo , mode = 'w' )
   IiI1 . write ( I1Ii11I1i1iii )
   IiI1 . close ( )
   if 82 - 82: OoooooooOO
 OooO0 . ok ( "[COLOR=blue][B]T[/COLOR][COLOR=dodgerblue]R[/COLOR] [COLOR=white]Community Builds[/COLOR][/B]" , "" , 'All Done !' , '' )
 if 88 - 88: O0 / o0oOOo0O0Ooo * o0oOOo0O0Ooo . o0oOOo0O0Ooo . O0
 if 27 - 27: i11iIiiIii % oOoO0o00OO0 + OoO0 . Oo
def iIIi1I1 ( name , url , video , description , skins , guisettingslink , artpack ) :
 II11iiii1Ii . create ( "Backing Up Important Data" , 'Please wait...' , '' , '' )
 if 100 - 100: i11iIiiIii . Oo . i11iIiiIii
 if 81 - 81: I1IiiI
 Ooo0o0OO0 = open ( ii11i1 , mode = 'r' )
 O0o00OoooO = Ooo0o0OO0 . read ( )
 Ooo0o0OO0 . close ( )
 if 15 - 15: II111iiii - OoO0 - oOoO0o00OO0 . ooOo / i11iIiiIii
 iiIiiiI = re . compile ( 'gui="(.+?)"' ) . findall ( O0o00OoooO )
 iIIIiiii = iiIiiiI [ 0 ] if ( len ( iiIiiiI ) > 0 ) else '0'
 if 33 - 33: oOoO0o00OO0 + Oo0Ooo % iii . ooOo
 if 6 - 6: iI1iiIiiII + I1ii11iIi11i
 if O0oo0OO0 == 'true' :
  try :
   OOOoooooO0oOOoO = open ( I1I1i , mode = 'r' )
   I1I1oOoooo0OooO = OOOoooooO0oOOoO . read ( )
   OOOoooooO0oOOoO . close ( )
   if 67 - 67: OoooooooOO + OoO0O00 / Oo0Ooo % o0oOOo0O0Ooo % i1IIi
  except :
   print "### No favourites file to copy"
   if 31 - 31: iI1iiIiiII . II111iiii % Oo0Ooo * OoO0 + OoO0
 if I1i1iiI1 == 'true' :
  try :
   oo0O0o = open ( oOOOoo0O0OoO , mode = 'r' )
   OoiiI1I = oo0O0o . read ( )
   oo0O0o . close ( )
   if 92 - 92: Oo0Ooo % o0oOOo0O0Ooo - iIII / iIII / OoOoOO00
  except :
   print "### No sources file to copy"
   if 84 - 84: Oo
   if 4 - 4: iI1iiIiiII . OOo00O0 / OoO0 / oOoO0o00OO0 + II111iiii
 IiiiiI = xbmc . getSkinDir ( )
 print "Current Skin: " + IiiiiI
 if video == 'fresh' and IiiiiI != "skin.confluence" :
  OooO0 . ok ( 'Default Confluence Skin Required' , '' , 'Please switch to the default Confluence skin.' , '' )
  xbmc . executebuiltin ( 'ActivateWindow(appearancesettings,return)' )
  return
  if 53 - 53: o0oOOo0O0Ooo % OoooooooOO - ooOo - i1IIi / OoO0O00
 i1111II1iIII = 1
 III1II1i ( )
 if 41 - 41: iI1iiIiiII * OoooooooOO . iIII % i11iIiiIii
 if 11 - 11: iIii1I11I1II1 . OOo00O0 - Oo0Ooo / iii + II111iiii
 if os . path . exists ( Oo0oOOo ) :
  if 29 - 29: iii . i11iIiiIii + i1IIi - OoO0 + O0 . I1IiiI
  if os . path . exists ( I11II1i ) :
   os . remove ( Oo0oOOo )
   if 8 - 8: o0oOOo0O0Ooo
  else :
   os . rename ( Oo0oOOo , I11II1i )
   if 78 - 78: i1IIi - Oo0Ooo
 if os . path . exists ( IIIII ) :
  os . remove ( IIIII )
  if 48 - 48: OoO0 - OoooooooOO + OOo00O0 % o0oOOo0O0Ooo - OoOoOO00 . I1IiiI
  if 42 - 42: OOo00O0
 if not os . path . exists ( Ooo0OO0oOO ) :
  Oo0oO00 = open ( Ooo0OO0oOO , mode = 'w+' )
  Oo0oO00 . close ( )
  if 70 - 70: o0oOOo0O0Ooo / iii + ooOo % I1IiiI % Oo0Ooo + OoO0O00
 II11iiii1Ii . close ( )
 II11iiii1Ii . create ( "Downloading Skin Fix" , "Downloading guisettings.xml" , '' , 'Please Wait' )
 o0III11IiI = os . path . join ( OOO0OOO00oo , 'guifix.zip' )
 if 80 - 80: Oo
 if 12 - 12: OoO0
 downloader . download ( guisettingslink , o0III11IiI , II11iiii1Ii )
 II11iiii1Ii . close ( )
 if 2 - 2: OoooooooOO
 if 100 - 100: Oo0Ooo / O0 * i11iIiiIii * OoooooooOO
 if zipfile . is_zipfile ( o0III11IiI ) :
  i1iI1IIi = str ( os . path . getsize ( o0III11IiI ) )
  if 46 - 46: O0 % OoooooooOO
 else :
  i1iI1IIi = iIIIiiii
  if 22 - 22: oOoO0o00OO0 + OoooooooOO - OoOoOO00 - OoO0O00 * OOo00O0 - ooOo
  if 99 - 99: iIII / I1IiiI . OoO0 - OoO0 * I1IiiI
 Oo0oO00 = open ( Ooo0OO0oOO , mode = 'r' )
 iiiO00O00O000OOO = Oo0oO00 . read ( )
 Oo0oO00 . close ( )
 if 24 - 24: iii * OoO0O00 - ooOo / iIii1I11I1II1 - Oo0Ooo . Oo
 o0000oO = re . compile ( 'id="(.+?)"' ) . findall ( iiiO00O00O000OOO )
 ooo0ooOoOoO = re . compile ( 'name="(.+?)"' ) . findall ( iiiO00O00O000OOO )
 o0o00OoOO = re . compile ( 'version="(.+?)"' ) . findall ( iiiO00O00O000OOO )
 if 2 - 2: iIII - O0 - I1ii11iIi11i / iii * OoOoOO00
 Iii1iii1I = o0000oO [ 0 ] if ( len ( o0000oO ) > 0 ) else ''
 oOo000Oo00o = ooo0ooOoOoO [ 0 ] if ( len ( ooo0ooOoOoO ) > 0 ) else ''
 i1Ii11I1II = o0o00OoOO [ 0 ] if ( len ( o0o00OoOO ) > 0 ) else ''
 if 26 - 26: I1ii11iIi11i + OOo00O0 - ooOo + iI1iiIiiII % Oo
 if os . path . exists ( Oo0OoO00oOO0o ) :
  os . removedirs ( Oo0OoO00oOO0o )
  if 84 - 84: iii % OoO0 % O0 * o0oOOo0O0Ooo
  if 15 - 15: ooOo - iIii1I11I1II1 - II111iiii - iI1iiIiiII % I1ii11iIi11i
 if iIIIiiii != i1iI1IIi :
  try :
   os . rename ( I11II1i , Oo0oOOo )
   if 80 - 80: iI1iiIiiII * oOoO0o00OO0 . i1IIi % OoO0 % I1ii11iIi11i + iIII
  except :
   OooO0 . ok ( "NO GUISETTINGS!" , 'No guisettings.xml file has been found.' , 'Please exit Kodi and try again' , '' )
   return
   if 6 - 6: I1ii11iIi11i . ooOo . OoO0O00 + iI1iiIiiII
   if 65 - 65: I1ii11iIi11i / iIII
 if video != 'fresh' :
  iIi1IiI = xbmcgui . Dialog ( ) . yesno ( name , 'We highly recommend backing up your existing build before installing any community builds. Would you like to perform a backup first?' , nolabel = 'Backup' , yeslabel = 'Install' )
  if 23 - 23: Oo / Oo * o0oOOo0O0Ooo * Oo
  if iIi1IiI == 0 :
   oooOOO00OOo = xbmc . translatePath ( os . path . join ( OOO0OOO00oo , 'Community Builds' , 'My Builds' ) )
   if 81 - 81: OoO0 + iIii1I11I1II1 - O0 - I1ii11iIi11i - I1IiiI
   if not os . path . exists ( oooOOO00OOo ) :
    os . makedirs ( oooOOO00OOo )
    if 64 - 64: I1ii11iIi11i / O0 % iI1iiIiiII % oOoO0o00OO0 % I1IiiI / OOo00O0
   IiI1Iii1 = OooooiIiiiIiIi ( heading = "Enter a name for this backup" )
   if 13 - 13: Oo0Ooo % I1ii11iIi11i . oOoO0o00OO0 % iI1iiIiiII / oOoO0o00OO0 * OoooooooOO
   if ( not IiI1Iii1 ) :
    return False , 0
    if 76 - 76: Oo
   O00oo = urllib . quote_plus ( IiI1Iii1 )
   OoOoooO000OO = xbmc . translatePath ( os . path . join ( oooOOO00OOo , O00oo + '.zip' ) )
   O00Oooi1 = [ 'plugin.program.totalinstaller' , 'plugin.program.tbs' ]
   oOOO0ooOO = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , 'Thumbs.db' , '.gitignore' ]
   i11Ii1iIiII = "Creating full backup of existing build"
   O0oOo00Ooo0o0 = "Archiving..."
   i1IiII1i1I = ""
   iI1ii1ii1I = "Please Wait"
   O0o00O0Oo0 ( OO0o , OoOoooO000OO , i11Ii1iIiII , O0oOo00Ooo0o0 , i1IiII1i1I , iI1ii1ii1I , O00Oooi1 , oOOO0ooOO )
   if 52 - 52: Oo0Ooo * iIii1I11I1II1 * Oo0Ooo * i1IIi
   if 9 - 9: oOoO0o00OO0 - oOoO0o00OO0
 if video == 'fresh' :
  IiIiIiooOoOO ( 'CB' )
  if 42 - 42: iii
 iIIiooO00O00oOO = open ( ii11i1 , mode = 'w+' )
 if 23 - 23: OoOoOO00 . OoO0O00
 if iIIIiiii != i1iI1IIi :
  iIIiooO00O00oOO . write ( 'id="' + str ( Iii1iii1I ) + '"\nname="' + oOo000Oo00o + ' [COLOR=yellow](Partially installed)[/COLOR]"\nversion="' + i1Ii11I1II + '"\ngui="' + i1iI1IIi + '"' )
  if 29 - 29: iii
 else :
  iIIiooO00O00oOO . write ( 'id="' + str ( Iii1iii1I ) + '"\nname="' + oOo000Oo00o + '"\nversion="' + i1Ii11I1II + '"\ngui="' + i1iI1IIi + '"' )
 iIIiooO00O00oOO . close ( )
 if 45 - 45: OoO0O00
 if 87 - 87: I1IiiI - O0 - iii * OOo00O0 % OOo00O0
 if video == 'libprofile' or video == 'library' or video == 'updatelibprofile' or video == 'updatelibrary' :
  try :
   shutil . copytree ( Oo00OOOOO , OOO00O , symlinks = False , ignore = shutil . ignore_patterns ( "Textures13.db" , "Addons16.db" , "Addons15.db" , "saltscache.db-wal" , "saltscache.db-shm" , "saltscache.db" , "onechannelcache.db" ) )
   if 99 - 99: O0 * i11iIiiIii % Oo * II111iiii
  except :
   i1111II1iIII = xbmcgui . Dialog ( ) . yesno ( name , 'There was an error trying to backup some databases. Continuing may wipe your existing library. Do you wish to continue?' , nolabel = 'No, cancel' , yeslabel = 'Yes, overwrite' )
   if 98 - 98: O0 + iIii1I11I1II1
   if i1111II1iIII == 0 :
    return
    if 94 - 94: i1IIi * OoO0O00 * OoOoOO00
  OoOoooO000OO = xbmc . translatePath ( os . path . join ( OOO0OOO00oo , 'Database.zip' ) )
  oOO ( OOO00O , OoOoooO000OO )
  if 93 - 93: iIII / Oo * O0
 if i1111II1iIII == 0 :
  return
  if 17 - 17: OoO0O00 / iIII % I1IiiI
 time . sleep ( 1 )
 if 47 - 47: Oo0Ooo * OoO0O00 / o0oOOo0O0Ooo * I1IiiI
 if 60 - 60: I1ii11iIi11i / iI1iiIiiII . i11iIiiIii / OoO0O00 % II111iiii
 i1II111II1 = xbmc . translatePath ( os . path . join ( OO0o , '..' , 'koditemp.zip' ) )
 time . sleep ( 2 )
 II11iiii1Ii . create ( "Community Builds" , "Downloading " + description + " build." , '' , 'Please Wait' )
 o0III11IiI = os . path . join ( Iii111II , description + '.zip' )
 if 8 - 8: iI1iiIiiII - I1ii11iIi11i * iIii1I11I1II1 % o0oOOo0O0Ooo / OoooooooOO * o0oOOo0O0Ooo
 if not os . path . exists ( Iii111II ) :
  os . makedirs ( Iii111II )
  if 74 - 74: ooOo % OoO0O00 / oOoO0o00OO0
 downloader . download ( url , o0III11IiI , II11iiii1Ii )
 if 88 - 88: oOoO0o00OO0 * Oo / i11iIiiIii / i1IIi
 if 76 - 76: OoO0 . iii - Oo + OoOoOO00 * OoO0O00 % OOo00O0
 if 24 - 24: iIii1I11I1II1 % Oo0Ooo % i11iIiiIii
 if 55 - 55: oOoO0o00OO0
 if 19 - 19: OoooooooOO / Oo * i11iIiiIii - I1IiiI
 if 99 - 99: OoO0O00 % O0 . OOo00O0 - I1ii11iIi11i . Oo0Ooo / OoOoOO00
 if 60 - 60: I1ii11iIi11i
 if 78 - 78: ooOo + II111iiii
 try :
  o0o = open ( o00oOO0 , mode = 'r' )
  i1II1I1Ii = o0o . read ( )
  o0o . close ( )
  if 13 - 13: iii + ooOo - II111iiii - o0oOOo0O0Ooo + oOoO0o00OO0 + OOo00O0
 except :
  print "### No profiles detected, most likely a fresh wipe performed"
  if 70 - 70: OoooooooOO + OoO0O00 * Oo0Ooo
 II11iiii1Ii . close ( )
 II11iiii1Ii . create ( "Community Builds" , "Checking " , '' , 'Please Wait' )
 if 20 - 20: i11iIiiIii - II111iiii - iIII % ooOo . iIII
 if 50 - 50: iIii1I11I1II1 + OOo00O0 - iii - OoooooooOO
 if zipfile . is_zipfile ( o0III11IiI ) :
  II11iiii1Ii . update ( 0 , "" , "Extracting Zip Please Wait" )
  oOOO ( o0III11IiI , OO0o , II11iiii1Ii )
  time . sleep ( 1 )
  if 84 - 84: OoOoOO00 - iii
 else :
  OooO0 . ok ( 'Not a valid zip file' , 'This file is not a valid zip file, please let the build author know on their support thread so they can amend the download path. It\'s most likely just a simple typo on their behalf.' )
  return
  if 80 - 80: i11iIiiIii % Oo - Oo0Ooo % Oo
  if 89 - 89: OoO0 * iii + OoOoOO00 / i11iIiiIii
  if 68 - 68: OoooooooOO * iii
 II11iiii1Ii . create ( "Restoring Dependencies" , "Checking " , '' , 'Please Wait' )
 II11iiii1Ii . update ( 0 , "" , "Extracting Zip Please Wait" )
 if 86 - 86: o0oOOo0O0Ooo / OoOoOO00
 if O0oo0OO0 == 'true' :
  try :
   print "### Attempting to add back favourites ###"
   iIIiooO00O00oOO = open ( I1I1i , mode = 'w+' )
   iIIiooO00O00oOO . write ( I1I1oOoooo0OooO )
   iIIiooO00O00oOO . close ( )
   II11iiii1Ii . update ( 0 , "" , "Copying Favourites" )
  except : print "### Failed to copy back favourites"
  if 40 - 40: oOoO0o00OO0
 if I1i1iiI1 == 'true' :
  try :
   print "### Attempting to add back sources ###"
   iIIiooO00O00oOO = open ( oOOOoo0O0OoO , mode = 'w+' )
   iIIiooO00O00oOO . write ( OoiiI1I )
   iIIiooO00O00oOO . close ( )
   II11iiii1Ii . update ( 0 , "" , "Copying Sources" )
   if 62 - 62: iIII / Oo
  except :
   print "### Failed to copy back favourites"
   if 74 - 74: oOoO0o00OO0 % OOo00O0 / OOo00O0 - iIii1I11I1II1 - II111iiii + Oo
 time . sleep ( 1 )
 if os . path . exists ( OOO00O ) :
  shutil . rmtree ( OOO00O )
  if 92 - 92: iii % OOo00O0
  if 18 - 18: iIII + OOo00O0 / Oo / ooOo + iIii1I11I1II1 % iI1iiIiiII
  if 94 - 94: iii
  if 37 - 37: ooOo
  if 52 - 52: I1ii11iIi11i * I1IiiI . Oo + i1IIi % ooOo / iIii1I11I1II1
  if 68 - 68: OOo00O0 - OoOoOO00 . i11iIiiIii + o0oOOo0O0Ooo
  if 71 - 71: i11iIiiIii / i1IIi * I1IiiI / OoOoOO00
  if 33 - 33: iii . Oo0Ooo
  if 89 - 89: oOoO0o00OO0 + i1IIi - iI1iiIiiII + iIII . II111iiii
  if 85 - 85: iIii1I11I1II1 - OoO0 * Oo0Ooo . ooOo + OOo00O0
  if 13 - 13: O0 + iIii1I11I1II1 % II111iiii + iIii1I11I1II1
 OOo = 'http://120.24.252.100/TI/Community_Builds/downloadcount.php?id=%s' % ( Iii1iii1I )
 if not 'update' in video :
  ooI1111i ( OOo )
  if 85 - 85: I1IiiI * iIii1I11I1II1 . oOoO0o00OO0 / oOoO0o00OO0
  if 43 - 43: I1IiiI
 if os . path . exists ( iiii11I ) :
  Oo0oO00 = open ( iiii11I , mode = 'r' )
  iiiO00O00O000OOO = Oo0oO00 . read ( )
  Oo0oO00 . close ( )
  O00O00 = re . compile ( 'version="[\s\S]*?"' ) . findall ( iiiO00O00O000OOO )
  IIIi1I1IIii1II = O00O00 [ 0 ] if ( len ( O00O00 ) > 0 ) else ''
  i1I1 = iiiO00O00O000OOO . replace ( IIIi1I1IIii1II , 'version="' + i1Ii11I1II + '"' )
  iIIiooO00O00oOO = open ( iiii11I , mode = 'w' )
  iIIiooO00O00oOO . write ( str ( i1I1 ) )
  iIIiooO00O00oOO . close ( )
  if 78 - 78: OoO0O00 % II111iiii + OoOoOO00 / I1IiiI
 else :
  iIIiooO00O00oOO = open ( iiii11I , mode = 'w+' )
  iIIiooO00O00oOO . write ( 'date="01011001"\nversion="' + i1Ii11I1II + '"' )
  iIIiooO00O00oOO . close ( )
  if 34 - 34: o0oOOo0O0Ooo % I1ii11iIi11i + OoO0 * iii / ooOo
  if 18 - 18: iIII
 if IiiIII111iI == 'false' :
  os . remove ( o0III11IiI )
  if 92 - 92: OoO0O00 % iIii1I11I1II1 / iI1iiIiiII * oOoO0o00OO0 . i1IIi + ooOo
  if 24 - 24: iI1iiIiiII . oOoO0o00OO0 * iI1iiIiiII % i11iIiiIii . i11iIiiIii + i1IIi
  if 64 - 64: iIii1I11I1II1 / iI1iiIiiII / Oo0Ooo - I1ii11iIi11i
  if 100 - 100: iI1iiIiiII + i1IIi * OoO0O00
  if 64 - 64: ooOo * i11iIiiIii . Oo0Ooo
  if 52 - 52: Oo0Ooo / iIII / oOoO0o00OO0 - o0oOOo0O0Ooo / oOoO0o00OO0
  if 74 - 74: i1IIi . iIii1I11I1II1
 if 'prof' in video :
  try :
   ooOoo = open ( o00oOO0 , mode = 'w+' )
   ooOoo . write ( i1II1I1Ii )
   ooOoo . close ( )
  except : print "### Failed to write existing profile info back into profiles.xml"
  if 25 - 25: iii . OoOoOO00
  if 3 - 3: OoOoOO00
 if video == 'library' or video == 'libprofile' or video == 'updatelibprofile' or video == 'updatelibrary' :
  oOOO ( OoOoooO000OO , Oo00OOOOO , II11iiii1Ii )
  if 52 - 52: OoOoOO00
  if 79 - 79: I1IiiI + Oo0Ooo % OoOoOO00 - iI1iiIiiII + I1IiiI * ooOo
  if i1111II1iIII != 1 :
   shutil . rmtree ( OOO00O )
 II11iiii1Ii . close ( )
 if 52 - 52: OoOoOO00 % I1ii11iIi11i * Oo0Ooo % OoooooooOO - OoO0O00
 if 13 - 13: Oo . OoO0 / iii
 if os . path . exists ( O00O0oOO00O00 ) :
  O0OOO0 ( description )
  if 93 - 93: iIII * I1IiiI * I1ii11iIi11i / I1ii11iIi11i
  try :
   os . remove ( O00O0oOO00O00 )
   if 62 - 62: iIII * OoO0 % I1ii11iIi11i - i1IIi - I1ii11iIi11i
  except :
   print "##' Failed to remove: " + O00O0oOO00O00
   if 24 - 24: Oo
  try :
   shutil . rmtree ( O0o0O00Oo0o0 )
   if 71 - 71: iI1iiIiiII - i1IIi
  except :
   print "##' Failed to remove: " + O0o0O00Oo0o0
   if 56 - 56: OoOoOO00 + ooOo
 else : print "### Community Builds - using an old build"
 if 74 - 74: oOoO0o00OO0 / OOo00O0 / II111iiii - oOoO0o00OO0 / ooOo % iii
 if 19 - 19: iI1iiIiiII % OoooooooOO + OoooooooOO
 if iIIIiiii != i1iI1IIi :
  print "### GUI SIZE DIFFERENT ATTEMPTING MERGE ###"
  i1II = os . path . join ( OO0o , 'newbuild' )
  if 50 - 50: OoOoOO00
  if not os . path . exists ( i1II ) :
   os . makedirs ( i1II )
   if 90 - 90: I1ii11iIi11i - OOo00O0
  os . makedirs ( Oo0OoO00oOO0o )
  time . sleep ( 1 )
  iiIi ( guisettingslink , video )
  time . sleep ( 1 )
  xbmc . executebuiltin ( 'UnloadSkin()' )
  time . sleep ( 1 )
  xbmc . executebuiltin ( 'ReloadSkin()' )
  time . sleep ( 1 )
  OooO0 . ok ( "Force Close Required" , "If you\'re seeing this message it means the force close was unsuccessful. Please close XBMC/Kodi via your operating system or pull the power." )
  if 25 - 25: oOoO0o00OO0
 if iIIIiiii == i1iI1IIi :
  OooO0 . ok ( 'Successfully Updated' , 'Congratulations the following build:[COLOR=dodgerblue]' , description , '[/COLOR]has been successfully updated!' )
  if 76 - 76: OoO0
  if 40 - 40: o0oOOo0O0Ooo * iI1iiIiiII / I1ii11iIi11i / OOo00O0 - iI1iiIiiII
def OOo00OOo ( url ) :
 o0Oooo0O00Ooo = 0
 i1111II1iIII = 0
 print "Restore Location: " + url
 if 84 - 84: i1IIi
 oOoO00 ( 'noobsandnerds.xml' )
 if 73 - 73: i11iIiiIii * I1ii11iIi11i . iii % I1IiiI - I1IiiI . OoOoOO00
 III1II1i ( )
 if 66 - 66: ooOo / i11iIiiIii / OoOoOO00 + I1ii11iIi11i / O0
 if url == 'local' :
  i11IIi1 = xbmcgui . Dialog ( ) . browse ( 1 , 'Select the backup file you want to restore' , 'files' , '.zip' , False , False , OOO0OOO00oo )
  if i11IIi1 == '' :
   o0Oooo0O00Ooo = 1
   if 97 - 97: i11iIiiIii
 if o0Oooo0O00Ooo == 1 :
  print "### No file selected, quitting restore process ###"
  return
  if 16 - 16: i1IIi
 if url != 'local' :
  II11iiii1Ii . create ( "Community Builds" , "Downloading build." , '' , 'Please Wait' )
  i11IIi1 = os . path . join ( Iii111II , iIo00OooooOOOO ( ) + '.zip' )
  if 12 - 12: OoOoOO00 % Oo + ooOo . O0 % iIii1I11I1II1
  if not os . path . exists ( Iii111II ) :
   os . makedirs ( Iii111II )
   if 41 - 41: OoooooooOO
  downloader . download ( url , i11IIi1 , II11iiii1Ii )
  if 13 - 13: iii + OOo00O0 - OOo00O0 % ooOo / iii
 if os . path . exists ( Oo0oOOo ) :
  if os . path . exists ( I11II1i ) :
   os . remove ( Oo0oOOo )
  else :
   os . rename ( Oo0oOOo , I11II1i )
   if 4 - 4: I1IiiI + Oo - iI1iiIiiII + oOoO0o00OO0
 if os . path . exists ( IIIII ) :
  os . remove ( IIIII )
  if 78 - 78: OoO0
  if 29 - 29: II111iiii
 if not os . path . exists ( Ooo0OO0oOO ) :
  Oo0oO00 = open ( Ooo0OO0oOO , mode = 'w+' )
  if 79 - 79: iIii1I11I1II1 - i11iIiiIii + iIII - II111iiii . iIii1I11I1II1
 if os . path . exists ( Oo0OoO00oOO0o ) :
  os . removedirs ( Oo0OoO00oOO0o )
  if 84 - 84: Oo0Ooo % iii * O0 * iii
  if 66 - 66: Oo / iIii1I11I1II1 - OoOoOO00 % O0 . iIII
 try :
  os . rename ( I11II1i , Oo0oOOo )
  if 12 - 12: Oo0Ooo + I1IiiI
 except :
  OooO0 . ok ( "NO GUISETTINGS!" , 'No guisettings.xml file has been found.' , 'Please exit XBMC and try again' , '' )
  return
  if 37 - 37: i1IIi * i11iIiiIii
 iIi1IiI = xbmcgui . Dialog ( ) . yesno ( I1ii1 , 'We highly recommend backing up your existing build before installing any builds. Would you like to perform a backup first?' , nolabel = 'Backup' , yeslabel = 'Install' )
 if iIi1IiI == 0 :
  oooOOO00OOo = xbmc . translatePath ( os . path . join ( OOO0OOO00oo , 'Community Builds' , 'My Builds' ) )
  if 95 - 95: i11iIiiIii % OOo00O0 * Oo0Ooo + i1IIi . O0 + I1ii11iIi11i
  if not os . path . exists ( oooOOO00OOo ) :
   os . makedirs ( oooOOO00OOo )
   if 7 - 7: OoO0O00 * i11iIiiIii * iIii1I11I1II1 / Oo / OOo00O0
  IiI1Iii1 = OooooiIiiiIiIi ( heading = "Enter a name for this backup" )
  if ( not IiI1Iii1 ) :
   return False , 0
   if 35 - 35: oOoO0o00OO0 * Oo
  O00oo = urllib . quote_plus ( IiI1Iii1 )
  OoOoooO000OO = xbmc . translatePath ( os . path . join ( oooOOO00OOo , O00oo + '.zip' ) )
  O00Oooi1 = [ I1IiI ]
  oOOO0ooOO = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , '.gitignore' ]
  i11Ii1iIiII = "Creating full backup of existing build"
  O0oOo00Ooo0o0 = "Archiving..."
  i1IiII1i1I = ""
  iI1ii1ii1I = "Please Wait"
  if 65 - 65: II111iiii % i1IIi
  O0o00O0Oo0 ( OO0o , OoOoooO000OO , i11Ii1iIiII , O0oOo00Ooo0o0 , i1IiII1i1I , iI1ii1ii1I , O00Oooi1 , oOOO0ooOO )
 III1II1iiI11 = xbmcgui . Dialog ( ) . yesno ( I1ii1 , 'Would you like to keep your existing database files or overwrite? Overwriting will wipe any existing music or video library you may have scanned in.' , nolabel = 'Overwrite' , yeslabel = 'Keep Existing' )
 if III1II1iiI11 == 1 :
  if os . path . exists ( OOO00O ) :
   shutil . rmtree ( OOO00O )
   if 38 - 38: i1IIi / iIii1I11I1II1 + oOoO0o00OO0
  try :
   shutil . copytree ( Oo00OOOOO , OOO00O , symlinks = False , ignore = shutil . ignore_patterns ( "Textures13.db" , "Addons16.db" , "Addons15.db" , "saltscache.db-wal" , "saltscache.db-shm" , "saltscache.db" , "onechannelcache.db" ) )
   if 26 - 26: I1ii11iIi11i . OoO0 % o0oOOo0O0Ooo
  except :
   i1111II1iIII = xbmcgui . Dialog ( ) . yesno ( I1ii1 , 'There was an error trying to backup some databases. Continuing may wipe your existing library. Do you wish to continue?' , nolabel = 'No, cancel' , yeslabel = 'Yes, overwrite' )
   if i1111II1iIII == 1 : pass
   if i1111II1iIII == 0 : o0Oooo0O00Ooo = 1 ; return
   if 4 - 4: OOo00O0
  OoOoooO000OO = xbmc . translatePath ( os . path . join ( OOO0OOO00oo , 'Database.zip' ) )
  oOO ( OOO00O , OoOoooO000OO )
  if 80 - 80: Oo0Ooo . O0 % o0oOOo0O0Ooo . o0oOOo0O0Ooo
 if o0Oooo0O00Ooo == 1 :
  print "### Chose to exit restore function ###"
  return
  if 52 - 52: OoO0O00 % i11iIiiIii . iIII % OoOoOO00 % OoooooooOO
 else :
  time . sleep ( 1 )
  O00Ooo0ooo0 = open ( I11i1 , mode = 'r' )
  OooO00o000 = O00Ooo0ooo0 . read ( )
  O00Ooo0ooo0 . close ( )
  if 5 - 5: OoOoOO00 / O0 / i11iIiiIii
  if 88 - 88: II111iiii - oOoO0o00OO0 / OoooooooOO
  print "### Checking zip file structure ###"
  ooOOOOOo = zipfile . ZipFile ( i11IIi1 )
  if 'xbmc.log' in ooOOOOOo . namelist ( ) or 'kodi.log' in ooOOOOOo . namelist ( ) or '.git' in ooOOOOOo . namelist ( ) or '.svn' in ooOOOOOo . namelist ( ) :
   print "### Whoever created this build has used completely the wrong backup method, lets try and fix it! ###"
   OooO0 . ok ( 'Fixing Bad Zip' , 'Whoever created this build has used the wrong backup method, please wait while we fix it - this could take some time! Click OK to proceed' )
   i1i111I = zipfile . ZipFile ( i11IIi1 , 'r' )
   iiOO00 = os . path . join ( Iii111II , 'fixed.zip' )
   iI1iII1 = zipfile . ZipFile ( iiOO00 , 'w' )
   if 70 - 70: iIII . OoO0O00 + I1IiiI
   II11iiii1Ii . create ( "Fixing Build" , "Checking " , '' , 'Please Wait' )
   if 34 - 34: OoO0 % I1ii11iIi11i . iIii1I11I1II1 - II111iiii
   for iIiII1 in i1i111I . infolist ( ) :
    buffer = i1i111I . read ( iIiII1 . filename )
    II1i111Ii = str ( iIiII1 . filename )
    if 1 - 1: O0 * OoO0
    if ( iIiII1 . filename [ - 4 : ] != '.log' ) and not '.git' in II1i111Ii and not '.svn' in II1i111Ii :
     iI1iII1 . writestr ( iIiII1 , buffer )
     II11iiii1Ii . update ( 0 , "Fixing..." , '[COLOR yellow]%s[/COLOR]' % iIiII1 . filename , 'Please Wait' )
     if 5 - 5: oOoO0o00OO0 - oOoO0o00OO0 / OOo00O0 % Oo0Ooo
   II11iiii1Ii . close ( )
   iI1iII1 . close ( )
   i1i111I . close ( )
   i11IIi1 = iiOO00
   if 61 - 61: ooOo - I1ii11iIi11i / oOoO0o00OO0 % I1ii11iIi11i + OoO0O00 / Oo0Ooo
  II11iiii1Ii . create ( "Restoring Backup Build" , "Checking " , '' , 'Please Wait' )
  II11iiii1Ii . update ( 0 , "" , "Extracting Zip Please Wait" )
  if 10 - 10: i11iIiiIii / OoOoOO00
  try :
   oOOO ( i11IIi1 , OO0o , II11iiii1Ii )
  except :
   OooO0 . ok ( 'ERROR IN BUILD ZIP' , 'Please contact the build author, there are errors in this zip file that has caused the install process to fail. Most likely cause is it contains files with special characters in the name.' )
   return
   if 27 - 27: I1IiiI / OoooooooOO
  time . sleep ( 1 )
  if 74 - 74: I1ii11iIi11i % OOo00O0 - OoO0O00 * iii . OoooooooOO * OoO0O00
  if III1II1iiI11 == 1 :
   oOOO ( OoOoooO000OO , Oo00OOOOO , II11iiii1Ii )
   if 99 - 99: OoOoOO00 . oOoO0o00OO0 - OoooooooOO - O0
   if i1111II1iIII != 1 :
    shutil . rmtree ( OOO00O )
    if 6 - 6: Oo
  Ii1111i11 = open ( I11i1 , mode = 'w+' )
  Ii1111i11 . write ( OooO00o000 )
  Ii1111i11 . close ( )
  try :
   os . rename ( I11II1i , IIIII )
   if 58 - 58: OoO0 * iIii1I11I1II1 + iIII . iIII
  except :
   print "NO GUISETTINGS DOWNLOADED"
   if 74 - 74: iIII - o0oOOo0O0Ooo * iI1iiIiiII % iIII
  time . sleep ( 1 )
  Oo0oO00 = open ( Oo0oOOo , mode = 'r' )
  iiiO00O00O000OOO = Oo0oO00 . read ( )
  Oo0oO00 . close ( )
  oOoO = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( iiiO00O00O000OOO )
  IIiIi = oOoO [ 0 ] if ( len ( oOoO ) > 0 ) else ''
  OOooooO = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( iiiO00O00O000OOO )
  I1I1IIiiI1 = OOooooO [ 0 ] if ( len ( OOooooO ) > 0 ) else ''
  oOoo00 = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( iiiO00O00O000OOO )
  oooOOO0o0O0 = oOoo00 [ 0 ] if ( len ( oOoo00 ) > 0 ) else ''
  if 93 - 93: iIii1I11I1II1 / OoOoOO00 % Oo0Ooo * OOo00O0 - OoO0O00 - o0oOOo0O0Ooo
  try :
   i1iiiiI11ii = open ( IIIII , mode = 'r' )
   oooooOOo0o = i1iiiiI11ii . read ( )
   i1iiiiI11ii . close ( )
   OOOOooO0 = re . compile ( '<skinsettings>[\s\S]*?<\/skinsettings>' ) . findall ( oooooOOo0o )
   Oo0Oo0 = OOOOooO0 [ 0 ] if ( len ( OOOOooO0 ) > 0 ) else ''
   Iii11ii1iIIi = re . compile ( '<skin default[\s\S]*?<\/skin>' ) . findall ( oooooOOo0o )
   oooOooooO = Iii11ii1iIIi [ 0 ] if ( len ( Iii11ii1iIIi ) > 0 ) else ''
   iiii1Ii1iii = re . compile ( '<lookandfeel>[\s\S]*?<\/lookandfeel>' ) . findall ( oooooOOo0o )
   i1I = iiii1Ii1iii [ 0 ] if ( len ( iiii1Ii1iii ) > 0 ) else ''
   i1I1 = iiiO00O00O000OOO . replace ( IIiIi , Oo0Oo0 ) . replace ( oooOOO0o0O0 , i1I ) . replace ( I1I1IIiiI1 , oooOooooO )
   iIIiooO00O00oOO = open ( Oo0oOOo , mode = 'w+' )
   iIIiooO00O00oOO . write ( str ( i1I1 ) )
   iIIiooO00O00oOO . close ( )
   if 44 - 44: OoooooooOO
  except :
   print "NO GUISETTINGS DOWNLOADED"
   if 82 - 82: OoOoOO00 . OoOoOO00
  if os . path . exists ( I11II1i ) :
   os . remove ( I11II1i )
   if 10 - 10: Oo0Ooo * I1ii11iIi11i . ooOo . OoooooooOO . Oo * I1ii11iIi11i
  os . rename ( Oo0oOOo , I11II1i )
  try :
   os . remove ( IIIII )
   if 80 - 80: OOo00O0 + iii . OOo00O0 + Oo
  except :
   pass
   if 85 - 85: i11iIiiIii . iii + OoO0 / OoO0
  os . makedirs ( Oo0OoO00oOO0o )
  time . sleep ( 1 )
  OoOooOo00o ( )
  if 43 - 43: iI1iiIiiII . OoooooooOO - II111iiii
  if 90 - 90: I1IiiI - iIii1I11I1II1 + I1ii11iIi11i * Oo * ooOo
  if 19 - 19: OOo00O0 * II111iiii % Oo0Ooo - i1IIi
  if 27 - 27: OoOoOO00 . O0 / I1ii11iIi11i . iIii1I11I1II1
  if 15 - 15: OoO0 + OoO0O00 % iIii1I11I1II1 - I1ii11iIi11i - i1IIi % o0oOOo0O0Ooo
  if 54 - 54: iI1iiIiiII - II111iiii . iIII + OoO0
  if 45 - 45: ooOo + II111iiii . oOoO0o00OO0 / I1ii11iIi11i
  if 76 - 76: OoO0 + oOoO0o00OO0 - iI1iiIiiII * iIii1I11I1II1 % i1IIi
  if 72 - 72: iIII + II111iiii . O0 - oOoO0o00OO0 / OoooooooOO . OOo00O0
  if 28 - 28: iIii1I11I1II1 . O0
  if 32 - 32: OoooooooOO
  if 29 - 29: I1ii11iIi11i
  if 41 - 41: OoO0
  if 49 - 49: OoO0 % II111iiii . OoO0 - o0oOOo0O0Ooo - iii * iI1iiIiiII
  if 47 - 47: O0 . o0oOOo0O0Ooo / OoO0 * oOoO0o00OO0
  if 63 - 63: OOo00O0 - ooOo - oOoO0o00OO0 - iIII / ooOo + OoO0O00
  if 94 - 94: iI1iiIiiII / I1IiiI . II111iiii
  if 32 - 32: ooOo . Oo % Oo . OoOoOO00
  if 37 - 37: Oo + O0 + Oo . oOoO0o00OO0 . o0oOOo0O0Ooo
def oO0oOo ( ) :
 III1II1i ( )
 OoO0IIiIi = xbmcgui . Dialog ( ) . browse ( 1 , 'Select the guisettings zip file you want to restore' , 'files' , '.zip' , False , False , OOO0OOO00oo )
 if 60 - 60: iIii1I11I1II1 / I1ii11iIi11i - II111iiii / Oo0Ooo
 if OoO0IIiIi == '' :
  return
  if 38 - 38: iii % OoO0O00 - O0 + II111iiii % OoO0 . I1IiiI
 else :
  OoO0ooOOoo = 1
  OoOooO0 ( OoO0IIiIi , OoO0ooOOoo )
  if 43 - 43: I1IiiI % I1ii11iIi11i * OoO0
  if 31 - 31: OoO0 / oOoO0o00OO0
def iI1111iI1iII ( url , name ) :
 iIi1IiI = xbmcgui . Dialog ( ) . yesno ( 'Full Wipe And New Install' , 'This is a great option for first time install or if you\'re encountering any issues with your device. This will wipe all your Kodi settings, do you wish to continue?' , nolabel = 'Cancel' , yeslabel = 'Accept' )
 if iIi1IiI == 0 :
  return
  if 61 - 61: Oo . Oo
 elif iIi1IiI == 1 :
  ii11 = '/storage/.restore/'
  iI1i1IiIIIIi = os . path . join ( ii11 , '20141128094249.tar' )
  if not os . path . exists ( ii11 ) :
   try :
    os . makedirs ( ii11 )
   except :
    pass
  downloader . download ( url , iI1i1IiIIIIi )
  time . sleep ( 2 )
  if 43 - 43: OoOoOO00 % OoO0 + Oo0Ooo - OoooooooOO . O0 % Oo0Ooo
  OOo = 'http://120.24.252.100/TI/Community_Builds/downloadcount.php?id=%s' % ( name )
  try :
   ooI1111i ( OOo )
  except :
   pass
   if 98 - 98: o0oOOo0O0Ooo * Oo0Ooo - OoO0 . iIII
  OooO0 . ok ( "Download Complete - Press OK To Reboot" , 'Once you press OK your device will attempt to reboot, if it hasn\'t rebooted within 30 seconds please pull the power to manually shutdown. When booting you may see lines of text, don\'t worry this is normal update behaviour!' )
  xbmc . executebuiltin ( 'Reboot' )
  if 2 - 2: Oo0Ooo - iIII % iIii1I11I1II1
  if 88 - 88: OOo00O0 - OoO0O00
def oO0Ooo0o00o ( ) :
 o0Oooo0O00Ooo = 0
 iIi1IiI = xbmcgui . Dialog ( ) . yesno ( 'Full Wipe And New Install' , 'This is a great option if you\'re encountering any issues with your device. This will wipe all your Kodi settings and restore with whatever is in the backup, do you wish to continue?' , nolabel = 'Cancel' , yeslabel = 'Accept' )
 if iIi1IiI == 0 :
  return
  if 53 - 53: OoOoOO00 % i1IIi
 elif iIi1IiI == 1 :
  i11IIi1 = xbmcgui . Dialog ( ) . browse ( 1 , 'Select the backup file you want to restore' , 'files' , '.tar' , False , False , O0Oo000ooO00 )
  if i11IIi1 == '' :
   o0Oooo0O00Ooo = 1
   if 35 - 35: OoO0 + I1ii11iIi11i . ooOo * Oo0Ooo
  if o0Oooo0O00Ooo == 1 :
   print "### No file selected, quitting restore process ###"
   return
  iI1i1IiIIIIi = os . path . join ( oO0 , '20141128094249.tar' )
  if not os . path . exists ( oO0 ) :
   try :
    os . makedirs ( oO0 )
   except :
    pass
  II11iiii1Ii . create ( 'Copying File To Restore Folder' , '' , 'Please wait...' )
  shutil . copyfile ( i11IIi1 , iI1i1IiIIIIi )
  xbmc . executebuiltin ( 'Reboot' )
  if 27 - 27: iIii1I11I1II1 / OoO0 - iI1iiIiiII - Oo0Ooo
  if 76 - 76: Oo . I1IiiI + Oo + iIii1I11I1II1 + iI1iiIiiII / iIii1I11I1II1
def oO0O000O0o ( ) :
 oOO0o0oo0 ( )
 if I1IIIIiii1i ( ) :
  OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue]Restore a locally stored OpenELEC Backup[/COLOR]' , '' , 'restore_local_OE' , 'Restore.png' , '' , '' , 'Restore A Full OE System Backup' )
  if 44 - 44: i1IIi % ooOo / OoOoOO00 % iI1iiIiiII . I1ii11iIi11i
 OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue]Restore A Locally stored build[/COLOR]' , 'local' , 'restore_local_CB' , 'Restore.png' , '' , '' , 'Restore A Full System Backup' )
 OOo0oO00ooO00 ( '' , '[COLOR=dodgerblue]Restore Local guisettings file[/COLOR]' , 'url' , 'LocalGUIDialog' , 'Restore.png' , '' , '' , 'Back Up Your Full System' )
 if 38 - 38: OoOoOO00 . iii
 if os . path . exists ( os . path . join ( OOO0OOO00oo , 'addons.zip' ) ) :
  OOo0oO00ooO00 ( '' , 'Restore Your Addons' , 'addons' , 'restore_zip' , 'Restore.png' , '' , '' , 'Restore Your Addons' )
  if 66 - 66: oOoO0o00OO0
 if os . path . exists ( os . path . join ( OOO0OOO00oo , 'addon_data.zip' ) ) :
  OOo0oO00ooO00 ( '' , 'Restore Your Addon UserData' , 'addon_data' , 'restore_zip' , 'Restore.png' , '' , '' , 'Restore Your Addon UserData' )
  if 61 - 61: i11iIiiIii / ooOo / i11iIiiIii
 if os . path . exists ( os . path . join ( OOO0OOO00oo , 'guisettings.xml' ) ) :
  OOo0oO00ooO00 ( '' , 'Restore Guisettings.xml' , I11II1i , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your guisettings.xml' )
  if 61 - 61: iii / iIii1I11I1II1 - i1IIi - iI1iiIiiII * i11iIiiIii
 if os . path . exists ( os . path . join ( OOO0OOO00oo , 'favourites.xml' ) ) :
  OOo0oO00ooO00 ( '' , 'Restore Favourites.xml' , I1I1i , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your favourites.xml' )
  if 86 - 86: iii % iii - OoOoOO00 + OOo00O0 / I1IiiI * OoooooooOO
 if os . path . exists ( os . path . join ( OOO0OOO00oo , 'sources.xml' ) ) :
  OOo0oO00ooO00 ( '' , 'Restore Source.xml' , oOOOoo0O0OoO , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your sources.xml' )
  if 26 - 26: II111iiii * oOoO0o00OO0 + o0oOOo0O0Ooo / O0 + i1IIi - iii
 if os . path . exists ( os . path . join ( OOO0OOO00oo , 'advancedsettings.xml' ) ) :
  OOo0oO00ooO00 ( '' , 'Restore Advancedsettings.xml' , ii1i1I1i , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your advancedsettings.xml' )
  if 56 - 56: Oo
 if os . path . exists ( os . path . join ( OOO0OOO00oo , 'keyboard.xml' ) ) :
  OOo0oO00ooO00 ( '' , 'Restore Advancedsettings.xml' , iIii11I , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your keyboard.xml' )
  if 76 - 76: i1IIi % iIii1I11I1II1 - o0oOOo0O0Ooo + iI1iiIiiII - iii
 if os . path . exists ( os . path . join ( OOO0OOO00oo , 'RssFeeds.xml' ) ) :
  OOo0oO00ooO00 ( '' , 'Restore RssFeeds.xml' , oOoo , 'resore_backup' , 'Restore.png' , '' , '' , 'Restore Your RssFeeds.xml' )
  if 81 - 81: I1ii11iIi11i + OoooooooOO - Oo * O0
  if 100 - 100: iIii1I11I1II1 - OoOoOO00
def iIi ( url ) :
 III1II1i ( )
 if 'addons' in url :
  I1Iii11II = xbmc . translatePath ( os . path . join ( OOO0OOO00oo , 'addons.zip' ) )
  ii11III1 = O00o0OO
  if 95 - 95: o0oOOo0O0Ooo * i11iIiiIii - OOo00O0 - OoooooooOO
 else :
  I1Iii11II = xbmc . translatePath ( os . path . join ( OOO0OOO00oo , 'addon_data.zip' ) )
  ii11III1 = O0o0Oo
  if 13 - 13: i1IIi . i11iIiiIii * Oo0Ooo % iIii1I11I1II1 + OOo00O0
 if 'Backup' in I1ii1 :
  i1Ii ( )
  II11iiii1Ii . create ( "Creating Backup" , "Backing Up" , '' , 'Please Wait' )
  o0I11iII = zipfile . ZipFile ( I1Iii11II , 'w' , zipfile . ZIP_DEFLATED )
  IiiIiI = len ( ii11III1 )
  iIIIIiiIii = [ ]
  ooO0oo = [ ]
  for I1Iii1iI1 , o0Oo0oOooOoOo , I1i in os . walk ( ii11III1 ) :
   for file in I1i :
    ooO0oo . append ( file )
  OO0oIiII1iiI = len ( ooO0oo )
  for I1Iii1iI1 , o0Oo0oOooOoOo , I1i in os . walk ( ii11III1 ) :
   for file in I1i :
    iIIIIiiIii . append ( file )
    oO000o = len ( iIIIIiiIii ) / float ( OO0oIiII1iiI ) * 100
    II11iiii1Ii . update ( int ( oO000o ) , "Backing Up" , '[COLOR yellow]%s[/COLOR]' % file , 'Please Wait' )
    o0Oo = os . path . join ( I1Iii1iI1 , file )
    if not 'temp' in o0Oo0oOooOoOo :
     if not I1IiI in o0Oo0oOooOoOo :
      import time
      oOoOo = '01/01/1980'
      oO0OO = time . strftime ( '%d/%m/%Y' , time . gmtime ( os . path . getmtime ( o0Oo ) ) )
      if oO0OO > oOoOo :
       o0I11iII . write ( o0Oo , o0Oo [ IiiIiI : ] )
  o0I11iII . close ( )
  II11iiii1Ii . close ( )
  OooO0 . ok ( "Backup Complete" , "You Are Now Backed Up" , '' , '' )
  if 51 - 51: I1ii11iIi11i % OoOoOO00 % i11iIiiIii + O0
 else :
  II11iiii1Ii . create ( "Extracting Zip" , "Checking " , '' , 'Please Wait' )
  II11iiii1Ii . update ( 0 , "" , "Extracting Zip Please Wait" )
  oOOO ( I1Iii11II , ii11III1 , II11iiii1Ii )
  time . sleep ( 1 )
  xbmc . executebuiltin ( 'UpdateLocalAddons ' )
  xbmc . executebuiltin ( "UpdateAddonRepos" )
  if 30 - 30: II111iiii % i1IIi * I1ii11iIi11i
  if 'Backup' in I1ii1 :
   OooO0 . ok ( "Install Complete" , 'Kodi will now close. Just re-open Kodi and wait for all the updates to complete.' )
   OoOooOo00o ( )
   if 93 - 93: O0 - i11iIiiIii - OoO0O00 + OoO0
  else :
   OooO0 . ok ( "SUCCESS!" , "You Are Now Restored" , '' , '' )
   if 86 - 86: I1IiiI / I1ii11iIi11i * OoO0 % i11iIiiIii
   if 20 - 20: oOoO0o00OO0 . OoooooooOO + oOoO0o00OO0 + iIII * I1ii11iIi11i
def i1IIiiI1iii1 ( url ) :
 xbmc . executebuiltin ( 'RunAddon(' + url + ')' )
 if 100 - 100: oOoO0o00OO0 / o0oOOo0O0Ooo
 if 11 - 11: I1ii11iIi11i * OoOoOO00 % i11iIiiIii - OoO0
def iI1ii1 ( title ) :
 oooOOOoO = ''
 iiII1IIii1i1 = xbmc . Keyboard ( oooOOOoO , title )
 iiII1IIii1i1 . doModal ( )
 if iiII1IIii1i1 . isConfirmed ( ) :
  oooOOOoO = iiII1IIii1i1 . getText ( ) . replace ( ' ' , '%20' )
  if oooOOOoO == None :
   return False
 return oooOOOoO
 if 79 - 79: I1ii11iIi11i - ooOo - o0oOOo0O0Ooo . Oo
 if 65 - 65: i11iIiiIii . OoO0O00 % oOoO0o00OO0 + iI1iiIiiII - i11iIiiIii
def oo00O0OO0oo0O ( url ) :
 IiI1Iii1 = OooooiIiiiIiIi ( heading = "Search for add-ons" )
 if 1 - 1: Oo0Ooo * O0 . I1IiiI + iIII / OoOoOO00 + iii
 if ( not IiI1Iii1 ) : return False , 0
 if 68 - 68: II111iiii
 if 61 - 61: Oo . I1ii11iIi11i * ooOo / OOo00O0 - OoO0O00
 O00oo = urllib . quote_plus ( IiI1Iii1 )
 url += O00oo
 OoIIiIIIII1I ( url )
 if 18 - 18: OOo00O0
 if 34 - 34: oOoO0o00OO0 + OOo00O0 * iii / II111iiii
def IiI1i1 ( url ) :
 IiI1Iii1 = OooooiIiiiIiIi ( heading = "Search for content" )
 if 13 - 13: oOoO0o00OO0 . oOoO0o00OO0 + i11iIiiIii % O0 % OOo00O0 + iI1iiIiiII
 if 42 - 42: i1IIi + oOoO0o00OO0 . OoooooooOO + I1ii11iIi11i . iii / OoO0
 if ( not IiI1Iii1 ) : return False , 0
 if 1 - 1: o0oOOo0O0Ooo
 if 95 - 95: Oo / i1IIi % OoO0O00 . OOo00O0 + OOo00O0
 O00oo = urllib . quote_plus ( IiI1Iii1 )
 url += O00oo
 iI1II1i ( url )
 if 80 - 80: O0 + I1ii11iIi11i + Oo
 if 95 - 95: I1ii11iIi11i
def O0o0ooo00o00 ( url ) :
 Oo0O00O000 = 'http://120.24.252.100/TI/Community_Builds/community_builds.php?id=%s' % ( url )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0oO = re . compile ( 'name="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I111iiIIiI1I = re . compile ( 'author="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IIo0Oo0oO0oOO00 = re . compile ( 'version="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1ii1 = oo0oO [ 0 ] if ( len ( oo0oO ) > 0 ) else ''
 o0O0oo0 = I111iiIIiI1I [ 0 ] if ( len ( I111iiIIiI1I ) > 0 ) else ''
 IiIiIi = IIo0Oo0oO0oOO00 [ 0 ] if ( len ( IIo0Oo0oO0oOO00 ) > 0 ) else ''
 OooO0 . ok ( I1ii1 , 'Author: [COLOR=dodgerblue]' + o0O0oo0 + '[/COLOR]      Latest Version: [COLOR=dodgerblue]' + IiIiIi + '[/COLOR]' , '' , 'Click OK to view the build page.' )
 try :
  IiIi1Ii ( url + '&visibility=homepage' , url )
 except :
  return
  print "### Could not find build No. " + url
  OooO0 . ok ( 'Build Not Found' , 'Sorry we couldn\'t find the build, it may be it\'s marked as private. Please try manually searching via the Community Builds section' )
  if 6 - 6: i11iIiiIii / OoO0O00 . i11iIiiIii / iIII
  if 26 - 26: O0 * OoO0 - I1IiiI - oOoO0o00OO0 / iIii1I11I1II1
def oO0Ooo00O ( url ) :
 OooO0 . ok ( "This build is not complete" , 'The guisettings.xml file was not copied over during the last install process. Click OK to go to the build page and complete Install Step 2 (guisettings fix).' )
 if 74 - 74: o0oOOo0O0Ooo % OoOoOO00 . oOoO0o00OO0 % OOo00O0 . O0 % II111iiii
 try :
  IiIi1Ii ( url + '&visibility=homepage' , url )
  if 5 - 5: ooOo - OoooooooOO / OoOoOO00
 except :
  return
  print "### Could not find build No. " + url
  OooO0 . ok ( 'Build Not Found' , 'Sorry we couldn\'t find the build, it may be it\'s marked as private. Please try manually searching via the Community Builds section' )
  if 30 - 30: iii % o0oOOo0O0Ooo + i1IIi * OoooooooOO * OoO0O00 - II111iiii
  if 55 - 55: OoO0O00
def I111II1ii11I1 ( ) :
 Oo0O00O000 = 'http://120.24.252.100/TI/login/login_details.php?user=%s&pass=%s' % ( o0oOoO00o , i1 )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 iIiiIII = re . compile ( 'posts="(.+?)"' ) . findall ( i11I1IiII1i1i )
 ii1I = re . compile ( 'messages="(.+?)"' ) . findall ( i11I1IiII1i1i )
 ooO00OO0ooo = re . compile ( 'unread="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O0oi1i1ii1Ii111i = re . compile ( 'email="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiiI1iiI11iii = ii1I [ 0 ] if ( len ( ii1I ) > 0 ) else ''
 o0O0oOOoo0O0 = ooO00OO0ooo [ 0 ] if ( len ( ooO00OO0ooo ) > 0 ) else ''
 OO00OOo = O0oi1i1ii1Ii111i [ 0 ] if ( len ( O0oi1i1ii1Ii111i ) > 0 ) else ''
 IiI11i1IiI1 = iIiiIII [ 0 ] if ( len ( iIiiIII ) > 0 ) else ''
 OooO0 . ok ( '[COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR]' , 'Username:  ' + o0oOoO00o , 'Email: ' + OO00OOo , 'Unread Messages: ' + o0O0oOOoo0O0 + '/' + iiiI1iiI11iii + '[CR]Posts: ' + IiI11i1IiI1 )
 if 88 - 88: Oo - O0 % o0oOOo0O0Ooo
 if 63 - 63: iIII * ooOo + iIII * OoO0 + Oo0Ooo / I1ii11iIi11i
def O00Oo00o00O ( url , type ) :
 if type == 'communitybuilds' :
  iiOOOO00oO = 'grab_builds'
  if url . endswith ( "visibility=premium" ) :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , '&reseller=' + urllib . quote ( I1IiiI ) + '&token=' + IIi1IiiiI1Ii + '&visibility=premium' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
  if url . endswith ( "visibility=reseller_private" ) :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , '&reseller=' + urllib . quote ( I1IiiI ) + '&token=' + IIi1IiiiI1Ii + '&visibility=reseller_private' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
  if url . endswith ( "visibility=public" ) :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , '&visibility=public' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
  if url . endswith ( "visibility=private" ) :
   OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow]Manual Search[/COLOR]' , '&visibility=private' , 'manual_search' , 'Manual_Search.png' , '' , '' , '' )
 if type == 'tutorials' :
  iiOOOO00oO = 'grab_tutorials'
 if type == 'hardware' :
  iiOOOO00oO = 'grab_hardware'
 if type == 'addons' :
  iiOOOO00oO = 'grab_addons'
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Sort by Most Popular[/COLOR]' , str ( url ) + '&sortx=downloads&orderx=DESC' , iiOOOO00oO , 'Popular.png' , '' , '' , '' )
 if type == 'hardware' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=lime]Filter Results[/COLOR]' , url , 'hardware_filter_menu' , 'Filter.png' , '' , '' , '' )
 if type != 'addons' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Sort by Most Popular[/COLOR]' , str ( url ) + '&sortx=downloadcount&orderx=DESC' , iiOOOO00oO , 'Popular.png' , '' , '' , '' )
 if type == 'tutorials' or type == 'hardware' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Sort by Newest[/COLOR]' , str ( url ) + '&sortx=Added&orderx=DESC' , iiOOOO00oO , 'Latest.png' , '' , '' , '' )
 else :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Sort by Newest[/COLOR]' , str ( url ) + '&sortx=created&orderx=DESC' , iiOOOO00oO , 'Latest.png' , '' , '' , '' )
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Sort by Recently Updated[/COLOR]' , str ( url ) + '&sortx=updated&orderx=DESC' , iiOOOO00oO , 'Recently_Updated.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Sort by A-Z[/COLOR]' , str ( url ) + '&sortx=name&orderx=ASC' , iiOOOO00oO , 'AtoZ.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Sort by Z-A[/COLOR]' , str ( url ) + '&sortx=name&orderx=DESC' , iiOOOO00oO , 'ZtoA.png' , '' , '' , '' )
 if type == 'public_CB' :
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Sort by Genre[/COLOR]' , url , 'genres' , 'Search_Genre.png' , '' , '' , '' )
  OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Sort by Country/Language[/COLOR]' , url , 'countries' , 'Search_Country.png' , '' , '' , '' )
  if 72 - 72: Oo . OoOoOO00 / II111iiii
  if 69 - 69: Oo * II111iiii - iIII - i1IIi + i11iIiiIii
def iiiiI1iiIi1i ( ) :
 o00iI1Ii11iIiiI1 ( 'Speed Test Instructions' , '[COLOR=blue][B]What file should I use: [/B][/COLOR][CR]This function will download a file and will work out your speed based on how long it took to download. You will then be notified of '
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
 if 11 - 11: O0 / OOo00O0 / iIii1I11I1II1 % OoO0
def I1iI1Ii1I1Iii1 ( ) :
 OOo0oO00ooO00 ( '' , '[COLOR=blue]Instructions - Read me first[/COLOR]' , 'none' , 'speed_instructions' , 'howto.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Download 16MB file   - [COLOR=lime]Server 1[/COLOR]' , 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/16MB.txt' , 'runtest' , 'Download16.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Download 32MB file   - [COLOR=lime]Server 1[/COLOR]' , 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/32MB.txt' , 'runtest' , 'Download32.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Download 64MB file   - [COLOR=lime]Server 1[/COLOR]' , 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/64MB.txt' , 'runtest' , 'Download64.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Download 128MB file - [COLOR=lime]Server 1[/COLOR]' , 'https://totalrevolution.googlecode.com/svn/trunk/download%20files/128MB.txt' , 'runtest' , 'Download128.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Download 10MB file   - [COLOR=yellow]Server 2[/COLOR]' , 'http://www.wswd.net/testdownloadfiles/10MB.zip' , 'runtest' , 'Download10.png' , '' , '' , '' )
 if 9 - 9: iIii1I11I1II1 / II111iiii * Oo
 if 96 - 96: OoO0 + I1ii11iIi11i * OoOoOO00 * iI1iiIiiII * I1ii11iIi11i . I1ii11iIi11i
def o00iI1Ii11iIiiI1 ( heading , anounce ) :
 class i1I11iIIiIIiIi ( ) :
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
   try : IiI1 = open ( anounce ) ; ii1IiI = IiI1 . read ( )
   except : ii1IiI = anounce
   self . win . getControl ( self . CONTROL_TEXTBOX ) . setText ( str ( ii1IiI ) )
   return
 i1I11iIIiIIiIi ( )
 while xbmc . getCondVisibility ( 'Window.IsVisible(textviewer)' ) :
  xbmc . sleep ( 500 )
  if 96 - 96: OoO0
  if 73 - 73: OOo00O0 + OoO0
def O0OO0OoOOo ( name , url ) :
 o00iI1Ii11iIiiI1 ( name , url )
 if 59 - 59: Oo % OoOoOO00
 if 71 - 71: I1ii11iIi11i
def iIo00OooooOOOO ( ) :
 iIiI1IiII1II1 = time . time ( )
 ooooOo0ooOOOO = time . localtime ( iIiI1IiII1II1 )
 return time . strftime ( '%Y%m%d%H%M%S' , ooooOo0ooOOOO )
 if 84 - 84: OoooooooOO - II111iiii
 if 28 - 28: i1IIi / iii . o0oOOo0O0Ooo
def iIIiiiIiiii11 ( ) :
 OOo0oO00ooO00 ( 'folder' , '[COLOR=orange]noobs[/COLOR][COLOR=dodgerblue]and[/COLOR][COLOR=orange]nerds[/COLOR] Keyword Install' , '' , 'nan_menu' , 'Keywords.png' , '' , '' , '' )
 if I1IIIIiii1i ( ) :
  OOo0oO00ooO00 ( '' , '[COLOR=darkcyan]Wi-Fi Settings[/COLOR]' , '' , 'openelec_settings' , 'Wi-Fi.png' , '' , '' , '' )
  if 22 - 22: iii
  if 50 - 50: iI1iiIiiII . iii / OoO0 . O0 . i11iIiiIii + II111iiii
  if 20 - 20: I1IiiI % i1IIi % OoOoOO00 % OOo00O0 + O0
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Add-on Maintenance/Fixes[/COLOR]' , 'none' , 'addonfixes' , 'Addon_Fixes.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Backup/Restore My Content[/COLOR]' , 'none' , 'backup_restore' , 'Backup.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , '[COLOR=dodgerblue]Clean/Wipe Options[/COLOR]' , 'none' , 'wipetools' , 'Addon_Fixes.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Check My IP Address' , 'none' , 'ipcheck' , 'Check_IP.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Check XBMC/Kodi Version' , 'none' , 'xbmcversion' , 'Version_Check.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Convert Physical Paths To Special' , OO0o , 'fix_special' , 'Special_Paths.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Force Close Kodi' , 'url' , 'kill_xbmc' , 'Kill_XBMC.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Test My Download Speed' , 'none' , 'speedtest_menu' , 'Speed_Test.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'Upload Log' , 'none' , 'uploadlog' , 'Log_File.png' , '' , '' , '' )
 OOo0oO00ooO00 ( '' , 'View My Log' , 'none' , 'log' , 'View_Log.png' , '' , '' , '' )
 if 54 - 54: O0
 if 3 - 3: I1ii11iIi11i
def I1III1i1Ii ( url ) :
 OOo0oO00ooO00 ( 'folder' , '[COLOR=yellow]1. Add-on Maintenance[/COLOR]' , str ( url ) + '&type=Maintenance' , 'grab_tutorials' , 'Maintenance.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Audio Add-ons' , str ( url ) + '&type=Audio' , 'grab_tutorials' , 'Audio.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Picture Add-ons' , str ( url ) + '&type=Pictures' , 'grab_tutorials' , 'Pictures.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Program Add-ons' , str ( url ) + '&type=Programs' , 'grab_tutorials' , 'Programs.png' , '' , '' , '' )
 OOo0oO00ooO00 ( 'folder' , 'Video Add-ons' , str ( url ) + '&type=Video' , 'grab_tutorials' , 'Video.png' , '' , '' , '' )
 if 79 - 79: iii * oOoO0o00OO0
 if 7 - 7: I1ii11iIi11i . i1IIi % iIii1I11I1II1
def III111 ( url ) :
 OOo = 'http://noobsandnerds.com/TI/TutorialPortal/downloadcount.php?id=%s' % ( url )
 ooI1111i ( OOo )
 Oo0O00O000 = 'http://noobsandnerds.com/TI/TutorialPortal/tutorialdetails.php?id=%s' % ( url )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 oo0oO = re . compile ( 'name="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I111iiIIiI1I = re . compile ( 'author="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i11i11i = re . compile ( 'video_guide1="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiI1iI = re . compile ( 'video_guide2="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Ooo00O0 = re . compile ( 'video_guide3="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OoO0OOoO0 = re . compile ( 'video_guide4="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiI11i = re . compile ( 'video_guide5="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0OoiiI1i = re . compile ( 'video_label1="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i11I = re . compile ( 'video_label2="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0oO0o0oo0O0 = re . compile ( 'video_label3="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O0oo00oOOO0o = re . compile ( 'video_label4="(.+?)"' ) . findall ( i11I1IiII1i1i )
 II1i = re . compile ( 'video_label5="(.+?)"' ) . findall ( i11I1IiII1i1i )
 II11iIIIii1i = re . compile ( 'about="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o00OooO = re . compile ( 'step1="(.+?)"' ) . findall ( i11I1IiII1i1i )
 IIiii1 = re . compile ( 'step2="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iiIII1ii1 = re . compile ( 'step3="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OOO00O00ooo0o = re . compile ( 'step4="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OoOoo = re . compile ( 'step5="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O0oOoOooo00oo = re . compile ( 'step6="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OOO0OO00 = re . compile ( 'step7="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oOO00 = re . compile ( 'step8="(.+?)"' ) . findall ( i11I1IiII1i1i )
 II1IiII1I1II = re . compile ( 'step9="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oooOII111iiI1Ii1 = re . compile ( 'step10="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oo0oO0oO00oO = re . compile ( 'step11="(.+?)"' ) . findall ( i11I1IiII1i1i )
 o0OOo000ooo0o = re . compile ( 'step12="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oo00oO0o000 = re . compile ( 'step13="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iIi1ii = re . compile ( 'step14="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1I11 = re . compile ( 'step15="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1I1oO00o0oOoo = re . compile ( 'screenshot1="(.+?)"' ) . findall ( i11I1IiII1i1i )
 oOOI1 = re . compile ( 'screenshot2="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OOI1i = re . compile ( 'screenshot3="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i1II1iII1 = re . compile ( 'screenshot4="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I11II11IiI11 = re . compile ( 'screenshot5="(.+?)"' ) . findall ( i11I1IiII1i1i )
 O00o = re . compile ( 'screenshot6="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Ii11Iiii1iiii = re . compile ( 'screenshot7="(.+?)"' ) . findall ( i11I1IiII1i1i )
 i1IIII1111 = re . compile ( 'screenshot8="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Ooo0o0000OO = re . compile ( 'screenshot9="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iIiI1II1I1 = re . compile ( 'screenshot10="(.+?)"' ) . findall ( i11I1IiII1i1i )
 OooiIiI1i1Ii = re . compile ( 'screenshot11="(.+?)"' ) . findall ( i11I1IiII1i1i )
 Oo0o00o = re . compile ( 'screenshot12="(.+?)"' ) . findall ( i11I1IiII1i1i )
 III1I1 = re . compile ( 'screenshot13="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iI1IIIIII = re . compile ( 'screenshot14="(.+?)"' ) . findall ( i11I1IiII1i1i )
 I1iIIiI1i = re . compile ( 'screenshot15="(.+?)"' ) . findall ( i11I1IiII1i1i )
 if 53 - 53: oOoO0o00OO0 * OoO0O00 / I1ii11iIi11i + I1IiiI + OoooooooOO
 I1ii1 = oo0oO [ 0 ] if ( len ( oo0oO ) > 0 ) else ''
 o0O0oo0 = I111iiIIiI1I [ 0 ] if ( len ( I111iiIIiI1I ) > 0 ) else ''
 I1I = i11i11i [ 0 ] if ( len ( i11i11i ) > 0 ) else 'None'
 ooooo = iiI1iI [ 0 ] if ( len ( iiI1iI ) > 0 ) else 'None'
 i11IIIiI1I = Ooo00O0 [ 0 ] if ( len ( Ooo00O0 ) > 0 ) else 'None'
 o0iiiI1I1iIIIi1 = OoO0OOoO0 [ 0 ] if ( len ( OoO0OOoO0 ) > 0 ) else 'None'
 Iii = iiI11i [ 0 ] if ( len ( iiI11i ) > 0 ) else 'None'
 O0Oo0o000oO = o0OoiiI1i [ 0 ] if ( len ( o0OoiiI1i ) > 0 ) else 'None'
 oO0o00oOOooO0 = i11I [ 0 ] if ( len ( i11I ) > 0 ) else 'None'
 OOOoO000 = o0oO0o0oo0O0 [ 0 ] if ( len ( o0oO0o0oo0O0 ) > 0 ) else 'None'
 oOOOO = O0oo00oOOO0o [ 0 ] if ( len ( O0oo00oOOO0o ) > 0 ) else 'None'
 IiIi1ii111i1 = II1i [ 0 ] if ( len ( II1i ) > 0 ) else 'None'
 oo000oOOo0Oo = II11iIIIii1i [ 0 ] if ( len ( II11iIIIii1i ) > 0 ) else ''
 iIi11111i1II = '[CR][CR][COLOR=dodgerblue]Step 1:[/COLOR][CR]' + o00OooO [ 0 ] if ( len ( o00OooO ) > 0 ) else ''
 oooooOoo = '[CR][CR][COLOR=dodgerblue]Step 2:[/COLOR][CR]' + IIiii1 [ 0 ] if ( len ( IIiii1 ) > 0 ) else ''
 O00O00iIi1i1Ii1 = '[CR][CR][COLOR=dodgerblue]Step 3:[/COLOR][CR]' + iiIII1ii1 [ 0 ] if ( len ( iiIII1ii1 ) > 0 ) else ''
 O00O0O = '[CR][CR][COLOR=dodgerblue]Step 4:[/COLOR][CR]' + OOO00O00ooo0o [ 0 ] if ( len ( OOO00O00ooo0o ) > 0 ) else ''
 iI1I = '[CR][CR][COLOR=dodgerblue]Step 5:[/COLOR][CR]' + OoOoo [ 0 ] if ( len ( OoOoo ) > 0 ) else ''
 oOoOO000 = '[CR][CR][COLOR=dodgerblue]Step 6:[/COLOR][CR]' + O0oOoOooo00oo [ 0 ] if ( len ( O0oOoOooo00oo ) > 0 ) else ''
 oOO0 = '[CR][CR][COLOR=dodgerblue]Step 7:[/COLOR][CR]' + OOO0OO00 [ 0 ] if ( len ( OOO0OO00 ) > 0 ) else ''
 i1i1iIi1IiI = '[CR][CR][COLOR=dodgerblue]Step 8:[/COLOR][CR]' + oOO00 [ 0 ] if ( len ( oOO00 ) > 0 ) else ''
 i11i11Iii = '[CR][CR][COLOR=dodgerblue]Step 9:[/COLOR][CR]' + II1IiII1I1II [ 0 ] if ( len ( II1IiII1I1II ) > 0 ) else ''
 OO0o00Oo0oo0 = '[CR][CR][COLOR=dodgerblue]Step 10:[/COLOR][CR]' + oooOII111iiI1Ii1 [ 0 ] if ( len ( oooOII111iiI1Ii1 ) > 0 ) else ''
 I11Oo0O00O0O00 = '[CR][CR][COLOR=dodgerblue]Step 11:[/COLOR][CR]' + oo0oO0oO00oO [ 0 ] if ( len ( oo0oO0oO00oO ) > 0 ) else ''
 II1I1i = '[CR][CR][COLOR=dodgerblue]Step 12:[/COLOR][CR]' + o0OOo000ooo0o [ 0 ] if ( len ( o0OOo000ooo0o ) > 0 ) else ''
 O00OoOo0OooOo = '[CR][CR][COLOR=dodgerblue]Step 13:[/COLOR][CR]' + oo00oO0o000 [ 0 ] if ( len ( oo00oO0o000 ) > 0 ) else ''
 OOooOoOOo0O = '[CR][CR][COLOR=dodgerblue]Step 14:[/COLOR][CR]' + iIi1ii [ 0 ] if ( len ( iIi1ii ) > 0 ) else ''
 IIi11ii = '[CR][CR][COLOR=dodgerblue]Step 15:[/COLOR][CR]' + I1I11 [ 0 ] if ( len ( I1I11 ) > 0 ) else ''
 Iii1i1Ii = I1I1oO00o0oOoo [ 0 ] if ( len ( I1I1oO00o0oOoo ) > 0 ) else ''
 III1iIii = oOOI1 [ 0 ] if ( len ( oOOI1 ) > 0 ) else ''
 iiIII1i1 = OOI1i [ 0 ] if ( len ( OOI1i ) > 0 ) else ''
 oOOo0OOoOO0 = i1II1iII1 [ 0 ] if ( len ( i1II1iII1 ) > 0 ) else ''
 IiIi = I11II11IiI11 [ 0 ] if ( len ( I11II11IiI11 ) > 0 ) else ''
 IIi1IiiIi1III = O00o [ 0 ] if ( len ( O00o ) > 0 ) else ''
 IiIiIiiIIii = Ii11Iiii1iiii [ 0 ] if ( len ( Ii11Iiii1iiii ) > 0 ) else ''
 OOo00O00o0O0 = i1IIII1111 [ 0 ] if ( len ( i1IIII1111 ) > 0 ) else ''
 iI1III = Ooo0o0000OO [ 0 ] if ( len ( Ooo0o0000OO ) > 0 ) else ''
 I1I111 = iIiI1II1I1 [ 0 ] if ( len ( iIiI1II1I1 ) > 0 ) else ''
 I1iI = OooiIiI1i1Ii [ 0 ] if ( len ( OooiIiI1i1Ii ) > 0 ) else ''
 IIiiI = Oo0o00o [ 0 ] if ( len ( Oo0o00o ) > 0 ) else ''
 ooO0 = III1I1 [ 0 ] if ( len ( III1I1 ) > 0 ) else ''
 IIOoOOoOo = iI1IIIIII [ 0 ] if ( len ( iI1IIIIII ) > 0 ) else ''
 OOOO0oO0OOo0o = I1iIIiI1i [ 0 ] if ( len ( I1iIIiI1i ) > 0 ) else ''
 I1iii = str ( '[COLOR=orange]Author: [/COLOR]' + o0O0oo0 + '[CR][CR][COLOR=lime]About: [/COLOR]' + oo000oOOo0Oo + iIi11111i1II + oooooOoo + O00O00iIi1i1Ii1 + O00O0O + iI1I + oOoOO000 + oOO0 + i1i1iIi1IiI + i11i11Iii + OO0o00Oo0oo0 + I11Oo0O00O0O00 + II1I1i + O00OoOo0OooOo + OOooOoOOo0O + IIi11ii )
 if 73 - 73: I1IiiI / Oo0Ooo - OoOoOO00 / i11iIiiIii
 if iIi11111i1II != '' :
  OOo0oO00ooO00 ( '' , '[COLOR=yellow][Text Guide][/COLOR]  ' + I1ii1 , I1iii , 'text_guide' , 'How_To.png' , iIi1ii1I1 , oo000oOOo0Oo , '' )
 if I1I != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + O0Oo0o000oO , I1I , 'play_video' , 'Video_Guide.png' , iIi1ii1I1 , '' , '' )
 if ooooo != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + oO0o00oOOooO0 , ooooo , 'play_video' , 'Video_Guide.png' , iIi1ii1I1 , '' , '' )
 if i11IIIiI1I != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + OOOoO000 , i11IIIiI1I , 'play_video' , 'Video_Guide.png' , iIi1ii1I1 , '' , '' )
 if o0iiiI1I1iIIIi1 != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + oOOOO , o0iiiI1I1iIIIi1 , 'play_video' , 'Video_Guide.png' , iIi1ii1I1 , '' , '' )
 if Iii != 'None' :
  OOo0oO00ooO00 ( '' , '[COLOR=lime][VIDEO][/COLOR]  ' + IiIi1ii111i1 , Iii , 'play_video' , 'Video_Guide.png' , iIi1ii1I1 , '' , '' )
  if 14 - 14: OoooooooOO + i11iIiiIii
  if 63 - 63: iii . I1IiiI . I1ii11iIi11i * OoO0
def IIIIII ( ) :
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
  if 22 - 22: OoOoOO00
  if 49 - 49: ooOo
def o0o000OOO ( ) :
 OooO0 = xbmcgui . Dialog ( )
 if OooO0 . yesno ( "Make Add-on Passwords Visible?" , "This will make all your add-on passwords visible in the add-on settings. Are you sure you wish to continue?" ) :
  for ooO , o0Oo0oOooOoOo , I1i in os . walk ( O00o0OO ) :
   for IiI1 in I1i :
    if IiI1 == 'settings.xml' :
     oOO000000oO0 = open ( os . path . join ( ooO , IiI1 ) ) . read ( )
     I111i1I1 = re . compile ( '<setting id=(.+?)>' ) . findall ( oOO000000oO0 )
     for o0o00o in I111i1I1 :
      if 'pass' in o0o00o :
       if 'option="hidden"' in o0o00o :
        try :
         o0OOo0O00OO0O = o0o00o . replace ( ' option="hidden"' , '' )
         IiI1 = open ( os . path . join ( ooO , IiI1 ) , mode = 'w' )
         IiI1 . write ( str ( oOO000000oO0 ) . replace ( o0o00o , o0OOo0O00OO0O ) )
         IiI1 . close ( )
        except :
         pass
  OooO0 . ok ( "Passwords Are now visible" , "Your passwords will now be visible in your add-on settings. If you want to undo this please use the option to hide passwords." )
  if 36 - 36: OOo00O0 * OOo00O0 % I1IiiI % O0 . I1IiiI % OoooooooOO
  if 96 - 96: ooOo % iIii1I11I1II1 / iIii1I11I1II1 . oOoO0o00OO0 . OoO0
def iII1I1iIIIiII ( ) :
 if o0O . getSetting ( 'email' ) == '' :
  OooO0 = xbmcgui . Dialog ( )
  OooO0 . ok ( "No Email Address Set" , "A new window will Now open for you to enter your Email address. The logfile will be sent here" )
  o0O . openSettings ( )
 xbmc . executebuiltin ( 'XBMC.RunScript(special://home/addons/' + I1IiI + '/uploadLog.py)' )
 if 41 - 41: OOo00O0 - O0 * Oo0Ooo % I1IiiI
 if 70 - 70: iI1iiIiiII
def i1Ii11 ( localbuildcheck , localversioncheck , localidcheck ) :
 if i1111 == 'true' :
  Oo0O00O000 = 'http://120.24.252.100/TI/login/login_details.php?user=%s&pass=%s' % ( o0oOoO00o , i1 )
 else : Oo0O00O000 = 'http://120.24.252.100/TI/login/login_details.php?user=%s&pass=%s' % ( '' , '' )
 i11I1IiII1i1i = ooI1111i ( Oo0O00O000 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
 OOoOOo0oo0O0o = re . compile ( 'login_msg="(.+?)"' ) . findall ( i11I1IiII1i1i )
 iIiII1IIIII1IIi = OOoOOo0oo0O0o [ 0 ] if ( len ( OOoOOo0oo0O0o ) > 0 ) else ''
 if 34 - 34: OOo00O0 * iii
 if 31 - 31: iI1iiIiiII . ooOo
 if not 'REGISTER FOR FREE' in iIiII1IIIII1IIi :
  iIIiooO00O00oOO = open ( I11i1I1I , mode = 'w+' )
  iIIiooO00O00oOO . write ( 'd="' + iIo00OooooOOOO ( ) + '"\nlogin_msg="' + iIiII1IIIII1IIi + '"' )
  iIIiooO00O00oOO . close ( )
  if 40 - 40: OoO0 - iii / II111iiii * i1IIi + iI1iiIiiII * II111iiii
 ooo0oo ( localbuildcheck , localversioncheck , localidcheck , iIiII1IIIII1IIi )
 if 53 - 53: I1ii11iIi11i - i11iIiiIii . OoO0O00 / OoOoOO00 - OOo00O0
 if 99 - 99: OoO0 - iI1iiIiiII - i1IIi / i11iIiiIii . iI1iiIiiII
def IIIii1I ( ) :
 xbmc . executebuiltin ( 'UpdateLocalAddons' )
 xbmc . executebuiltin ( 'UpdateAddonRepos' )
 xbmcgui . Dialog ( ) . ok ( 'Force Refresh Started Successfully' , 'Depending on the speed of your device it could take a few minutes for the update to take effect.' )
 return
 if 58 - 58: Oo
 if 12 - 12: I1IiiI . o0oOOo0O0Ooo * OoooooooOO
def OOO0oo ( ) :
 ii1iII1 = 1
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
      OooO0 . ok ( "NO INTERNET CONNECTION" , 'It looks like this device isn\'t connected to the internet. Only some of the maintenance options will work until you fix the connectivity problem.' )
      ooo0oo ( '' , '' , '' , '[COLOR=orange]NO INTERNET CONNECTION[/COLOR]' )
      ii1iII1 = 0
 if ii1iII1 == 1 :
  Iii1I1 ( )
  if 87 - 87: OoooooooOO - ooOo - iIII * I1ii11iIi11i
  if 44 - 44: ooOo * II111iiii * II111iiii + I1IiiI / Oo0Ooo
def Iii1I1 ( ) :
 ooo0OoO = 'None'
 OO = '0'
 if 9 - 9: Oo0Ooo - iI1iiIiiII
 if 30 - 30: OoooooooOO % Oo
 Oo0oO00 = open ( iiii11I , mode = 'r' )
 iiiO00O00O000OOO = Oo0oO00 . read ( )
 Oo0oO00 . close ( )
 if 14 - 14: OoOoOO00 / OoO0O00 / i11iIiiIii - OoOoOO00 / o0oOOo0O0Ooo - Oo
 o0o00O00Oo0 = re . compile ( 'date="(.+?)"' ) . findall ( iiiO00O00O000OOO )
 ooOO0oo0o0o = o0o00O00Oo0 [ 0 ] if ( len ( o0o00O00Oo0 ) > 0 ) else ''
 O00O00 = re . compile ( 'version="(.+?)"' ) . findall ( iiiO00O00O000OOO )
 IIIi1I1IIii1II = O00O00 [ 0 ] if ( len ( O00O00 ) > 0 ) else ''
 if 23 - 23: OOo00O0 * oOoO0o00OO0 . II111iiii - OoooooooOO + OoO0
 i1iiiiI11ii = open ( ii11i1 , mode = 'r' )
 oooooOOo0o = i1iiiiI11ii . read ( )
 i1iiiiI11ii . close ( )
 if 73 - 73: OoooooooOO % iIII . i1IIi - iIii1I11I1II1 . OoO0O00
 II1i111 = re . compile ( 'id="(.+?)"' ) . findall ( oooooOOo0o )
 II111i1ii1iII = re . compile ( 'name="(.+?)"' ) . findall ( oooooOOo0o )
 OO = II1i111 [ 0 ] if ( len ( II1i111 ) > 0 ) else 'None'
 ooo0OoO = II111i1ii1iII [ 0 ] if ( len ( II111i1ii1iII ) > 0 ) else ''
 if 100 - 100: i1IIi * i1IIi
 if 26 - 26: Oo . OoO0O00 % OoOoOO00
 if oO == 'true' :
  try :
   i11I1IiII1i1i = ooI1111i ( i1iiIIiiI111 ) . replace ( '\n' , '' ) . replace ( '\r' , '' )
   ooOO0o0ooOo0 = re . compile ( 'date="(.+?)"' ) . findall ( i11I1IiII1i1i )
   i11iii11 = re . compile ( 'video="https://www.youtube.com/watch\?v=(.+?)"' ) . findall ( i11I1IiII1i1i )
   Ii11i = ooOO0o0ooOo0 [ 0 ] if ( len ( ooOO0o0ooOo0 ) > 0 ) else ''
   I11111i = i11iii11 [ 0 ] if ( len ( i11iii11 ) > 0 ) else ''
   if 46 - 46: OoooooooOO
   if 80 - 80: O0 * oOoO0o00OO0
   if int ( ooOO0oo0o0o ) < int ( Ii11i ) :
    i1I1 = iiiO00O00O000OOO . replace ( ooOO0oo0o0o , Ii11i )
    iIIiooO00O00oOO = open ( iiii11I , mode = 'w' )
    iIIiooO00O00oOO . write ( str ( i1I1 ) )
    iIIiooO00O00oOO . close ( )
    if 73 - 73: iI1iiIiiII / OoO0 + OOo00O0 . Oo - II111iiii / iIii1I11I1II1
   yt . PlayVideo ( I11111i , forcePlayer = True )
   xbmc . sleep ( 500 )
   while xbmc . Player ( ) . isPlaying ( ) :
    xbmc . sleep ( 500 )
  except : pass
 if not os . path . exists ( I11i1I1I ) :
  print "### First login check ###"
  i1Ii11 ( ooo0OoO , IIIi1I1IIii1II , OO )
  if 79 - 79: OOo00O0 * Oo0Ooo . o0oOOo0O0Ooo - OOo00O0
  if 16 - 16: I1IiiI - O0 * I1ii11iIi11i . I1ii11iIi11i % Oo
 else :
  IiI11 = open ( I11i1I1I , mode = 'r' )
  I1iiiii = IiI11 . read ( )
  IiI11 . close ( )
  if 54 - 54: Oo . I1ii11iIi11i * iii % OOo00O0 . O0 * iI1iiIiiII
  o00OOOOoOO = re . compile ( 'd="(.+?)"' ) . findall ( I1iiiii )
  OooOoOoo0ooo0 = re . compile ( 'login_msg="(.+?)"' ) . findall ( I1iiiii )
  O000O = o00OOOOoOO [ 0 ] if ( len ( o00OOOOoOO ) > 0 ) else '0'
  iIiII1IIIII1IIi = OooOoOoo0ooo0 [ 0 ] if ( len ( OooOoOoo0ooo0 ) > 0 ) else ''
  if 69 - 69: Oo0Ooo * iIII
  if int ( O000O ) + 2000000 > int ( iIo00OooooOOOO ( ) ) :
   print "### Login successful ###"
   ooo0oo ( ooo0OoO , IIIi1I1IIii1II , OO , iIiII1IIIII1IIi )
  else :
   print "### Checking login ###"
   i1Ii11 ( ooo0OoO , IIIi1I1IIii1II , OO )
   if 91 - 91: o0oOOo0O0Ooo . iIII / OoO0O00 / i11iIiiIii * o0oOOo0O0Ooo
   if 52 - 52: I1IiiI - i11iIiiIii / iI1iiIiiII . ooOo
def OooO0OOo ( ) :
 II1i1I = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'cache' )
 if os . path . exists ( II1i1I ) == True :
  for ooO , o0Oo0oOooOoOo , I1i in os . walk ( II1i1I ) :
   IIi1ii = 0
   IIi1ii += len ( I1i )
   if IIi1ii > 0 :
    for IiI1 in I1i :
     try :
      os . unlink ( os . path . join ( ooO , IiI1 ) )
     except :
      pass
    for iIiI1IIiii11 in o0Oo0oOooOoOo :
     try :
      shutil . rmtree ( os . path . join ( ooO , iIiI1IIiii11 ) )
     except :
      pass
 OOo0Oo = os . path . join ( xbmc . translatePath ( 'special://home' ) , 'temp' )
 if os . path . exists ( OOo0Oo ) == True :
  for ooO , o0Oo0oOooOoOo , I1i in os . walk ( OOo0Oo ) :
   IIi1ii = 0
   IIi1ii += len ( I1i )
   if IIi1ii > 0 :
    for IiI1 in I1i :
     try :
      os . unlink ( os . path . join ( ooO , IiI1 ) )
     except :
      pass
    for iIiI1IIiii11 in o0Oo0oOooOoOo :
     try :
      shutil . rmtree ( os . path . join ( ooO , iIiI1IIiii11 ) )
     except :
      pass
 if xbmc . getCondVisibility ( 'system.platform.ATV2' ) :
  iI1iIiI1Ii1iI = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'Other' )
  for ooO , o0Oo0oOooOoOo , I1i in os . walk ( iI1iIiI1Ii1iI ) :
   IIi1ii = 0
   IIi1ii += len ( I1i )
   if IIi1ii > 0 :
    for IiI1 in I1i :
     os . unlink ( os . path . join ( ooO , IiI1 ) )
    for iIiI1IIiii11 in o0Oo0oOooOoOo :
     shutil . rmtree ( os . path . join ( ooO , iIiI1IIiii11 ) )
  OooOooo00OOO0o = os . path . join ( '/private/var/mobile/Library/Caches/AppleTV/Video/' , 'LocalAndRental' )
  for ooO , o0Oo0oOooOoOo , I1i in os . walk ( OooOooo00OOO0o ) :
   IIi1ii = 0
   IIi1ii += len ( I1i )
   if IIi1ii > 0 :
    for IiI1 in I1i :
     os . unlink ( os . path . join ( ooO , IiI1 ) )
    for iIiI1IIiii11 in o0Oo0oOooOoOo :
     shutil . rmtree ( os . path . join ( ooO , iIiI1IIiii11 ) )
     if 41 - 41: Oo % i11iIiiIii * I1IiiI + o0oOOo0O0Ooo / ooOo
 ooO0i11i1i1i = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.module.simple.downloader' ) , '' )
 if os . path . exists ( ooO0i11i1i1i ) == True :
  for ooO , o0Oo0oOooOoOo , I1i in os . walk ( ooO0i11i1i1i ) :
   IIi1ii = 0
   IIi1ii += len ( I1i )
   if IIi1ii > 0 :
    for IiI1 in I1i :
     os . unlink ( os . path . join ( ooO , IiI1 ) )
    for iIiI1IIiii11 in o0Oo0oOooOoOo :
     shutil . rmtree ( os . path . join ( ooO , iIiI1IIiii11 ) )
     if 83 - 83: II111iiii + iI1iiIiiII - o0oOOo0O0Ooo % o0oOOo0O0Ooo * o0oOOo0O0Ooo
 o0iiiii1i1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.image.music.slideshow/cache' ) , '' )
 if os . path . exists ( o0iiiii1i1 ) == True :
  for ooO , o0Oo0oOooOoOo , I1i in os . walk ( o0iiiii1i1 ) :
   IIi1ii = 0
   IIi1ii += len ( I1i )
   if IIi1ii > 0 :
    for IiI1 in I1i :
     os . unlink ( os . path . join ( ooO , IiI1 ) )
    for iIiI1IIiii11 in o0Oo0oOooOoOo :
     shutil . rmtree ( os . path . join ( ooO , iIiI1IIiii11 ) )
     if 18 - 18: OoOoOO00 * OoOoOO00 - o0oOOo0O0Ooo % iIII % II111iiii - iI1iiIiiII
 OOoi1Iiiiiii = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache' ) , '' )
 if os . path . exists ( OOoi1Iiiiiii ) == True :
  for ooO , o0Oo0oOooOoOo , I1i in os . walk ( OOoi1Iiiiiii ) :
   IIi1ii = 0
   IIi1ii += len ( I1i )
   if IIi1ii > 0 :
    for IiI1 in I1i :
     os . unlink ( os . path . join ( ooO , IiI1 ) )
    for iIiI1IIiii11 in o0Oo0oOooOoOo :
     shutil . rmtree ( os . path . join ( ooO , iIiI1IIiii11 ) )
     if 62 - 62: iIii1I11I1II1 % OOo00O0 % I1ii11iIi11i * iI1iiIiiII
 oO0OO0o0oo0o = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.itv/Images' ) , '' )
 if os . path . exists ( oO0OO0o0oo0o ) == True :
  for ooO , o0Oo0oOooOoOo , I1i in os . walk ( oO0OO0o0oo0o ) :
   IIi1ii = 0
   IIi1ii += len ( I1i )
   if IIi1ii > 0 :
    for IiI1 in I1i :
     os . unlink ( os . path . join ( ooO , IiI1 ) )
    for iIiI1IIiii11 in o0Oo0oOooOoOo :
     shutil . rmtree ( os . path . join ( ooO , iIiI1IIiii11 ) )
     if 55 - 55: iI1iiIiiII
 iiii11IiI1 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/script.navi-x/cache' ) , '' )
 if os . path . exists ( iiii11IiI1 ) == True :
  for ooO , o0Oo0oOooOoOo , I1i in os . walk ( iiii11IiI1 ) :
   IIi1ii = 0
   IIi1ii += len ( I1i )
   if IIi1ii > 0 :
    for IiI1 in I1i :
     os . unlink ( os . path . join ( ooO , IiI1 ) )
    for iIiI1IIiii11 in o0Oo0oOooOoOo :
     shutil . rmtree ( os . path . join ( ooO , iIiI1IIiii11 ) )
     if 1 - 1: OoooooooOO / o0oOOo0O0Ooo / iii / OOo00O0
 o0o00oO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.phstreams/Cache' ) , '' )
 if os . path . exists ( o0o00oO ) == True :
  for ooO , o0Oo0oOooOoOo , I1i in os . walk ( o0o00oO ) :
   IIi1ii = 0
   IIi1ii += len ( I1i )
   if IIi1ii > 0 :
    for IiI1 in I1i :
     os . unlink ( os . path . join ( ooO , IiI1 ) )
    for iIiI1IIiii11 in o0Oo0oOooOoOo :
     shutil . rmtree ( os . path . join ( ooO , iIiI1IIiii11 ) )
     if 54 - 54: OoO0 % iI1iiIiiII * OoooooooOO
 OO000o0O0OO0 = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.audio.ramfm/cache' ) , '' )
 if os . path . exists ( OO000o0O0OO0 ) == True :
  for ooO , o0Oo0oOooOoOo , I1i in os . walk ( OO000o0O0OO0 ) :
   IIi1ii = 0
   IIi1ii += len ( I1i )
   if IIi1ii > 0 :
    for IiI1 in I1i :
     os . unlink ( os . path . join ( ooO , IiI1 ) )
    for iIiI1IIiii11 in o0Oo0oOooOoOo :
     shutil . rmtree ( os . path . join ( ooO , iIiI1IIiii11 ) )
     if 97 - 97: OoO0 % OoOoOO00 / I1ii11iIi11i / iIii1I11I1II1 * OoooooooOO * Oo
 oOoOOo00oO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.whatthefurk/cache' ) , '' )
 if os . path . exists ( oOoOOo00oO ) == True :
  for ooO , o0Oo0oOooOoOo , I1i in os . walk ( oOoOOo00oO ) :
   IIi1ii = 0
   IIi1ii += len ( I1i )
   if IIi1ii > 0 :
    for IiI1 in I1i :
     os . unlink ( os . path . join ( ooO , IiI1 ) )
    for iIiI1IIiii11 in o0Oo0oOooOoOo :
     shutil . rmtree ( os . path . join ( ooO , iIiI1IIiii11 ) )
     if 71 - 71: i11iIiiIii * OoOoOO00 * Oo + ooOo + Oo0Ooo
 try :
  oOoOo0OOOOOO = os . path . join ( xbmc . translatePath ( 'special://profile/addon_data/plugin.video.genesis' ) , 'cache.db' )
  Oooo = database . connect ( oOoOo0OOOOOO )
  I1iIiii = Oooo . cursor ( )
  I1iIiii . execute ( "DROP TABLE IF EXISTS rel_list" )
  I1iIiii . execute ( "VACUUM" )
  Oooo . commit ( )
  I1iIiii . execute ( "DROP TABLE IF EXISTS rel_lib" )
  I1iIiii . execute ( "VACUUM" )
  Oooo . commit ( )
 except :
  pass
  if 12 - 12: iI1iiIiiII + o0oOOo0O0Ooo - Oo / Oo / oOoO0o00OO0 * OoooooooOO
  if 40 - 40: Oo0Ooo * OoooooooOO + iI1iiIiiII
def IiIiIiooOoOO ( mode ) :
 if zip == '' :
  OooO0 . ok ( 'Please set your backup location before proceeding' , 'You have not set your backup storage folder.\nPlease update the addon settings and try again.' )
  o0O . openSettings ( sys . argv [ 0 ] )
  ooOO0 = o0O . getSetting ( 'zip' )
  if ooOO0 == '' :
   IiIiIiooOoOO ( mode )
 oooOOO00OOo = xbmc . translatePath ( os . path . join ( OOO0OOO00oo , 'Community Builds' , 'My Builds' ) )
 if not os . path . exists ( oooOOO00OOo ) :
  os . makedirs ( oooOOO00OOo )
 iIi1IiI = xbmcgui . Dialog ( ) . yesno ( "ABSOLUTELY CERTAIN?!!!" , 'Are you absolutely certain you want to wipe?' , '' , 'All addons and settings will be completely wiped!' , yeslabel = 'Yes' , nolabel = 'No' )
 if 17 - 17: Oo - ooOo
 if iIi1IiI == 1 :
  if o00OO00OoO != "skin.confluence" :
   OooO0 . ok ( 'Default Confluence Skin Required' , 'Please switch to the default Confluence skin before performing a wipe.' )
   xbmc . executebuiltin ( "ActivateWindow(appearancesettings,return)" )
   return
  else :
   if 1 - 1: iIii1I11I1II1 / i11iIiiIii * II111iiii
   iIi1IiI = xbmcgui . Dialog ( ) . yesno ( "VERY IMPORTANT" , 'This will completely wipe your install.' , 'Would you like to create a backup before proceeding?' , '' , yeslabel = 'No' , nolabel = 'Yes' )
   if iIi1IiI == 0 :
    if not os . path . exists ( oooOOO00OOo ) :
     os . makedirs ( oooOOO00OOo )
    IiI1Iii1 = OooooiIiiiIiIi ( heading = "Enter a name for this backup" )
    if ( not IiI1Iii1 ) : return False , 0
    O00oo = urllib . quote_plus ( IiI1Iii1 )
    OoOoooO000OO = xbmc . translatePath ( os . path . join ( oooOOO00OOo , O00oo + '.zip' ) )
    O00Oooi1 = [ 'plugin.program.totalinstaller' , 'plugin.program.tbs' ]
    oOOO0ooOO = [ "xbmc.log" , "xbmc.old.log" , "kodi.log" , "kodi.old.log" , '.DS_Store' , '.setup_complete' , 'XBMCHelper.conf' , '.gitignore' ]
    i11Ii1iIiII = "Creating full backup of existing build"
    O0oOo00Ooo0o0 = "Archiving..."
    i1IiII1i1I = ""
    iI1ii1ii1I = "Please Wait"
    O0o00O0Oo0 ( OO0o , OoOoooO000OO , i11Ii1iIiII , O0oOo00Ooo0o0 , i1IiII1i1I , iI1ii1ii1I , O00Oooi1 , oOOO0ooOO )
    if 48 - 48: I1ii11iIi11i + O0 * ooOo + I1ii11iIi11i + I1ii11iIi11i
    if 60 - 60: II111iiii % Oo0Ooo
   II11iiii1Ii . create ( "Wiping Existing Content" , '' , 'Please wait...' , '' )
   for ooO , o0Oo0oOooOoOo , I1i in os . walk ( OO0o , topdown = True ) :
    o0Oo0oOooOoOo [ : ] = [ iIiI1IIiii11 for iIiI1IIiii11 in o0Oo0oOooOoOo if iIiI1IIiii11 not in i1Oo00 ]
    for I1ii1 in I1i :
     try :
      II11iiii1Ii . update ( 0 , "Removing [COLOR=yellow]" + I1ii1 + '[/COLOR]' , '' , 'Please wait...' )
      os . unlink ( os . path . join ( ooO , I1ii1 ) )
      os . remove ( os . path . join ( ooO , I1ii1 ) )
      os . rmdir ( os . path . join ( ooO , I1ii1 ) )
     except : print "Failed to remove file: " + I1ii1
     if 62 - 62: O0 + oOoO0o00OO0 - oOoO0o00OO0 % iIii1I11I1II1
   i1III1i = [ I1ii1 for I1ii1 in os . listdir ( Ooo ) if os . path . isdir ( os . path . join ( Ooo , I1ii1 ) ) ]
   try :
    for I1ii1 in i1III1i :
     try :
      if I1ii1 not in i1Oo00 :
       II11iiii1Ii . update ( 0 , "Cleaning Directory: [COLOR=yellow]" + I1ii1 + ' [/COLOR]' , '' , 'Please wait...' )
       shutil . rmtree ( os . path . join ( Ooo , I1ii1 ) )
     except : print "Failed to remove: " + I1ii1
   except : pass
   if 39 - 39: II111iiii - OoO0 / ooOo . iI1iiIiiII % I1IiiI
   for ooO , o0Oo0oOooOoOo , I1i in os . walk ( Ooo , topdown = True ) :
    o0Oo0oOooOoOo [ : ] = [ iIiI1IIiii11 for iIiI1IIiii11 in o0Oo0oOooOoOo if iIiI1IIiii11 not in i1Oo00 ]
    for I1ii1 in I1i :
     try :
      II11iiii1Ii . update ( 0 , "Removing [COLOR=yellow]" + I1ii1 + '[/COLOR]' , '' , 'Please wait...' )
      os . unlink ( os . path . join ( ooO , I1ii1 ) )
      os . remove ( os . path . join ( ooO , I1ii1 ) )
     except : print "Failed to remove file: " + I1ii1
     if 18 - 18: OoooooooOO * OoOoOO00 . II111iiii + O0 - OoooooooOO * o0oOOo0O0Ooo
   Ii1IiIiI1Ii = [ I1ii1 for I1ii1 in os . listdir ( O00o0OO ) if os . path . isdir ( os . path . join ( O00o0OO , I1ii1 ) ) ]
   try :
    for I1ii1 in Ii1IiIiI1Ii :
     try :
      if iiIIIII1i1iI == 'true' :
       if I1ii1 not in i1Oo00 and not 'repo' in I1ii1 :
        II11iiii1Ii . update ( 0 , "Removing Add-on: [COLOR=yellow]" + I1ii1 + ' [/COLOR]' , '' , 'Please wait...' )
        shutil . rmtree ( os . path . join ( O00o0OO , I1ii1 ) )
      else :
       if I1ii1 not in i1Oo00 :
        II11iiii1Ii . update ( 0 , "Removing Add-on: [COLOR=yellow]" + I1ii1 + ' [/COLOR]' , '' , 'Please wait...' )
        shutil . rmtree ( os . path . join ( O00o0OO , I1ii1 ) )
     except : print "Failed to remove: " + I1ii1
   except : pass
   if 60 - 60: iii * I1IiiI . iIII
   i11ii111II1II = [ I1ii1 for I1ii1 in os . listdir ( O0o0Oo ) if os . path . isdir ( os . path . join ( O0o0Oo , I1ii1 ) ) ]
   try :
    for I1ii1 in i11ii111II1II :
     try :
      if I1ii1 not in i1Oo00 :
       II11iiii1Ii . update ( 0 , "Removing Add-on Data: [COLOR=yellow]" + I1ii1 + ' [/COLOR]' , '' , 'Please wait...' )
       shutil . rmtree ( os . path . join ( O0o0Oo , I1ii1 ) )
     except : print "Failed to remove: " + I1ii1
   except : pass
   if 2 - 2: II111iiii + OoO0 - OoO0O00 / oOoO0o00OO0 - OoO0O00 * I1ii11iIi11i
   oooOOOoo0O = [ I1ii1 for I1ii1 in os . listdir ( OO0o ) if os . path . isdir ( os . path . join ( OO0o , I1ii1 ) ) ]
   try :
    for I1ii1 in oooOOOoo0O :
     try :
      if I1ii1 not in i1Oo00 :
       II11iiii1Ii . update ( 0 , "Cleaning Directory: [COLOR=yellow]" + I1ii1 + ' [/COLOR]' , '' , 'Please wait...' )
       shutil . rmtree ( os . path . join ( OO0o , I1ii1 ) )
     except : print "Failed to remove: " + I1ii1
   except : pass
  if mode != 'CB' :
   OooO0 . ok ( 'Wipe Complete' , 'Kodi will now close.' , 'When you next load up Kodi it should boot into the default Confluence skin and you should have a fresh install.' )
   xbmc . executebuiltin ( 'quit' )
  try :
   os . remove ( iiii11I )
  except : print "### Failed to remove startup.xml"
  try :
   os . remove ( ii11i1 )
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
 if 78 - 78: OOo00O0
 if 62 - 62: I1IiiI + OoooooooOO + OOo00O0
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
 if 60 - 60: O0 / i1IIi % i11iIiiIii / oOoO0o00OO0
def ooo00o0OO0 ( url ) :
 iIii = xbmc . getInfoLabel ( "System.BuildVersion" )
 IiIiIi = float ( iIii [ : 4 ] )
 if IiIiIi < 14 :
  oO0OOOo0OO = 'You are running XBMC'
 else :
  oO0OOOo0OO = 'You are running Kodi'
 OooO0 = xbmcgui . Dialog ( )
 OooO0 . ok ( oO0OOOo0OO , "Your version is: %s" % IiIiIi )
 if 25 - 25: Oo / OoooooooOO - I1ii11iIi11i
 if 31 - 31: iii + OoO0O00 / I1IiiI * O0 + O0
 if 34 - 34: iI1iiIiiII
 if 5 - 5: OoO0O00 . I1IiiI
 if 48 - 48: Oo0Ooo - OoO0O00 . iii - iIii1I11I1II1 % OoO0
 if 47 - 47: oOoO0o00OO0 / OoooooooOO - II111iiii
 if 91 - 91: OoOoOO00 + o0oOOo0O0Ooo
 if 23 - 23: i1IIi
 if 9 - 9: i1IIi % OOo00O0 - OoO0O00 * OoOoOO00 . o0oOOo0O0Ooo
 if 18 - 18: OoO0 . OoOoOO00 + oOoO0o00OO0 . I1IiiI + OoooooooOO . OoO0O00
 if 31 - 31: OOo00O0 - iii
 if 49 - 49: iIii1I11I1II1 - iIii1I11I1II1 - OoOoOO00 + iI1iiIiiII / OoOoOO00
 if 74 - 74: OoooooooOO + I1ii11iIi11i % O0
 if 32 - 32: I1ii11iIi11i + I1ii11iIi11i
 if 89 - 89: iIII + ooOo + OoO0 - Oo
 if 12 - 12: OoOoOO00 - o0oOOo0O0Ooo - OOo00O0 / iii
 if 17 - 17: OoO0O00 - OOo00O0 - II111iiii / OOo00O0 / OoO0
 if 30 - 30: Oo * I1ii11iIi11i % I1ii11iIi11i + oOoO0o00OO0 * iI1iiIiiII
 if 33 - 33: o0oOOo0O0Ooo + iii * O0 * OoO0O00 . I1ii11iIi11i
 if 74 - 74: oOoO0o00OO0 * oOoO0o00OO0 * o0oOOo0O0Ooo / ooOo
 if 91 - 91: i11iIiiIii . I1ii11iIi11i / II111iiii
 if 97 - 97: OoO0 % i1IIi % iI1iiIiiII + Oo0Ooo - O0 - iii
OOOOOoooO = ooo0 ( )
Oo0o0000OOoO = None
IIi11 = None
ii1iOO00Oooo000 = None
o0O0oo0 = None
o00ooo0O = None
oO0OOOOO00O0OO = None
I1iii = None
OO00OOo = None
i1iiIIi1I = None
IiIIIIIi = None
Ii1IiIiIi1IiI = None
i11I1IiII1i1i = None
OoO0ooOOoo = None
iiiI1iiI11iii = None
oO0o0O00O00O = None
I1ii1 = None
IiI11i1IiI1 = None
iI1 = None
IiIi1I1ii111 = None
O0OoO0ooOO0o = None
o00oo0oO00O000 = None
o0Ooo0o0Oo = None
oO0o = None
O00oo = None
IIiI1 = None
o0O0oOOoo0O0 = None
iiIIiIi = None
IiIiIi = None
ooO0oOOooOo0 = None
oo00ooooOOo00 = None
iIiII1IIIII1IIi = None
I1ii1I11iIi = None
IiO00oo0o0ooO = 'maintenance'
if 70 - 70: Oo0Ooo + OOo00O0 + Oo . I1ii11iIi11i - I1ii11iIi11i
try : Oo0o0000OOoO = urllib . unquote_plus ( OOOOOoooO [ "addon_id" ] )
except : pass
try : iIiI = urllib . unquote_plus ( OOOOOoooO [ "adult" ] )
except : pass
try : IIi11 = urllib . unquote_plus ( OOOOOoooO [ "artpack" ] )
except : pass
try : ii1iOO00Oooo000 = urllib . unquote_plus ( OOOOOoooO [ "audioaddons" ] )
except : pass
try : o0O0oo0 = urllib . unquote_plus ( OOOOOoooO [ "author" ] )
except : pass
try : o00ooo0O = urllib . unquote_plus ( OOOOOoooO [ "buildname" ] )
except : pass
try : oO0OOOOO00O0OO = urllib . unquote_plus ( OOOOOoooO [ "data_path" ] )
except : pass
try : I1iii = urllib . unquote_plus ( OOOOOoooO [ "description" ] )
except : pass
try : OO00OOo = urllib . unquote_plus ( OOOOOoooO [ "email" ] )
except : pass
try : i1iiIIi1I = urllib . unquote_plus ( OOOOOoooO [ "fanart" ] )
except : pass
try : IiIIIIIi = urllib . unquote_plus ( OOOOOoooO [ "forum" ] )
except : pass
try : iIIiiiI1iI1 = urllib . unquote_plus ( OOOOOoooO [ "guisettingslink" ] )
except : pass
try : Ii1IiIiIi1IiI = urllib . unquote_plus ( OOOOOoooO [ "iconimage" ] )
except : pass
try : i11I1IiII1i1i = urllib . unquote_plus ( OOOOOoooO [ "link" ] )
except : pass
try : OoO0ooOOoo = urllib . unquote_plus ( OOOOOoooO [ "local" ] )
except : pass
try : iiiI1iiI11iii = urllib . unquote_plus ( OOOOOoooO [ "messages" ] )
except : pass
try : oO0o0O00O00O = str ( OOOOOoooO [ "mode" ] )
except : pass
try : I1ii1 = urllib . unquote_plus ( OOOOOoooO [ "name" ] )
except : pass
try : ii111iiIii = urllib . unquote_plus ( OOOOOoooO [ "pictureaddons" ] )
except : pass
try : IiI11i1IiI1 = urllib . unquote_plus ( OOOOOoooO [ "posts" ] )
except : pass
try : iI1 = urllib . unquote_plus ( OOOOOoooO [ "programaddons" ] )
except : pass
try : IiIi1I1ii111 = urllib . unquote_plus ( OOOOOoooO [ "provider_name" ] )
except : pass
try : o00oo0oO00O000 = urllib . unquote_plus ( OOOOOoooO [ "repo_link" ] )
except : pass
try : O0OoO0ooOO0o = urllib . unquote_plus ( OOOOOoooO [ "repo_id" ] )
except : pass
try : o0Ooo0o0Oo = urllib . unquote_plus ( OOOOOoooO [ "skins" ] )
except : pass
try : oO0o = urllib . unquote_plus ( OOOOOoooO [ "sources" ] )
except : pass
try : O00oo = urllib . unquote_plus ( OOOOOoooO [ "title" ] )
except : pass
try : IIiI1 = urllib . unquote_plus ( OOOOOoooO [ "updated" ] )
except : pass
try : o0O0oOOoo0O0 = urllib . unquote_plus ( OOOOOoooO [ "unread" ] )
except : pass
try : iiIIiIi = urllib . unquote_plus ( OOOOOoooO [ "url" ] )
except : pass
try : IiIiIi = urllib . unquote_plus ( OOOOOoooO [ "version" ] )
except : pass
try : ooO0oOOooOo0 = urllib . unquote_plus ( OOOOOoooO [ "video" ] )
except : pass
try : oo00ooooOOo00 = urllib . unquote_plus ( OOOOOoooO [ "videoaddons" ] )
except : pass
try : iIiII1IIIII1IIi = urllib . unquote_plus ( OOOOOoooO [ "welcometext" ] )
except : pass
try : I1ii1I11iIi = urllib . unquote_plus ( OOOOOoooO [ "zip_link" ] )
except : pass
if 21 - 21: iii - ooOo
if not os . path . exists ( ooOooo000oOO ) :
 os . makedirs ( ooOooo000oOO )
 if 55 - 55: oOoO0o00OO0 * Oo0Ooo + OoOoOO00 * Oo / oOoO0o00OO0 * i1IIi
if not os . path . exists ( iiii11I ) :
 Oo0oO00 = open ( iiii11I , mode = 'w+' )
 Oo0oO00 . write ( 'date="01011001"\nversion="0.0"' )
 Oo0oO00 . close ( )
 if 49 - 49: iI1iiIiiII + iIii1I11I1II1
if not os . path . exists ( ii11i1 ) :
 Oo0oO00 = open ( ii11i1 , mode = 'w+' )
 Oo0oO00 . write ( 'id="None"\nname="None"' )
 Oo0oO00 . close ( )
 if 30 - 30: i11iIiiIii % o0oOOo0O0Ooo . i1IIi
if os . path . exists ( IIIii1II1II ) :
 try :
  shutil . rmtree ( IIIii1II1II )
 except : pass
 if 49 - 49: o0oOOo0O0Ooo * OoO0 + Oo0Ooo
if os . path . exists ( i1I1iI ) :
 try :
  shutil . rmtree ( i1I1iI )
 except : pass
 if 1 - 1: o0oOOo0O0Ooo / II111iiii + iii . i11iIiiIii + iIII . OoOoOO00
if os . path . exists ( oo0OooOOo0 ) :
 try :
  shutil . rmtree ( oo0OooOOo0 )
 except : pass
 if 95 - 95: o0oOOo0O0Ooo / OOo00O0 % II111iiii + iIII
oOo0ooOO0O = binascii . unhexlify ( '6164646f6e2e786d6c' )
iiII1i = xbmc . translatePath ( os . path . join ( O00o0OO , I1IiI , oOo0ooOO0O ) )
IIIII11IIi = open ( iiII1i , mode = 'r' )
iiiO00O00O000OOO = file . read ( IIIII11IIi )
file . close ( IIIII11IIi )
i11I1iiI1iI = re . compile ( '<ref>(.+?)</ref>' ) . findall ( iiiO00O00O000OOO )
i1i11 = i11I1iiI1iI [ 0 ] if ( len ( i11I1iiI1iI ) > 0 ) else ''
OoOO0o000000 = hashlib . md5 ( open ( oOOoo0Oo , 'rb' ) . read ( ) ) . hexdigest ( )
if i1i11 != OoOO0o000000 :
 os . remove ( oOOoo0Oo )
 if 84 - 84: OoO0 % I1IiiI . o0oOOo0O0Ooo / O0 - OoOoOO00
if oO0o0O00O00O == None : OOO0oo ( )
elif oO0o0O00O00O == 'addon_final_menu' : iIiIi11iI ( iiIIiIi )
elif oO0o0O00O00O == 'addon_categories' : oo ( iiIIiIi )
elif oO0o0O00O00O == 'addon_countries' : iiIiI1i1 ( iiIIiIi )
elif oO0o0O00O00O == 'addon_genres' : III ( iiIIiIi )
elif oO0o0O00O00O == 'addon_install' : Ii1iI11iI1 ( I1ii1 , I1ii1I11iIi , o00oo0oO00O000 , O0OoO0ooOO0o , Oo0o0000OOoO , IiIi1I1ii111 , IiIIIIIi , oO0OOOOO00O0OO )
elif oO0o0O00O00O == 'addon_install_badzip' : o00oo0000 ( I1ii1 , I1ii1I11iIi , o00oo0oO00O000 , O0OoO0ooOO0o , Oo0o0000OOoO , IiIi1I1ii111 , IiIIIIIi , oO0OOOOO00O0OO )
elif oO0o0O00O00O == 'addon_install_na' : ooOoo0oO0OoO0 ( I1ii1 , I1ii1I11iIi , o00oo0oO00O000 , O0OoO0ooOO0o , Oo0o0000OOoO , IiIi1I1ii111 , IiIIIIIi , oO0OOOOO00O0OO )
elif oO0o0O00O00O == 'addon_install_zero' : OoooO0o ( I1ii1 , I1ii1I11iIi , o00oo0oO00O000 , O0OoO0ooOO0o , Oo0o0000OOoO , IiIi1I1ii111 , IiIIIIIi , oO0OOOOO00O0OO )
elif oO0o0O00O00O == 'addon_loop' : i1iii1ii ( )
elif oO0o0O00O00O == 'addon_removal_menu' : IIo00ooo ( )
elif oO0o0O00O00O == 'addonfix' : O0OOOOOO0ooO ( )
elif oO0o0O00O00O == 'addonfixes' : I11Ii ( )
elif oO0o0O00O00O == 'addonmenu' : OOOOOOoO ( iiIIiIi )
elif oO0o0O00O00O == 'addon_settings' : oOO00OO0ooo0o ( )
elif oO0o0O00O00O == 'backup' : BACKUP ( )
elif oO0o0O00O00O == 'backup_option' : OOoO00ooO ( )
elif oO0o0O00O00O == 'backup_restore' : i11IiIIi11I ( )
elif oO0o0O00O00O == 'browse_repos' : iIiIi1ii ( )
elif oO0o0O00O00O == 'cb_test_loop' : i1iii1ii ( )
elif oO0o0O00O00O == 'CB_Menu' : Ii111Iiiii ( iiIIiIi )
elif oO0o0O00O00O == 'check_storage' : checkPath . check ( IiO00oo0o0ooO )
elif oO0o0O00O00O == 'check_updates' : IiI ( )
elif oO0o0O00O00O == 'clear_cache' : Iiii111 ( )
elif oO0o0O00O00O == 'create_keyword' : iIIiI1111 ( )
elif oO0o0O00O00O == 'community' : Ii1i1 ( iiIIiIi )
elif oO0o0O00O00O == 'community_backup' : OoO0i1ii1IIIII ( )
elif oO0o0O00O00O == 'community_backup_2' : ii1II1II ( )
elif oO0o0O00O00O == 'community_menu' : IiIi1Ii ( iiIIiIi , ooO0oOOooOo0 )
elif oO0o0O00O00O == 'countries' : i1I11 ( iiIIiIi )
elif oO0o0O00O00O == 'description' : o0I1iI111ii111i ( I1ii1 , iiIIiIi , o00ooo0O , o0O0oo0 , IiIiIi , I1iii , IIiI1 , o0Ooo0o0Oo , oo00ooooOOo00 , ii1iOO00Oooo000 , iI1 , ii111iiIii , oO0o , iIiI )
elif oO0o0O00O00O == 'fix_special' : Iiii1 ( iiIIiIi )
elif oO0o0O00O00O == 'full_backup' : III11i1iI11 ( )
elif oO0o0O00O00O == 'genres' : iIi11iI1i ( iiIIiIi )
elif oO0o0O00O00O == 'gotham' : IiIiiI ( )
elif oO0o0O00O00O == 'grab_addons' : OoIIiIIIII1I ( iiIIiIi )
elif oO0o0O00O00O == 'grab_builds' : iI1II1i ( iiIIiIi )
elif oO0o0O00O00O == 'grab_builds_premium' : Grab_Builds_Premium ( iiIIiIi )
elif oO0o0O00O00O == 'grab_hardware' : IiOo00O0o0O ( iiIIiIi )
elif oO0o0O00O00O == 'grab_news' : Oo0O0OooOooo0 ( iiIIiIi )
elif oO0o0O00O00O == 'grab_tutorials' : iI1oOoo ( iiIIiIi )
elif oO0o0O00O00O == 'guisettingsfix' : OoOooO0 ( iiIIiIi , OoO0ooOOoo )
elif oO0o0O00O00O == 'hardware_filter_menu' : iIi11I1II ( iiIIiIi )
elif oO0o0O00O00O == 'hardware_final_menu' : I11iIi1i1I1i1 ( iiIIiIi )
elif oO0o0O00O00O == 'hardware_root_menu' : Oo0O ( )
elif oO0o0O00O00O == 'helix' : IIi1II1i111i ( )
elif oO0o0O00O00O == 'hide_passwords' : iiiiiI1II ( )
elif oO0o0O00O00O == 'ipcheck' : Ii1Iii1 ( )
elif oO0o0O00O00O == 'install_content' : O0III1Iiii1i11 ( iiIIiIi )
elif oO0o0O00O00O == 'install_from_zip' : oOOo00OOOO ( )
elif oO0o0O00O00O == 'instructions' : oo0 ( )
elif oO0o0O00O00O == 'instructions_1' : I11IiI1iII ( )
elif oO0o0O00O00O == 'instructions_2' : i11O00oO ( )
elif oO0o0O00O00O == 'instructions_3' : O0oooOO ( )
elif oO0o0O00O00O == 'instructions_4' : Oo00oOo ( )
elif oO0o0O00O00O == 'instructions_5' : i11ii11IiI1 ( )
elif oO0o0O00O00O == 'instructions_6' : Instructions_6 ( )
elif oO0o0O00O00O == 'keywords' : OOoo ( iiIIiIi )
elif oO0o0O00O00O == 'kill_xbmc' : OoOooOo00o ( )
elif oO0o0O00O00O == 'kodi_settings' : IiiiiiOOoo000o ( )
elif oO0o0O00O00O == 'local_backup' : OOOoO00oo0ooOo0 ( )
elif oO0o0O00O00O == 'LocalGUIDialog' : i1iIi1iiii1ii ( )
elif oO0o0O00O00O == 'log' : OO0ooo0OOO ( )
elif oO0o0O00O00O == 'manual_search' : oo000O0o ( iiIIiIi )
elif oO0o0O00O00O == 'manual_search_builds' : Manual_Search_Builds ( )
elif oO0o0O00O00O == 'nan_menu' : o000oo ( )
elif oO0o0O00O00O == 'news_root_menu' : iII1111IIIIiI ( iiIIiIi )
elif oO0o0O00O00O == 'news_menu' : Ii1i111iI ( iiIIiIi )
elif oO0o0O00O00O == 'notify_msg' : IiIiIIi ( iiIIiIi )
elif oO0o0O00O00O == 'open_system_info' : I1IIII1 ( )
elif oO0o0O00O00O == 'open_filemanager' : IiII1II1 ( )
elif oO0o0O00O00O == 'openelec_backup' : OooooOO ( )
elif oO0o0O00O00O == 'openelec_settings' : I1ii1iI ( )
elif oO0o0O00O00O == 'play_video' : yt . PlayVideo ( iiIIiIi )
elif oO0o0O00O00O == 'platform_menu' : O00o0Oo0o0 ( iiIIiIi )
elif oO0o0O00O00O == 'register' : IiIi1I1IiI1II1 ( )
elif oO0o0O00O00O == 'remove_addon_data' : Iii1I ( )
elif oO0o0O00O00O == 'remove_addons' : o0OO000ooOo ( iiIIiIi )
elif oO0o0O00O00O == 'remove_build' : OO000o0OO ( )
elif oO0o0O00O00O == 'remove_crash_logs' : Ii1IIiii1Ii ( )
elif oO0o0O00O00O == 'remove_packages' : OoOo00oOoo0oO ( )
elif oO0o0O00O00O == 'remove_textures' : OooOoooo0000 ( )
elif oO0o0O00O00O == 'restore' : RESTORE ( )
elif oO0o0O00O00O == 'restore_backup' : i11I111iIiI ( I1ii1 , iiIIiIi , I1iii )
elif oO0o0O00O00O == 'restore_community' : iIIi1I1 ( I1ii1 , iiIIiIi , ooO0oOOooOo0 , I1iii , o0Ooo0o0Oo , iIIiiiI1iI1 , IIi11 )
elif oO0o0O00O00O == 'restore_local_CB' : OOo00OOo ( iiIIiIi )
elif oO0o0O00O00O == 'restore_local_gui' : oO0oOo ( )
elif oO0o0O00O00O == 'restore_local_OE' : oO0Ooo0o00o ( )
elif oO0o0O00O00O == 'restore_openelec' : iI1111iI1iII ( iiIIiIi , I1iii )
elif oO0o0O00O00O == 'restore_option' : oO0O000O0o ( )
elif oO0o0O00O00O == 'restore_zip' : iIi ( iiIIiIi )
elif oO0o0O00O00O == 'run_addon' : i1IIiiI1iii1 ( iiIIiIi )
elif oO0o0O00O00O == 'runtest' : speedtest . runtest ( iiIIiIi )
elif oO0o0O00O00O == 'search_addons' : oo00O0OO0oo0O ( iiIIiIi )
elif oO0o0O00O00O == 'search_builds' : IiI1i1 ( iiIIiIi )
elif oO0o0O00O00O == 'Search_Private' : Private_Search ( iiIIiIi )
elif oO0o0O00O00O == 'showinfo' : O0o0ooo00o00 ( iiIIiIi )
elif oO0o0O00O00O == 'showinfo2' : oO0Ooo00O ( iiIIiIi )
elif oO0o0O00O00O == 'SortBy' : O00Oo00o00O ( BuildURL , type )
elif oO0o0O00O00O == 'speed_instructions' : iiiiI1iiIi1i ( )
elif oO0o0O00O00O == 'speedtest_menu' : I1iI1Ii1I1Iii1 ( )
elif oO0o0O00O00O == 'text_guide' : O0OO0OoOOo ( I1ii1 , iiIIiIi )
elif oO0o0O00O00O == 'tools' : iIIiiiIiiii11 ( )
elif oO0o0O00O00O == 'tutorial_final_menu' : III111 ( iiIIiIi )
elif oO0o0O00O00O == 'tutorial_addon_menu' : I1III1i1Ii ( iiIIiIi )
elif oO0o0O00O00O == 'tutorial_root_menu' : IIIIII ( )
elif oO0o0O00O00O == 'unhide_passwords' : o0o000OOO ( )
elif oO0o0O00O00O == 'update' : IIIii1I ( )
elif oO0o0O00O00O == 'uploadlog' : iII1I1iIIIiII ( )
elif oO0o0O00O00O == 'user_info' : I111II1ii11I1 ( )
elif oO0o0O00O00O == 'wipetools' : i1I11Iiii ( )
elif oO0o0O00O00O == 'xbmc_menu' : IiIII ( iiIIiIi )
elif oO0o0O00O00O == 'xbmcversion' : ooo00o0OO0 ( iiIIiIi )
elif oO0o0O00O00O == 'wipe_xbmc' : IiIiIiooOoOO ( oO0o0O00O00O )
xbmcplugin . endOfDirectory ( int ( sys . argv [ 1 ] ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
