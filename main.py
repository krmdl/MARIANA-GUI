import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QTabWidget, QLabel, QPushButton, 
                           QGridLayout, QGroupBox, QFrame, QSplitter)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QPalette, QColor, QIcon, QPixmap, QPainter, QBrush, QPen

class ModernButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton:pressed {
                background-color: #0D47A1;
            }
        """)

class ModernGroupBox(QGroupBox):
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.setStyleSheet("""
            QGroupBox {
                background-color: #FFFFFF;
                border: 2px solid #E0E0E0;
                border-radius: 8px;
                margin-top: 1em;
                padding: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
                color: #424242;
                font-weight: bold;
            }
        """)

class MarianaIcon(QIcon):
    def __init__(self):
        super().__init__()
        # Create different sizes of the icon
        sizes = [16, 32, 48, 64, 128, 256]
        for size in sizes:
            pixmap = QPixmap(size, size)
            pixmap.fill(Qt.transparent)
            
            painter = QPainter(pixmap)
            painter.setRenderHint(QPainter.Antialiasing)
            
            # Draw background circle
            painter.setBrush(QBrush(QColor("#2196F3")))
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(0, 0, size, size)
            
            # Draw "M" letter
            painter.setPen(QPen(Qt.white, size//8, Qt.SolidLine))
            font = QFont("Arial")
            font.setPointSize(size//2)
            font.setBold(True)
            painter.setFont(font)
            painter.drawText(pixmap.rect(), Qt.AlignCenter, "M")
            
            painter.end()
            self.addPixmap(pixmap)

class AUVControlSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MARIANA Control System")
        self.setGeometry(100, 100, 1600, 900)
        self.setWindowIcon(MarianaIcon())
        self.setStyleSheet("""
            QMainWindow {
                background-color: #F5F5F5;
            }
            QTabWidget::pane {
                border: 1px solid #E0E0E0;
                border-radius: 5px;
                background-color: #FFFFFF;
            }
            QTabBar::tab {
                background-color: #E0E0E0;
                color: #424242;
                padding: 8px 20px;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }
            QTabBar::tab:selected {
                background-color: #2196F3;
                color: white;
            }
            QLabel {
                color: #424242;
            }
        """)
        
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)
        
        # Create main splitter
        main_splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(main_splitter)
        
        # Create left panel (Telemetry and Controls)
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(0, 0, 0, 0)
        
        # Create telemetry section
        telemetry_frame = QFrame()
        telemetry_frame.setStyleSheet("""
            QFrame {
                background-color: #FFFFFF;
                border-radius: 10px;
                border: 2px solid #E0E0E0;
            }
        """)
        telemetry_layout = QGridLayout(telemetry_frame)
        telemetry_layout.setSpacing(15)
        
        # Create telemetry indicators
        indicators = [
            ("Depth", "0.0 m", "#2196F3"),
            ("Heading", "0°", "#4CAF50"),
            ("Pitch/Roll", "0°/0°", "#FF9800"),
            ("Altitude", "0.0 m", "#9C27B0"),
            ("Battery", "100%", "#F44336"),
            ("Link Quality", "Good", "#00BCD4"),
            ("Speed", "0.0 m/s", "#795548"),
            ("GPS", "Not Available", "#607D8B"),
            ("Mode", "STABILIZE", "#E91E63"),
            ("Mission Status", "Waiting", "#3F51B5")
        ]
        
        for i, (label, value, color) in enumerate(indicators):
            group = ModernGroupBox(label)
            group_layout = QVBoxLayout()
            
            value_label = QLabel(value)
            value_label.setAlignment(Qt.AlignCenter)
            value_label.setFont(QFont('Arial', 14, QFont.Bold))
            value_label.setStyleSheet(f"color: {color};")
            
            group_layout.addWidget(value_label)
            group.setLayout(group_layout)
            telemetry_layout.addWidget(group, i // 2, i % 2)
        
        left_layout.addWidget(telemetry_frame)
        
        # Create controls section
        controls_frame = QFrame()
        controls_frame.setStyleSheet("""
            QFrame {
                background-color: #FFFFFF;
                border-radius: 10px;
                border: 2px solid #E0E0E0;
                padding: 10px;
            }
        """)
        controls_layout = QGridLayout(controls_frame)
        controls_layout.setSpacing(10)
        
        # Create control buttons
        buttons = [
            ("Arm/Disarm Motors", "#F44336"),
            ("Start/Stop Mission", "#4CAF50"),
            ("Change Mode", "#2196F3"),
            ("Surface", "#FF9800"),
            ("Depth Hold", "#9C27B0"),
            ("Yaw Hold", "#00BCD4"),
            ("Camera Control", "#795548")
        ]
        
        for i, (button_text, color) in enumerate(buttons):
            btn = ModernButton(button_text)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {color};
                    color: white;
                    border: none;
                    padding: 15px 25px;
                    border-radius: 5px;
                    font-weight: bold;
                    font-size: 14px;
                }}
                QPushButton:hover {{
                    background-color: {color}DD;
                }}
                QPushButton:pressed {{
                    background-color: {color}AA;
                }}
            """)
            controls_layout.addWidget(btn, i // 2, i % 2)
        
        left_layout.addWidget(controls_frame)
        main_splitter.addWidget(left_panel)
        
        # Create right panel (Logo, Camera and Map)
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(15)
        
        # Create logo section
        logo_frame = QFrame()
        logo_frame.setStyleSheet("""
            QFrame {
                background-color: #FFFFFF;
                border-radius: 10px;
                border: 2px solid #E0E0E0;
                padding: 10px;
            }
        """)
        logo_layout = QVBoxLayout(logo_frame)
        
        # Create a stylized logo using text and shapes
        logo_label = QLabel("MARIANA CONTROL SYSTEM")
        logo_label.setAlignment(Qt.AlignCenter)
        logo_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 28px;
                font-weight: bold;
                padding: 15px;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #2196F3, stop:1 #00BCD4);
                border-radius: 5px;
            }
        """)
        logo_layout.addWidget(logo_label)
        
        # Add a decorative line
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("background-color: #2196F3;")
        line.setFixedHeight(2)
        logo_layout.addWidget(line)
        
        right_layout.addWidget(logo_frame)
        
        # Create camera section
        camera_frame = QFrame()
        camera_frame.setStyleSheet("""
            QFrame {
                background-color: #000000;
                border-radius: 10px;
                border: 2px solid #E0E0E0;
            }
        """)
        camera_layout = QVBoxLayout(camera_frame)
        
        camera_view = QLabel("Camera View")
        camera_view.setAlignment(Qt.AlignCenter)
        camera_view.setStyleSheet("color: white; font-size: 16px;")
        camera_view.setMinimumHeight(400)
        camera_layout.addWidget(camera_view)
        
        # Camera controls
        camera_controls = QHBoxLayout()
        camera_controls.setSpacing(10)
        
        for btn_text in ["Start Recording", "Stop Recording", "Take Snapshot"]:
            btn = ModernButton(btn_text)
            camera_controls.addWidget(btn)
        
        camera_layout.addLayout(camera_controls)
        right_layout.addWidget(camera_frame)
        
        # Create map section
        map_frame = QFrame()
        map_frame.setStyleSheet("""
            QFrame {
                background-color: #FFFFFF;
                border-radius: 10px;
                border: 2px solid #E0E0E0;
            }
        """)
        map_layout = QVBoxLayout(map_frame)
        
        map_view = QLabel("Map View")
        map_view.setAlignment(Qt.AlignCenter)
        map_view.setStyleSheet("color: #424242; font-size: 16px;")
        map_view.setMinimumHeight(200)
        map_layout.addWidget(map_view)
        
        right_layout.addWidget(map_frame)
        main_splitter.addWidget(right_panel)
        
        # Set initial splitter sizes
        main_splitter.setSizes([600, 1000])
        
        # Create status bar
        self.statusBar().showMessage("System Ready")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Set application-wide font
    font = QFont("Segoe UI", 10)
    app.setFont(font)
    
    window = AUVControlSystem()
    window.show()
    sys.exit(app.exec_())
