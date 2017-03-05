import sys
import gtk

from dialog import MainWindow
from model.ImagePortion import ImagePortion

def help():
    print "usage"
    print "%s path-to-image" % sys.argv[0]

def main():
    if len(sys.argv) != 2:
        help()
        return 1
    else:
        path = sys.argv[1]
    
    pixmap    = gtk.gdk.pixbuf_new_from_file(path)
    selection = ImagePortion(pixmap.get_width(), pixmap.get_height())
    if 1:
        selection.x0.set(100)
        selection.y0.set(200)
        selection.x1.set(100 + 640)
        selection.y1.set(200 + 480)
        selection.aspectratio = 640/480.

    app = MainWindow(path, pixmap, selection)
    app.run()

    return 0

if __name__ == '__main__':
    sys.exit(main())
