import psycopg2
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QTabWidget, QAbstractScrollArea,
                             QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox,
                             QTableWidgetItem, QPushButton, QMessageBox)


def day(d):
    if d == 0:
        daytxt = "Понедельник"
    elif d == 1:
        daytxt = "Вторник"
    elif d == 2:
        daytxt = "Среда"
    elif d == 3:
        daytxt = "Четверг"
    elif d == 4:
        daytxt = "Пятница"
    elif d == 5:
        daytxt = "Суббота"
    else:
        daytxt = "Ошибка"
    return (daytxt)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self._connect_to_db()

        self.setWindowTitle("Schedule")

        self.vbox = QVBoxLayout(self)

        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)

        self._create_shedule_tab()
        self._create_teacher_tab()
        self._create_subject_tab()

    def _connect_to_db(self):
        self.conn = psycopg2.connect(database="tgbot_db",
                                     user="postgres",
                                     password="1804#Mtn",
                                     host="localhost",
                                     port="5432")

        self.cursor = self.conn.cursor()

    def _create_shedule_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "Расписание")

        self.day_gbox = [QGroupBox(day(var1)) for var1 in range(6)]
        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)
        for var2 in range(6):
            self.shbox1.addWidget(self.day_gbox[var2])
        self.day_table = [QTableWidget() for var3 in range(6)]
        self._create_day_table()

        self.update_shedule_button = QPushButton("Обновить информацию о расписании")
        self.shbox2.addWidget(self.update_shedule_button)
        self.update_shedule_button.clicked.connect(self._update_shedule)

        self.shedule_tab.setLayout(self.svbox)

    def _create_day_table(self):
        count = 0
        while count <= 5:
            self.day_table[count].setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
            self.day_table[count].setColumnCount(8)
            self.day_table[count].setHorizontalHeaderLabels(
                ["id записи", "Предмет", "Время", "Кабинет", "Неделя", "Учитель", "", ""])
            self._update_day_table(count)
            self.mvbox = QVBoxLayout()
            self.mvbox.addWidget(self.day_table[count])
            self.day_gbox[count].setLayout(self.mvbox)
            count += 1

    def _update_day_table(self, count):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"SELECT * FROM timetable WHERE day='{day(count)}'")
        records = list(self.cursor.fetchall())

        self.day_table[count].setRowCount(len(records) + 1)
        if records:
            for i, r in enumerate(records):
                r = list(r)
                joinButton = QPushButton("Изменить/\nДобавить")
                deleteButton = QPushButton("Удалить")

                self.day_table[count].setItem(i, 0,
                                              QTableWidgetItem(str(r[0])))
                self.day_table[count].setItem(i, 1,
                                              QTableWidgetItem(str(r[2])))
                self.day_table[count].setItem(i, 2,
                                              QTableWidgetItem(str(r[4])))
                self.day_table[count].setItem(i, 3,
                                              QTableWidgetItem(str(r[3])))
                self.day_table[count].setItem(i, 4,
                                              QTableWidgetItem(str(r[5])))
                self.cursor = self.conn.cursor()
                self.cursor.execute(f"SELECT * FROM teacher WHERE subject='{r[2]}'")
                records1 = list(self.cursor.fetchall())
                if records1:
                    self.TabItem = QTableWidgetItem(records1[0][1])
                    self.TabItem.setFlags(QtCore.Qt.ItemIsEditable)
                    self.day_table[count].setItem(i, 5, self.TabItem)
                else:
                    self.TabItem = QTableWidgetItem("У предмета нет преподавателя")
                    self.TabItem.setFlags(QtCore.Qt.ItemIsEditable)
                    self.day_table[count].setItem(i, 5, self.TabItem)
                self.day_table[count].setCellWidget(i, 6, joinButton)
                self.day_table[count].setCellWidget(i, 7, deleteButton)
                joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num, count))
                deleteButton.clicked.connect(lambda ch, num=i: self._delete_day_from_table(num, count))
        else:
            for i in range(1):
                joinButton = QPushButton("Добавить")
                deleteButton = QPushButton("Нельзя\nудалить")

                self.day_table[count].setItem(i, 0,
                                              QTableWidgetItem("Создать ID"))
                self.day_table[count].setItem(i, 1,
                                              QTableWidgetItem("Добавить предмет"))
                self.day_table[count].setItem(i, 2,
                                              QTableWidgetItem("Добавить кабинет"))
                self.day_table[count].setItem(i, 3,
                                              QTableWidgetItem("Добавить время"))
                self.day_table[count].setItem(i, 4,
                                              QTableWidgetItem("Добавить неделю"))
                self.day_table[count].setCellWidget(i, 6, joinButton)
                self.day_table[count].setCellWidget(i, 7, deleteButton)
                joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num, count))
        self.day_table[count].resizeRowsToContents()

    def _change_day_from_table(self, rowNum, count):
        row = list()
        for i in range(self.day_table[count].columnCount()):
            try:
                row.append(self.day_table[count].item(rowNum, i).text())
            except:
                row.append(None)
        try:
            test = int(row[0])
            try:
                self.cursor = self.conn.cursor()
                self.cursor.execute(f"SELECT * FROM timetable WHERE id = {row[0]}")
                records = list(self.cursor.fetchall())
                if records:
                    self.cursor = self.conn.cursor()
                    self.cursor.execute(
                        f"UPDATE timetable SET subject = '{row[1]}', start_time = '{row[2]}', room_numb = '{row[3]}', week = '{row[4]}' WHERE id = {row[0]}")
                    self.conn.commit()
                else:
                    self.cursor = self.conn.cursor()
                    self.cursor.execute(
                        f"INSERT INTO timetable(day,subject, start_time, room_numb, week, id) VALUES ('{day(count)}','{row[1]}','{row[2]}','{row[3]}','{row[4]}',{row[0]}) ")
                    self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Enter all fields in right format")
        except:
            QMessageBox.about(self, "Error", "id NAN")

    def _delete_day_from_table(self, rowNum, count):
        row = list()
        for i in range(self.day_table[count].columnCount()):
            try:
                row.append(self.day_table[count].item(rowNum, i).text())
            except:
                row.append(None)

        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"DELETE FROM timetable WHERE id = {row[0]}")
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "IDK")

    def _update_shedule(self):
        count = 0
        while count <= 5:
            self._update_day_table(count)
            count += 1
#
# teachers
#
    def _create_teacher_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "Учителя")
        self.teacher_gbox = QGroupBox()
        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)

        self.shbox1.addWidget(self.teacher_gbox)
        self.teacher_table = QTableWidget()
        self._create_teacher_table()

        self.update_teacher_button = QPushButton("Обновить информацию об учителях")
        self.shbox2.addWidget(self.update_teacher_button)
        self.update_teacher_button.clicked.connect(self._update_teacher)

        self.shedule_tab.setLayout(self.svbox)
    def _create_teacher_table(self):
        self.teacher_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.teacher_table.setColumnCount(5)
        self.teacher_table.setHorizontalHeaderLabels(
            ["id записи", "Полное имя", "Предмет", "", ""])
        self._update_teacher_table()
        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.teacher_table)
        self.teacher_gbox.setLayout(self.mvbox)

    def _update_teacher_table(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"SELECT * FROM teacher")
        records = list(self.cursor.fetchall())

        self.teacher_table.setRowCount(len(records) + 1)
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Изменить/\nДобавить")
            deleteButton = QPushButton("Удалить")

            self.teacher_table.setItem(i, 0,
                                          QTableWidgetItem(str(r[0])))
            self.teacher_table.setItem(i, 1,
                                          QTableWidgetItem(str(r[1])))
            self.teacher_table.setItem(i, 2,
                                          QTableWidgetItem(str(r[2])))
            self.teacher_table.setCellWidget(i, 3, joinButton)
            self.teacher_table.setCellWidget(i, 4, deleteButton)
            joinButton.clicked.connect(lambda ch, num=i: self._change_teacher_from_table(num))
            deleteButton.clicked.connect(lambda ch, num=i: self._delete_teacher_from_table(num))

        joinButton1 = QPushButton("Добавить")
        deleteButton1 = QPushButton("Нельзя\nудалить")

        self.teacher_table.setItem(len(records), 0,
                                      QTableWidgetItem("Создать ID"))
        self.teacher_table.setItem(len(records), 1,
                                      QTableWidgetItem("Добавить имя"))
        self.teacher_table.setItem(len(records), 2,
                                      QTableWidgetItem("Добавить предмет"))
        self.teacher_table.setCellWidget(len(records), 3, joinButton1)
        self.teacher_table.setCellWidget(len(records), 4, deleteButton1)
        joinButton1.clicked.connect(lambda ch, num=len(records): self._change_teacher_from_table(num))
        self.teacher_table.resizeRowsToContents()

    def _change_teacher_from_table(self, rowNum):
        row = list()
        for i in range(self.teacher_table.columnCount()):
            try:
                row.append(self.teacher_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            test = int(row[0])
            try:
                self.cursor = self.conn.cursor()
                self.cursor.execute(f"SELECT * FROM teacher WHERE id = {row[0]}")
                records = list(self.cursor.fetchall())
                if records:
                    self.cursor = self.conn.cursor()
                    self.cursor.execute(
                        f"UPDATE teacher SET subject = '{str(row[2])}', full_name = '{str(row[1])}', WHERE id = {row[0]}")
                    self.conn.commit()
                else:
                    self.cursor = self.conn.cursor()
                    self.cursor.execute(
                        f"INSERT INTO teacher(subject, full_name, id) VALUES ('{str(row[2])}','{str(row[1])}','{row[0]}') ")
                    self.conn.commit()
            except:
                QMessageBox.about(self, "Error", "Enter all fields in right format")
        except:
            QMessageBox.about(self, "Error", "id NAN")

    def _delete_teacher_from_table(self, rowNum):
        row = list()
        for i in range(self.teacher_table.columnCount()):
            try:
                row.append(self.teacher_table.item(rowNum, i).text())
            except:
                row.append(None)

        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"DELETE FROM timetable WHERE subject = '{row[2]}';")
            self.cursor.execute(f"DELETE FROM teacher WHERE id = {row[0]}")
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "IDK")

    def _update_teacher(self):
        self._update_teacher_table()
#
#
#
    def _create_subject_tab(self):
        self.shedule_tab = QWidget()
        self.tabs.addTab(self.shedule_tab, "Предметы")
        self.subject_gbox = QGroupBox()
        self.svbox = QVBoxLayout()
        self.shbox1 = QHBoxLayout()
        self.shbox2 = QHBoxLayout()
        self.svbox.addLayout(self.shbox1)
        self.svbox.addLayout(self.shbox2)

        self.shbox1.addWidget(self.subject_gbox)
        self.subject_table = QTableWidget()
        self._create_subject_table()

        self.update_subject_button = QPushButton("Обновить информацию о предметах")
        self.shbox2.addWidget(self.update_subject_button)
        self.update_subject_button.clicked.connect(self._update_subject)

        self.shedule_tab.setLayout(self.svbox)
    def _create_subject_table(self):
        self.subject_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.subject_table.setColumnCount(3)
        self.subject_table.setHorizontalHeaderLabels(
            ["Имя предмета", "", ""])
        self._update_subject_table()
        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.subject_table)
        self.subject_gbox.setLayout(self.mvbox)

    def _update_subject_table(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"SELECT * FROM subject")
        records = list(self.cursor.fetchall())

        self.subject_table.setRowCount(len(records) + 1)
        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Изменить/\nДобавить")
            deleteButton = QPushButton("Удалить")

            self.subject_table.setItem(i, 0,
                                          QTableWidgetItem(str(r[0])))
            self.subject_table.setCellWidget(i, 1, joinButton)
            self.subject_table.setCellWidget(i, 2, deleteButton)
            joinButton.clicked.connect(lambda ch, num=i: self._change_subject_from_table(num))
            deleteButton.clicked.connect(lambda ch, num=i: self._delete_subject_from_table(num))

        joinButton1 = QPushButton("Добавить")
        deleteButton1 = QPushButton("Нельзя\nудалить")

        self.subject_table.setItem(len(records), 0,
                                      QTableWidgetItem("Создать ID"))
        self.subject_table.setCellWidget(len(records), 1, joinButton1)
        self.subject_table.setCellWidget(len(records), 2, deleteButton1)
        joinButton1.clicked.connect(lambda ch, num=len(records): self._change_subject_from_table(num))
        self.subject_table.resizeRowsToContents()

    def _change_subject_from_table(self, rowNum):
        row = list()
        for i in range(self.subject_table.columnCount()):
            try:
                row.append(self.subject_table.item(rowNum, i).text())
            except:
                row.append(None)
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(
                f"INSERT INTO subject VALUES ('{row[0]}') ")
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Enter all fields in right format")

    def _delete_subject_from_table(self, rowNum):
        row = list()
        for i in range(self.subject_table.columnCount()):
            try:
                row.append(self.subject_table.item(rowNum, i).text())
            except:
                row.append(None)

        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"DELETE FROM timetable WHERE subject = '{row[0]}';")
            self.cursor.execute(f"DELETE FROM teacher WHERE subject = '{row[0]}';")
            self.cursor.execute(f"DELETE FROM subject WHERE name = '{row[0]}'")
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "IDK")

    def _update_subject(self):
        self._update_subject_table()


app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
