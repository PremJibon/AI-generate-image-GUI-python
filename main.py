import customtkinter as ctk
import tkinter
import os
import openai
from PIL import Image,ImageTk
import requests ,io


def generate():
    openai.api_key = os.getenv("OPENAI_API_KEY")

    user_prompt = prompt_entry.get("0.0",tkinter.END)
    user_prompt += "in style:" + style_dropdown.get()

    response = openai.Image.create(
        prompt = user_prompt,
        n=1,
        size="1024x1024"

    )
    image_url = response['data'][0]['url']
    response = requests.get(image_url)
    image = Image.open(io.BytesIO(response.content))
    image = ImageTk.PhotoImage(image) 
    
    canvas.image = image
    canvas.create_image(0,0,anchor='nw',image=image)
    


root = ctk.CTk()
root.title("Ai Image Generator")

ctk.set_appearance_mode("dark")

input_frame = ctk.CTkFrame(root)
input_frame.pack(side='left',expand=True,padx=20,pady=20)

prompt_label = ctk.CTkLabel(input_frame,text="Prompt")
prompt_label.grid(row=0,column=0,padx=10,pady=10)

prompt_entry = ctk.CTkTextbox(input_frame,height=10)
prompt_entry.grid(row=0,column=1,padx=10,pady=10)

style_label = ctk.CTkLabel(input_frame,text='style')
style_label.grid(row=1,column=0,padx=10,pady=10)
style_dropdown = ctk.CTkComboBox(input_frame,values=["Realistic","Cartoon","#D Illustration","Flat Art"])
style_dropdown.grid(row=1,column=1,padx=10,pady=10)

number_label = ctk.CTkLabel(input_frame,text='# Images')
number_label.grid(row=2,column=0)

number_slider = ctk.CTkSlider(input_frame,from_=1,to=10,number_of_steps=9)
number_slider.grid(row=2,column=1)

generate_button = ctk.CTkButton(input_frame,text="Generate",command=generate)
generate_button.grid(row=3,column=0,columnspan=2,sticky='news',padx=10,pady=10)


canvas = tkinter.Canvas(root,width=512,height=512)
canvas.pack(side="left")



root.mainloop()