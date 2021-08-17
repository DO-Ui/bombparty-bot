CoordMode, Mouse, Screen
a := 0
b := 0
#SingleInstance force
~*F6::
MouseGetPos, a, b
msgbox, %a%, %b%
return
~`::
exitapp
return