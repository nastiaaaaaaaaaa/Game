from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import QPixmap 
import os 
 
from PIL import Image, ImageFilter 
 
app = QApplication([]) 
 
win = QWidget() 
win.resize(700,500) 
win.setWindowTitle('Easy Editor') 
win.show() 
 
 
btn_file = QPushButton('Folder') 
btn_left = QPushButton('Left') 
btn_right = QPushButton('Right') 
btn_mirror = QPushButton('Mirror') 
btn_sharp = QPushButton('Sharp') 
btn_blur = QPushButton('Blur') 
btn_black_white = QPushButton('B/W') 
 
lbl_picture = QLabel('Picture') 
 
list_file = QListWidget() 
 
v1 = QVBoxLayout() 
v2 = QVBoxLayout() 
h1 = QHBoxLayout() 
h2 = QHBoxLayout() 
main_layout = QHBoxLayout() 
 
v1.addWidget(btn_file) 
v1.addWidget(list_file) 
 
h1.addWidget(btn_left) 
h1.addWidget(btn_right) 
h1.addWidget(btn_mirror) 
h1.addWidget(btn_sharp) 
h1.addWidget(btn_black_white) 
 
h2.addWidget(btn_blur) 
 
v2.addWidget(lbl_picture) 
v2.addLayout(h1) 
v2.addLayout(h2) 
 
main_layout.addLayout(v1) 
main_layout.addLayout(v2) 
win.setLayout(main_layout) 
 
#===================================================================================================== 
# змінна для збереження імені папки 
#===================================================================================================== 
 
workdir = '' 
 
def chooseWorkgir(): 
    global workdir 
    workdir = QFileDialog.getExistingDirectory() 
 
def filter(filenames, extensions): 
    result = [] 
    for filename in filenames: 
        for ext in extensions: 
            if filename.endswith(ext): 
                result.append(filename) 
        return result 
     
def showfilenamesList(): 
    chooseWorkgir() 
    extensions = ['.jpg', '.png', 'jpeg', '.bpm', '.git'] 
    filenames = filter(os.listdir(workdir), extensions) 
    list_file.clear() 
    for file in filenames: 
        list_file.addItem(file) 
 
class ImageProcessor(): 
    def __init__(self): 
        self.image = None 
        self.filename = None 
        self.dir = None 
        self.savedir = 'Modified/' 
 
    def loadImage(self, filename, dir): 
        self.filename = filename 
        self.dir = dir 
        image_path = os.path.join(dir, filename) 
        self.image = Image.open(image_path) 
 
    def showImage(self): 
        temp_image_path = os.path.join(workdir,self.savedir, self.filename) 
        pixmapimage = QPixmap(temp_image_path) 
        w = lbl_picture.width() 
        h = lbl_picture.height() 
        pixmapimage = pixmapimage.scaled(w,h,Qt.KeepAspectRatio) 
        lbl_picture.setPixmap(pixmapimage) 
 
    def saveImage(self): 
        path = os.path.join(workdir, self.savedir) 
        if not os.path.exists(path): 
            os.mkdir(path) 
        image_path = os.path.join(path, self.savedir) 
        self.image.save(image_path)

    def do_bw(self):
        self.image =  self.image.convert('L')
        self.saveImage()
        self.showImage()

    def do_mirror(self):
        self.image = self.image.tranapose(Image.FLIP.LEFT_RIGHT)
        self.saveImage()
        self.showImage()
    
    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        self.showImage()

    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        self.showImage()
        

    def do_sharp(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        self.showImage()


    def do_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        self.showImage()
 
app.exec_()

    # Update display and control the frame rate
    display.update()
    clock.tick(FPS)
