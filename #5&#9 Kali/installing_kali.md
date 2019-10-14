# My Acquaintance to Kali

TO BEGIN WITH,from the Internet, I learnt that *Kali* is used to do some magical test. what surprise me is THERE IS SO MANY VERSIONS OF *LINUX*!!!



## Failed to Mount cd-rom

I spend efforts to use *Win32DiskImager*, *UltraIso*, *UniversalUSBInstaller*  to write the *kali.iso* into my USB drive. But at last, my efforts were all paid in vain. My computer can't mount the cd-rom. I tried many method, such as using the shell with `umount /media`(as it is said wrongly mount to media) . BUT absolutely, I failed.



##  I found the VMware

IT IS 22 O'CLOCK NOW, I finally decide to give up installing double system. I turn to install *VMware*. 

During installing *Kali* in *VMware*, I mistook RAM as ROM, so I spent a great efforts to figure out why I keep getting into low memory model...



## HELLO, KALI!

FINALLY, AT 00:40, I successfully installed *Kali*. 

Now I am going to learn how to use it!



## FIRST TIME

It is a new day now, after coming back to the flat, I couldn't wait to turn on my laptop and start my *Kali*. On the blog of *JoTang*, it is said the new *Kali* should not run `apt-get update` successfully. HOWEVER, I don't know why, my *Kali* seems run it without difficult(except for I need to get the root permission, and I make it with *Baidu* no longer than a second)



## OH MY GOD ##

I find that I have to make a *Kali* in my USB drive! 

I have to deal with the *KALI LINUX USB LIVE PERSISTENCE* ......



## HE WHO TAKES CHALLENGES ALWAYS WINS ##

~~(not always)~~

WELL WELL WELL, I'll take the challenge.

I began under the guide of a course on *CSDN*(where now I think is no better than *Baidu*). I used the *MiniTool* and the *Win32DiskImager*.  Firstly I run the *MiniTool* to create new partition. However, problems show up much 'beyond my expectation', I found the Drive Letter and the Partition Label isn't what I just set. (I should have notice the application isn't stable!!!) I  and revised them, not taking the problem seriously.

I began with the course step by step, all seems to be correct.

However, things didn't go well for long... I amazingly found that in *Kali* my USB drive have only one partition which is different from what the course says. I tried to create partitions in the USB drive with *Kali*, but immediately I found that creating partitions will delete all data in my USB drive where the *Kali* itself is in.

I thought the problem may be caused by not totally delete the data in the USB drive by fill it with 0. So,I restart the stuff,and waited for tens of minuets until the deletion is done. And I did what I've done half an hour ago, of course, with the problem that I have to set the Drive Letter and the Partition Label twice.

NO WONDER, THE PROBLEM CAME AGAIN!

AND AGAIN, AND AGAIN!!!! I TRIED MORE THAN THERE TIMES!! AND IT TOOK MY WHOLE AFTERNOON TIME AND LEFTED ME NO TIME TO HAVE A NAP!

I had to try to create new partition in *Kali* and without doubt, I failed and my Kali was gone, and I have to write it into my USB drive again and again.

Finally, I gave up doing this with *MiniTool*, and I decide to create new partition with the tool provided by Windows 10. (and marked down the experience of the afternoon on the C class after dinner)

I am sure I will keep going!

## FINALLY I SUCCEEDED!!! ##

THE ONLY THING I WANT TO SAY IS, TO LEARN SOME TACHNICAL THINGS, *GOOGLE* IS THE BEST, *YOUTUBE* IS THE BEST!!!

I tried to use the partition creater from win10, but it doesn't make sense either.

SO, I SERCH COURSE IN *GOOGLE*, AND I FOUND A  VIDEO IN *YOUTUBE*, FROM A GUY WITH RUSSIA ACCENT BUT EXCELLENT AWESOME TECHNIQUE!!!!!!

WITH A SERIES OF OPERATION, AND I CREATED A FOLDER, AND REBOOT, ANNNND, IT IS STILL THERE, WHICH MEANS I HAVE SUCCESSFULLY INSTALL THE *KALI LINUX USB LIVE PERSISTENCE* !!!!!!!

## Using Kali To Get The WIFI Passwords ##

A new day came, I couldn't wait to login my Kali and try to get others' WIFI passwords. Firstly, I used my own phone *hotspot* to do some tests. This time I got my course from *YOUTUBE*, because I didn't want to get tricked by *Baidu* for another time. Surprisingly, with my roommate, the victim, yelling 'OMG I am disconnected', I successfully got my WIFI passwords '87654321'. But it is still obsessing me that why my roommate disconnected the WIFI when I was catching the *Handshake*.

Then, without doubt, I want to try my new technique on other's WIFI. But I found that  it was difficult for me to catch the *Handshake*, maybe it was because the user is not that active due to the late night. I finally get a *Handshake*, and downloaded a dictionary suitable for Chinese WIFI. And I found that even though the system didn't tell you had successfully get the pack with passwords(it is said it should tell you when you successfully get the *Handshake*), you can check if you are successful by check out the size of the file. 

But, after waiting for tens of minuets, the passwords didn't show up like what happened when I did the test on my own hotspot. THE KEY ISN'T FOUND. Obviously, their passwords are stable...

WELL, it seems that I need to learn another way to get their passwords.







<!--ok, see you at next markdown: hello_kali-->