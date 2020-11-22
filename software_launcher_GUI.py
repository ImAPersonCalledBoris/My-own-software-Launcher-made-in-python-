import tkinter as tk

window = tk.Tk()
window.geometry("600x600")
window.title("Software_launcher_GUI")

def main_menu_A_option():
	text = "funzione da implementare : ("
	text_output = tk.Label(window, text=text)
	text_output.grid(row=281, column=281)

def main_menu_B_option():
	text = "Funzione da implementare : ("
	text_output = tk.Label(window, text=text)
	text_output.grid(row=285, column=285)
	
def main_menu_C_option():
	text = "Funzione da implementare : ( "
	text_output = tk.Label(window, text=text)
	text_output.grid(row=305, column=305)

main_menu_option_A = tk.Button(text="Software_Launcher", command=main_menu_A_option )
main_menu_option_A.grid(row=280, column=280)

main_menu_option_B = tk.Button(text="Changelog", command=main_menu_B_option)
main_menu_option_B.grid(row=283, column=283)

main_menu_option_C = to.Button(text="Credits", command=main_menu_C_option)
main_menu_option_C.grid(row=300, column=300)


if __name__ == "__main__":
	window.mainloop()
