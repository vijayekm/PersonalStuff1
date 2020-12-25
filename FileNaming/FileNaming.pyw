

from datetime import datetime
import logging
import sys
import os
import shutil
import re
import time

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
ID_DOTIFY = 9
ID_SPACIFY = 10
ID_DO_ALL=11

DEFAULT_DIR = "C:\\COL\\"


TEMP_DIR_EXT="tmp_1"
TEMP_DIR=TEMP_DIR_EXT

ELIM_CONF_FILE="strelem.conf"
g_elem_lines = []

#format = "%(asctime)s: %(message)s"
format = "%(asctime)s:[%(filename)s:%(lineno)s-%(funcName)15s()] %(message)s"
LOG_FILENAME = sys.argv[0] + datetime.now().strftime('_%H_%M_%S_%d_%m_%Y.log')
#logging.basicConfig(filename=LOG_FILENAME,format=format, level=logging.INFO, datefmt="%H:%M:%S")

logging.basicConfig(format=format, level=logging.DEBUG, datefmt="%H:%M:%S")




class FNException(Exception):
	def __init__(self,msg):
		self.msg = msg

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

		self.ParentDirName =""
		self.FileList = []
		self.CurrentFileIndex = -1


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

	def HandleTextModification(self,ctrl=None):
		num = self.txtNumCtrl.GetValue()
		edition = self.txtEditionCtrl.GetValue()
		dt=self.txtDateCtrl.GetValue()

		newName = ""

		newName+= num+"-" if len(num) > 0 else ""
		newName+= self.txtNamePartCtrl.GetValue()

		newName+= "-Edition-"+edition if len(edition) > 0 else ""
		newName+= "-"+dt if len(dt) > 0 else ""

		newName+= self.lblExt.GetLabel()

		logging.debug("Modified file name = %s",newName)

		self.lblNewFileName.SetValue(newName)


	def DuplicateName(self):
		if self.txtFileNameCtrl.GetValue()==None or len(self.txtFileNameCtrl.GetValue() ) == 0 :
			return

		fileName = self.txtFileNameCtrl.GetValue()

		fn,ext = os.path.splitext(fileName)

		logging.debug("fileNamewithoutExt = %s | ext = %s",fn, ext)
		self.txtNamePartCtrl.SetValue(fn)

	def ExtractDetailsFromFileName(self,fn):
		"""
		TODO
		The expected format is number-name-edition-enum-date
		The date could be
			1) having year-month-dayOfMonth
			2) having only year-month
			3) having only year
		logic for extractaion
			1) first check if the edition details are there and if yes extract
			2) initial set of digits constitute the number, extract them
			3) last set of digits is the date = year-mm-dayOfMonth
				3.1 first check for full date format
				3.2 next check for only year and month
				3.3 next check for only year
				3.4 the postion of the string should be after the edition details
		"""

		#set to defaults
		num=None
		name=fn
		edition=None
		dt=None


		"""
		For now only extract the num and year
		[ -][0-9]{4}$ is the regex for year
		^[0-9]+ is the regex for num
		"""
		NUM_PAT = "^(?P<num>[0-9]+)"
		YEAR_PRE_PAT="[ -.]"
		YEAR_PAT= YEAR_PRE_PAT+"(?P<yr>[0-9]{4})$"

		#check and extract number part
		num_match = re.search(NUM_PAT,fn)
		if num_match:
			#found the number part
			num = num_match.group("num")
			fn = re.sub(NUM_PAT,"",fn)
			logging.debug("After extraction of number = %s name %s", num,fn)

		#check and extract year part
		yr_match = re.search(YEAR_PAT,fn)
		if yr_match:
			#found the year part
			yr = yr_match.group("yr")
			fn = re.sub(YEAR_PAT,"",fn)
			dt = yr
			logging.debug("After extraction of date = %s name %s", dt,fn)

		name = fn
		"""
		After num extraction the name can possibly have the [. -_] as prefix.
		For now remove the "-"
		TODO handle the other chars also
		"""
		if name[0] == '-':
			name = name[1:]

		return num,name,edition,dt

	def ExtractDetailsFromFileNameAndUpdate(self,fn=None):

		if not fn :
			fn = self.txtNamePartCtrl.GetValue()

		num,name,edition,dt = self.ExtractDetailsFromFileName(fn)

		if name:
			self.txtNamePartCtrl.SetValue(name)
		if num :
			self.txtNumCtrl.SetValue(num)
		if edition:
			self.txtEditionCtrl.SetValue(edition)
		if dt:
			self.txtDateCtrl.SetValue(dt)

	def UpdateControls(self):
		self.CleanControls()
		filePath = self.FileList[self.CurrentFileIndex]

		logging.debug("now at : %s",filePath)

		self.treeDirCtrl.SetPath( filePath )

		fileName = os.path.basename(filePath)
		fn,ext = os.path.splitext(fileName)

		self.ExtractDetailsFromFileNameAndUpdate(fn)

		self.txtFileNameCtrl.SetValue(fileName)
		self.lblExt.SetLabel(ext)

		self.HandleTextModification()
		#self.DuplicateName()

	def FillDefaults(self):
		"""
		This fills the defaults for the date and num fields if they are empty
		The num field is set with 1234567891234
		The date field is filled with 9999
		"""
		num_def = "1234567891234"
		dt_def = "9999"

		num = self.txtNumCtrl.GetValue()
		dt = self.txtDateCtrl.GetValue()

		if len(num) < 1:
			self.txtNumCtrl.SetValue(num_def)

		if len(dt) < 1 :
			self.txtDateCtrl.SetValue(dt_def)

		self.HandleTextModification()

	def DoAllFiles(self):
		if len(self.FileList) < 1:
			logging.info("File list is empty..")
			return

		self.CurrentFileIndex =-1

		dlg = wx.MessageDialog(self, "Do you want to Format all files ?", "Confirmation", wx.YES_NO)

		if dlg.ShowModal() != wx.ID_YES :
			logging.debug("user aborted")
			return

		logging.info("Start processing the File list..")

		while self.DoNext():
			self.FormatFileName()
			wx.Yield()
			self.FillDefaults()
			wx.Yield()
			self.DotifyFileName()
			wx.Yield()
			self.SaveFile()
			wx.Yield()
			time.sleep(3)

		logging.info("Completed processing the File list..")

		dlg = wx.MessageDialog(self, "Completed processing the File list", "Complete")
		dlg.ShowModal()


	def ModFont(self):
		logging.debug("Mod font...")

		font = self.GetFont()
		size = font.GetPointSize()
		size = size*2
		font.SetPointSize(size)
		self.SetFont(font)

	def SetupAccelerators(self):

		acc_list = [
		( wx.ACCEL_CTRL, ord('d'), ID_DUP),
		( wx.ACCEL_CTRL, ord('f'), ID_FORMAT),
		( wx.ACCEL_CTRL, ord('g'), ID_DO_ALL),
		( wx.ACCEL_CTRL, ord('i'), ID_FORMAT_NUM),
		( wx.ACCEL_CTRL, ord('l'), ID_CLEAN),
		( wx.ACCEL_CTRL, ord('n'), ID_NEXT ),
		( wx.ACCEL_CTRL, ord('o'), ID_OPEN),
		( wx.ACCEL_CTRL, ord('p'), ID_PREV ),
		( wx.ACCEL_CTRL, ord('s'), ID_SAVE),
		( wx.ACCEL_CTRL, ord('.'), ID_DOTIFY),
		( wx.ACCEL_CTRL, ord(' '), ID_SPACIFY)

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
		self.Bind(wx.EVT_MENU, self.evt_dotify, id=ID_DOTIFY)
		self.Bind(wx.EVT_MENU, self.evt_spacify, id=ID_SPACIFY)
		self.Bind(wx.EVT_MENU, self.evt_do_all, id=ID_DO_ALL)

	def SaveFile(self):
		oldName = ""
		newName =""
		try:
			if(self.CurrentFileIndex < 0 or self.CurrentFileIndex > len(self.FileList) ) :
				logging.error("invalide List location..%d",self.CurrentFileIndex)
				raise FNException("Invalid current index " +str(self.CurrentFileIndex))

			oldName = self.FileList[self.CurrentFileIndex]
			olddir = os.path.dirname(oldName)
			newName = olddir + os.sep + self.lblNewFileName.GetValue()

			if(oldName == newName) :
				logging.debug("Not renaming since Old and new files names same %s -> %s",oldName,newName)
				return

			logging.debug("Renaming: %s -> %s",oldName,newName)
			os.rename(oldName,newName)

			#update the file into the list so that it can be changed/opened again if needed
			self.FileList[self.CurrentFileIndex] = newName

		except Exception as ex:
			logging.error("Error in renaming File.. %s to %s\n %s",oldName, newName, str(ex))
		else :
			logging.debug("Success in renaming File.. %s to %s",oldName, newName)

	def OpenFile(self):
		fileName = ""
		try:
			if(self.CurrentFileIndex < 0 or self.CurrentFileIndex > len(self.FileList) ) :
				logging.error("invalide List location..%d",self.CurrentFileIndex)
				raise FNException("Invalid current index " +str(self.CurrentFileIndex))

			filePath = self.FileList[self.CurrentFileIndex]


			fileName = os.path.basename( filePath )
			dstFilePath = os.path.join(TEMP_DIR,fileName)
			shutil.copy(filePath,dstFilePath)

			#cmd = 'start "{0}"'.format(dstFilePath)
			cmd = '"{0}"'.format(dstFilePath)
			logging.debug("Executing Command = %s",cmd)
			os.system(cmd)

		except Exception as ex:
			logging.error("Error in Opening File.. %s \n %s",fileName, str(ex))
		else :
			logging.debug("Opened File successfully.. %s ",fileName)


	def FormatFileName(self):
		global g_elem_lines
		fn = self.txtNamePartCtrl.GetValue()

		s = fn
		#eliminate strings
		for es in g_elem_lines:
			s = s.replace(es," ")

		#remove special characters
		#TODO need to find a  better replacement alternative
		UW_LST = ",[](){}*_"

		for unwanted in UW_LST:
			s  = s.replace(unwanted," ")

		logging.debug("String after unwanted removal %s",s)

		s = s.strip()
		s = s.replace("  "," ")
		s = s.replace("- ","-")
		s = s.replace(" -","-")
		s = s.replace(" .",".")
		s = s.replace(". ",".")

		logging.debug("String after space related changes %s",s)

		s = s.strip("-.,_")

		s = s.title() #it does camel casing of the text

		s = s.replace("'S","'s") # camel casing sometimes converts india's to India'S - hence reverting

		self.txtNamePartCtrl.SetValue(s)
		self.HandleTextModification()

	def DotifyFileName(self):
		fn = self.txtNamePartCtrl.GetValue()
		s = fn

		s = s.replace(" ",".")

		logging.debug("String after space dotify %s",s)

		self.txtNamePartCtrl.SetValue(s)
		self.HandleTextModification()

	def SpacifyFileName(self):
		fn = self.txtNamePartCtrl.GetValue()
		s = fn

		s = s.replace("."," ")

		logging.debug("String after dot spacify %s",s)

		self.txtNamePartCtrl.SetValue(s)
		self.HandleTextModification()

	def CleanupTempDir(self,p_strDirName):

		dlg = wx.MessageDialog(self, "Do you want to cleanup tmp dir ?", "Confirmation", wx.YES_NO)

		if dlg.ShowModal() != wx.ID_YES :
			logging.debug("Cleaning Dir : user aborted")
			return

		logging.debug("Cleaning Dir : %s",p_strDirName)

		for subdir, dirs, files in os.walk(p_strDirName):
			for filename in files:
				if filename == '.' or filename == '..' :
					continue

				fullFileName = os.path.join(subdir,filename)

				if os.path.isdir(fullFileName):
					continue

				logging.debug("Deleting File : %s",fullFileName)
				os.remove(fullFileName)

	def DoNext(self):
		if self.CurrentFileIndex +1 < len(self.FileList):
			self.CurrentFileIndex +=1
			self.UpdateControls()
			return True
		else :
			logging.debug("reached last")
		return False

	def DoPrev(self):
		if self.CurrentFileIndex > 0 :
			self.CurrentFileIndex -=1
			self.UpdateControls()
			return True
		else:
			logging.debug("reached first")
		return False

	def evt_next(self,id):
		logging.debug("need to go next ")
		self.DoNext()

	def evt_prev(self,id):
		logging.debug("need to go prev")
		self.DoPrev()


	def evt_format(self,id):
		logging.debug("need to format ")
		self.FormatFileName()

	def evt_dotify(self,id):
		logging.debug("need to dotify ")
		self.DotifyFileName()

	def evt_spacify(self,id):
		logging.debug("need to spacify ")
		self.SpacifyFileName()

	def evt_do_all(self,id):
		logging.debug("need to do all")
		self.DoAllFiles()

	def evt_dup(self,id):
		logging.debug("need to duplicate ")
		pass

	def evt_save(self,id):
		logging.debug("need to save ")
		self.SaveFile()
		pass

	def evt_open(self,id):
		logging.debug("need to open ")
		self.OpenFile();
		pass

	def evt_delete(self,id):
		logging.debug("need to delete ")
		self.CleanupTempDir(TEMP_DIR)


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

def LoadElemStrings():

	global g_elem_lines
	fn = os.path.join(os.path.dirname(os.path.realpath(__file__)),ELIM_CONF_FILE)
	if not os.path.exists(fn) :
		return

	fi = open(fn, 'r')
	g_elem_lines = fi.readlines()
	fi.close()

	for i in range(0,len(g_elem_lines)):
		g_elem_lines[i] = g_elem_lines[i].strip()

def main():

	TEMP_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)),TEMP_DIR_EXT)

	logging.debug("temp directory = %s",TEMP_DIR)

	if not os.path.exists(TEMP_DIR) :
		logging.info("Creating temp directory %s",TEMP_DIR)
		os.mkdir(TEMP_DIR)

	LoadElemStrings()

	guiMain()

main()