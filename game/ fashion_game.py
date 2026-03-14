import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time

class FashionGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.current_question = 0
        self.questions = []
        self.initUI()
        self.setupQuestions()
        self.showQuestion()

    def initUI(self):
        self.setWindowTitle('ЛЭЙМ ТЫ ИЛИ НЕТ?')
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #0a0a0a;
            }
            QLabel {
                color: white;
                font-family: 'Arial';
            }
            QPushButton {
                background-color: #333;
                color: white;
                border: 2px solid #555;
                border-radius: 10px;
                padding: 15px;
                font-size: 16px;
                font-weight: bold;
                min-width: 200px;
            }
            QPushButton:hover {
                background-color: #555;
                border-color: #777;
            }
            QPushButton:pressed {
                background-color: #777;
            }
        """)

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)
        self.layout.setSpacing(20)
        self.layout.setContentsMargins(40, 40, 40, 40)

        # Заголовок
        self.title_label = QLabel("ЛЭЙМ ТЫ ИЛИ НЕТ?")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("""
            font-size: 32px;
            font-weight: bold;
            color: #FFD700;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px #000000;
        """)
        self.layout.addWidget(self.title_label)

        # Область изображения
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setMinimumHeight(250)
        self.image_label.setStyleSheet("""
            border: 3px solid #444;
            border-radius: 15px;
            background-color: #1a1a1a;
        """)
        self.layout.addWidget(self.image_label)

        # Текст вопроса
        self.question_label = QLabel()
        self.question_label.setAlignment(Qt.AlignCenter)
        self.question_label.setWordWrap(True)
        self.question_label.setStyleSheet("""
            font-size: 20px;
            color: #FFFFFF;
            margin: 20px;
            padding: 15px;
            border-radius: 10px;
            background-color: rgba(50, 50, 50, 0.7);
        """)
        self.layout.addWidget(self.question_label)

        # Контейнер для кнопок
        self.buttons_container = QWidget()
        self.buttons_layout = QHBoxLayout(self.buttons_container)
        self.buttons_layout.setSpacing(30)
        self.layout.addWidget(self.buttons_container)

        # Кнопки выбора
        self.button1 = QPushButton()
        self.button1.clicked.connect(lambda: self.answer(1))
        self.buttons_layout.addWidget(self.button1)

        self.button2 = QPushButton()
        self.button2.clicked.connect(lambda: self.answer(2))
        self.buttons_layout.addWidget(self.button2)

        # Метка счета
        self.score_label = QLabel(f"Баллы: {self.score}")
        self.score_label.setAlignment(Qt.AlignCenter)
        self.score_label.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
            color: #00FF00;
            margin-top: 20px;
        """)
        self.layout.addWidget(self.score_label)

        # Прогресс
        self.progress_label = QLabel()
        self.progress_label.setAlignment(Qt.AlignCenter)
        self.progress_label.setStyleSheet("color: #888; font-size: 14px;")
        self.layout.addWidget(self.progress_label)

    def setupQuestions(self):
        self.questions = [
            {
                "image": "👟",
                "question": "Начнем с кроссовок, бро!\nВыбирай внимательно...",
                "option1": "BALENCIAGA RUNNER",
                "option2": "Adidas Samba",
                "points1": 2,
                "points2": 1,
                "response1": "Хороший выбор, ты настоящий игрок! 👟🔥",
                "response2": "Фу бл#ть, че за калжевал... 🤢"
            },
            {
                "image": "👖",
                "question": "Следующий этап - Штаны (джинсы)\nНе подведи нас!",
                "option1": "kappa pants",
                "option2": "Drugonit fluffy",
                "points1": 2,
                "points2": 5,
                "response1": "Братишка, я все понимаю, но купи мне новые глаза лучше 😵",
                "response2": "ООО, ГАД ДЭМН, отличный выбор! 👖🔥"
            },
            {
                "image": "🧥",
                "question": "Следующий этап - зипка\nНе просрись тут бро!",
                "option1": "VETEMENTS PENTOGRAMMA",
                "option2": "BAPE SHARK",
                "points1": 7,
                "points2": 4,
                "response1": "Да ты шаришь мужик, респект откинул! 🙏",
                "response2": "Бл#, ну если не фиолетовый то еще пойдет... 👕"
            }
        ]

    def showQuestion(self):
        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]
            
            # Устанавливаем изображение (эмодзи)
            self.image_label.setText(q["image"])
            self.image_label.setStyleSheet("""
                font-size: 100px;
                border: 3px solid #444;
                border-radius: 15px;
                background-color: #1a1a1a;
                padding: 20px;
            """)
            
            # Текст вопроса
            self.question_label.setText(q["question"])
            
            # Текст на кнопках
            self.button1.setText(f"1. {q['option1']}")
            self.button2.setText(f"2. {q['option2']}")
            
            # Обновляем прогресс
            self.progress_label.setText(f"Вопрос {self.current_question + 1}/{len(self.questions)}")
            
            # Обновляем счет
            self.score_label.setText(f"Баллы: {self.score}")
        else:
            self.showResult()

    def answer(self, choice):
        q = self.questions[self.current_question]
        
        if choice == 1:
            self.score += q["points1"]
            response = q["response1"]
        else:
            self.score += q["points2"]
            response = q["response2"]
        
        # Показываем ответ
        self.showResponse(response)
        
        # Переходим к следующему вопросу через 2 секунды
        QTimer.singleShot(2000, self.nextQuestion)

    def showResponse(self, response):
        # Временно меняем интерфейс для показа ответа
        self.button1.hide()
        self.button2.hide()
        self.question_label.setText(response)
        self.question_label.setStyleSheet("""
            font-size: 18px;
            color: #FFD700;
            margin: 20px;
            padding: 20px;
            border-radius: 10px;
            background-color: rgba(100, 50, 0, 0.3);
            border: 2px solid #FFD700;
        """)

    def nextQuestion(self):
        self.current_question += 1
        
        # Восстанавливаем обычный вид
        self.button1.show()
        self.button2.show()
        self.question_label.setStyleSheet("""
            font-size: 20px;
            color: #FFFFFF;
            margin: 20px;
            padding: 15px;
            border-radius: 10px;
            background-color: rgba(50, 50, 50, 0.7);
        """)
        
        self.showQuestion()

    def showResult(self):
        # Очищаем интерфейс
        for i in reversed(range(self.layout.count())): 
            widget = self.layout.itemAt(i).widget()
            if widget:
                widget.hide()
        
        # Показываем результат
        result_text = QLabel()
        result_text.setAlignment(Qt.AlignCenter)
        
        if self.score >= 8:
            result = "🎉 ПОЗДРАВЛЯЮ - ТЫ ИГРОК! 🎉"
            color = "#00FF00"
            emoji = "👑🔥💸"
        else:
            result = "😔 ТЫ ЛЭЙМ БРО... 😔"
            color = "#FF4444"
            emoji = "💀🚫👎"
        
        result_text.setText(f"""
            <div style='font-size: 36px; font-weight: bold; color: {color}; margin: 30px;'>
                {result}
            </div>
            <div style='font-size: 100px; margin: 30px;'>
                {emoji}
            </div>
            <div style='font-size: 28px; color: #FFD700; margin: 20px;'>
                Твой результат: {self.score} баллов
            </div>
            <div style='font-size: 18px; color: #AAAAAA; margin: 20px;'>
                {self.getResultDescription()}
            </div>
        """)
        
        # Кнопка для выхода
        exit_button = QPushButton("ВЫЙТИ ИЗ ИГРЫ")
        exit_button.clicked.connect(self.close)
        exit_button.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                padding: 20px;
                background-color: #333;
                color: white;
                border-radius: 15px;
                min-width: 300px;
            }
            QPushButton:hover {
                background-color: #555;
            }
        """)
        
        # Перезапуск игры
        restart_button = QPushButton("ИГРАТЬ СНОВА")
        restart_button.clicked.connect(self.restartGame)
        restart_button.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                padding: 20px;
                background-color: #2E8B57;
                color: white;
                border-radius: 15px;
                min-width: 300px;
            }
            QPushButton:hover {
                background-color: #3CB371;
            }
        """)
        
        # Размещаем элементы
        self.layout.addWidget(result_text)
        
        button_container = QWidget()
        button_layout = QVBoxLayout(button_container)
        button_layout.setSpacing(20)
        button_layout.addWidget(restart_button)
        button_layout.addWidget(exit_button)
        
        self.layout.addWidget(button_container)

    def getResultDescription(self):
        if self.score >= 12:
            return "Ты настоящий король стиля! Все твои выборы - огонь! 🔥"
        elif self.score >= 8:
            return "Неплохо, бро! Ты в теме, но есть куда расти 📈"
        elif self.score >= 5:
            return "Хм... нужно больше разбираться в моде, братишка 🤔"
        else:
            return "Эээ... может тебе стоит посмотреть пару модных блогов? 👀"

    def restartGame(self):
        self.score = 0
        self.current_question = 0
        
        # Восстанавливаем интерфейс
        for i in reversed(range(self.layout.count())): 
            widget = self.layout.itemAt(i).widget()
            if widget:
                widget.show()
        
        self.showQuestion()

def main():
    app = QApplication(sys.argv)
    
    # Устанавливаем стиль
    app.setStyle('Fusion')
    
    # Создаем и показываем окно
    game = FashionGame()
    game.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()