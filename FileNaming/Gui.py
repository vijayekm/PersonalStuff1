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

		bsizer4Tree = wx.BoxSizer( wx.HORIZONTAL )

		self.treeDirCtrl = wx.GenericDirCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE, wx.EmptyString, 0 )

		self.treeDirCtrl.ShowHidden( False )
		bsizer4Tree.Add( self.treeDirCtrl, 1, wx.ALL|wx.EXPAND, 5 )


		TopVertical.Add( bsizer4Tree, 1, wx.EXPAND|wx.FIXED_MINSIZE, 5 )

		RightSideHorizontal = wx.BoxSizer( wx.VERTICAL )

		DirSelection = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticSelectDir = wx.StaticText( self, wx.ID_ANY, u"SelectDir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticSelectDir.Wrap( -1 )

		DirSelection.Add( self.m_staticSelectDir, 0, wx.ALL, 5 )

		self.txtDirCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		DirSelection.Add( self.txtDirCtrl, 0, wx.ALL, 5 )

		self.m_btnOpenDir = wx.Button( self, wx.ID_ANY, u"&Open Dir", wx.DefaultPosition, wx.DefaultSize, 0 )
		DirSelection.Add( self.m_btnOpenDir, 0, wx.ALL, 5 )

		self.m_btnCollectFiles = wx.Button( self, wx.ID_ANY, u"Collect &Files", wx.DefaultPosition, wx.DefaultSize, 0 )
		DirSelection.Add( self.m_btnCollectFiles, 0, wx.ALL, 5 )


		RightSideHorizontal.Add( DirSelection, 0, wx.ALL, 5 )

		self.m_lblCurrFN = wx.StaticText( self, wx.ID_ANY, u"&Current File Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lblCurrFN.Wrap( -1 )

		RightSideHorizontal.Add( self.m_lblCurrFN, 0, wx.ALL, 5 )

		self.txtFileNameCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		RightSideHorizontal.Add( self.txtFileNameCtrl, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_lblNumber = wx.StaticText( self, wx.ID_ANY, u"N&umber", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lblNumber.Wrap( -1 )

		RightSideHorizontal.Add( self.m_lblNumber, 0, wx.ALL, 5 )

		self.txtNumCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		RightSideHorizontal.Add( self.txtNumCtrl, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_lblNamePart = wx.StaticText( self, wx.ID_ANY, u"&Name Part", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lblNamePart.Wrap( -1 )

		RightSideHorizontal.Add( self.m_lblNamePart, 0, wx.ALL, 5 )

		self.txtNamePartCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		RightSideHorizontal.Add( self.txtNamePartCtrl, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_lblEdition = wx.StaticText( self, wx.ID_ANY, u"&Edition", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lblEdition.Wrap( -1 )

		RightSideHorizontal.Add( self.m_lblEdition, 0, wx.ALL, 5 )

		self.txtEditionCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		RightSideHorizontal.Add( self.txtEditionCtrl, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_lblDate = wx.StaticText( self, wx.ID_ANY, u"&Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lblDate.Wrap( -1 )

		RightSideHorizontal.Add( self.m_lblDate, 0, wx.ALL, 5 )

		self.txtDateCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		RightSideHorizontal.Add( self.txtDateCtrl, 0, wx.ALL|wx.EXPAND, 5 )

		self.lblExt = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblExt.Wrap( -1 )

		RightSideHorizontal.Add( self.lblExt, 0, wx.ALL, 5 )

		self.m_lblNewName = wx.StaticText( self, wx.ID_ANY, u"New FileName", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_lblNewName.Wrap( -1 )

		RightSideHorizontal.Add( self.m_lblNewName, 0, wx.ALL, 5 )

		self.lblNewFileName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		RightSideHorizontal.Add( self.lblNewFileName, 0, wx.ALL|wx.EXPAND, 5 )


		TopVertical.Add( RightSideHorizontal, 4, wx.EXPAND, 5 )


		self.SetSizer( TopVertical )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_btnOpenDir.Bind( wx.EVT_BUTTON, self.m_btnOpenDirOnButtonClick )
		self.m_btnCollectFiles.Bind( wx.EVT_BUTTON, self.m_btnCollectFilesOnButtonClick )
		self.txtNumCtrl.Bind( wx.EVT_TEXT, self.HandleTextModification )
		self.txtNamePartCtrl.Bind( wx.EVT_TEXT, self.HandleTextModification )
		self.txtEditionCtrl.Bind( wx.EVT_TEXT, self.HandleTextModification )
		self.txtDateCtrl.Bind( wx.EVT_TEXT, self.HandleTextModification )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_btnOpenDirOnButtonClick( self, event ):
		event.Skip()

	def m_btnCollectFilesOnButtonClick( self, event ):
		event.Skip()

	def HandleTextModification( self, event ):
		event.Skip()





