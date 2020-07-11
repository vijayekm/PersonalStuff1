# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class ReminderAppFrame
###########################################################################

class ReminderAppFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"ReminderApp", pos = wx.DefaultPosition, size = wx.Size( 700,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

		self.m_remindersGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_remindersGrid.CreateGrid( 10, 2 )
		self.m_remindersGrid.EnableEditing( False )
		self.m_remindersGrid.EnableGridLines( True )
		self.m_remindersGrid.EnableDragGridSize( False )
		self.m_remindersGrid.SetMargins( 0, 0 )

		# Columns
		self.m_remindersGrid.SetColSize( 0, 200 )
		self.m_remindersGrid.SetColSize( 1, 400 )
		self.m_remindersGrid.EnableDragColMove( False )
		self.m_remindersGrid.EnableDragColSize( True )
		self.m_remindersGrid.SetColLabelSize( 30 )
		self.m_remindersGrid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_remindersGrid.AutoSizeRows()
		self.m_remindersGrid.EnableDragRowSize( True )
		self.m_remindersGrid.SetRowLabelSize( 80 )
		self.m_remindersGrid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_remindersGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer1.Add( self.m_remindersGrid, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


