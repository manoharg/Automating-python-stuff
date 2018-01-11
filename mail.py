#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 11:00:29 2017

@author: manohar
"""

import smtplib
#import socks
#socks.setdefaultproxy(socks.SOCKS5, '172.31.103.29', 3128)
#socks.wrapmodule(smtplib)
m=smtplib.SMTP('smtp.gmail.com',587)
m.ehlo()
m.starttls()
m.login('golamanohar.gm@gmail.com','9701874183')
m.sendmail('golamanohar.gm@gmail.com','golamanohar.gm@gmail.com','Subject:helo\n.Nothinnnnng')
m.quit()

