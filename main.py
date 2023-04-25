#Quantos monitores: xrandr -d :0 -q | grep ' connected' | wc -l
#Dump da config: dconf dump /org/cinnamon/
# sudo apt install libcairo2-dev libgirepository1.0-dev
# echo $XDG_CURRENT_DESKTOP == X-Cinnamon
import gi
import os

desktop = os.getenv('XDG_CURRENT_DESKTOP')
print(desktop)

if desktop == 'X-Cinnamon':
    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk

    win = Gtk.Window()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
print("Not running Cinnamon, quitting now...")