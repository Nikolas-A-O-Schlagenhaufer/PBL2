import tkinter as tk
from main import get_decision_tree
from study import Study
import numpy as np

# Definir qual paciente deseja ser testado, indicando o seu número,
# correspondente ao número do arquivo .csv na pasta treated_data/motor_movement
# com os dados
pessoa = 61

# Definir o intervalo de atualização da interface em milissegundos
interval = 2

# Definir a função que acende a lâmpada quando o botão é pressionado
def on_press():
	global button_pressed
	button_pressed = True

# Definir a função que apaga a lâmpada quando o botão é solto
def on_release():
	global button_pressed
	button_pressed = False

# Definir a função que atualiza a interface
def update():
	if button_pressed:
		canvas.itemconfigure(bulb_on, fill="grey")
		canvas.itemconfigure(bulb_off, fill="yellow")
	else:
		canvas.itemconfigure(bulb_on, fill="yellow")
		canvas.itemconfigure(bulb_off, fill="grey")
	# Agendar a próxima atualização após 1 segundo
	root.after(interval, update)
	
# Definicar a função que verifica se a pessoa está piscando
def verifica_pisque(prox):
	if prox < len(data):
		teste = np.array(data.iloc[prox]).reshape(1, -1)
		return DTC.predict(teste) == 1, prox + 1
	button_label.config(text='Fim do Teste!')
	return False, prox

# Definir a função que checa o estado do botão e atualiza button_pressed
def check_button_state():
	global button_pressed, prox, piscando
	piscando, prox = verifica_pisque(prox)
	if piscando:
		button_pressed = True
	# if button['state'] == 'active':
	#     button_pressed = True
	else:
		button_pressed = False
	# Agendar a próxima checagem após 100 milissegundos
	root.after(interval, check_button_state)

# Criar a janela principal
root = tk.Tk()
root.title("Interface com o Modelo")

# Criar o canvas para desenhar a lâmpada
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack(pady=20)

# Desenhar os retângulos para a lâmpada acesa e apagada
bulb_on = canvas.create_oval(50, 50, 150, 150, fill="grey")
bulb_off = canvas.create_oval(50, 50, 150, 150, fill="yellow")

button_pressed = False
prox = 0
piscando = False
DTC = get_decision_tree()
study = Study()
data = study.tests[1].get_subject(pessoa).data_sets[0].data

# Criar o botão
button_label = tk.Label(root, text=f"Testando paciente {pessoa}", font=("Helvetica", 24))
button_label.pack()

# Configurar o botão para chamar as funções on_press() e on_release() quando for pressionado e solto
# button = tk.Button(root, text="Button", font=("Helvetica", 24), bg="blue", fg="white", activebackground="blue", activeforeground="white", command=on_press)
# button.bind("<ButtonRelease-1>", lambda event: on_release())
# button.pack(pady=20)

# Agendar a chamada da função update() a cada 10 milissegundos
root.after(interval, update)

# Agendar a chamada da função check_button_state() a cada 10 milissegundos
root.after(interval, check_button_state)

# Iniciar o loop da interface gráfica
root.mainloop()