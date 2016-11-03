from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
#from kivy.core.window import Window
from kivy.garden.graph import Graph, MeshLinePlot
from kivy.properties import ObjectProperty

#Window.clearcolor = (1, 1, 1, 1)

Builder.load_string("""
<Loginprompt>
    id: loginprompt
    BoxLayout:
        orientation: 'vertical'
        padding: [20, 20, 20, 20]
        spacing: 30
        canvas.before: 
            Color: 
                rgb: 0.6, 0.6, 0.6
            Rectangle:
                size: self.size
                pos: self.pos
        Image:
            id: logoimage
            source: 'jklogo1.png'
            size_hint_y: 0.32
        BoxLayout:
            id: middlebox
            size_hint_y:0.34
            BoxLayout:
                size_hint_x: 0.2
            Button:
                id: studentlogin
                size_hint_x: 0.6
                text: 'Student Login'
                font_size: 50
                on_press: loginprompt.slogin('studentlogin')
                canvas.before:
                    Color:
                        rgba: 0.5, 0, 0, 1
                        Rectangle:
                            size: self.size
                            pos: self.pos
            BoxLayout:
                size_hint_x:0.2
        BoxLayout:
            id: middlebox
            size_hint_y:0.34
            BoxLayout:
                size_hint_x: 0.2
            Button:
                id: adminlogin
                size_hint_x: 0.6
                text: 'Admin Login'
                font_size: 50
                on_press: loginprompt.slogin('adminlogin')
            BoxLayout:
                size_hint_x:0.2
                
<LoginScreen>:
    id: loginscreen
    uname: unameinput
    passw: passinput
    action: loginbutton
    BoxLayout:
        orientation: 'vertical'
        
        BoxLayout:
            id: bottombox
            size_hint_y: 0.40
        
        BoxLayout:
            id: focus
            size_hint_y: 0.15
            
            BoxLayout:
                id: sidebox1
                size_hint_x: 0.15
            
            BoxLayout:
                id:middlebox
                orientation: 'vertical'
                size_hint_x:0.70
                canvas.before: 
                    Color: 
                        rgba: 0.1, 0.2, 0.3, 1
                    Rectangle:
                        size: self.size
                        pos: self.pos
                            
                BoxLayout:
                    id: unamebox
                    Label:
                        id:unamelabel
                        text: 'Username : '
                    TextInput:
                        id:unameinput
                        multiline: False
                        
                BoxLayout:
                    id: passbox
                    
                    Label:
                        id:passlabel
                        text: 'Password : '
                    TextInput:
                        id:passinput
                        password:True
                        multiline: False
                        
                Button:
                    id: loginbutton
                    text: 'Login'
                    canvas.before:
                        Color:
                            rgba: 0.2, 0.3, 0.4, 1
                            Rectangle:
                                size: self.size
                    on_press: loginscreen.validation()
                    
                    
                       
                        
            BoxLayout:
                id:sidebox2
                size_hint_x:0.15
                
        BoxLayout:
            id: bottombox
            size_hint_y: 0.45

<Dstudent>:
    id: dstudent
    sname: nameinput
    entry: entryinput
    branch: branchinput
    yop: yopinput
    address: addressinput
    subjects: [subjectsinput1, subjectsinput2, subjectsinput3]
    marks: [marksinput1, marksinput2, marksinput3]
    
    BoxLayout:
        BoxLayout:
            size_hint_x: 0.10
        BoxLayout:
            orientation: 'vertical'
            size_hint_x: 0.80
            padding: [25, 70, 25, 150]
            spacing: 15
            BoxLayout:
                Label: 
                    text: 'Name'
                    text_size: self.size
                    halign: 'left'
                    valign: 'top'
                    color: 0, 0, 0, 1
                    size_hint_x: 0.25
                TextInput:
                    id: nameinput
            BoxLayout:
                Label:
                    text: 'Entry No.'
                    text_size: self.size
                    halign: 'left'
                    valign: 'top'
                    color: 0, 0, 0, 1
                    size_hint_x: 0.25
                TextInput:
                    id: entryinput
            BoxLayout:
                Label:
                    text: 'Branch'
                    text_size: self.size
                    halign: 'left'
                    valign: 'top'
                    color: 0, 0, 0, 1
                    size_hint_x: 0.25
                TextInput:
                    id: branchinput
            BoxLayout:
                Label:
                    text: 'Year of Passing (DD:MM:YYYY)'
                    text_size: self.size
                    halign: 'left'
                    valign: 'top'
                    color: 0, 0, 0, 1
                    size_hint_x: 0.25
                TextInput:
                    id: yopinput
            BoxLayout:
                Label:
                    text: 'Address'
                    text_size: self.size
                    halign: 'left'
                    valign: 'top'
                    color: 0, 0, 0, 1
                    size_hint_x: 0.25
                TextInput:
                    id: addressinput
            BoxLayout:
                Label:
                    text: 'Subjects'
                    text_size: self.size
                    halign: 'left'
                    valign: 'top'
                    color: 0, 0, 0, 1
                    size_hint_x: 0.25
                BoxLayout:
                    TextInput:
                        id: subjectsinput1
                    TextInput:
                        id: subjectsinput2
                    TextInput:
                        id: subjectsinput3
                
            BoxLayout:
                Label:
                    text: 'Marks'
                    text_size: self.size
                    halign: 'left'
                    color: 0, 0, 0, 1
                    size_hint_x: 0.25
                BoxLayout:
                    TextInput:
                        id: marksinput1
                    TextInput:
                        id: marksinput2
                    TextInput:
                        id: marksinput3

            BoxLayout:
                padding: [220, 0, 220, 0]
                Button:
                    id: savebutton
                    text: 'Save & Logout'
                    on_press: dstudent.save()
            
                    
        BoxLayout:
            size_hint_x: 0.10
    
        

<Dadmin>:
    id: dadmin
    entry: entryinput
    BoxLayout:
        padding: [130, 280, 130, 280]
        spacing: 50
        Label: 
            text: 'Student Info'
        TextInput:
            id: entryinput
            text: 'Entry No.'
            multiline: False
            
        Button:
            text: 'Display Info'
            on_press: dadmin.call('info')
        Button:
            text: 'Display Graph'
            on_press: dadmin.call('graph')

<StudentInfo>:
    id: studentinfo
    sname: name
    entryno: entryno
    branch: branch
    address: address
    yop: yop
    subjects: [subject1, subject2, subject3]
    marks: [marks1, marks2, marks3]
    
    BoxLayout:
        orientation: 'vertical'
        padding: [75, 100, 75, 100]
        BoxLayout:
            Label: 
                text: 'Name'
                text_size: self.size
                halign: 'left'
                valign: 'top'
                color: 0, 0, 0, 1
                size_hint_x: 0.25
            Label:
                id: name
                text: str(studentinfo.sname)
                text_size: self.size
                halign: 'left'
                valign: 'top'
                color: 0, 0, 0, 1

        BoxLayout:
            Label: 
                text: 'Entry No.'
                text_size: self.size
                halign: 'left'
                valign: 'top'
                color: 0, 0, 0, 1
                size_hint_x: 0.25
            Label:
                id: entryno
                text: str(studentinfo.entryno)
                text_size: self.size
                halign: 'left'
                valign: 'top'
                color: 0, 0, 0, 1
        BoxLayout:
            Label: 
                text: 'Branch'
                text_size: self.size
                halign: 'left'
                valign: 'top'
                color: 0, 0, 0, 1
                size_hint_x: 0.25
            Label:
                id: branch
                text: str(studentinfo.branch)
                text_size: self.size
                halign: 'left'
                valign: 'top'
                color: 0, 0, 0, 1
        BoxLayout:
            Label: 
                text: 'Address'
                text_size: self.size
                halign: 'left'
                valign: 'top'
                color: 0, 0, 0, 1
                size_hint_x: 0.25
            Label:
                id: address
                text: str(studentinfo.address)
                text_size: self.size
                halign: 'left'
                valign: 'top'
                color: 0, 0, 0, 1
        BoxLayout:
            Label: 
                text: 'Year of Passing'
                text_size: self.size
                halign: 'left'
                valign: 'top'
                color: 0, 0, 0, 1
                size_hint_x: 0.25
            Label:
                id: yop
                text: str(studentinfo.yop)
                text_size: self.size
                halign: 'left'
                valign: 'top'
                color: 0, 0, 0, 1
        BoxLayout:
            spacing: 50
            Label: 
                text: 'Subjects'
                text_size: self.size
                halign: 'left'
                valign: 'top'
                color: 0, 0, 0, 1
                size_hint_x: 0.25
            BoxLayout:
                Label:
                    id: subject1
                    text: str(studentinfo.subjects[0])
                    text_size: self.size
                    halign: 'left'
                    valign: 'top'
                    color: 0, 0, 0, 1
                Label:
                    id: subject2
                    text: str(studentinfo.subjects[1])
                    text_size: self.size
                    halign: 'left'
                    valign: 'top'
                    color: 0, 0, 0, 1
                Label:
                    id: subject3
                    text: str(studentinfo.subjects[2])
                    text_size: self.size
                    halign: 'left'
                    valign: 'top'
                    color: 0, 0, 0, 1
        BoxLayout:
            Label: 
                text: 'Marks'
                text_size: self.size
                halign: 'left'
                valign: 'top'
                color: 0, 0, 0, 1
                size_hint_x: 0.25
            BoxLayout:
                Label:
                    id: marks1
                    text: str(studentinfo.marks[0])
                    text_size: self.size
                    halign: 'left'
                    valign: 'top'
                    color: 0, 0, 0, 1
                Label:
                    id: marks2
                    text: str(studentinfo.marks[1])
                    text_size: self.size
                    halign: 'left'
                    valign: 'top'
                    color: 0, 0, 0, 1
                Label:
                    id: marks3
                    text: str(studentinfo.marks[2])
                    text_size: self.size
                    halign: 'left'
                    valign: 'top'
                    color: 0, 0, 0, 1
                    
<StudentGraph>:
    id: studentgraph
    BoxLayout:
        MyGraph:
                
""")
marksGlobal = [75, 74, 76]


class Loginprompt(Screen):
    def __init__(self, **kwargs):
        super(Loginprompt, self).__init__(**kwargs)
        
    def slogin(self, id):
        print id
        if id=='adminlogin':
            sm.switch_to(LoginScreen(auth='admin'))
        if id=='studentlogin':
            sm.switch_to(LoginScreen(auth='student'))


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        if 'auth' in kwargs:
            self.auth=kwargs['auth']
            
        
    def validation(self):
        if self.auth=='student':
            if self.action.text=='Login':
                if self.uname.text=='bsy167508' and self.passw.text=='password':
                    sm.switch_to(Dstudent(name='screen 3'))
                else:
                    self.action.text='Wrong credentials, click to try again.'
            else:
                self.uname.text=''
                self.passw.text=''
                self.action.text='Login'
        else:
            if self.action.text=='Login':
                if self.uname.text=='ahm.rimer' and self.passw.text=='password':
                    sm.switch_to(Dadmin(name= 'screen 4'))
                else:
                    self.action.text='Wrong credentials, click to try again.'
            else:
                self.uname.text=''
                self.passw.text=''
                self.action.text='Login'
        
            
class Dstudent(Screen):
    def __init__(self, **kwargs):
        print 'admin'
        super(Dstudent, self).__init__(**kwargs)
        
    def save(self):
        if not os.path.exists('student_info'):
                os.makedirs('student_info')
                print 'Directory created'
        file = open('student_info/'+self.entry.text+'.txt', 'w')
        file.writelines(['Name:'+self.sname.text+'\n', 'Entry No.:'+self.entry.text+'\n', 'Branch:'+self.branch.text+'\n', 'Address:'+self.address.text+'\n', 'Year of Passing:'+self.yop.text+'\n',]) 
        file.writelines(['Subjects:'+' '.join([self.subjects[i].text for i in xrange(3) ])+'\n','Marks:'+' '.join([self.marks[i].text for i in xrange(3) ])+'\n'])
        sm.switch_to(Loginprompt(name='screen 1'))
        file.close()
        
            
class Dadmin(Screen):
    def __init__(self, **kwargs):
        super(Dadmin, self).__init__(**kwargs)
    
    def call(self, param):
        if param=='info':
            sm.switch_to(StudentInfo(name='screen 5', entry=self.entry.text))
        else:
            sm.switch_to(StudentGraph(name='screen 5', entry=self.entry.text))

class StudentInfo(Screen):
    def __init__(self, **kwargs):
        super(StudentInfo, self).__init__(**kwargs)
        if 'entry' in kwargs:
            self.entry=kwargs['entry']
            file = open('student_info/'+self.entry+'.txt')
            for line in file:
                key, value = line.split(':')
                if key=='Name':
                    self.sname=value
                if key=='Entry No.':
                    self.entryno=value
                if key=='Year of Passing':
                    self.yop=value
                if key=='Address':
                    self.address=value
                if key=='Branch':
                    self.branch=value
                if key=='Subjects':
                    self.subjects=value.split(' ')
                if key=='Marks':
                    self.marks=value.split(' ')
            file.close()       

class StudentGraph(Screen):
    def __init__(self, **kwargs):
        super(StudentGraph, self).__init__(**kwargs)
        if 'entry' in kwargs:
            self.entry=kwargs['entry']
            with open('student_info/'+self.entry+'.txt', 'rb') as file:
                for line in file:
                    key, value = line.split(':')
                    if key=='Subjects':
                        self.subjects=value.split(' ')
                        print self.subjects
                    if key=='Marks':
                        self.marks = value.split(' ')

class MyGraph(Graph):
    def __init__(self, **kwargs):
        super(MyGraph, self).__init__(**kwargs)
        self.xlabel = 'Subjects'
        self.ylabel = 'Marks'
        self.x_ticks_minor = 1
        self.x_ticks_major = 1
        self.y_ticks_major = 25
        self.y_ticks_minor = 5
        self.y_grid_label = True
        self.x_grid_label = True
        self.padding = 5
        self.xlog = False
        self.ylog = False
        self.x_grid = True
        self.y_grid = True
        self.xmin = 0
        self.xmax = 4
        self.ymin = 0
        self.ymax = 100
        self.linePlot = MeshLinePlot(color=[1, 0, 0, 1])
        self.linePlot.points = [(i+1, marksGlobal[i]) for i in [0, 1, 2]]
        self.add_plot(self.linePlot)
        
sm = ScreenManager()
sm.add_widget(Loginprompt(name='screen 1'))
sm.add_widget(LoginScreen(name='screen 2'))
sm.add_widget(Dstudent(name='screen 3'))
sm.add_widget(Dadmin(name='screen 4'))
sm.add_widget(StudentInfo(name='screen 5'))
sm.add_widget(StudentGraph(name='screen 6'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()
