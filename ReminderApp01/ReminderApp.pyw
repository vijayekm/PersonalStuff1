import wx
import time
import threading
from datetime import datetime
import logging
import sys
import ReminderAppGui

format = "%(asctime)s: %(message)s"
LOG_FILENAME = sys.argv[0] + datetime.now().strftime('_%H_%M_%S_%d_%m_%Y.log')
logging.basicConfig(filename=LOG_FILENAME,format=format, level=logging.INFO, datefmt="%H:%M:%S")

if len (sys.argv) !=2 :
    logging.error("Input file not provided as arg")
    exit();

IN_FILE = sys.argv[1]

today = datetime.today()

year= today.year
month=today.month
day=today.day
shuttingDown = False

app = None
window = None

import pyttsx3

stop_voice = False
vt_running = False
vt = None

voice_message =None

def voice_thread_main(name):
    global engine, vt_running, stop_voice

    engine = pyttsx3.init()

    logging.info("Thread %s: starting", name)

    while stop_voice == False :
        if voice_message is not None:
            msg = voice_message
            logging.debug("Saying %s", msg)
            engine.say(msg)
            logging.debug("Going to wait %s", msg)
            engine.runAndWait()
            time.sleep(1)
        logging.debug("Going to sleep in %s",name )
        time.sleep(1)

    stop_voice = False
    vt_running = False

    logging.info("Thread %s: finishing", name)


def start_voice_thread():

    global vt, stop_voice, vt_running

    stop_voice = False
    vt_running = True

    logging.info("Main    : before creating thread")
    vt = threading.Thread(target=voice_thread_main, args=("VT",))
    logging.info("Main    : before running thread")
    vt.start()
    logging.info("Main    : wait for the thread to finish")


class OneReminder:
    def __init__(self, p_at, msg):

        self.at = p_at
        hour,min = p_at.split(":")

        self.time = datetime(year,month,day,int(hour),int(min) );
        self.msg = msg

def GetReminderKey(rem):
    return rem.at

class ReminderManager():
    reminders = []

    def __init__(self):
        pass

    @staticmethod
    def addReminder(str):
        ar = str.split(" ",1)
        logging.info( "time = {0} msg = {1}".format(ar[0],ar[1]) )
        ReminderManager.reminders.append( OneReminder(ar[0],ar[1]) )

    @staticmethod
    def prepareData():
        ReminderManager.reminders.sort( key=GetReminderKey )

    @staticmethod
    def GetNextSleepableReminder():
        #return 4,OneReminder("11:21","Test Message");

        ReminderManager.prepareData();

        now = datetime.now()

        for x in ReminderManager.reminders:
            if x.time > now:
                wait_time = x.time - now
                return wait_time.seconds, x

        return None, None


def FillGui():
    i=0;
    for rem in ReminderManager.reminders:
        window.m_remindersGrid.SetCellValue(i,0,rem.at )
        window.m_remindersGrid.SetCellValue(i,1,rem.msg )
        i+=1;


def LoadData():

    logging.info("Loading Data...")

    with open(IN_FILE) as file:
        for str in file:
            str=str.strip()
            if len(str) >0:
                ReminderManager.addReminder(str);

        ReminderManager.prepareData()

def guiMain():

    global app, window

    app = wx.App()
    window = ReminderAppGui.ReminderAppFrame(None)
    window.SetIcon(wx.Icon("circle.png"))
    window.Show(True)

    app.MainLoop()

    return 1


def processReminders():
    global shuttingDown, stop_voice, voice_message

    while shuttingDown == False:
        sec,reminder = ReminderManager.GetNextSleepableReminder()

        if sec is not None and reminder is not None:
            logging.info("Sleeping for "+str(sec) )
            time.sleep(sec)

            dialog = wx.MessageDialog(None, "Time for "+reminder.msg,"Reminder", wx.OK)

            voice_message = reminder.msg
            dialog.ShowModal()
            dialog.Destroy()
            voice_message = None
        else:
            logging.debug("Sleeping for next iter")
            time.sleep(10)

def daemonMain() :
    LoadData();

    while window is None:
        time.sleep(1)

    FillGui();
    processReminders()


def main():

    global window, shuttingDown

    start_voice_thread()

    x = threading.Thread(target=daemonMain)
    x.start()

    guiMain()

    shuttingDown = True


main()