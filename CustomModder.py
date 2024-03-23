import tkinter as tk
from tkinter import messagebox
import platform
import psutil 
import os

class CustomModderApp:
    def __init__(self, master):
        self.master = master
        master.title("CustomModder")

        self.create_buttons()
        
    def create_buttons(self):
        self.create_button("Overclock CPU", self.overclock_cpu)
        self.create_button("Change GPU settings", self.change_gpu_settings)
        self.create_button("Modify fan speed", self.modify_fan_speed)
        self.create_button("Monitor System Info", self.monitor_system_info)
        self.create_button("Control RGB Lighting", self.control_rgb_lighting)
        self.create_button("Adjust Power Settings", self.adjust_power_settings)
        self.create_button("Disk Management", self.disk_management)
        self.create_button("Network Monitoring", self.network_monitoring)
        self.create_button("Advanced Fan Control", self.advanced_fan_control)
        self.create_button("Settings Menu", self.settings_menu)
        self.create_button("Exit", self.master.quit)
    
    def create_button(self, text, command):
        button = tk.Button(self.master, text=text, command=command, width=20)
        button.pack(pady=5)
    
    def overclock_cpu(self):
        # Functionality for overclocking CPU
        messagebox.showinfo("Overclock CPU", "Overclock CPU functionality not implemented yet.")
    
    def change_gpu_settings(self):
        # Functionality for changing GPU settings
        messagebox.showinfo("Change GPU Settings", "Change GPU settings functionality not implemented yet.")
    
    def modify_fan_speed(self):
        # Functionality for modifying fan speed
        messagebox.showinfo("Modify Fan Speed", "Modify fan speed functionality not implemented yet.")
    
    def monitor_system_info(self):
        # Functionality for monitoring system information
        info = f"Operating System: {platform.system()} {platform.release()}\n"
        info += f"CPU Usage: {psutil.cpu_percent()}%\n"
        info += f"Memory Usage: {psutil.virtual_memory().percent}%\n"
        info += f"Disk Usage: {psutil.disk_usage('/').percent}%"
        messagebox.showinfo("System Information", info)
    
    def control_rgb_lighting(self):
        # Functionality for controlling RGB lighting
        messagebox.showinfo("Control RGB Lighting", "Control RGB lighting functionality not implemented yet.")
    
    def adjust_power_settings(self):
        # Functionality for adjusting power settings
        messagebox.showinfo("Adjust Power Settings", "Adjust power settings functionality not implemented yet.")
    
    def disk_management(self):
        # Functionality for disk management
        if platform.system() == "Windows":
            os.system("diskmgmt.msc")
        else:
            messagebox.showinfo("Disk Management", "Disk management tools not available on this platform.")
    
    def network_monitoring(self):
        # Functionality for network monitoring
        messagebox.showinfo("Network Monitoring", "Network monitoring functionality not implemented yet.")
    
    def advanced_fan_control(self):
        # Functionality for advanced fan control
        messagebox.showinfo("Advanced Fan Control", "Advanced fan control functionality not implemented yet.")
    
    def settings_menu(self):
        # Functionality for settings menu
        messagebox.showinfo("Settings Menu", "Settings menu functionality not implemented yet.")

def main():
    root = tk.Tk()
    app = CustomModderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
