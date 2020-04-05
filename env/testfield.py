import maya.cmds as cmds

#    Create a window with a some fields for entering text.
#
window = cmds.window()
cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 0), columnWidth=[(1, 100), (2, 250)] )
cmds.text( label='Name' )
name = cmds.textField()
cmds.text( label='Address' )
address = cmds.textField()
cmds.text( label='Phone Number' )
phoneNumber = cmds.textField()
cmds.text( label='Email' )
email = cmds.textField()

#    Attach commands to pass focus to the next field if the Enter
#    key is pressed. Hitting just the Return key will keep focus
#    in the current field.
#
cmds.textField( name, edit=True, enterCommand=('cmds.setFocus(\"' + address + '\")') )
cmds.textField( address, edit=True, enterCommand=('cmds.setFocus(\"' + phoneNumber + '\")') )
cmds.textField( phoneNumber, edit=True, enterCommand=('cmds.setFocus(\"' + email + '\")') )
cmds.textField( email, edit=True, enterCommand=('cmds.setFocus(\"' + name + '\")') )

cmds.showWindow( window )
