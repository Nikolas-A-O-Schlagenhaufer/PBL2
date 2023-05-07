import tkinter as tk

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
        canvas.itemconfigure(bulb_on, fill="yellow")
        canvas.itemconfigure(bulb_off, fill="grey")
    else:
        canvas.itemconfigure(bulb_on, fill="grey")
        canvas.itemconfigure(bulb_off, fill="yellow")
    # Agendar a próxima atualização após 1 segundo
    root.after(1000, update)

# Definir a função que checa o estado do botão e atualiza button_pressed
def check_button_state():
    global button_pressed
    if button['state'] == 'active':
        button_pressed = True
    else:
        button_pressed = False
    # Agendar a próxima checagem após 100 milissegundos
    root.after(100, check_button_state)

# Criar a janela principal
root = tk.Tk()
root.title("Button and Bulb Interface")

# Criar o canvas para desenhar a lâmpada
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack(pady=20)

# Desenhar os retângulos para a lâmpada acesa e apagada
bulb_on = canvas.create_oval(50, 50, 150, 150, fill="grey")
bulb_off = canvas.create_oval(50, 50, 150, 150, fill="yellow")

# Criar o botão
button_label = tk.Label(root, text="Press and hold the button", font=("Helvetica", 24))
button_label.pack()

# Configurar o botão para chamar as funções on_press() e on_release() quando for pressionado e solto
button_pressed = False
button = tk.Button(root, text="Button", font=("Helvetica", 24), bg="blue", fg="white", activebackground="blue", activeforeground="white", command=on_press)
button.bind("<ButtonRelease-1>", lambda event: on_release())
button.pack(pady=20)

# Agendar a chamada da função update() a cada segundo
root.after(1000, update)

# Agendar a chamada da função check_button_state() a cada 100 milissegundos
root.after(100, check_button_state)

# Iniciar o loop da interface gráfica
root.mainloop()