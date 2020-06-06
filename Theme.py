import qdarkstyle


class Theme():

    @staticmethod
    def dark_theme(mainWindow):
        mainWindow.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    @staticmethod
    def light_theme(mainWindow):

        style = """
    QPalette{background:#EAF7FF;}QGroupBox#gboxDevicePanel>QLabel{color:#00466B;}

QWidget#frmMain,QWidget[Form="true"]{
border:1px solid #C0DCF2;
border-radius:0px;
}

.QFrame{
border:1px solid #C0DCF2;
border-radius:5px;
}

QLabel,QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox,QGroupBox,QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit,QSpinBox,QTreeView,QListView,QTableView,QTabWidget::pane{
color:#00466B;
}

QWidget#widget_title{
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

QLabel#lab_Ico,QLabel#lab_Title{
border-radius:0px;
color:#00466B;
background-color:rgba(0,0,0,0);
border-style:none;
}

QToolButton::menu-indicator{
image:None;
}

QToolButton,QWidget#widget_frm>QLabel{
border-style:none;
padding:10px;
color:#00466B;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

QToolButton:hover,QWidget#widget_frm>QLabel:hover{
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
}

QLabel[labVideo="true"]{
color:#00466B;
border:1px solid #C0DCF2;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

QLabel[labVideo="true"]:focus{
border:1px solid #FF0000;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
}

QLineEdit,QTextEdit,QPlainTextEdit,QSpinBox{
border:1px solid #C0DCF2;
border-radius:5px;
padding:2px;
background:none;
selection-background-color:#DEF0FE;
selection-color:#00466B;
}

QLineEdit[echoMode="2"]{
lineedit-password-character:9679;
}

.QGroupBox{
border:1px solid #C0DCF2;
border-radius:5px;
}

.QPushButton{
border-style:none;
border:1px solid #C0DCF2;
color:#00466B;
padding:5px;
min-height:20px;
border-radius:5px;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

.QPushButton:hover{
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
}

.QPushButton:pressed{
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

.QPushButton:disabled{
color:#838383;
background:#F4F4F4;
}

QPushButton#btnSplitterH{
padding:2px;
min-height:8px;
}

QPushButton#btnMenu,QPushButton#btnMenu_Min,QPushButton#btnMenu_Max,QPushButton#btnMenu_Close,QPushButton#btnSplitterV,QPushButton#btnSplitterH{
border-radius:0px;
color:#00466B;
background-color:rgba(0,0,0,0);
border-style:none;
}

QPushButton#btnMenu:hover,QPushButton#btnMenu_Min:hover,QPushButton#btnMenu_Max:hover,QPushButton#btnSplitterV:hover,QPushButton#btnSplitterH:hover{
background-color:qlineargradient(spread:pad,x1:0,y1:1,x2:0,y2:0,stop:0 rgba(25,134,199,0),stop:1 #F2F9FF);
}

QPushButton#btnMenu_Close:hover{
background-color:qlineargradient(spread:pad,x1:0,y1:1,x2:0,y2:0,stop:0 rgba(238,0,0,128),stop:1 rgba(238,44,44,255));
}

QCheckBox{
color:#00466B;
spacing:2px;
}

QCheckBox::indicator{
width:20px;
height:20px;
}

QCheckBox::indicator:unchecked{
image:url(:/images/checkbox_unchecked);
}

QCheckBox::indicator:checked{
image:url(:/images/checkbox_checked);
}

QRadioButton{
color:#00466B;
spacing:2px;
background:transparent;
}

QRadioButton::indicator{
width:15px;
height:15px;
}

QRadioButton::indicator::unchecked{
image:url(:/resource/radio_normal.png);
}

QRadioButton::indicator::checked{
image:url(:/resource/radio_selected.png);
}

QSpinBox::up-button,QDateEdit::up-button,QTimeEdit::up-button,QDateTimeEdit::up-button{
image:url(:/images/add_top.png);
}

QSpinBox::down-button,QDateEdit::down-button,QTimeEdit::down-button,QDateTimeEdit::down-button{
image:url(:/images/add_bottom.png);
}

QComboBox,QDateEdit,QTimeEdit,QDateTimeEdit,QSpinBox{
border-radius:3px;
padding:3px 5px 3px 5px;
border:1px solid #C0DCF2;
background:none;
selection-background-color:#DEF0FE;
selection-color:#00466B;
}

QComboBox::drop-down,QDateEdit::drop-down,QTimeEdit::drop-down,QDateTimeEdit::drop-down{
subcontrol-origin:padding;
subcontrol-position:top right;
width:15px;
border-left-width:1px;
border-left-style:solid;
border-top-right-radius:3px;
border-bottom-right-radius:3px;
border-left-color:#C0DCF2;
}

QComboBox::down-arrow,QDateEdit::down-arrow,QTimeEdit::down-arrow,QDateTimeEdit::down-arrow{
image:url(:/images/add_bottom.png);
}

QScrollBar:vertical{
width:10px;
background-color:rgba(0,0,0,0%);
padding-top:10px;
padding-bottom:10px;
}

QScrollBar:horizontal{
height:10px;
background-color:rgba(0,0,0,0%);
padding-left:10px;
padding-right:10px;
}

QScrollBar::handle:vertical,QScrollBar::handle:horizontal{
width:10px;
background:#C0DEF6;
}

QScrollBar::handle:vertical:hover,QScrollBar::handle:horizontal:hover{
width:10px;
background:#C0DEF6;
}

QScrollBar::add-line:vertical{
height:10px;
width:10px;
subcontrol-position:bottom;
subcontrol-origin:margin;
border-image:url(:/images/add_bottom.png);
}

QScrollBar::add-line:horizontal{
height:10px;
width:10px;
subcontrol-position:right;
subcontrol-origin:margin;
border-image:url(:/images/add_right.png);
}

QScrollBar::sub-line:vertical{
height:10px;
width:10px;
subcontrol-position:top;
subcontrol-origin:margin;
border-image:url(:/images/add_top.png);
}

QScrollBar::sub-line:horizontal{
height:10px;
width:10px;
subcontrol-position:left;
subcontrol-origin:margin;
border-image:url(:/images/add_left.png);
}

QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical,QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal{
width:10px;
background:#DAEFFF;
}

QScrollArea{
border:0px;
}

QTreeView,QListView,QTableView,QTabWidget::pane{
border:1px solid #C0DCF2;
selection-background-color:#F2F9FF;
selection-color:#00466B;
alternate-background-color:#DAEFFF;
}

QTableView::item:selected,QListView::item:selected,QTreeView::item:selected{
color:#00466B;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

QTableView::item:hover,QListView::item:hover,QTreeView::item:hover{
color:#00466B;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
}

QTableView::item,QListView::item,QTreeView::item{
padding:5px;
margin:0px;
}

QHeaderView::section,QTableCornerButton:section{
padding:3px;
margin:0px;
color:#00466B;
border:1px solid #C0DCF2;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
}

QTabBar::tab{
border-radius:5px;
border:1px solid #C0DCF2;
color:#00466B;
min-width:55px;
min-height:20px;
padding:3px 8px 3px 8px;
margin:1px;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
}

QTabBar::tab:selected,QTabBar::tab:hover{
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

QStatusBar::item{
border:0px solid #DEF0FE;
border-radius:3px;
}

QToolBox::tab,QToolTip,QGroupBox#gboxDevicePanel{
padding:3px;
border-radius: 5px;
color:#00466B;
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #DEF0FE,stop:1 #C0DEF6);
}

QToolBox::tab:selected{
background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #F2F9FF,stop:1 #DAEFFF);
}
    """
        mainWindow.setStyleSheet(style)

    @staticmethod
    def system_theme(mainWindow):
        mainWindow.setStyleSheet(None)

    @staticmethod
    def custum_theme(mainWindow):
        try:
            with open("style.qss") as f:
                style = f.read()
                mainWindow.setStyleSheet(style)
        except:
            Theme.dark_theme(mainWindow)
