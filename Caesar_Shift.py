import tkinter as tk
def encrpt():
  Aferbet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  sheted_aferbet = []
  emcrptedmesige = ""
  key = input("key: ")
  input_new = input("input: ").upper()
  
  for x in range(0, len(Aferbet) - int(key)):
    if int(key) + x != 28:
      number = int(key) + x
      #print(number)
      sheted_aferbet.append(Aferbet[number])
      #print(sheted_aferbet)
  for x in range(0, int(key)):
    if x != int(key):
      sheted_aferbet.append(Aferbet[x])
      #print(sheted_aferbet)
    
  for x in range(0, len(input_new)):
    tiom_place_non_encrpted = Aferbet.find(input_new[x])
    #print(tiom_place_non_encrpted)
    tiom_place_encrpted = sheted_aferbet[tiom_place_non_encrpted]

    emcrptedmesige = emcrptedmesige + tiom_place_encrpted
    #print(emcrptedmesige)
  print(emcrptedmesige)

def decrpt():
  pass
def start(eord):
  
  root = tk.Tk()

  title = tk.Label(root, text = "Caesar shift", font =("HelvLight",16))

  lable1 = tk.Label(root, text = "Mesige to be encripted")
  mesige = tk.Entry(root)
  if eord == "e":
    submit = tk.Button(root, text = "submit", command= encrpt())
  else:
    submit = tk.Button(root, text = "submit", command= decrpt())
