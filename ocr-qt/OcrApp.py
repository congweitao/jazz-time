import sys
import time

import cv2
import easyocr
from PyQt5 import uic, QtGui
from PyQt5.Qt import QLabel, QApplication, QPushButton, QWidget, QTextEdit, QProgressBar
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QToolBar, QMenu, QMenuBar, QAction


class ProgressBarThread(QThread):
    change_value_signal = pyqtSignal(int)
    finished_signal = pyqtSignal(str)

    def __init__(self):
        super(ProgressBarThread, self).__init__()

    def __del__(self):
        self.wait()

    @pyqtSlot()
    def run(self):
        for i in range(101):
            time.sleep(0.1)
            self.change_value_signal.emit(i)
        self.finished_signal.emit("finished()")


class OcrApp(QWidget):
    def __init__(self):
        super().__init__()

        self.window = uic.loadUi('ocr_app.ui')
        self.image_file = ''

        self.label = self.window.findChild(QLabel, 'labelImage')
        self.result_text = self.window.findChild(QTextEdit, 'textEdit')
        self.progress = self.window.findChild(QProgressBar, 'progressBar')

        self.menu = self.window.findChild(QMenu, 'menu')
        self.quit_action = QAction('&关闭', self)
        self.quit_icon = QtGui.QIcon()
        self.quit_icon.addPixmap(QtGui.QPixmap("exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.quit_action.setIcon(self.quit_icon)
        self.quit_action.setShortcut("Ctrl+X")
        self.quit_action.triggered.connect(self.window.close)
        self.menu.addAction(self.quit_action)

        self.action_quit = self.window.findChild(QAction, 'action_quit')
        self.action_quit.triggered.connect(self.window.close)
        self.action_open = self.window.findChild(QAction, 'action_open')
        self.action_open.triggered.connect(self.open_file_handler)
        self.action_save = self.window.findChild(QAction, 'action_save')
        self.action_save.triggered.connect(self.save)

        self.action_90 = self.window.findChild(QAction, 'action_90')
        self.action_90.triggered.connect(self.rotate_90)
        self.action_91 = self.window.findChild(QAction, 'action_91')
        self.action_91.triggered.connect(self.rotate_neg_90)

        self.btn_open_file = self.window.findChild(QPushButton, 'pushButtonOpenFile')
        self.btn_open_file.clicked.connect(self.open_file_handler)

        self.btn_detect = self.window.findChild(QPushButton, 'pushButtonDetect')
        self.btn_detect.clicked.connect(self.start_ocr_detection)

        self.window.show()

    def rotate_90(self):
        m_image = QPixmap(self.image_file)
        matrix = QTransform()
        matrix.rotate(90)
        m_image = m_image.transformed(matrix)
        self.label.setPixmap(QPixmap(m_image))

    def rotate_neg_90(self):
        m_image = QPixmap(self.image_file)
        matrix = QTransform()
        matrix.rotate(-90)
        m_image = m_image.transformed(matrix)
        self.label.setPixmap(QPixmap(m_image))

    def open_file_handler(self):
        '''自动调整图片，适合窗口显示'''
        self.image_file = QFileDialog.getOpenFileName(self, 'Open File', './', 'Images (*.png *.jpg)')[0]
        self.label.setPixmap(QPixmap(self.image_file))
        self.label.setScaledContents(True)
        # 初始化进度条
        self.step = 0
        self.progress.setValue(0)

    def start_ocr_detection(self):
        '''OCR算法优化，提取识别信息加以利用'''
        if self.image_file == '':
            '''log error： No image file is selected.'''
            QMessageBox.information(self, "警告", "No image file is selected.")
            return

        self.progress.setValue(50)
        img_obj = cv2.imread(self.image_file)
        img_obj_grey = cv2.cvtColor(img_obj, cv2.COLOR_BGR2GRAY)
        reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)

        tic = time.perf_counter()
        result = reader.readtext(img_obj_grey, detail=0)
        toc = time.perf_counter()
        self.progress.setValue(100)
        self.result_text.insertPlainText(f"消耗时间：  {toc - tic:0.2f} seconds, 识别信息: \n")
        '''处理识别的信息'''
        for res in result:
            self.result_text.insertPlainText(res)
        self.result_text.append('\n')

    def set_progress_value(self):
        '''
        分配另一个线程显示进度条
        '''
        self.thread = ProgressBarThread()
        self.thread.change_value_signal.connect(self.setProgressVal)
        self.thread.finished_signal.connect(self.done)
        self.thread.start()

    def setProgressVal(self, val):
        self.progress.setValue(val)

    def done(self):
        self.progress.setValue(100)
        QMessageBox.information(self, "Done!", "Done OCR Processing!")

    def save(self):
        save_file = 'log/test.log'
        txt = self.result_text.toPlainText()
        if save_file is not None:
            with open(file=save_file, mode='a+', encoding='utf-8') as file:
                file.write(txt)
        print('saved.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    exe = OcrApp()
    sys.exit(app.exec_())
