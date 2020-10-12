#wabafet simple pia rotation
import subprocess
import os
import sys
import schedule
import time
import random
import datetime
import sched, time
import simpleaudio as sa
import glob
from subprocess import Popen, PIPE

'''
Windows
Run the following command to install the simpleaudio module:
pip install simpleaudio
Linux
For Linux users, you have to install additional dependencies apart from the command above. For Debian variants, you can do so with the following commands. We will first install the python3 development package:
sudo apt-get install python3-dev
Then, we get the ALSA development package:
sudo apt-get install libasound2-dev

sudo apt-get install secure-delete _>only if u want to perform self destruct u need to be root or use insecure no_passwd for sudo

or do not expect  to efficiently wipe anything
'''
failed_connections = 0
sudo_pass = ""#prompt for user input of sudo passwd while script is run incase root is needed to wipe it
extracted_partitions = []
#i am not auto enabling self destruct u enable that peril is all yours dont cry later
imminent_danger_message = "Connection Not SuccessFul 3 retries Before self destruct sequence initiated"
windows_location = "\"C:\\Program Files\\Private Internet Access\\piactl.exe\""
success_message = "Connection  Initiated to {} Rotation Complete"
is_self_destructible = False #if this is set to tRue and you break your pc not my problem run on a burner vm
total_file_list = []
if is_self_destructible:
    pass_cal = input("Enter your sudo pass to securely wipe stuff hey u enabled it: ")
    sudo_pass += pass_cal

#secure file wipe will not be added for windows on alpha as if your using that i cant help u too many things to narc on u
#no matter what this takes awhile to secure wipe so if your doing something that requires better maybe u shouldn't be doing it



#use following lines to set global platform type so we can do a few lines in each function to determine paths
platform_type = ""
if "windows" in sys.platform:
   speaker = win32com.client.Dispatch("SAPI.SpVoice")
   import win32com.client as wincl
   import win32com.client
   from playsound import playsound
   #call windows logic
   platform_type += "windows"

if "linux" in sys.platform:
    platform_type += "linux"


s = sched.scheduler(time.time, time.sleep)

desired_regions = [ "singapore",
"armenia",
"austria",
"andorra",
"saudi-arabia",
"nigeria",
"romania",
"sweeden",
"qatar",
"estonia",
"cambodia"]

get_regions = "get regions"
#https://www.privateinternetaccess.com/helpdesk/kb/articles/pia-desktop-command-line-interface
#https://medium.com/better-programming/how-to-play-audio-files-in-python-3a430b6b2657

def play_danger():
    #file is the audio stored in the modernsubdive.wav in same dir from dod samples website compare if u like
    wave_obj = sa.WaveObject.from_wave_file("modernsubdive.wav")
    play_obj = wave_obj.play()
    # play_obj.wait_done() #blocking call
    while True:
        if (play_obj.is_playing()):
            print('Playing Danger Alert')
        else:
            print('Ended Danger Alert')
            break



def sudo_command(command_in):
    sudo_password = sudo_pass
    command = command_in.split()
    print(command)
    p = Popen(['sudo', '-S'] + command, stdin=PIPE, stderr=PIPE,universal_newlines=True)
    sudo_prompt = p.communicate(sudo_password + '\n')[1]


def wipe_free(partition):
    cmd = "sfill -v {}".format(partition)
    try:
        sudo_command(command_in)
    except Exception as ex2:
        print(ex2)
        pass


def wipe_files_secure(path):
    cmd = "srm  -v  -r {}".format(path)
    try:
        print("Securely Deleting File {}".format(path))
        print(cmd)
        sudo_command(cmd)

        '''
        for partition in set(extracted_partitions):
            print("erasing free space on partition {}".format(partition))
            wipe_free(partition)
        '''

    except Exception as ex2:
        print(ex2)
        pass



def linux_destruct_squence():
    cmd = "cat /proc/partitions"
    sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    output = ""
    while True:
        out = sp.stdout.read(1).decode('utf-8')
        if out == '' and sp.poll() != None:
            break
        if out != '':
            output += out
            sys.stdout.write(out)
            sys.stdout.flush()

    if output:
        return output



def Self_Destruct():
    try:
        cmd = ""

        if "windows" in platform_type:
            windows_wiper()#beta release ill look into it but get off windows hacking or whistleblowing

        if "linux" in platform_type:
            # in linux piactl is symlinked to /usr/local/bin
            if is_self_destructible:
               partitions = linux_destruct_squence()
               lines = partitions.splitlines()
               for line in lines:
                   if line:
                       name = line.split()
                       extracted_name = name[3]
                       if "name" in extracted_name:
                           pass

                       else:
                           extracted_partitions.append(extracted_name)
            if extracted_partitions:
                print("Enumerated Partitions about to wipe Your stuff obv if this is enabled you cant recover ever")
                try:


                    try:
                        folder = '/'
                        filepaths = [os.path.join(folder, f) for f in os.listdir(folder)]
                        if filepaths:
                           print(filepaths)
                           for paths in filepaths:
                               if paths:
                                  if "/home"  in paths:
                                     files_found = fileList(paths)
                                     if files_found:
                                         print(files_found)
                                  if "/tmp" in paths:
                                      #if u go wiping certain shit in linux it will break so be safe
                                      #keep files in home dir and tmp dont leave lingering files if u want to be safe
                                      #the drives supposed to be encrytped after this smash with hammer lol
                                      #yes this will break downloads just having fun
                                      wipe_files_secure('/home/devcoinfet/Downloads/')
                                      '''
                                      wipe_files_secure('/home/devcoinfet/Downloads')
                                      Self_Destruct()
                                      files_found = fileList(paths)
                                      if files_found:
                                          print(files_found)
                                      '''

                    except Exception as filex:
                        print(filex)
                        pass

                except Exception as ex:
                    print(ex)


    except Exception as err:
        print(err)
        pass



def fileList(source):
    matches = []
    for root, dirnames, filenames in os.walk('/home/devcoinfet/Downloads'):
        for filename in filenames:
            if filename:#.endswith(('.txt', '.pdf', '.doc', '.wav')):
                matches.append(os.path.join(root, filename))
    wipe_files_secure('/home/devcoinfet/Downloads')
    return matches


def get_region_data():
    try:
        cmd = ""

        if "windows" in platform_type:
            cmd += windows_location + " get regions"

        if "linux" in platform_type:
            # in linux piactl is symlinked to /usr/local/bin
            cmd += "piactl get regions"

        sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
       
        output = ""
        while True:
            out = sp.stdout.read(1).decode('utf-8')
            if out == '' and sp.poll() != None:
               break
            if out != '':
               output += out
               sys.stdout.write(out)
               sys.stdout.flush()

        if output:
          return list(set(output.split()))

    except Exception as err:
        print(err)
        pass



def job():
   #code in logic to play message correctly based on system type
   print("Vpn Ip Rotation")
   #check for win linux here to pass paths correctly
   schedule_next_run()
   is_connected = get_connected_state()
   print(is_connected)
   system_type = sys.platform
   if "Connected" in str(is_connected):
      region_data = get_region_data()
      for region in region_data:
          print("Vpn Region :"+str(region)+" Discovered")
      rand_location = random.choice(desired_regions)
      locale_result = set_rotation_locale(rand_location)
      print(locale_result)


      #if "Connected" in str(is_connected):
      if "windows" in str(system_type):
         speaker.Speak(success_message.format(rand_location))

      if "linux" in str(system_type):
         linux_speak(success_message.format(rand_location))

   if "Reconnecting" in str(is_connected):
       #try to reconnect 7 times here on delay of 1 minute if that doesnt work self destruct
       #internet can go out if your paranoid set to 1,3 minutes hops so it only takes 20 minutes or so max
       #internet drops maintenance gets done so this should be good buffer
       if "windows" in str(system_type):
           speaker.Speak(imminent_danger_message)
           play_danger()
           failed_connections += 1

       if "linux" in str(system_type):
           linux_speak(imminent_danger_message)
           play_danger()
           failed_connections += 1


       if failed_connections  == 7:
          # wipe device if connection is not maintained after 7 tries
          print("self destruct initiated")
          Self_Destruct()




   return schedule.CancelJob


def linux_speak(message):
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(str(message))
    engine.runAndWait()




def schedule_next_run():
   #random times based on a time range provided so any run 1- 7 minutes is chosen randomly
   time_span = random.randint(1, 7)
   schedule.clear()
   print(f'Scheduled in {time_span} minutes')
   schedule.every(time_span).minutes.do(job)


def set_rotation_locale(region):
    try:
        cmd = ""
        
        if "windows" in platform_type:
            cmd += windows_location + "set region "+str(region)

        if "linux" in platform_type:
            # in linux piactl is symlinked to /usr/local/bin
            cmd += "piactl set region "+str(region)
       
        sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
      
        output = ""
        while True:
            out = sp.stdout.read(1).decode('utf-8')
            if out == '' and sp.poll() != None:
               break
            if out != '':
               output += out
               sys.stdout.write(out)
               sys.stdout.flush()
        if output:
           return output
          
    except Exception as err:
        print(err)
        return output


def get_connected_state():
    try:
       cmd = ""
       if "windows" in platform_type:
          cmd += windows_location+ " get connectionstate"

       if "linux" in platform_type:
           #in linux piactl is symlinked to /usr/local/bin
           cmd += "piactl get connectionstate"
       sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
       
       output = ""
       while True:
          out = sp.stdout.read(1).decode('utf-8')
          if out == '' and sp.poll() != None:
              break
          if out != '':
             output += out
             sys.stdout.write(out)
             sys.stdout.flush()
       if output:
          return output
    except Exception as err:
        print(err)
        pass

def main():
    '''
    schedule_next_run()
    while True:
        schedule.run_pending()
    '''
    Self_Destruct()

if __name__ == "__main__":
    main()

