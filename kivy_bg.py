from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder


Builder.load_string('''
<GridLayout>
    canvas.before:
        BorderImage:
            # BorderImage behaves like the CSS BorderImage
            border: 10, 10, 10, 10
            source: '/usr/share/kivy-examples/widgets/sequenced_images/data/images/button_white.png'
            pos: self.pos
            size: self.size

<RootWidget>
    GridLayout:
        size_hint: .9, .9
        pos_hint: {'center_x': .5, 'center_y': .5}
        rows:1
        Slider:
            orientation: 'vertical'
            max: 200
            padding: 50
        Label:
            text: '< Couleur & intensite >'
            text_size: self.width-20, self.height-20
            valign: 'middle'
            halign: 'center'
        Slider:
            orientation: 'vertical'
            max: 200
            padding: 50
    FloatLayout:
        Label:
            text: "Gestion lumiere salon"
            text_size: self.width-20, self.height-20
            size: self.texture_size
            pos_hint: {'x':.40, 'y':.0}


''')

class RootWidget(FloatLayout):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MainApp().run()
