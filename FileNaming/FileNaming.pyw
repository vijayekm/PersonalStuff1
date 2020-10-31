

from datetime import datetime
import logging
import sys

from Gui import FileNamingDlg

import wx
import wx.xrc

ID_NEXT     = 1
ID_PREV     = 2
ID_FORMAT   = 3
ID_DUP      = 4
ID_SAVE     = 5
ID_OPEN     = 6
ID_CLEAN   = 7
ID_FORMAT_NUM  = 8

format = "%(asctime)s: %(message)s"
LOG_FILENAME = sys.argv[0] + datetime.now().strftime('_%H_%M_%S_%d_%m_%Y.log')
#logging.basicConfig(filename=LOG_FILENAME,format=format, level=logging.INFO, datefmt="%H:%M:%S")

logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")


class FileNaming(FileNamingDlg):

    def __init__(self,input):
        super(FileNaming,self).__init__(input)
        self.SetupAccelerators()

    def SetupAccelerators(self):

        acc_list = [
        ( wx.ACCEL_CTRL, ord('n'), ID_NEXT ),
        ( wx.ACCEL_CTRL, ord('p'), ID_PREV ),
        ( wx.ACCEL_CTRL, ord('f'), ID_FORMAT),
        ( wx.ACCEL_CTRL, ord('d'), ID_DUP),
        ( wx.ACCEL_CTRL, ord('s'), ID_SAVE),
        ( wx.ACCEL_CTRL, ord('o'), ID_OPEN),
        ( wx.ACCEL_CTRL, ord('l'), ID_CLEAN),
        ( wx.ACCEL_CTRL, ord('i'), ID_FORMAT_NUM)
        ]

        acc_table = wx.AcceleratorTable( acc_list )
        self.SetAcceleratorTable(acc_table)

        self.Bind(wx.EVT_MENU, self.evt_next, id=ID_NEXT)
        self.Bind(wx.EVT_MENU, self.evt_prev, id=ID_PREV)
        self.Bind(wx.EVT_MENU, self.evt_format, id=ID_FORMAT)
        self.Bind(wx.EVT_MENU, self.evt_dup, id=ID_DUP)
        self.Bind(wx.EVT_MENU, self.evt_save, id=ID_SAVE)
        self.Bind(wx.EVT_MENU, self.evt_open, id=ID_OPEN)
        self.Bind(wx.EVT_MENU, self.evt_delete, id=ID_CLEAN)
        self.Bind(wx.EVT_MENU, self.evt_format_num, id=ID_FORMAT_NUM)

    def evt_next(self,id):
        logging.debug("need to go next ")
        pass

    def evt_prev(self,id):
        logging.debug("need to go prev")
        pass

    def evt_format(self,id):
        logging.debug("need to format ")
        pass

    def evt_dup(self,id):
        logging.debug("need to duplicate ")
        pass

    def evt_save(self,id):
        logging.debug("need to save ")
        pass

    def evt_open(self,id):
        logging.debug("need to open ")
        pass

    def evt_delete(self,id):
        logging.debug("need to delete ")
        pass

    def evt_format_num(self,id):
        logging.debug("need to format num ")
        pass

    def m_btnOpenDirOnButtonClick( self, event ):
    	logging.debug("Open dir button clicked")

    def m_btnCollectFilesOnButtonClick( self, event ):
        logging.debug("Collect files button clicked")

def guiMain():

    app = wx.App()

    dialog = FileNaming(None)
    dialog.ShowModal()

    return

guiMain()