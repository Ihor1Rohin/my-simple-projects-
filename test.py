import hashlib
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import os

class win(QMainWindow):
    def __init__(self):
        super(win,self).__init__()

        self.setWindowTitle("Rudko")
        self.setGeometry(600, 500, 700, 400)
        self.text = QtWidgets.QLabel(self)
        #self.text.setText("BAVOVNA")
        self.text.move(100, 100)
        self.text.adjustSize()

        self.but = QtWidgets.QPushButton(self)
        self.but.move(175, 150)
        self.but.setText("hash")
        self.but.clicked.connect(self.btn)

        self.hash = QtWidgets.QLabel(self)
        self.hash.move(200, 0)
        self.hash.setText("Введіть строку")

        self.ent= QtWidgets.QLineEdit(self)
        self.ent.move(175,25)
        self.res=QtWidgets.QLabel(self)
        self.res.move(300,300)

        self.lab_file=QtWidgets.QLabel(self)
        self.lab_file.move(100,60)
        self.lab_file.setText("Оберіть файл:")

        self.btn_search= QtWidgets.QPushButton(self)
        self.btn_search.move(175,60)
        self.btn_search.setText("File choose")
        self.btn_search.clicked.connect(lambda: self.o_f())

        self.lab_file = QtWidgets.QLabel(self)
        self.lab_file.move(100, 100)
        self.lab_file.setText("Оберіть фото:")
        self.btn_search = QtWidgets.QPushButton(self)
        self.btn_search.move(175, 100)
        self.btn_search.setText("Оберіть фото")
        self.btn_search.clicked.connect(lambda: self.pic())

        self.file_hash=QtWidgets.QLabel(self)
        self.file_hash.move(300, 60)

        self.pic_hash= QtWidgets.QLabel(self)
        self.pic_hash.move(300, 120)

    def pic(self):
        p_o = QtWidgets.QFileDialog.Options()
        p_o |= QtWidgets.QFileDialog.ReadOnly
        pic_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Бяк бяк", "",
                                                            "Усі типи даних (*);;Картинки(*.png *.jpg *.jpeg *.bmp)",
                                                            options=p_o)
        if pic_name:
            print("picked photo", pic_name)

            h_sha = hashlib.sha256()
            h_md5 = hashlib.md5()
            with open(pic_name, "rb") as photo_file:
                chunk = photo_file.read(8192)
                while chunk:
                    h_sha.update(chunk)
                    h_md5.update(chunk)
                    chunk = photo_file.read(8192)

            pic_hash_text = "З картинки: {} буде хеш:\n sha256: {}\n md5: {}".format(pic_name, h_sha.hexdigest(),
                                                                                     h_md5.hexdigest())
            self.pic_hash.setText(pic_hash_text)
            self.pic_hash.adjustSize()

    def btn(self):
        hash_text=self.ent.text()
        print("text=",hash_text)
        h_sha = hashlib.sha256()
        h_md5= hashlib.md5()
        h_sha.update(hash_text.encode("utf-8"))
        h_md5.update(hash_text.encode("utf-8"))
        print(h_sha.hexdigest())
        print(h_md5.hexdigest())

        self.hash.setText("З тексту: {} буде хеш: sha256: {}\n md5: {}".format(hash_text,h_sha.hexdigest(),h_md5.hexdigest()))
        self.hash.move(300,20)
        self.hash.adjustSize()

    def o_f(self):
        f_o = QtWidgets.QFileDialog.Options()
        f_o |= QtWidgets.QFileDialog.ReadOnly
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Виберіть файл", "", "Всі файли (*);;Текстові файли (*.txt);;Документи Word (*.docx)", options=f_o)
        if file_name:
            print("picked", file_name)
            h_sha = hashlib.sha256()
            h_md5 = hashlib.md5()
            buffer_size = 8192
            with open(file_name, "rb") as text_file:
                chunk_file = text_file.read(buffer_size)
                while chunk_file:
                    h_sha.update(chunk_file)
                    h_md5.update(chunk_file)
                    chunk_file = text_file.read(buffer_size)

            file_hash_text = "З файлу: {} буде хеш:\n sha256: {}\n md5: {}".format(file_name, h_sha.hexdigest(), h_md5.hexdigest())
            self.file_hash.setText(file_hash_text)
            self.file_hash.adjustSize()

def app():
        app =  QApplication(sys.argv)
        window =win()
        window.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    app()











