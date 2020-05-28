import os
import sys

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from DashboardItem import DashboardItem

from pyside_material import apply_stylesheet

class Dashboard(QWidget):
    def __init__(self, stacks, containers, images, volumes, networks):
        QWidget.__init__(self, None)

        # Setup Customize (Image)
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, 'images')

        stacks_path = os.path.join(path, 'stacks.png')
        containers_path = os.path.join(path, 'containers.png')
        images_path = os.path.join(path, 'images.png')
        volumes_path = os.path.join(path, 'volumes.png')
        networks_path = os.path.join(path, 'networks.png')

        self.stacks = DashboardItem(stacks, stacks_path, "Stacks")
        self.containers = DashboardItem(containers, containers_path, "Containers")
        self.images = DashboardItem(images, images_path, "Images")
        self.volumes = DashboardItem(volumes, volumes_path, "Volumes")
        self.networks = DashboardItem(networks, networks_path, "Networks")

        # Setup Qt
        self.label = QLabel('DASHBOARD')
        self.label.setStyleSheet('font-size: 16pt;')
    
        
        self.row1 = QHBoxLayout()
        self.row1.addWidget(self.label)
        self.row1.setAlignment(Qt.AlignLeft)

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.stacks)
        top_layout.addWidget(self.containers)

        mid_layout = QHBoxLayout()
        mid_layout.addWidget(self.images)
        mid_layout.addWidget(self.volumes)

        sub_layout = QVBoxLayout()
        sub_layout.addLayout(top_layout)
        sub_layout.addLayout(mid_layout)
        sub_layout.addWidget(self.networks)
        sub_layout.setSpacing(50)

        layout = QVBoxLayout(self)
        layout.addLayout(self.row1)
        layout.addLayout(sub_layout)
        layout.setAlignment(Qt.AlignTop)
        layout.setSpacing(150)

        