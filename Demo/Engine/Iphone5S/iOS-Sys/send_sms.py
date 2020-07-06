# -*- coding: utf-8 -*-
"""
Open the texting view, write a short message 
with 26-key keyboard and input phone number 
with 9-key keyboard, click icons to send the short message
"""
from rcs import Rcs

te = Rcs()

#Open the texting view
te.click('message.png')

#Write a short message
te.click('write.png')

#Change the 26-key keyboard to 9-key keyboard
te.press_keyboard('Iphone26key', '[123]')

#Input Phone Number
te.press_keyboard('Iphone9key', '13236569169')

#Input short message
te.click('message_input.png')
te.press_keyboard('Iphone26key', 'test[Return]')

#Click icon to send shortmessage
te.click('send.png')

te.reset_arms()

te.assert_exist('send_message.png')