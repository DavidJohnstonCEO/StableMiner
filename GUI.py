#! /usr/bin/env python
#
# Generated by PAGE version 4.1
# In conjuction with Tcl version 8.6
#    Jan. 10, 2014 11:59:08 PM
import sys, os, subprocess

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

try:
    from Tkinter import *
except ImportError:
    from tkinter import *
try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1



def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('EasyMiner')
    root.geometry('600x240+426+561')
    set_Tk_var()
    w = New_Toplevel_1 (root)
    root.wm_iconbitmap('design.ico')
    init()
    root.mainloop()

w = None
def create_New_Toplevel_1 (root):
    '''Starting point when module is imported by another program.'''
    global w, w_win
    if w: # So we have only one instance of window.
        return
    w = Toplevel (root)
    w.title('New_Toplevel_1')
    w.geometry('600x240+426+561')
    set_Tk_var()
    w_win = New_Toplevel_1 (w)
    init()
    return w_win

def destroy_New_Toplevel_1 ():
    global w
    w.destroy()
    w = None


def set_Tk_var():
    # These are Tk variables used passed to Tkinter and must be
    # defined before the widgets using them are created.
    global address
    address = StringVar()

    global bar
    bar = IntVar()

    global flaglist
    flaglist = StringVar()

    global flags
    flags = StringVar()


def init():
    pass

def start():
    location = os.path.join(dname, "p2pool/run_p2pool.py")
    global p2pool
    p2pool = subprocess.Popen([sys.executable,location])
    batfile = "cgminer --url http://192.168.1.217:9332/ --userpass " + str(address) + ":123 " + str(flags)
    batfile = batfile.replace("PY_VAR0", "anyusername") #If a bitcoin address is not given, it is replaced by 'anyusername', it should still work by sending the bitcoins to the local bitcoind/qt address
    batfile = batfile.replace("PY_VAR3", "") #Removes junk if flags aren't given
    batloc = dname + "\cgminer\mine.bat"
    save = open(batloc, 'w+')
    save.write(batfile)
    save.close()
    global cgminer
    cgminer = subprocess.Popen(batloc, shell=True)
    print "------------------------------------------------------------"
    print "Mining operations started, work should now generate."
    print "------------------------------------------------------------"


def stop ():
    p2pool.kill()
    cgminer.kill
    print
    print "------------------------------------------------------------"
    print "Mining operations have stopped."
    print "------------------------------------------------------------"
    sys.stdout.flush()


class New_Toplevel_1:
    def __init__(self, master=None):
        _bgcolor = 'SystemButtonFace'  # X11 color: #f0f0f0
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'SystemButtonFace' # X11 color: #f0f0f0
        _ana1color = 'SystemButtonFace' # X11 color: #f0f0f0
        _ana2color = 'SystemButtonFace' # X11 color: #f0f0f0
        font11 = "-family {Courier New} -size 10 -weight normal -slant " + \
            " roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])
        master.configure(highlightcolor="black")


        self.style.configure('TNotebook.Tab',background=_bgcolor)
        self.style.configure('TNotebook.Tab',foreground=_fgcolor)
        self.style.map('TNotebook.Tab',background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(master)
        self.TNotebook1.place(relx=0.02,rely=0.04,relheight=0.94,relwidth=0.97)
        self.TNotebook1.configure(width=584)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_pg0 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_pg0, padding=3)
        self.TNotebook1.tab(0, text="Start Mining",underline="-1",)
        self.TNotebook1_pg1 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_pg1, padding=3)
        self.TNotebook1.tab(1, text="Info",underline="-1",)
        self.TNotebook1_pg2 = ttk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_pg2, padding=3)
        self.TNotebook1.tab(2, text="Flag List",underline="-1",)

        self.TButton1 = ttk.Button (self.TNotebook1_pg0)
        self.TButton1.place(relx=0.34,rely=0.66,height=25,width=76)
        self.TButton1.configure(command=start)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Start Mining''')

        self.Label1 = Label (self.TNotebook1_pg0)
        self.Label1.place(relx=0.02,rely=0.05,height=21,width=91)
        self.Label1.configure(activebackground="#ffffff")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(disabledforeground="#b4b4b4")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Bitcoin Address:''')

        self.Entry1 = Entry (self.TNotebook1_pg0)
        self.Entry1.place(relx=0.19,rely=0.05,relheight=0.1,relwidth=0.78)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#b4b4b4")
        self.Entry1.configure(font=font11)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#d8d8d8")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.configure(textvariable=address)

        self.Label2 = Label (self.TNotebook1_pg0)
        self.Label2.place(relx=0.02,rely=0.25,height=21,width=36)
        self.Label2.configure(activebackground="#ffffff")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(disabledforeground="#b4b4b4")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Flags:''')

        self.Entry2 = Entry (self.TNotebook1_pg0)
        self.Entry2.place(relx=0.09,rely=0.25,relheight=0.1,relwidth=0.89)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#b4b4b4")
        self.Entry2.configure(font=font11)
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#d8d8d8")
        self.Entry2.configure(selectforeground="black")
        self.Entry2.configure(textvariable=flags)

        self.TButton2 = ttk.Button (self.TNotebook1_pg0)
        self.TButton2.place(relx=0.52,rely=0.66,height=25,width=76)
        self.TButton2.configure(command=stop)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Stop Mining''')

        self.TProgressbar1 = ttk.Progressbar (self.TNotebook1_pg0)
        self.TProgressbar1.place(relx=0.78,rely=0.86,relheight=0.11
                ,relwidth=0.21)
        self.TProgressbar1.configure(variable=bar)

        self.TLabel7 = ttk.Label (self.TNotebook1_pg0)
        self.TLabel7.place(relx=-0.19,rely=0.83,height=1,width=794)
        self.TLabel7.configure(background="#000000")
        self.TLabel7.configure(foreground="#000000")
        self.TLabel7.configure(relief="flat")
        self.TLabel7.configure(text='''______________________________________________________________________________________________________________________________________________________________''')

        self.TLabel8 = ttk.Label (self.TNotebook1_pg0)
        self.TLabel8.place(relx=0.02,rely=0.87,height=19,width=436)
        self.TLabel8.configure(background=_bgcolor)
        self.TLabel8.configure(foreground="#000000")
        self.TLabel8.configure(relief="flat")
        self.TLabel8.configure(text='''Mining info goes here''')
        self.TLabel8.configure(width=436)

        self.TLabel1 = ttk.Label (self.TNotebook1_pg1)
        self.TLabel1.place(relx=0.02,rely=0.04,height=19,width=193)
        self.TLabel1.configure(background=_bgcolor)
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text='''Version: Bitcoin x32 Beta + CGMiner''')

        self.TLabel2 = ttk.Label (self.TNotebook1_pg1)
        self.TLabel2.place(relx=0.02,rely=0.13,height=19,width=117)
        self.TLabel2.configure(background=_bgcolor)
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(text='''Created: 01/09/2014''')

        self.TLabel3 = ttk.Label (self.TNotebook1_pg1)
        self.TLabel3.place(relx=0.02,rely=0.35,height=19,width=263)
        self.TLabel3.configure(background=_bgcolor)
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(text='''This software was created by Argutus1 on Reddit.''')

        self.TLabel4 = ttk.Label (self.TNotebook1_pg1)
        self.TLabel4.place(relx=0.02,rely=0.44,height=19,width=511)
        self.TLabel4.configure(background=_bgcolor)
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(relief="flat")
        self.TLabel4.configure(text='''This software may be edited and redistributed, on the condition that this page will not be edited.''')

        self.TLabel5 = ttk.Label (self.TNotebook1_pg1)
        self.TLabel5.place(relx=0.02,rely=0.53,height=19,width=352)
        self.TLabel5.configure(background=_bgcolor)
        self.TLabel5.configure(foreground="#000000")
        self.TLabel5.configure(relief="flat")
        self.TLabel5.configure(text='''Donations may be sent to: 13GGffkBfcf8nbfBE2qxnxgpqXAbjEyehF''')

        self.TLabel6 = ttk.Label (self.TNotebook1_pg1)
        self.TLabel6.place(relx=0.02,rely=0.76,height=19,width=576)
        self.TLabel6.configure(background=_bgcolor)
        self.TLabel6.configure(foreground="#000000")
        self.TLabel6.configure(relief="flat")
        self.TLabel6.configure(text='''Bitcoind or qt must be running to use this software. The config file also must have server mode enabled.''')

        self.Label3 = Label (self.TNotebook1_pg1)
        self.Label3.place(relx=0.02,rely=0.68,height=21,width=407)
        self.Label3.configure(activebackground="#ffffff")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(disabledforeground="#b4b4b4")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''EasyMiner uses CGMiner for its mining process, look it up for available flags ''')

        self.Scrolledlistbox1 = ScrolledListBox(self.TNotebook1_pg2)
        self.Scrolledlistbox1.place(relx=0.01,rely=0.04,relheight=0.82
                ,relwidth=0.97)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(disabledforeground="#b4b4b4")
        self.Scrolledlistbox1.configure(font=font11)
        self.Scrolledlistbox1.configure(foreground="black")
        self.Scrolledlistbox1.configure(highlightcolor="SystemButtonFace")
        self.Scrolledlistbox1.configure(selectbackground="#d8d8d8")
        self.Scrolledlistbox1.configure(selectforeground="black")
        self.Scrolledlistbox1.configure(width=10)
        self.Scrolledlistbox1.configure(listvariable=flaglist)






# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        self.configure(yscrollcommand=self._autoscroll(vsb),
            xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (took from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

if __name__ == '__main__':
    vp_start_gui()

