# programa para explicar como criar um aplicativo de desenho no kivy
     
# import kivy module    
import kivy  
       
# a classe base de seu aplicativo herda da classe de aplicativo.   
# app:always se refere à instância de seu aplicativo  
from kivy.app import App 
     
# isso restringe a versão kivy, ou seja
# abaixo desta versão kivy você não pode
# use o aplicativo ou software
kivy.require('1.9.0') 
 
# Widgets são elementos de um
# interface gráfica do usuário que
# fazem parte da User Experience.
from kivy.uix.widget import Widget
 
# Este layout permite que você defina coordenadas relativas para crianças.
from kivy.uix.relativelayout import RelativeLayout
 
# Crie a classe Widget
class Paint_brush(Widget):
    pass
 
# Crie a classe de layout
# onde você está definindo o funcionamento de
# Paint_brush() class
class Drawing(RelativeLayout):
 
    # Ao pressionar o mouse como Paint_brush se comporta
    def on_touch_down(self, touch):
        pb = Paint_brush()
        pb.center = touch.pos
        self.add_widget(pb)
         
    # No movimento do mouse, como o Paint_brush se comporta
    def on_touch_move(self, touch):
        pb = Paint_brush()
        pb.center = touch.pos
        self.add_widget(pb)
 
#  Crie a classe App
class DrawingChongolaApp(App):
    def build(self):
        return Drawing()
 
DrawingChongolaApp().run()