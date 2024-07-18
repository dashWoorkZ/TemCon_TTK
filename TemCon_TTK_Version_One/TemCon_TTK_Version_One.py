from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import os

#Main Window
window = tk.Tk()
window.title("TemCon TTK Ver 1")
# Center The Main Program Window When Launched
width = 310
height = 440
x = (window.winfo_screenwidth()//2)-(width//2)
y = (window.winfo_screenheight()//2)-(height//2)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
window.configure(background="#ffe4c4")
style=ttk.Style()   # ttk Style Library
menu = tk.Menu(window)
style.theme_use("clam")


style.configure("mainFrameLight.TFrame",  relief=tk.SUNKEN,takefocus=False, background="#ffe4c4")
style.configure("mainFrameDark.TFrame",  relief=tk.SUNKEN,takefocus=False, background="#fc9211")

style.configure("mainFrameTitleLight.TFrame", relief=tk.SUNKEN,takefocus=False, bd=5, highlightthickness=5, background="#ffe4c4", foreground="#00fa9a", highlightbackground='#ffa500',  highlightcolor='#fc9211', anchor="center")
style.configure("mainFrameTitleDark.TFrame", relief=tk.SUNKEN,takefocus=False, bd=5, highlightthickness=5,  background="#00fa9a", foreground="#ffe4c4", highlightbackground='#fc9211', highlightcolor='#ffa500', anchor="center")

style.configure("mainLabelLight.TLabel",relief=tk.RAISED, font=("Times New Roman", 12, "bold"), background="#ffe4c4", foreground="#5c3608", highlightbackground='#ffa500', pady=10, highlightcolor='#deb887', highlightthickness=3, takefocus=True)
style.configure("mainLabelDark.TLabel",relief=tk.RAISED, font=("Times New Roman", 12, "bold"), background="#5c3608", foreground="#ffe4c4", highlightbackground='#deb887', highlightcolor='#c97911', highlightthickness=3, takefocus=True)

style.configure("mainLabelTitleLight.TLabel",relief=tk.RAISED, font=("Times New Roman", 11, "bold"), background="#ffe4c4", foreground="#5c3608", highlightbackground='#ffa500', pady=10, highlightcolor='#deb887', highlightthickness=3, takefocus=True)
style.configure("mainLabelTitleDark.TLabel",relief=tk.RAISED, font=("Times New Roman", 11, "bold"), background="#5c3608", foreground="#ffe4c4",  highlightbackground='#deb887', highlightcolor='#c97911', highlightthickness=3, takefocus=True)

style.configure("scaleChoiceLight.TLabel",relief=tk.RAISED, font=("Times New Roman", 11, "bold"), background="#347898", foreground="#5c3608", highlightbackground='#ffa500', pady=10, highlightcolor='#deb887', highlightthickness=3, takefocus=True)
style.configure("scaleChoiceDark.TLabel",relief=tk.RAISED, font=("Times New Roman", 11, "bold"), background="#fc9211", foreground="#aad3fc",  highlightbackground='#deb887', highlightcolor='#c97911', highlightthickness=3, takefocus=True)

style.configure("tempSettingFrameLight.TFrame", bg="#faebd7", cursor="umbrella", highlightcolor="#f5e856", takefocus=True, width=25, background="#70c5c2", foreground="#5c3608")
style.configure("tempSettingFrameDark.TFrame", bg="#faebd7", cursor="umbrella", highlightcolor="#f5e856", takefocus=True, width=25, background="#559492", foreground="#995c11")

style.configure("scaleSetButtonLight.TButton", relief=tk.RAISED, font=("Times New Roman", 11, "bold"), background="#4f788a", foreground="#00ffff", ipady=2, ipadx=5, highlightbackground='#ffa500', highlightcolor='#deb887', highlightthickness=3, takefocus=True, justify="center", anchor="center")
style.configure("scaleSetButtonDark.TButton", relief=tk.RAISED, font=("Times New Roman", 11, "bold"), background="#70c5c2", foreground="#4f788a", ipady=2, ipadx=5,   highlightbackground='#deb887', highlightcolor='#c97911', highlightthickness=3, takefocus=True, justify="center", anchor="center")

style.configure("setTempLight.TEntry", foreground="#00ffff", insertionwidth=5, insertcolor="#00ffff", font=("Times New Roman", 14, "bold"), selectborderwidth=10, cursor="umbrella", relief=tk.RAISED, selectbackground="#99cfe7", selectforeground="#00ffff", takefocus=True, fieldbackground="#347898", justify=CENTER, bordercolor="#5c3608")
style.configure("setTempDark.TEntry", foreground="#347898", insertionwidth=5, insertcolor="#5c3608", font=("Times New Roman", 14, "bold"), selectborderwidth=10, cursor="umbrella", relief=tk.RAISED, selectbackground="#f3e1c9", selectforeground="#ec8c15", takefocus=True, fieldbackground="#70c5c2", justify=CENTER, bordercolor="#5c3608")

style.configure("scalesLight.TLabel",relief=tk.RAISED, direction="below", activebackground="#347898",  activeforeground="#00ffff", font=("Times New Roman", 11, "bold"), background="#4f788a", foreground="#00ffff", ipady=2, ipadx=5, highlightbackground='#70c5c2', pady=10, highlightcolor='#deb887', highlightthickness=3, takefocus=True, justify="center", anchor="center",  width=12)
style.configure("scalesDark.TLabel",relief=tk.RAISED, direction="below", activebackground="#00ffff",  activeforeground="#347898", font=("Times New Roman", 11, "bold"), background="#70c5c2", foreground="#4f788a", ipady=2, ipadx=5,  highlightbackground='#deb887', pady=10, highlightcolor='#70c5c2', highlightthickness=3, takefocus=True, justify="center", anchor="center", width=12)

style.configure("scalesResponseFrameLight.TFrame", relief=tk.SUNKEN, takefocus=False, bd=5, highlightthickness=5,bg="#00ffff", fg="#347898", background="#559492", foreground="#347898", highlightbackground='#8fbc8f', highlightcolor='#dd8929', anchor="center")
style.configure("scalesResponseFrameDark.TFrame", relief=tk.SUNKEN, takefocus=False, bd=5, highlightthickness=5,  bg="#347898", fg="#00ffff", background="#347898", foreground="#559492", highlightbackground='#dd8929', highlightcolor='#8fbc8f', anchor="center")

style.configure("convertedScaleLableFrameLight.TLabel", relief=tk.SUNKEN, takefocus=False, ipadx=5, ipady=5, bg="#00ffff", fg="#347898", bd=5, highlightthickness=5, background="#347898", foreground="#347898", highlightbackground='#8fbc8f', highlightcolor='#dd8929', anchor="center")
style.configure("convertedScaleLableFrameDark.TLabel", relief=tk.SUNKEN, takefocus=False,  ipadx=5, ipady=5, bg="#70c5c2", fg="#00ffff", bd=5, highlightthickness=5,  background="#559492", foreground="#00ffff", highlightbackground='#dd8929', highlightcolor='#8fbc8f', anchor="center")

style.configure("convertedScaleLableFrameLableLight.TLabel",relief=tk.RAISED, font=("Times New Roman", 12, "bold"),  ipadx=5, ipady=10, background="#70c5c2", foreground="#347898", highlightbackground='#ffa500', highlightcolor='#deb887', highlightthickness=3, takefocus=True)
style.configure("convertedScaleLableFrameLableDark.TLabel",relief=tk.RAISED, font=("Times New Roman", 12, "bold"), ipadx=5, ipady=10, background="#559492", foreground="#70c5c2",  highlightbackground='#deb887', highlightcolor='#c97911', highlightthickness=3, takefocus=True)

style.configure("privacyLight.TLabel",relief=tk.RAISED, font=("Times New Roman", 12, "bold"), background="#ffe4c4", foreground="#5c3608", highlightbackground='#ffa500', pady=10, highlightcolor='#deb887', highlightthickness=3, takefocus=True)
style.configure("privacyDark.TLabel",relief=tk.RAISED, font=("Times New Roman", 12, "bold"), background="#5c3608", foreground="#ffe4c4", highlightbackground='#deb887', highlightcolor='#c97911', highlightthickness=3, takefocus=True)

style.configure("lawfulLight.TLabel",relief=tk.RAISED, font=("Times New Roman", 12, "bold"), background="#ffe4c4", foreground="#5c3608", highlightbackground='#ffa500', pady=10, highlightcolor='#deb887', highlightthickness=3, takefocus=True)
style.configure("lawfulDark.TLabel",relief=tk.RAISED, font=("Times New Roman", 12, "bold"), background="#5c3608", foreground="#ffe4c4", highlightbackground='#deb887', highlightcolor='#c97911', highlightthickness=3, takefocus=True)

style.configure("tcttkLight.TLabel",relief=tk.RAISED, font=("Times New Roman", 12, "bold"), background="#ffe4c4", foreground="#5c3608", highlightbackground='#ffa500', pady=10, highlightcolor='#deb887', highlightthickness=3, takefocus=True)
style.configure("tcttkDark.TLabel",relief=tk.RAISED, font=("Times New Roman", 12, "bold"), background="#5c3608", foreground="#ffe4c4", highlightbackground='#deb887', highlightcolor='#c97911', highlightthickness=3, takefocus=True)

style.configure("feedbackFrameLight.TFrame", relief=tk.SUNKEN, takefocus=False, bd=5, highlightthickness=5,bg="#00ffff", fg="#347898", background="#559492", foreground="#347898", highlightbackground='#8fbc8f', highlightcolor='#dd8929', anchor="center")
style.configure("feedbackFrameDark.TFrame", relief=tk.SUNKEN, takefocus=False, bd=5, highlightthickness=5,  bg="#347898", fg="#00ffff", background="#347898", foreground="#559492", highlightbackground='#dd8929', highlightcolor='#8fbc8f', anchor="center")

style.configure("heroFrameLight.TFrame", relief=tk.SUNKEN, takefocus=False, bd=5, highlightthickness=5,bg="#00ffff", fg="#347898", background="#559492", foreground="#347898", highlightbackground='#8fbc8f', highlightcolor='#dd8929', anchor="center")
style.configure("heroFrameDark.TFrame", relief=tk.SUNKEN, takefocus=False, bd=5, highlightthickness=5,  bg="#347898", fg="#00ffff", background="#347898", foreground="#559492", highlightbackground='#dd8929', highlightcolor='#8fbc8f', anchor="center")


style.configure("heroFrameLabelLight.TLabel",relief=tk.RAISED, font=("Times New Roman", 9, "bold"), background="#ffe4c4", foreground="#5c3608", highlightbackground='#ffa500', pady=10, highlightcolor='#deb887', highlightthickness=3, takefocus=True)
style.configure("heroFrameLabelDark.TLabel",relief=tk.RAISED, font=("Times New Roman", 9, "bold"), background="#5c3608", foreground="#ffe4c4",  highlightbackground='#deb887', highlightcolor='#c97911', highlightthickness=3, takefocus=True)


# info Menu to display the info page
info_menu = tk.Menu(menu, tearoff = False, activeforeground="antiquewhite", activebackground="#5c3608", background="antiquewhite", foreground="#5c3608")
info_menu.add_command(label = "Lawful Notice", command=lambda: getInfo())
info_menu.add_command(label = "MIT License", command=lambda: open_mit_window())
info_menu.add_command(label = "Contact", command=lambda: open_contact_window())
info_menu.add_command(label = "Donate", command=lambda: open_donate_window())
menu.add_cascade(label ="[> Info <]", menu = info_menu, activeforeground="antiquewhite", activebackground="#5c3608", background="antiquewhite", foreground="#5c3608")
# Apps Menu to Open and Close TempCalc and to Exit the Program
apps_menu = tk.Menu(menu, tearoff = False, activeforeground="antiquewhite", activebackground="#5c3608", background="antiquewhite", foreground="#5c3608")
apps_menu.add_command(label = "Open", command=lambda: openTC())
apps_menu.add_command(label = "Close", command=lambda: closeTC())
apps_menu.add_command(label = "Exit", command = lambda: quit_main())
menu.add_cascade(label ="<[T]> Apps <[C]>", menu = apps_menu, foreground="antiquewhite", background="burlywood", activebackground="antiquewhite", activeforeground="burlywood")


# Styles Menu to choose between Light and Dark
styles_menu = tk.Menu(menu, tearoff = False, activeforeground="antiquewhite", activebackground="#5c3608", background="antiquewhite", foreground="#5c3608")
styles_menu.add_command(label = "Flip Style", command=lambda: changestyle())
menu.add_cascade(label ="[> Styles <]", menu = styles_menu,  activeforeground="antiquewhite", activebackground="#5c3608", background="antiquewhite", foreground="#5c3608")


# List of Function Calls
# Apps Menu Item to Exit the Program
def quit_main():
    window.quit()



def getInfo():
       closeTC()
       lawful_privacy_frame.pack(fill="both", expand="True")



def hideLawful():
        lawful_privacy_frame.pack_forget()
        main_frame.pack(fill="both", expand=True)



def openTC():      
       hideLawful()
       main_frame.pack(fill="both", expand=True)
       


def closeTC():
       main_frame.pack_forget()
             
      
# A default Function Call to replace "pass"
def notImplemented():
    raise NotImplementedError("This is for Example only!")


# Note: TFrame doesn't seem to respond to "Style" Settings, neither as tk or ttk
main_frame = ttk.Frame(master=window)
main_frame.configure(style="mainFrameLight.TFrame")
main_frame.pack(fill="y", expand=True)
main_frame_title = ttk.Frame(master=main_frame)
main_frame_title.configure(style="mainFrameTitleLight.TFrame")
main_frame_title.pack(fill="both", expand=True, side="top")

main_label = ttk.Label(main_frame_title)
main_label.configure(text="TemCon\n TTk Ver 1", style="mainLabelLight.TLabel", justify="center", anchor="center", compound="left") 
main_label.pack(fill="both", expand=True, side="right")

# tcttk Logo Image used in Frame
tc2024_logo = ImageTk.PhotoImage(Image.open("imgs/tc2024_logo.png"), width=12, height=12)
tc2024_logo_label = ttk.Label(master = main_frame_title,image=tc2024_logo)
tc2024_logo_label.configure(anchor="nw")
tc2024_logo_label.pack(fill="none", expand=True, side="top")

main_label_title = ttk.Label(main_frame)
main_label_title.configure(text="TEMPERATURE CONVERSION TOOL", style="mainLabelTitleLight.TLabel", justify="center", anchor="center") 
main_label_title.pack(fill="both", expand=True, side="top")

global choice
global temp

def display_selected(choice):
        choice = scale.get()
        scale.set(choice)
        scaleTemp.delete(0, END)
        clearTable()


# My answer to no ability to import a Style Configuration file
def changeMainLabel():
        styles = main_label.cget("style")
        if styles == "mainLabelLight.TLabel":
                main_label.configure(style="mainLabelDark.TLabel")
        elif styles == "mainLabelDark.TLabel":
                main_label.configure(style="mainLabelLight.TLabel")
        breakpoint



def changeMainTitle():
        styles = main_label_title.cget("style")
        if styles == "mainLabelTitleLight.TLabel":
                main_label_title.configure(style="mainLabelTitleDark.TLabel")
        elif styles == "mainLabelTitleDark.TLabel":
                main_label_title.configure(style="mainLabelTitleLight.TLabel")
                breakpoint


def changeMainFrame():
        styles = main_frame.cget("style")
        if styles == "mainFrameLight.TFrame":
                main_frame.configure(style="mainFrameDark.TFrame")
        elif styles == "mainFrameDark.TLabel":
                main_frame.configure(style="mainFrameLight.TFrame")
                breakpoint


def changeTempFrame():
        styles = temperature_setting_frame.cget("style")
        if styles == "tempSettingFrameLight.TFrame":
                temperature_setting_frame.configure(style="tempSettingFrameDark.TFrame")
        elif styles == "tempSettingFrameDark.TFrame":
                temperature_setting_frame.configure(style="tempSettingFrameLight.TFrame")
                breakpoint


def changeScales():
        styles = scales.cget("style")
        if styles =="scalesLight.TLabel":
                scales.configure(style="scalesDark.TLabel")
        elif styles == "scalesDark.TLabel":
                scales.configure(style="scalesLight.TLabel")
                breakpoint


def changeSCL():
        styles = scaleChoice_label.cget("style")
        if styles == "mainLabelTitleLight.TLabel":
                scaleChoice_label.configure(style="mainLabelTitleDark.TLabel")
        elif styles == "mainLabelTitleDark.TLabel":
                scaleChoice_label.configure(style="mainLabelTitleLight.TLabel")
                breakpoint


def changeSSB():
        styles = scaleSet_button.cget("style")
        if styles == "scaleSetButtonLight.TButton":
                scaleSet_button.configure(style="scaleSetButtonDark.TButton")
        elif styles == "scaleSetButtonDark.TButton":
                scaleSet_button.configure(style="scaleSetButtonLight.TButton")
                breakpoint


def changeScaleTemp():
        styles = scaleTemp.cget("style")
        if styles == "setTempLight.TEntry":
                scaleTemp.configure(style="setTempDark.TEntry")
        elif styles == "setTempDark.TEntry":
                scaleTemp.configure(style="setTempLight.TEntry")
                breakpoint



def changeSRF():
        styles = scales_response_frame.cget("style")
        if styles == "scalesResponseFrameLight.TFrame":
                scales_response_frame.configure(style="scalesResponseFrameDark.TFrame")
        elif styles == "scalesResponseFrameDark.TFrame":
                scales_response_frame.configure(style="scalesResponseFrameLight.TFrame")
                breakpoint



def changeResponse1():
        styles = converted_scale_one_labelframe_label.cget("style")
        if styles == "convertedScaleLableFrameLableLight.TLabel":
                 converted_scale_one_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel")
        elif styles == "convertedScaleLableFrameLableDark.TLabel":
                converted_scale_one_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel")
                breakpoint



def changeResponse2():
        styles = converted_scale_two_labelframe_label.cget("style")
        if styles == "convertedScaleLableFrameLableLight.TLabel":
                 converted_scale_two_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel")
        elif styles == "convertedScaleLableFrameLableDark.TLabel":
                converted_scale_two_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel")
                breakpoint



def changeResponse3():
        styles = converted_scale_three_labelframe_label.cget("style")
        if styles == "convertedScaleLableFrameLableLight.TLabel":
                 converted_scale_three_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel")
        elif styles == "convertedScaleLableFrameLableDark.TLabel":
                converted_scale_three_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel")
                breakpoint



def changeResponse4():
        styles = converted_scale_four_labelframe_label.cget("style")
        if styles == "convertedScaleLableFrameLableLight.TLabel":
                 converted_scale_four_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel")
        elif styles == "convertedScaleLableFrameLableDark.TLabel":
                converted_scale_four_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel")
                breakpoint



def changeResponseF():
        styles = converted_scales_frame.cget("style")
        if styles == "scalesResponseFrameLight.TFrame":
                 converted_scales_frame.configure(style="scalesResponseFrameDark.TFrame")
        elif styles == "scalesResponseFrameDark.TFrame":
                converted_scales_frame.configure(style="scalesResponseFrameLight.TFrame")
                breakpoint



def changeHeroFrame():
        styles = hero_frame.cget("style")
        if styles == "heroFrameLight.TFrame":
                 hero_frame.configure(style="heroFrameDark.TFrame")
        elif styles == "heroFrameDark.TFrame":
                hero_frame.configure(style="heroFrameLight.TFrame")
                breakpoint

def changeHeroLabel():
        styles = hero_frame_label.cget("style")
        if styles == "heroFrameLabelLight.TLabel":
                 hero_frame_label.configure(style="heroFrameLabelDark.TLabel")
        elif styles == "heroFrameLabelDark.TLabel":
                hero_frame_label.configure(style="heroFrameLabelLight.TLabel")
                breakpoint



def changeFeedback():
        styles = feedback_frame_label.cget("style")
        if styles == "mainLabelTitleLight.TLabel":
                 feedback_frame_label.configure(style="mainLabelTitleDark.TLabel")
        elif styles == "mainLabelTitleDark.TLabel":
                feedback_frame_label.configure(style="mainLabelTitleLight.TLabel")
                breakpoint



def changeLawful():
        styles = lawful_privacy_frame.cget("style")
        if styles == "lawfulLight.TFrame":
                 lawful_privacy_frame.configure(style="lawfulDark.TFrame")
        elif styles == "lawfulDark.TFrame":
                lawful_privacy_frame.configure(style="lawfulLight.TFrame")
                breakpoint


def changestyle():
        changeMainFrame()
        changeTempFrame()
        changeMainLabel()     
        changeMainTitle()
        changeScales()
        changeSCL()
        changeSSB()
        changeScaleTemp()
        changeResponseF()
        changeSRF()
        changeResponse1()
        changeResponse2()
        changeResponse3()
        changeResponse4()
        changeHeroFrame()
        changeHeroLabel()
        changeFeedback()
        changeLawful()

      
      
# General Function Call to Clear the Conversion Table and Entry Input    
def clearTable():
    converted_scale_one_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel",text="")
    converted_scale_two_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel",text="")
    converted_scale_three_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel",text="")
    converted_scale_four_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel",text="")
    scaleTemp.delete(0, END)

def tempError001():
        error_screen_window = Toplevel(window)
        error_screen_window.title("!!! Temperature Error 001 !!!")
        error_screen_window.configure(bg="#f0f0f0")
        width = 375
        height = 200
        x = (error_screen_window.winfo_screenwidth()//2)-(width//2)
        y = (error_screen_window.winfo_screenheight()//2)-(height//2)
        error_screen_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        error_label = tk.Label(master = error_screen_window)
        error_label.configure(bg="#ca8888", fg="#9932cc", font=("Roboto, sans-serif", 14, "bold"), wraplength=290,  text="!!! Temperature Not Found 001 !!!\n\nPlease enter a number to convert!!")
        error_label.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5)
        
def scaleError001():
        error_screen_window = Toplevel(window)
        error_screen_window.title("!!! Scale Error 002 !!!")
        error_screen_window.configure(bg="#f0f0f0")
        width = 375
        height = 200
        x = (error_screen_window.winfo_screenwidth()//2)-(width//2)
        y = (error_screen_window.winfo_screenheight()//2)-(height//2)
        error_screen_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        error_label = tk.Label(master = error_screen_window)
        error_label.configure(bg="#ca8888", fg="#9932cc", font=("Roboto, sans-serif", 14, "bold"), wraplength=290,  text="!!! Scale Not Found 002 !!!\n\nPlease enter a scale to convert!!")
        error_label.pack(fill="both", expand=True, side="top", ipady=5, ipadx=5)

    
# Function retrieves the Scale Chosen and the Temperature to convert, then displays the Conversion Table
def setScaleTemp() -> [str]: 
        choice = scale.get()
        temp = scaleTemp.get()
        if choice == 'Choose A Scale':
                scaleError001()
                return
        elif temp == '':
                tempError001()
                return
        elif choice == "Kelvin":
                converted_scale_one_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round(int(temp) * 1, 1), width=7, anchor='center', justify="center")
                converted_scale_two_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(((int(temp) - 273.15) * 1.8) + 32, 2), width=7, anchor='center', justify="center")
                converted_scale_three_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(int(temp) - 273.15, 1), width=7, anchor='center', justify="center")
                converted_scale_four_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(int(temp) + 491.67, 1), width=7, anchor='center', justify="center")
                scales_response_frame.pack( fill="x", expand=True)
                return
                
        elif choice == "Fahrenheit":
                converted_scale_one_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(((int(temp) - 32) / 1.79999999) + 273.15, 2), width=7, anchor='center', justify="center")
                converted_scale_two_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round(int(temp) * 1, 1), width=7, anchor='center', justify="center")
                converted_scale_three_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round((int(temp) - 32) * (5/9), 2),  width=7, anchor='center', justify="center")
                converted_scale_four_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(int(temp) + 459.67, 2) ,width=7, anchor='center', justify="center")
                scales_response_frame.pack( fill="x", expand=True)
                return

        elif choice == "Rankine":
                converted_scale_one_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(((int(temp)- 491.67) / 1.79999999) + 273.15, 2), width=7, anchor='center', justify="center")
                converted_scale_two_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(int(temp) - 459.67, 2), width=7, anchor='center', justify="center")
                converted_scale_three_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round((int(temp) - 491.67) / 1.79999999, 2), width=7, anchor='center', justify="center")
                converted_scale_four_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round(int(temp) * 1, 1), width=7, anchor='center', justify="center")
                scales_response_frame.pack( fill="x", expand=True)
                return
        
        elif choice == "Celcius":
                converted_scale_one_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(int(temp)  + 273.15, 2), width=7, anchor='center', justify="center")
                converted_scale_two_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round(int(temp)  * (9/5) + 32, 2), width=7, anchor='center', justify="center")
                converted_scale_three_labelframe_label.configure(style="convertedScaleLableFrameLableDark.TLabel", text= round(int(temp) * 1, 2) , width=7, anchor='center', justify="center")
                converted_scale_four_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= round((int(temp) * 1.8) + 459.67, 2), width=7, anchor='center', justify="center")
                scales_response_frame.pack( fill="x", expand=True)
                return


        # Math note: Source of information regarding Rounding Numbers in Python : https://bobbyhadz.com/blog/python-round-float-3-decimal-places         


# Main Frame
temperature_frame = ttk.Frame(master = main_frame)
temperature_frame.configure(style="TempFrameLight.TLabel") 
temperature_frame.pack(fill="both", expand=True, side="top")

# =========  Temperature Setting Frame Start
scaleChoice = ttk.Frame(master = temperature_frame)
scaleChoice.configure(style="scaleChoiceLight.TLabel")
scaleChoice.pack(fill="both", expand=True, side="top")
scaleChoice_label = ttk.Label(scaleChoice)
scaleChoice_label.configure(style="mainLabelTitleLight.TLabel", text='Enter a Number To Convert', justify="center", anchor="center")
scaleChoice_label.pack(fill="x", expand=True, side="top", ipady=5)
                          
temperature_setting_frame = ttk.Frame(master = scaleChoice) 
temperature_setting_frame.configure(style="tempSettingFrameLight.TFrame")
temperature_setting_frame.pack(side="top", fill="both", expand=True)

scaleSet_button = ttk.Button(master = temperature_setting_frame)
scaleSet_button.configure(style="scaleSetButtonLight.TButton", takefocus=True, command=setScaleTemp, text="Convert")
scaleSet_button.pack(fill="none", expand=True, padx=3, side="right")

# Scale Temperature Setting
scaleTemp = ttk.Entry(master = temperature_setting_frame)
scaleTemp.config(style="setTempLight.TEntry", width=2, justify="center") 
scaleTemp.pack(fill="x", expand=True, padx=3, side="right", ipadx=2, ipady=2)

# creating Option Menu widget
scaleSet = ['Choose A Scale','Celcius','Fahrenheit', 'Kelvin', 'Rankine']

# setting variable for Integers and Strings
scale = StringVar()
scale.set(scaleSet[0])

scales = ttk.OptionMenu(
    temperature_setting_frame,
    scale,
    *scaleSet,
    command=display_selected)

scales.configure(style="scalesLight.TLabel")
scales.pack(fill="x", expand=True, padx=5, side="left", ipady=5, ipadx=5)
# ====== Scales Conversion Frame 
scales_response_frame = ttk.Frame(master = scaleChoice)
scales_response_frame.configure(style="scalesResponseFrameLight.TFrame")
scales_response_frame.pack( fill="x", expand=True)

setTemp = StringVar()
temp = 0

def setTemp(temp):
    temp = round(setTemp)
    print(setTemp)
 
            
#Converted Scales Frame
converted_scales_frame = ttk.Frame(master = scales_response_frame)
converted_scales_frame.configure(style="scalesResponseFrameLight.TFrame")
converted_scales_frame.pack(fill='both', expand=True, side="bottom", anchor="center", pady=10, padx=10)

# Converted Scale Kelvin
converted_scale_one_labelframe = ttk.LabelFrame(master = converted_scales_frame)
converted_scale_one_labelframe.configure(style="convertedScaleLableFrameLight.TLabel", text="  Kelvin ", width=7)
converted_scale_one_labelframe.pack(fill="both", expand=True, side="left")

converted_scale_one_labelframe_label = ttk.Label(master = converted_scale_one_labelframe)
converted_scale_one_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= "", justify="center", width=7)
converted_scale_one_labelframe_label.pack(fill="both", expand=True, side="bottom")

# Converted Scale Fahrenheit
converted_scale_two_labelframe = ttk.LabelFrame(master = converted_scales_frame)
converted_scale_two_labelframe.configure(style="convertedScaleLableFrameLight.TLabel", text=" Fahrenheit ", width=7)
converted_scale_two_labelframe.pack(fill="both", expand=True, side="top", ipady=5)

converted_scale_two_labelframe_label = ttk.Label(converted_scale_two_labelframe)
converted_scale_two_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text="", justify="center", width=7)
converted_scale_two_labelframe_label.pack(fill="both", expand=True, side="bottom")

# Converted Scale Celcius
converted_scale_three_labelframe = ttk.LabelFrame(master = converted_scales_frame)
converted_scale_three_labelframe.configure(style="convertedScaleLableFrameLight.TLabel", text=" Celcius ", width=7)
converted_scale_three_labelframe.pack(fill="both", expand=True, side="right")

converted_scale_three_labelframe_label = ttk.Label(converted_scale_three_labelframe)
converted_scale_three_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= "", justify="center", width=7)
converted_scale_three_labelframe_label.pack(fill="both", expand=True, side="bottom", ipady=5)

# Converted Scale Rankine
converted_scale_four_labelframe = ttk.LabelFrame(master = converted_scales_frame)
converted_scale_four_labelframe.configure(style="convertedScaleLableFrameLight.TLabel", text=" Rankine ", width=7)
converted_scale_four_labelframe.pack(fill="both", expand=True, side="right")

converted_scale_four_labelframe_label = ttk.Label(master = converted_scale_four_labelframe)
converted_scale_four_labelframe_label.configure(style="convertedScaleLableFrameLableLight.TLabel", text= "", justify="center", width=7)
converted_scale_four_labelframe_label.pack(fill="both", expand=True, side="bottom", ipady=5)

# Sponsored Advertising Frame
hero_frame = ttk.Frame(main_frame)
hero_frame.configure(style="heroFrameLight.TFrame", relief="sunken", width=28)
hero_frame.pack(fill="both", expand=True, side="top")
# Sponsored Advertiseing Label
hero_frame_label = ttk.Label(hero_frame)
hero_frame_label.configure(style="heroFrameLabelLight.TLabel", text="Jeanette's Impressions Art\njeanette.elizabeth@dashwoorkz.ca\nCommunity Services Director", justify="center", anchor="center")
hero_frame_label.grid(row=0, column=0, padx=6, pady=5, ipadx=10, ipady=9)

# jeia Logo Image used in Advertising Frame
jeia_logo = ImageTk.PhotoImage(Image.open("imgs/jeia_thumb.png"), width=120, height=80)
jeia_logo_label = ttk.Label(master = hero_frame,image=jeia_logo)
jeia_logo_label.configure()
jeia_logo_label.grid(row=0, column=1)


feedback_frame = ttk.Frame(master=hero_frame)
feedback_frame.configure(style="feedbackFrameLight.TFrame")
feedback_frame.grid(row=1, column=0, columnspan=4, pady=5)
feedback_frame_label = ttk.Label(master=feedback_frame)
feedback_frame_label.configure(style="mainLabelTitleLight.TLabel", font=("Times New Roman", 10, "bold"), wraplength=270, anchor="center", justify="center", text="FeedBack:\ndashWoorkZ Sovereign Society would welcome any comments or suggestions.\n Email: dashwoorkz@dashwoorkz.ca")
feedback_frame_label.pack(fill="x", expand="True", side="bottom", ipady=5, ipadx=10)

footer_frame = ttk.Frame(master=main_frame)
footer_frame.configure(style="footerFrameLight.TFrame")
footer_frame.pack(fil="both", expand=True, side="top")

lawful_privacy_frame = ttk.Frame(master=window)
lawful_privacy_frame.configure(style="lawfulLight.TFrame")
lawful_privacy_frame.pack(fill="both", expand="True")
logo_frame = ttk.Frame(master=lawful_privacy_frame)
logo_frame.configure(style="lawfulLight.TFrame")
logo_frame.pack(fil="both", expand=True, side="top")
# tcttk Logo Image used in Frame
dwrx_logo = ImageTk.PhotoImage(Image.open("imgs/dss_logo.png"))
dwrx_logo_label = ttk.Label(master = logo_frame,image=dwrx_logo, width=150)
dwrx_logo_label.configure(style="tcttkLight.TLabel", anchor="center", justify="center")
dwrx_logo_label.pack(fill="both", expand=True, side="top",)
privacy_frame = ttk.Frame(master=lawful_privacy_frame)
privacy_frame.configure(style="lawfulLight.TFrame")
privacy_frame.pack(fill="both", expand=True)
privacy_frame_label = ttk.Label(master=privacy_frame)
privacy_frame_label.configure(style="privacyLight.TLabel", font=("Times New Roman", 10, "bold"), anchor="center", justify="center", wraplength=290, text="dashWoorkz Sovereign Society\n is a Private Society, we will not invade Your Privacy, or provide anyone any information we may have about you, any information we have about you will have been acquired with Your Consent, if we were to do anything with the information we have about you, it would be with Your Consent")
privacy_frame_label.pack(fill="x", expand="True", side="top", ipady=5, ipadx=5)

lawful_frame = ttk.Frame(master=lawful_privacy_frame)
lawful_frame.configure(style="lawfulLight.TFrame")
lawful_frame.pack(fill="both", expand=True)
lawful_frame_label = ttk.Label(master=lawful_frame)
lawful_frame_label.configure(style="lawfulLight.TLabel", font=("Times New Roman", 10, "bold"), justify="center", anchor="center", wraplength=300, text="dashWoorkz Sovereign Society\nEstablished: 2023\nTemCon TTK Version One(1)\nTemperature Conversion Tool\nConverts:\n Celcius, Kelvin, Fahrenheit and Rankine")
lawful_frame_label.pack(fill="x", expand="True", side="top", ipady=5, ipadx=5)


def open_donate_window():
    donate_window = Toplevel(window)
    donate_window.title("Donate")
    width = 400
    height = 350
    x = (donate_window.winfo_screenwidth()//2)-(width//2)
    y = (donate_window.winfo_screenheight()//2)-(height//2)
    donate_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    donate_window.configure(bg="#f0f0f0")
    donate_label = Label(donate_window)
    donate_label.configure(font=("Times New Roman", 11, "bold"),highlightbackground='#ffa500', pady=10, highlightcolor='#deb887', highlightthickness=3, takefocus=True,  background="#ffe4c4", foreground="#5c3608", text="Donate:\nIf you enjoyed this program and would\n like to contribute to our work:\n\ndashWoorkz Sovereign Society:\ndashwoorkz@dashwoorkz.ca\n\nE-Transfer:\nLord :Dash: La Londe\nManaging Director:\ndash@dashwoorkz.ca\n\n Bitcoin:\nBTC:38YwKspQ8hdxAmGQUPP7LvXPRucdZURNu5\n\n Merchandise Online:\nhttp://everythingdash.creator-spring.com/")
    donate_label.pack(fill="both", expand=True)
    



def open_contact_window():
    contact_window = Toplevel(window)
    contact_window.title("Contact Us")
    contact_window.geometry("310x200")
    width = 310
    height = 220
    x = (contact_window.winfo_screenwidth()//2)-(width//2)
    y = (contact_window.winfo_screenheight()//2)-(height//2)
    contact_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    contact_window.configure(bg="#f0f0f0")
    
    label_contact = Label(contact_window, text="Contact Information", foreground="#fd3adf", bg="#f7d4f6", font=("Helvetica", 12, "bold"))
    label_contact.pack(fill="both", expand=True)

    label_society = Label(contact_window, text="dashWoorkZ Sovereign Society", foreground="#4169e1", bg="#99cfe7", font=("Helvetica", 10, "bold"))
    label_society.pack(fill="both", expand=True)
    
    label_email = Label(contact_window, text="Email: dashwoorkz@dashwoorkz.ca", foreground="#4169e1", bg="#99cfe7", font=("Helvetica", 10))
    label_email.pack(fill="both", expand=True)
    
    label_mdirector = Label(contact_window, text="Managing Director:", foreground="#2e8b57", bg="#c4ecc4", font=("Helvetica", 10, "bold"))
    label_mdirector.pack(fill="both", expand=True)
    
    label_mdName = Label(contact_window, text="Lord :Dash: La Londe", foreground="#2e8b57", bg="#c4ecc4", font=("Helvetica", 10))
    label_mdName.pack(fill="both", expand=True)

    label_md_email = Label(contact_window, text="Email: dash@dashwoorkz.ca", foreground="#2e8b57", bg="#c4ecc4", font=("Helvetica", 10, "bold"))
    label_md_email.pack(fill="both", expand=True)

    label_csDirector = Label(contact_window, text="Community Services Director:", foreground="#c27012", bg="#f3e1c9", font=("Helvetica", 10, "bold"))
    label_csDirector.pack(fill="both", expand=True)
    
    label_csdName = Label(contact_window, text="Lady :Jeanette-Elizabeth: Hiuser", foreground="#c27012", bg="#f3e1c9", font=("Helvetica", 10))
    label_csdName.pack(fill="both", expand=True)

    label_cs_email = Label(contact_window, text="Email: jeanette.elizabeth@dashwoorkz.ca", foreground="#c27012", bg="#f3e1c9", font=("Helvetica", 10))
    label_cs_email.pack(fill="both", expand=True)
    
    label_dwrx = Label(contact_window, text="Visit: http://dashwoorkz.ca", foreground="#c27012", bg="#cae8f3", font=("Helvetica", 16))
    label_dwrx.pack(fill="both", expand=True, ipady=5)


def open_mit_window():
    mit_window = Toplevel(window)
    mit_window.title("MIT License")
    width = 350
    height = 400
    x = (mit_window.winfo_screenwidth()//2)-(width//2)
    y = (mit_window.winfo_screenheight()//2)-(height//2)
    mit_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    mit_window.configure(bg="#f0f0f0")
    mit_label = Label(mit_window)
    mit_label.configure(font=("Times New Roman", 9, "bold"),highlightbackground='#2391ff', wraplength=280, pady=10, highlightcolor='#35cbe6', highlightthickness=3, takefocus=True,  background="#85c0ea", foreground="#206eff", 
    text= "Copyright (c) 2024 dashWoorkZ Sovereign Society\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.")
    mit_label.pack(fill="both", expand=True)




       

hideLawful()

window.configure(menu = menu)


window.mainloop()
