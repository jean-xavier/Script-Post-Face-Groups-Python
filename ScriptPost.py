# coding: utf-8
import facebook
import json
from tkinter import *
from tkinter import messagebox
import urllib.request

def btn_onclick_post():
    try:
        post = ed.get('1.0', END)
        for id_group in data['data']:
            graph.put_object(parent_object=id_group, connection_name='feed', message=post)
        messagebox.showinfo('Sucesso!','Mensagem Postada com Exito!')
    except Exception as e:
        messagebox.showerror('Erro', 'Erro ao Postar Mensagem!\n%s' %e)

token = ''
url = 'https://graph.facebook.com/v2.3/me/groups?fields=id&access_token=' + token

try:
    resp = urllib.request.urlopen(url).read()
    data = json.loads(resp.decode('utf-8'))
except Exception as e:
    messagebox.showwarning('Erro de conexão', 'Seu token está expirado!\n%s' %e)

graph = facebook.GraphAPI(access_token=token, version='2.3')

#Interface
App = Tk()
App.title("Divulgação!")
App["background"] = 'Gainsboro'

ed = Text(App)
ed.pack(padx=10, pady=10)

bt = Button(App, width=20, text="Postar", command=btn_onclick_post)
bt.pack()

App.geometry("570x420+500+300")
App.mainloop()