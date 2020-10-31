# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FileNamingDlg
###########################################################################

class FileNamingDlg ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"FileNaming", pos = wx.DefaultPosition, size = wx.Size( 1034,598 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		TopVertical = wx.BoxSizer( wx.HORIZONTAL )

		self.m_treeCtrl = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		TopVertical.Add( self.m_treeCtrl, 0, wx.ALL, 5 )

		RightSideHorizontal = wx.BoxSizer( wx.VERTICAL )

		DirSelection = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticSelectDir = wx.StaticText( self, wx.ID_ANY, u"SelectDir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticSelectDir.Wrap( -1 )

		DirSelection.Add( self.m_staticSelectDir, 0, wx.ALL, 5 )

		self.m_txtDir = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		DirSelection.Add( self.m_txtDir, 0, wx.ALL, 5 )

		self.m_btnOpenDir = wx.Button( self, wx.ID_ANY, u"&Open Dir", wx.DefaultPosition, wx.DefaultSize, 0 )
		DirSelection.Add( self.m_btnOpenDir, 0, wx.ALL, 5 )

		self.m_btnCollectFiles = wx.Button( self, wx.ID_ANY, u"Collect &Files", wx.DefaultPosition, wx.DefaultSize, 0 )
		DirSelection.Add( self.m_btnCollectFiles, 0, wx.ALL, 5 )


		RightSideHorizontal.Add( DirSelection, 1, wx.ALL, 5 )

		self.m_lblCurrFN = wx.StaticText( self, wx.ID_ANY, u"&Current File Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lblCurrFN.Wrap( -1 )

		RightSideHorizontal.Add( self.m_lblCurrFN, 0, wx.ALL, 5 )

		self.m_txtCtrlCurrentFileName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		RightSideHorizontal.Add( self.m_txtCtrlCurrentFileName, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_lblNumber = wx.StaticText( self, wx.ID_ANY, u"N&umber", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lblNumber.Wrap( -1 )

		RightSideHorizontal.Add( self.m_lblNumber, 0, wx.ALL, 5 )

		self.m_txtCtrlNumber = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		RightSideHorizontal.Add( self.m_txtCtrlNumber, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_lblNamePart = wx.StaticText( self, wx.ID_ANY, u"&Name Part", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lblNamePart.Wrap( -1 )

		RightSideHorizontal.Add( self.m_lblNamePart, 0, wx.ALL, 5 )

		self.m_txtCtrlNamePart = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		RightSideHorizontal.Add( self.m_txtCtrlNamePart, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_lblEdition = wx.StaticText( self, wx.ID_ANY, u"&Edition", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lblEdition.Wrap( -1 )

		RightSideHorizontal.Add( self.m_lblEdition, 0, wx.ALL, 5 )

		self.m_txtCtrlEdition = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		RightSideHorizontal.Add( self.m_txtCtrlEdition, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_lblDate = wx.StaticText( self, wx.ID_ANY, u"&Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lblDate.Wrap( -1 )

		RightSideHorizontal.Add( self.m_lblDate, 0, wx.ALL, 5 )

		self.m_txtCtrlDate = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		RightSideHorizontal.Add( self.m_txtCtrlDate, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_lblNewName = wx.StaticText( self, wx.ID_ANY, u"New FileName", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lblNewName.Wrap( -1 )

		RightSideHorizontal.Add( self.m_lblNewName, 0, wx.ALL, 5 )

		self.m_txtCtrlNewName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		RightSideHorizontal.Add( self.m_txtCtrlNewName, 0, wx.ALL|wx.EXPAND, 5 )


		TopVertical.Add( RightSideHorizontal, 1, wx.EXPAND, 5 )


		self.SetSizer( TopVertical )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_btnOpenDir.Bind( wx.EVT_BUTTON, self.m_btnOpenDirOnButtonClick )
		self.m_btnCollectFiles.Bind( wx.EVT_BUTTON, self.m_btnCollectFilesOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_btnOpenDirOnButtonClick( self, event ):
		event.Skip()

	def m_btnCollectFilesOnButtonClick( self, event ):
		event.Skip()


