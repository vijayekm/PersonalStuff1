

from datetime import datetime
import logging
import sys
import os

from Gui import FileNamingDlg

import wx
import wx.xrc

ID_NEXT	 = 1
ID_PREV	 = 2
ID_FORMAT   = 3
ID_DUP	  = 4
ID_SAVE	 = 5
ID_OPEN	 = 6
ID_CLEAN   = 7
ID_FORMAT_NUM  = 8

DEFAULT_DIR = "C:\\COL\\"

format = "%(asctime)s: %(message)s"
LOG_FILENAME = sys.argv[0] + datetime.now().strftime('_%H_%M_%S_%d_%m_%Y.log')
#logging.basicConfig(filename=LOG_FILENAME,format=format, level=logging.INFO, datefmt="%H:%M:%S")

logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")

def CollectFileNames(p_strDirName):
	ret = []
	str = ""
	logging.debug("Processing Dir : %s",p_strDirName)

	for subdir, dirs, files in os.walk(p_strDirName):
		for filename in files:
			if filename == '.' or filename == '..' :
				continue

			fullFileName = subdir + os.sep + filename

			logging.debug("Processing File : %s",fullFileName)

			if os.path.isdir(fullFileName):
				ret.append( CollectFileNames(fullFileName) )
			else:
				ret.append(fullFileName)

	return ret


class FileNaming(FileNamingDlg):

	def __init__(self,input):
		super(FileNaming,self).__init__(input)
		self.ModFont()

		self.SetupAccelerators()

		self.m_theDir = DEFAULT_DIR
		self.txtDirCtrl.SetValue(self.m_theDir)
		self.treeDirCtrl.SetPath(self.m_theDir)
		self.treeDirCtrl.ExpandPath(self.m_theDir)

	def resetFileSetProcessing(self):
		self.ParentDirName =""
		self.FileList = []
		self.CurrentFileIndex = -1

		self.CleanControls()

	def CleanControls(self):
		if self.txtFileNameCtrl:
			self.txtFileNameCtrl.SetValue("")

		if self.txtNumCtrl:
			self.txtNumCtrl.SetValue("")

		if self.txtNamePartCtrl:
			self.txtNamePartCtrl.SetValue("")

		if self.txtEditionCtrl :
			self.txtEditionCtrl.SetValue("")

		if self.txtDateCtrl:
			self.txtDateCtrl.SetValue("")

		if self.lblExt:
			self.lblExt.SetLabel("")

		if self.lblNewFileName :
			self.lblNewFileName.SetValue("")

	def UpdateControls(self):
		self.CleanControls()
		filePath = self.FileList[self.CurrentFileIndex]

		logging.debug("now at : %s",filePath)

		self.treeDirCtrl.SetPath( filePath )

		fileName = os.path.basename(filePath)
		fn,ext = os.path.splitext(fileName)

		self.txtFileNameCtrl.SetValue(fn)
		self.lblExt.SetLabel(ext)

##		HandleTextModification()
##		DuplicateName()


	def ModFont(self):
		logging.debug("Mod font...")

		font = self.GetFont()
		size = font.GetPointSize()
		size = size*2
		font.SetPointSize(size)
		self.SetFont(font)

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

		if self.CurrentFileIndex +1 < len(self.FileList):
			self.CurrentFileIndex +=1
			self.UpdateControls()

	def evt_prev(self,id):
		logging.debug("need to go prev")

		if self.CurrentFileIndex > 0 :
			self.CurrentFileIndex -=1
			self.UpdateControls()

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

		dia = wx.DirDialog(self, "Choose a directory", self.txtDirCtrl.GetValue() )

		if  wx.ID_OK == dia.ShowModal() :
			self.txtDirCtrl.SetValue(dia.GetPath() )

	def m_btnCollectFilesOnButtonClick( self, event ):
		logging.debug("Collect files button clicked")

		self.treeDirCtrl.CollapseTree()
		self.treeDirCtrl.SetPath(self.txtDirCtrl.GetValue())
		self.treeDirCtrl.ExpandPath(self.txtDirCtrl.GetValue())

		self.resetFileSetProcessing()
		self.ParentDirName = self.txtDirCtrl.GetValue()

		self.FileList = CollectFileNames(self.txtDirCtrl.GetValue())
		self.FileList.sort()

		#          Wx::MessageDialog.new(self, str).show_modal()
		#Wx::MessageDialog.new(self, @FileList.to_s).show_modal()
		self.CurrentFileIndex =0
		self.UpdateControls()


	def FileNamingDlgOnInitDialog( self, event ):
		logging.debug("init dialog...")

def guiMain():

	app = wx.App()

	dialog = FileNaming(None)
	dialog.ShowModal()

	return

guiMain()