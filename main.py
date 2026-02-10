from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivy.properties import ObjectProperty
from math import *

screen_man = """
ScreenManager:
    MainScreen:
    D2AreaShapeScreen:
    D2PeriShapeScreen:
    SquareScreenarea:
    SquareScreen:
    CircleScreenarea:
    CircleScreen:
    RhombusScreenarea:
    RhombusScreen:
    EllipseScreenarea:
    EllipseScreen:
    RectangleScreenarea:
    RectangleScreen:
    TriangleScreen:
    TriangleScreenarea:

<MainScreen>:
    name: "main"
    MDScreen:
        md_bg_color: [78/255, 212/255, 217/255, 1]
        MDCard:
            radius: [30]
            size_hint: (.5,.3)
            pos_hint: {"center_x": 0.5,"center_y":0.8}
            elevation: 0
            md_bg_color: [60/255, 140/255, 255/255, 1]
            padding: 10
            spacing: 10
            orientation: "vertical"
            MDIconButton:
                icon: "crop-square"
                user_font_size: "64sp"
                pos_hint: {"center_x":0.5,"center_y":0.85}
                on_press: 
                    root.manager.current = "D2area"
                    root.manager.transition.direction = 'left'
            MDLabel: 
                text: "2D Area"
                pos_hint: {"center_x":0.5,"center_y":0.72}
                size_hint: (3,3)
                halign: "center"
                font_style: "H6"

        MDCard:
            radius: [30]
            size_hint: (.5,.3)
            pos_hint: {"center_x": 0.5,"center_y":0.3}
            elevation: 0
            md_bg_color: [60/255, 140/255, 255/255, 1] 
            padding: 10
            spacing: 10
            orientation: "vertical"
            MDIconButton:
                icon: "crop-square"
                user_font_size: "64sp"
                pos_hint: {"center_x":0.5,"center_y":0.35}
                on_press: 
                    root.manager.current = "D2peri"
                    root.manager.transition.direction = 'left'
            MDLabel: 
                text: "2D Perimeter"
                pos_hint: {"center_x":0.5,"center_y":0.2}
                size_hint: (3,3)
                halign: "center"
                font_style: "H6"

<D2AreaShapeScreen>:
    name: "D2area"
    MDScreen:
        md_bg_color: [125/255, 232/255, 182/255, 1]

        ScrollView:
            bar_width: 0
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                padding: 100
                spacing: 100
                MDCard:
                    radius: [30]
                    size_hint: .65, None
                    size: 0, 250
                    pos_hint: {"center_x": 0.5,"center_y":0.5}
                    elevation: 0
                    md_bg_color: [14/255, 240/255, 97/255, 1]
                    padding: 8
                    spacing: 10
                    orientation: "vertical"
                    MDIconButton:
                        icon: "crop-square"
                        user_font_size: "64sp"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        on_press: 
                            root.manager.current = "Squarearea"
                            root.manager.transition.direction = 'left'

                    MDLabel: 
                        text: "Square"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        size_hint: (3,3)
                        halign: "center"
                        font_style: "H6"

                MDCard:
                    radius: [30]
                    size_hint: .65, None
                    size: 0 , 250
                    pos_hint: {"center_x": 0.5,"center_y":0.4}
                    elevation: 0
                    md_bg_color: [14/255, 240/255, 97/255, 1]
                    padding: 8
                    spacing: 10
                    orientation: "vertical"
                    MDIconButton:
                        icon: "circle-outline"
                        user_font_size: "64sp"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        on_press: 
                            root.manager.current = "Circlearea"
                            root.manager.transition.direction = 'left'

                    MDLabel: 
                        text: "Circle"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        size_hint: (3,3)
                        halign: "center"
                        font_style: "H6"

                MDCard:
                    radius: [30]
                    size_hint: .65, None
                    size: 0, 250
                    pos_hint: {"center_x": 0.5,"center_y":0.3}
                    elevation: 0
                    md_bg_color: [14/255, 240/255, 97/255, 1]
                    padding: 8
                    spacing: 10
                    orientation: "vertical"
                    MDIconButton:
                        icon: "rhombus-outline"
                        user_font_size: "64sp"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        on_press: 
                            root.manager.current = "Rhombusarea"
                            root.manager.transition.direction = 'left'


                    MDLabel: 
                        text: "Rhombus"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        size_hint: (3,3)
                        halign: "center"
                        font_style: "H6"

                MDCard:
                    radius: [30]
                    size_hint: .65, None
                    size: 0, 250
                    pos_hint: {"center_x": 0.5,"center_y":0.2}
                    elevation: 0
                    md_bg_color: [14/255, 240/255, 97/255, 1]
                    padding: 8
                    spacing: 10
                    orientation: "vertical"
                    MDIconButton:
                        icon: "ellipse-outline"
                        user_font_size: "64sp"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        on_press: 
                            root.manager.current = "Ellipsearea"
                            root.manager.transition.direction = 'left'

                    MDLabel: 
                        text: "Ellipse"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        size_hint: (3,3)
                        halign: "center"
                        font_style: "H6"
                        
                MDCard:
                    radius: [30]
                    size_hint: .65, None
                    size: 0, 250
                    pos_hint: {"center_x": 0.5,"center_y":0.1}
                    elevation: 0
                    md_bg_color: [14/255, 240/255, 97/255, 1]
                    padding: 8
                    spacing: 10
                    orientation: "vertical"
                    MDIconButton:
                        icon: "rectangle-outline"
                        user_font_size: "64sp"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        on_press: 
                            root.manager.current = "Rectanglearea"
                            root.manager.transition.direction = 'left'
                    MDLabel: 
                        text: "Rectangle"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        size_hint: (3,3)
                        halign: "center"
                        font_style: "H6"

                MDCard:
                    radius: [30]
                    size_hint: .65, None
                    size: 0, 250
                    pos_hint: {"center_x": 0.5,"center_y":0}
                    elevation: 0
                    md_bg_color: [14/255, 240/255, 97/255, 1]
                    padding: 8
                    spacing: 10
                    orientation: "vertical"
                    MDIconButton:
                        icon: "triangle-outline"
                        user_font_size: "64sp"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        on_press: 
                            root.manager.current = "Trianglearea"
                            root.manager.transition.direction = 'left'
                    MDLabel: 
                        text: "Triangle"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        size_hint: (3,3)
                        halign: "center"
                        font_style: "H6"

        MDIconButton:
            icon: "arrow-left-circle"
            user_font_size: "40sp"
            pos_hint: {"center_x":0.1,"center_y":0.9}
            on_press: 
                root.manager.current = "main"
                root.manager.transition.direction = 'right'

<D2PeriShapeScreen>:
    name: "D2peri"
    MDScreen:
        md_bg_color: [125/255, 232/255, 182/255, 1]

        ScrollView:
            bar_width: 0
            MDBoxLayout:
                adaptive_height: True
                orientation: "vertical"
                padding: 100
                spacing: 100
                MDCard:
                    radius: [30]
                    size_hint: .65, None
                    size: 0, 250
                    pos_hint: {"center_x": 0.5,"center_y":0.5}
                    elevation: 0
                    md_bg_color: [14/255, 240/255, 97/255, 1]
                    padding: 8
                    spacing: 10
                    orientation: "vertical"
                    MDIconButton:
                        icon: "crop-square"
                        user_font_size: "64sp"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        on_press: 
                            root.manager.current = "Square"
                            root.manager.transition.direction = 'left'
                    MDLabel: 
                        text: "Square"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        size_hint: (3,3)
                        halign: "center"
                        font_style: "H6"

                MDCard:
                    radius: [30]
                    size_hint: .65, None
                    size: 0, 250
                    pos_hint: {"center_x": 0.5,"center_y":0.4}
                    elevation: 0
                    md_bg_color: [14/255, 240/255, 97/255, 1]
                    padding: 8
                    spacing: 10
                    orientation: "vertical"
                    MDIconButton:
                        icon: "circle-outline"
                        user_font_size: "64sp"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        on_press: 
                            root.manager.current = "Circle"
                            root.manager.transition.direction = 'left'

                    MDLabel: 
                        text: "Circle"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        size_hint: (3,3)
                        halign: "center"
                        font_style: "H6"

                MDCard:
                    radius: [30]
                    size_hint: .65, None
                    size: 0, 250
                    pos_hint: {"center_x": 0.5,"center_y":0.3}
                    elevation: 0
                    md_bg_color: [14/255, 240/255, 97/255, 1]
                    padding: 8
                    spacing: 10
                    orientation: "vertical"
                    MDIconButton:
                        icon: "rhombus-outline"
                        user_font_size: "64sp"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        on_press: 
                            root.manager.current = "Rhombus"
                            root.manager.transition.direction = 'left'


                    MDLabel: 
                        text: "Rhombus"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        size_hint: (3,3)
                        halign: "center"
                        font_style: "H6"

                MDCard:
                    radius: [30]
                    size_hint: .65, None
                    size: 0, 250
                    pos_hint: {"center_x": 0.5,"center_y":0.2}
                    elevation: 0
                    md_bg_color: [14/255, 240/255, 97/255, 1]
                    padding: 8
                    spacing: 10
                    orientation: "vertical"
                    MDIconButton:
                        icon: "ellipse-outline"
                        user_font_size: "64sp"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        on_press: 
                            root.manager.current = "Ellipse"
                            root.manager.transition.direction = 'left'

                    MDLabel: 
                        text: "Ellipse"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        size_hint: (3,3)
                        halign: "center"
                        font_style: "H6"

                MDCard:
                    radius: [30]
                    size_hint: .65, None
                    size: 0 , 250
                    pos_hint: {"center_x": 0.5,"center_y":0.1}
                    elevation: 0
                    md_bg_color: [14/255, 240/255, 97/255, 1]
                    padding: 8
                    spacing: 10
                    orientation: "vertical"
                    MDIconButton:
                        icon: "rectangle-outline"
                        user_font_size: "64sp"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        on_press: 
                            root.manager.current = "Rectangle"
                            root.manager.transition.direction = 'left'
                    MDLabel: 
                        text: "Rectangle"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        size_hint: (3,3)
                        halign: "center"
                        font_style: "H6"

                MDCard:
                    radius: [30]
                    size_hint: .65, None
                    size: 0, 250
                    pos_hint: {"center_x": 0.5,"center_y":0}
                    elevation: 0
                    md_bg_color: [14/255, 240/255, 97/255, 1]
                    padding: 8
                    spacing: 10
                    orientation: "vertical"
                    MDIconButton:
                        icon: "triangle-outline"
                        user_font_size: "64sp"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        on_press: 
                            root.manager.current = "Triangle"
                            root.manager.transition.direction = 'left'
                    MDLabel: 
                        text: "Triangle"
                        pos_hint: {"center_x":0.5,"center_y":0.5}
                        size_hint: (3,3)
                        halign: "center"
                        font_style: "H6"    

        MDIconButton:
            icon: "arrow-left-circle"
            user_font_size: "40sp"
            on_press: 
                root.manager.current = "main"
                root.manager.transition.direction = 'right'
            pos_hint: {"center_x":0.1,"center_y":0.9}          

<SquareScreenarea>:
    name: "Squarearea"
    square_label: square_label
    square_input: square_input
    MDScreen:
        md_bg_color: [255/255, 206/255, 138/255, 1]
        MDIconButton:
            icon: "arrow-left-circle"
            user_font_size: "40sp"
            pos_hint: {"center_x":0.1,"center_y":0.9}
            on_press: 
                root.manager.current = "D2area"
                root.manager.transition.direction = 'right'
        MDLabel:
            text: "Area of Square"    
            pos_hint: {"center_x":0.5,"center_y":0.8}
            halign: "center"
            font_style: "H5"
        MDLabel:
            id: square_label
            text:""    
            pos_hint: {"center_x":0.5,"center_y":0.2}
            halign : 'center'
            font_style: "H6"
        MDCard:
            radius: [30]
            size_hint: (.5,.4)
            pos_hint: {"center_x": 0.5,"center_y":0.8}
            elevation: 0
            md_bg_color: [230/255, 219/255, 9/255,1]
            padding: 10
            spacing: 60
            pos_hint: {"center_x":0.5,"center_y":0.5}
            orientation: "vertical"
            MDTextField:
                id: square_input
                hint_text: "Length"
                pos_hint: {"center_x":0.5,"center_y":0.5}
                size_hint : (0.9,0)
            MDFillRoundFlatButton:
                text: "Calculate"
                pos_hint: {"center_x":0.5,"center_y":0.6}
                on_press: root.ans_square_area()
<SquareScreen>:
    name: "Square"
    square_labelp: square_labelp
    square_inputp: square_inputp
    MDScreen:
        md_bg_color: [255/255, 206/255, 138/255, 1]
        MDIconButton:
            icon: "arrow-left-circle"
            user_font_size: "40sp"
            pos_hint: {"center_x":0.1,"center_y":0.9}
            on_press: 
                root.manager.current = "D2peri"
                root.manager.transition.direction = 'right'
        MDLabel:
            text: "Perimeter of Square"    
            pos_hint: {"center_x":0.5,"center_y":0.8}
            halign: "center"
            font_style: "H5"
        MDLabel:
            id: square_labelp
            text:""    
            pos_hint: {"center_x":0.5,"center_y":0.2}
            halign : 'center'
            font_style: "H6"
        MDCard:
            radius: [30]
            size_hint: (.5,.4)
            pos_hint: {"center_x": 0.5,"center_y":0.8}
            elevation: 0
            md_bg_color: [230/255, 219/255, 9/255,1]
            padding: 10
            spacing: 60
            pos_hint: {"center_x":0.5,"center_y":0.5}
            orientation: "vertical"
            MDTextField:
                id: square_inputp
                hint_text: "Length"
                pos_hint: {"center_x":0.5,"center_y":0.5}
                input_type: 'number'
                size_hint : (0.9,0)
            MDFillRoundFlatButton:
                text: "Calculate"
                pos_hint: {"center_x":0.5,"center_y":0.6}
                on_press: root.ans_square_peri()

<CircleScreenarea>:
    name: "Circlearea"
    circle_label: circle_label
    circle_input: circle_input
    MDScreen:
        md_bg_color: [255/255, 206/255, 138/255, 1]
        MDIconButton:
            icon: "arrow-left-circle"
            user_font_size: "40sp"
            pos_hint: {"center_x":0.1,"center_y":0.9}
            on_press: 
                root.manager.current = "D2area"
                root.manager.transition.direction = 'right'
        MDLabel:
            text: "Area of Circle"    
            pos_hint: {"center_x":0.5,"center_y":0.8}
            halign: "center"
            font_style: "H5"
        MDLabel:
            id: circle_label
            text:""    
            pos_hint: {"center_x":0.5,"center_y":0.2}
            halign : 'center'
            font_style: "H6"
        MDCard:
            radius: [30]
            size_hint:(.5,.4)
            pos_hint: {"center_x": 0.5,"center_y":0.8}
            elevation: 0
            md_bg_color: [230/255, 219/255, 9/255,1]
            padding: 10
            spacing: 60
            pos_hint: {"center_x":0.5,"center_y":0.5}
            orientation: "vertical"
            MDTextField:
                id: circle_input
                hint_text: "Radius"
                pos_hint: {"center_x":0.5,"center_y":0.5}
                input_type: 'number'
                size_hint: (0.9,0)
            MDFillRoundFlatButton:
                text: "Calculate"
                pos_hint: {"center_x":0.5,"center_y":0.1}
                on_press: root.ans_circle_area()
<CircleScreen>:
    circle_labelp: circle_labelp
    circle_inputp: circle_inputp
    name: "Circle"
    MDScreen:
        md_bg_color: [255/255, 206/255, 138/255, 1]
        MDIconButton:
            icon: "arrow-left-circle"
            user_font_size: "40sp"
            pos_hint: {"center_x":0.1,"center_y":0.9}
            on_press: 
                root.manager.current = "D2peri"
                root.manager.transition.direction = 'right'
        MDLabel:
            text: "Circumference of Circle"    
            pos_hint: {"center_x":0.5,"center_y":0.8}
            halign: "center"
            font_style: "H5"
        MDLabel:
            id : circle_labelp
            text:""    
            pos_hint: {"center_x":0.5,"center_y":0.2}
            halign : 'center'
            font_style: "H6"
        MDCard:
            radius: [30]
            size_hint: (.5,.4)
            pos_hint: {"center_x": 0.5,"center_y":0.8}
            elevation: 0
            md_bg_color: [230/255, 219/255, 9/255,1]
            padding: 10
            spacing: 60
            pos_hint: {"center_x":0.5,"center_y":0.5}
            orientation: "vertical"
            MDTextField:
                id: circle_inputp
                hint_text: "Radius"
                pos_hint: {"center_x":0.5,"center_y":0.5}
                input_type: 'number'
                size_hint: (0.9,0)
            MDFillRoundFlatButton:
                text: "Calculate"
                pos_hint: {"center_x":0.5,"center_y":0.6}
                on_press: root.ans_circle_peri()
<RhombusScreenarea>:
    rhombus_label : rhombus_label
    rhombus_input1: rhombus_input1
    rhombus_input2: rhombus_input2
    name: "Rhombusarea"
    MDScreen:
        md_bg_color: [255/255, 206/255, 138/255, 1]
        MDIconButton:
            icon: "arrow-left-circle"
            user_font_size: "40sp"
            pos_hint: {"center_x":0.1,"center_y":0.9}
            on_press: 
                root.manager.current = "D2area"
                root.manager.transition.direction = 'right'
        MDLabel:
            text: "Area of Rhombus"    
            pos_hint: {"center_x":0.5,"center_y":0.8}
            halign: "center"
            font_style: "H5"
        MDLabel:
            id: rhombus_label
            text:""    
            pos_hint: {"center_x":0.5,"center_y":0.2}
            halign : 'center'
            font_style: "H6"
        MDCard:
            radius: [30]
            size_hint: (.5,.4)
            pos_hint: {"center_x": 0.5,"center_y":0.8}
            elevation: 0
            md_bg_color: [230/255, 219/255, 9/255,1]
            padding: 10
            spacing: 40
            pos_hint: {"center_x":0.5,"center_y":0.5}
            orientation: "vertical"
            MDTextField:
                id: rhombus_input1
                hint_text: "p Diagonal"
                pos_hint: {"center_x":0.5,"center_y":0.55}
                input_type: 'number'
                size_hint: (0.9,0)
            MDTextField:
                id: rhombus_input2
                hint_text: "q Diagonal"
                pos_hint: {"center_x":0.5,"center_y":0.5}
                input_type: 'number'
                size_hint: (0.9,0)
            MDFillRoundFlatButton:
                text: "Calculate"
                pos_hint: {"center_x":0.5,"center_y":0.6}
                on_press: root.ans_rhombus_area()
<RhombusScreen>:
    rhombus_labelp: rhombus_labelp
    rhombus_inputp: rhombus_inputp

    name: "Rhombus"
    MDScreen:
        md_bg_color: [255/255, 206/255, 138/255, 1]
        MDIconButton:
            icon: "arrow-left-circle"
            user_font_size: "40sp"
            pos_hint: {"center_x":0.1,"center_y":0.9}
            on_press: 
                root.manager.current = "D2peri"
                root.manager.transition.direction = 'right'
        MDLabel:
            text: "Perimeter of Rhombus"    
            pos_hint: {"center_x":0.5,"center_y":0.8}
            halign: "center"
            font_style: "H5"
        MDLabel:
            id: rhombus_labelp
            text:""    
            pos_hint: {"center_x":0.5,"center_y":0.2}
            halign : 'center'
            font_style: "H6"
        MDCard:
            radius: [30]
            size_hint: (.5,.4)
            pos_hint: {"center_x": 0.5,"center_y":0.8}
            elevation: 0
            md_bg_color: [230/255, 219/255, 9/255,1]
            padding: 10
            spacing: 60
            pos_hint: {"center_x":0.5,"center_y":0.5}
            orientation: "vertical"
            MDTextField:
                id: rhombus_inputp
                hint_text: "Side"
                pos_hint: {"center_x":0.5,"center_y":0.5}
                input_type: 'number'
                size_hint: (0.9,0)
            MDFillRoundFlatButton:
                text: "Calculate"
                pos_hint: {"center_x":0.5,"center_y":0.6}
                on_press: root.ans_rhombus_peri()
<EllipseScreenarea>:
    ellipse_label: ellipse_label
    ellipse_input1: ellipse_input1
    ellipse_input2: ellipse_input2
    name: "Ellipsearea"
    MDScreen:
        md_bg_color: [255/255, 206/255, 138/255, 1]
        MDIconButton:
            icon: "arrow-left-circle"
            user_font_size: "40sp"
            pos_hint: {"center_x":0.1,"center_y":0.9}
            on_press: 
                root.manager.current = "D2area"
                root.manager.transition.direction = 'right'
        MDLabel:
            text: "Area of Ellipse"    
            pos_hint: {"center_x":0.5,"center_y":0.8}
            halign: "center"
            font_style: "H5"
        MDLabel:
            id: ellipse_label
            text:""    
            pos_hint: {"center_x":0.5,"center_y":0.2}
            halign : 'center'
            font_style: "H6"
        MDCard:
            radius: [30]
            size_hint: (.5,.4)
            pos_hint: {"center_x": 0.5,"center_y":0.8}
            elevation: 0
            md_bg_color: [230/255, 219/255, 9/255,1]
            padding: 10
            spacing: 40
            pos_hint: {"center_x":0.5,"center_y":0.5}
            orientation: "vertical"
            MDTextField:
                id: ellipse_input1
                hint_text: "a Axis"
                pos_hint: {"center_x":0.5,"center_y":0.55}
                input_type: 'number'
                size_hint: (0.9,0)
            MDTextField:
                id: ellipse_input2
                hint_text: "b Axis"
                pos_hint: {"center_x":0.5,"center_y":0.5}
                input_type: 'number'
                size_hint: (0.9,0)
            MDFillRoundFlatButton:
                text: "Calculate"
                pos_hint: {"center_x":0.5,"center_y":0.6}
                on_press: root.ans_ellipse_area()
<EllipseScreen>:
    ellipse_labelp: ellipse_labelp
    ellipse_input1p: ellipse_input1p
    ellipse_input2p: ellipse_input2p
    name: "Ellipse"
    MDScreen:
        md_bg_color: [255/255, 206/255, 138/255, 1]
        MDIconButton:
            icon: "arrow-left-circle"
            user_font_size: "40sp"
            pos_hint: {"center_x":0.1,"center_y":0.9}
            on_press: 
                root.manager.current = "D2peri"
                root.manager.transition.direction = 'right'
        MDLabel:
            text: "Circumference of Ellipse"    
            pos_hint: {"center_x":0.5,"center_y":0.8}
            halign: "center"
            font_style: "H5"
        MDLabel:
            id: ellipse_labelp
            text:""    
            pos_hint: {"center_x":0.5,"center_y":0.2}
            halign : 'center'
            font_style: "H6"
        MDCard:
            radius: [30]
            size_hint: (.5,.4)
            pos_hint: {"center_x": 0.5,"center_y":0.8}
            elevation: 0
            md_bg_color: [230/255, 219/255, 9/255,1]
            padding: 10
            spacing: 40
            pos_hint: {"center_x":0.5,"center_y":0.5}
            orientation: "vertical"
            MDTextField:
                id: ellipse_input1p
                hint_text: "a Axis"
                pos_hint: {"center_x":0.5,"center_y":0.55}
                input_type: 'number'
                size_hint: (0.9,0)
            MDTextField:
                id: ellipse_input2p
                hint_text: "b Axis"
                pos_hint: {"center_x":0.5,"center_y":0.5}
                input_type: 'number'
                size_hint: (0.9,0)
            MDFillRoundFlatButton:
                text: "Calculate"
                pos_hint: {"center_x":0.5,"center_y":0.6}
                on_press: root.ans_ellipse_peri()

<RectangleScreenarea>:
    rectangle_label: rectangle_label
    rectangle_input1: rectangle_input1
    rectangle_input2: rectangle_input2
    name: "Rectanglearea"
    MDScreen:
        md_bg_color: [255/255, 206/255, 138/255, 1]
        MDIconButton:
            icon: "arrow-left-circle"
            user_font_size: "40sp"
            pos_hint: {"center_x":0.1,"center_y":0.9}
            on_press: 
                root.manager.current = "D2area"
                root.manager.transition.direction = 'right'
        MDLabel:
            text: "Area of rectangle"    
            pos_hint: {"center_x":0.5,"center_y":0.8}
            halign: "center"
            font_style: "H5"
        MDLabel:
            id: rectangle_label
            text:""    
            pos_hint: {"center_x":0.5,"center_y":0.2}
            halign : 'center'
            font_style: "H6"
        MDCard:
            radius: [30]
            size_hint: (.5,.4)
            pos_hint: {"center_x": 0.5,"center_y":0.8}
            elevation: 0
            md_bg_color: [230/255, 219/255, 9/255,1]
            padding: 10
            spacing: 40
            pos_hint: {"center_x":0.5,"center_y":0.5}
            orientation: "vertical"
            MDTextField:
                id: rectangle_input1
                hint_text: "Length"
                pos_hint: {"center_x":0.5,"center_y":0.55}
                input_type: 'number'
                size_hint: (0.9,0)
            MDTextField:
                id: rectangle_input2
                hint_text: "Breadth"
                pos_hint: {"center_x":0.5,"center_y":0.5}
                input_type: 'number'
                size_hint: (0.9,0)
            MDFillRoundFlatButton:
                text: "Calculate"
                pos_hint: {"center_x":0.5,"center_y":0.6}
                on_press: root.ans_rectangle_area()
<RectangleScreen>:
    rectangle_labelp: rectangle_labelp
    rectangle_input1p: rectangle_input1p
    rectangle_input2p: rectangle_input2p
    name: "Rectangle"
    MDScreen:
        md_bg_color: [255/255, 206/255, 138/255, 1]
        MDIconButton:
            icon: "arrow-left-circle"
            user_font_size: "40sp"
            pos_hint: {"center_x":0.1,"center_y":0.9}
            on_press: 
                root.manager.current = "D2peri"
                root.manager.transition.direction = 'right'
        MDLabel:
            text: "Perimeter of Rectangle"    
            pos_hint: {"center_x":0.5,"center_y":0.8}
            halign: "center"
            font_style: "H5"
        MDLabel:
            id: rectangle_labelp
            text:""    
            pos_hint: {"center_x":0.5,"center_y":0.2}
            halign : 'center'
            font_style: "H6"
        MDCard:
            radius: [30]
            size_hint: (.5,.4)
            pos_hint: {"center_x": 0.5,"center_y":0.8}
            elevation: 0
            md_bg_color: [230/255, 219/255, 9/255,1]
            padding: 10
            spacing: 40
            pos_hint: {"center_x":0.5,"center_y":0.5}
            orientation: "vertical"
            MDTextField:
                id: rectangle_input1p
                hint_text: "Length"
                pos_hint: {"center_x":0.5,"center_y":0.55}
                input_type: 'number'
                size_hint: (0.9,0)
            MDTextField:
                id: rectangle_input2p
                hint_text: "Breadth"
                pos_hint: {"center_x":0.5,"center_y":0.5}
                input_type: 'number'
                size_hint: (0.9,0)
            MDFillRoundFlatButton:
                text: "Calculate"
                pos_hint: {"center_x":0.5,"center_y":0.6}
                on_press: root.ans_rectangle_peri()
<TriangleScreenarea>:
    triangle_label: triangle_label
    triangle_input1: triangle_input1
    triangle_input2: triangle_input2
    name: "Trianglearea"
    MDScreen:
        md_bg_color: [255/255, 206/255, 138/255, 1]
        MDIconButton:
            icon: "arrow-left-circle"
            user_font_size: "40sp"
            pos_hint: {"center_x":0.1,"center_y":0.9}
            on_press: 
                root.manager.current = "D2area"
                root.manager.transition.direction = 'right'
        MDLabel:
            text: "Area of Triangle"    
            pos_hint: {"center_x":0.5,"center_y":0.8}
            halign: "center"
            font_style: "H5"
        MDLabel:
            id:  triangle_label
            text:""    
            pos_hint: {"center_x":0.5,"center_y":0.2}
            halign : 'center'
            font_style: "H6"
        MDCard:
            radius: [30]
            size_hint: (.5,.4)
            pos_hint: {"center_x": 0.5,"center_y":0.8}
            elevation: 0
            md_bg_color: [230/255, 219/255, 9/255,1]
            padding: 10
            spacing: 40
            pos_hint: {"center_x":0.5,"center_y":0.5}
            orientation: "vertical"
            MDTextField:
                id: triangle_input1
                hint_text: "Base"
                pos_hint: {"center_x":0.5,"center_y":0.55}
                input_type: 'number'
                size_hint: (0.9,0)
            MDTextField:
                id: triangle_input2
                hint_text: "Height"
                pos_hint: {"center_x":0.5,"center_y":0.5}
                input_type: 'number'
                size_hint: (0.9,0)
            MDFillRoundFlatButton:
                text: "Calculate"
                pos_hint: {"center_x":0.5,"center_y":0.6}
                on_press: root.ans_triangle_area()
<TriangleScreen>:
    triangle_labelp: triangle_labelp
    triangle_input1p: triangle_input1p
    triangle_input2p: triangle_input2p
    triangle_input3p: triangle_input3p
    name: "Triangle"
    MDScreen:
        md_bg_color: [255/255, 206/255, 138/255, 1]
        MDIconButton:
            icon: "arrow-left-circle"
            user_font_size: "40sp"
            pos_hint: {"center_x":0.1,"center_y":0.9}
            on_press: 
                root.manager.current = "D2peri"
                root.manager.transition.direction = 'right'
        MDLabel:
            text: "Perimeter of Triangle"    
            pos_hint: {"center_x":0.5,"center_y":0.8}
            halign: "center"
            font_style: "H5"
        MDLabel:
            id: triangle_labelp
            text:""    
            pos_hint: {"center_x":0.5,"center_y":0.2}
            halign : 'center'
            font_style: "H6"
        MDCard:
            radius: [30]
            size_hint: (.5,.4)
            pos_hint: {"center_x": 0.5,"center_y":0.8}
            elevation: 0
            md_bg_color: [230/255, 219/255, 9/255,1]
            padding: 10
            spacing: 10
            pos_hint: {"center_x":0.5,"center_y":0.5}
            orientation: "vertical"
            MDTextField:
                id: triangle_input1p
                hint_text: "Side"
                pos_hint: {"center_x":0.5,"center_y":0.55}
                input_type: 'number'
                size_hint: (0.9,0)
            MDTextField:
                id: triangle_input2p
                hint_text: "Base"
                pos_hint: {"center_x":0.5,"center_y":0.5}
                input_type: 'number'
                size_hint: (0.9,0)
            MDTextField:
                id: triangle_input3p
                hint_text: "Side"
                pos_hint: {"center_x":0.5,"center_y":0.45}
                input_type: 'number'
                size_hint: (0.9,0)
            MDFillRoundFlatButton:
                text: "Calculate"
                pos_hint: {"center_x":0.5,"center_y":0.6}
                on_press: root.ans_triangle_peri()
"""


class MainScreen(Screen):
    pass


class D2AreaShapeScreen(Screen):
    pass


class D2PeriShapeScreen(Screen):
    pass


class SquareScreenarea(Screen):
    square_label = ObjectProperty(None)
    square_input = ObjectProperty(None)

    def ans_square_area(self):
        try:
            ans = float(self.square_input.text) * float(self.square_input.text)
            self.square_label.text = "Area of Square is " + str(ans) + " sq.units"
        except ValueError:
            self.square_label.text = "Please Enter a Number"


class SquareScreen(Screen):
    square_labelp = ObjectProperty(None)
    square_inputp = ObjectProperty(None)

    def ans_square_peri(self):
        try:
            ans = 4 * float(self.square_inputp.text)
            self.square_labelp.text = "Perimeter of Square is " + str(ans) + "sq.units"
        except ValueError:
            self.square_labelp.text = "Please Enter a Number"


class CircleScreenarea(Screen):
    circle_label = ObjectProperty(None)
    circle_input = ObjectProperty(None)

    def ans_circle_area(self):
        try:
            ans = 22 / 7 * float(self.circle_input.text) * float(self.circle_input.text)
            self.circle_label.text = "Area of Circle is " + str(ans) + " sq.units"
        except ValueError:
            self.circle_label.text = "Please Enter a Number"


class CircleScreen(Screen):
    circle_labelp = ObjectProperty(None)
    circle_inputp = ObjectProperty(None)

    def ans_circle_peri(self):
        try:
            ans = 2 * 22 / 7 * float(self.circle_inputp.text)
            self.circle_labelp.text = "Circumference of Circle is " + str(ans) + " sq.units"
        except ValueError:
            self.circle_labelp.text = "Please Enter a Number"


class RhombusScreenarea(Screen):
    rhombus_label = ObjectProperty(None)
    rhombus_input1 = ObjectProperty(None)
    rhombus_input2 = ObjectProperty(None)

    def ans_rhombus_area(self):
        try:
            ans = 1 / 2 * float(self.rhombus_input1.text) * float(self.rhombus_input2.text)
            self.rhombus_label.text = "Area of Rhombus is " + str(ans) + " sq.units"
        except ValueError:
            self.rhombus_label.text = "Please Enter a Number"


class RhombusScreen(Screen):
    rhombus_labelp = ObjectProperty(None)
    rhombus_inputp = ObjectProperty(None)

    def ans_rhombus_peri(self):
        try:
            ans = 4 * float(self.rhombus_inputp.text)
            self.rhombus_labelp.text = "Perimeter of Rhombus is " + str(ans) + " sq.units"
        except ValueError:
            self.rhombus_labelp.text = "Please Enter a Number"


class EllipseScreenarea(Screen):
    ellipse_label = ObjectProperty(None)
    ellipse_input1 = ObjectProperty(None)
    ellipse_input2 = ObjectProperty(None)

    def ans_ellipse_area(self):
        try:
            ans = 22 / 7 * float(self.ellipse_input1.text) * float(self.ellipse_input2.text)
            self.ellipse_label.text = "Area of Ellipse is " + str(ans) + " sq.units"
        except ValueError:
            self.ellipse_label.text = "Please Enter a Number"


class EllipseScreen(Screen):
    ellipse_labelp = ObjectProperty(None)
    ellipse_input1p = ObjectProperty(None)
    ellipse_input2p = ObjectProperty(None)

    def ans_ellipse_peri(self):
        try:
            a = self.ellipse_input1p.text
            b = self.ellipse_input2p.text
            ans = 22 / 7 * (3 * (float(a) + float(b)) - (sqrt(
                (3 * float(a) + float(b)) * (
                        float(a) + 3 * float(b)))))
            self.ellipse_labelp.text = "Circumference of Ellipse is " + str(ans) + " sq.units"
        except ValueError:
            self.ellipse_labelp.text = "Please Enter a Number"


class RectangleScreenarea(Screen):
    rectangle_label = ObjectProperty(None)
    rectangle_input1 = ObjectProperty(None)
    rectangle_input2 = ObjectProperty(None)

    def ans_rectangle_area(self):
        try:
            ans = float(self.rectangle_input1.text) * float(self.rectangle_input2.text)
            self.rectangle_label.text = "Area of Rectangle is " + str(ans) + " sq.units"
        except ValueError:
            self.rectangle_label.text = "Please Enter a Number"


class RectangleScreen(Screen):
    rectangle_labelp = ObjectProperty(None)
    rectangle_input1p = ObjectProperty(None)
    rectangle_input2p = ObjectProperty(None)

    def ans_rectangle_peri(self):
        try:
            ans = 2 * (float(self.rectangle_input1p.text) + float(self.rectangle_input2p.text))
            self.rectangle_labelp.text = "Perimeter of Rectangle is " + str(ans) + " sq.units"
        except ValueError:
            self.rectangle_labelp.text = "Please Enter a Number"


class TriangleScreenarea(Screen):
    triangle_label = ObjectProperty(None)
    triangle_input1 = ObjectProperty(None)
    triangle_input2 = ObjectProperty(None)

    def ans_triangle_area(self):
        try:
            ans = 1 / 2 * float(self.triangle_input1.text) * float(self.triangle_input2.text)
            self.triangle_label.text = "Area of Triangle is " + str(ans) + " sq.units"
        except ValueError:
            self.triangle_label.text = "Please Enter a Number"


class TriangleScreen(Screen):
    triangle_labelp = ObjectProperty(None)
    triangle_input1p = ObjectProperty(None)
    triangle_input2p = ObjectProperty(None)
    triangle_input3p = ObjectProperty(None)

    def ans_triangle_peri(self):
        try:
            ans = float(self.triangle_input1p.text) + float(self.triangle_input2p.text) + float(
                self.triangle_input3p.text)
            self.triangle_labelp.text = "Perimeter of Triangle is " + str(ans) + " sq.uints"
        except ValueError:
            self.triangle_labelp.text = "Please Enter a Number"


class AreaApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_man)
        return screen


AreaApp().run()
