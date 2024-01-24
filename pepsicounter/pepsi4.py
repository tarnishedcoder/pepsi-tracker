# import tkinter as tk

# from tkinter import messagebox
# from PIL import Image, ImageTk
# import os

# def calculate_total():
#     try:
#         global total_spent
#         cans_per_day = int(entry_cans_per_day.get())
#         cost_per_can = float(entry_cost_per_can.get())
#         daily_spent = cans_per_day * cost_per_can
#         total_spent += daily_spent
#         save_total_spent(total_spent)
#         result_label.config(text=f"Total spent: {total_spent:.2f} SEK")
#     except ValueError:
#         messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# def save_total_spent(total_spent):
#     with open("total_spent.txt", "w") as file:
#         file.write(str(total_spent))

# def load_total_spent():
#     try:
#         with open("total_spent.txt", "r") as file:
#             return float(file.read())
#     except FileNotFoundError:
#         return 0

# def delete_saved_data():
#     global total_spent
#     total_spent = 0
#     if os.path.exists("total_spent.txt"):
#         os.remove("total_spent.txt")
#     result_label.config(text="All saved data has been deleted.")

# def update_background(event):
#     new_width = event.width
#     new_height = event.height
#     canvas.config(width=new_width, height=new_height)

#     resized_image = background_image_resized.subsample(int(original_width / new_width), int(original_height / new_height))
#     canvas.itemconfig(background, image=resized_image)

# # Create main window
# root = tk.Tk()
# root.title("Pepsi Consumption Calculator")
# root.geometry("1280x720")

# # Create Canvas widget
# canvas = tk.Canvas(root, width=1280, height=720)
# canvas.pack()

# # Open the GIF file using Pillow
# background_image = Image.open("pepsimanola.gif")
# original_width, original_height = background_image.size

# # Resize the image to fit the canvas
# resized_image = background_image.resize((1280, 720), Image.ANTIALIAS)
# background_image_resized = ImageTk.PhotoImage(resized_image)

# # Add background image to the canvas
# background = canvas.create_image(0, 0, anchor=tk.NW, image=background_image_resized)

# # Bind the update_background function to the window resize event
# canvas.bind("<Configure>", update_background)

# # Labels and entry widgets
# label_cans_per_day = tk.Label(canvas, text="Number of Pepsi cans consumed per day:")
# label_cans_per_day.place(relx=0.1, rely=0.1)  # Adjust the placement as needed

# entry_cans_per_day = tk.Entry(canvas)
# entry_cans_per_day.place(relx=0.4, rely=0.1)  # Adjust the placement as needed

# label_cost_per_can = tk.Label(canvas, text="Cost per Pepsi can (in SEK):")
# label_cost_per_can.place(relx=0.1, rely=0.2)  # Adjust the placement as needed

# entry_cost_per_can = tk.Entry(canvas)
# entry_cost_per_can.place(relx=0.4, rely=0.2)  # Adjust the placement as needed

# # Calculate button
# calculate_button = tk.Button(canvas, text="Calculate Total Spent", command=calculate_total)
# calculate_button.place(relx=0.3, rely=0.3)  # Adjust the placement as needed

# # Delete data button
# delete_button = tk.Button(canvas, text="Delete Saved Data", command=delete_saved_data)
# delete_button.place(relx=0.3, rely=0.4)  # Adjust the placement as needed

# # Result label
# result_label = tk.Label(canvas, text="")
# result_label.place(relx=0.1, rely=0.5)  # Adjust the placement as needed

# # Load total spent from the file
# total_spent = load_total_spent()

# # Start the Tkinter main loop
# root.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import os

# def calculate_total():
#     try:
#         global total_spent
#         cans_per_day = int(entry_cans_per_day.get())
#         cost_per_can = float(entry_cost_per_can.get())
#         daily_spent = cans_per_day * cost_per_can
#         total_spent += daily_spent
#         save_total_spent(total_spent)
#         result_label.config(text=f"Total spent: {total_spent:.2f} SEK")
#     except ValueError:
#         messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# def save_total_spent(total_spent):
#     with open("total_spent.txt", "w") as file:
#         file.write(str(total_spent))

# def load_total_spent():
#     try:
#         with open("total_spent.txt", "r") as file:
#             return float(file.read())
#     except FileNotFoundError:
#         return 0

# def delete_saved_data():
#     global total_spent
#     total_spent = 0
#     if os.path.exists("total_spent.txt"):
#         os.remove("total_spent.txt")
#     result_label.config(text="All saved data has been deleted.")

# def update_background(event):
#     new_width = event.width
#     new_height = event.height
#     canvas.config(width=new_width, height=new_height)

#     resized_image = background_image_resized.subsample(int(original_width / new_width), int(original_height / new_height))
#     canvas.itemconfig(background, image=resized_image)

# def update_animation():
#     global current_frame
#     current_frame = (current_frame + 1) % num_frames
#     canvas.itemconfig(background, image=frames[current_frame])
#     canvas.after(50, update_animation)  # Update every 50 milliseconds

# # Create main window
# root = tk.Tk()
# root.title("Pepsi Consumption Calculator")
# root.geometry("1280x720")

# # Create Canvas widget
# canvas = tk.Canvas(root, width=1280, height=720)
# canvas.pack()

# # Open the GIF file using Pillow
# background_image = Image.open("pepsimanola.gif")
# original_width, original_height = background_image.size

# # Resize the image to fit the canvas
# resized_image = background_image.resize((1280, 720), Image.ANTIALIAS)
# background_image_resized = ImageTk.PhotoImage(resized_image)

# # Add background image to the canvas
# background = canvas.create_image(0, 0, anchor=tk.NW, image=background_image_resized)

# # Bind the update_background function to the window resize event
# canvas.bind("<Configure>", update_background)

# # Labels and entry widgets
# label_cans_per_day = tk.Label(canvas, text="Number of Pepsi cans consumed per day:")
# label_cans_per_day.place(relx=0.1, rely=0.1)  # Adjust the placement as needed

# entry_cans_per_day = tk.Entry(canvas)
# entry_cans_per_day.place(relx=0.4, rely=0.1)  # Adjust the placement as needed

# label_cost_per_can = tk.Label(canvas, text="Cost per Pepsi can (in SEK):")
# label_cost_per_can.place(relx=0.1, rely=0.2)  # Adjust the placement as needed

# entry_cost_per_can = tk.Entry(canvas)
# entry_cost_per_can.place(relx=0.4, rely=0.2)  # Adjust the placement as needed

# # Calculate button
# calculate_button = tk.Button(canvas, text="Calculate Total Spent", command=calculate_total)
# calculate_button.place(relx=0.3, rely=0.3)  # Adjust the placement as needed

# # Delete data button
# delete_button = tk.Button(canvas, text="Delete Saved Data", command=delete_saved_data)
# delete_button.place(relx=0.3, rely=0.4)  # Adjust the placement as needed

# # Result label
# result_label = tk.Label(canvas, text="")
# result_label.place(relx=0.1, rely=0.5)  # Adjust the placement as needed

# # Load total spent from the file
# total_spent = load_total_spent()

# # Create frames for animation
# frames = []
# num_frames = 10  # Adjust the number of frames as needed

# for i in range(num_frames):
#     frame = ImageTk.PhotoImage(resized_image)
#     frames.append(frame)

# # Initialize animation variables
# current_frame = 0

# # Start animation
# update_animation()

# # Start the Tkinter main loop
# root.mainloop()

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import imageio
import os

def calculate_total():
    try:
        global total_spent
        cans_per_day = int(entry_cans_per_day.get())
        cost_per_can = float(entry_cost_per_can.get())
        daily_spent = cans_per_day * cost_per_can
        total_spent += daily_spent
        save_total_spent(total_spent)
        result_label.config(text=f"Total spent: {total_spent:.2f} SEK")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

def save_total_spent(total_spent):
    with open("total_spent.txt", "w") as file:
        file.write(str(total_spent))

def load_total_spent():
    try:
        with open("total_spent.txt", "r") as file:
            return float(file.read())
    except FileNotFoundError:
        return 0

def delete_saved_data():
    global total_spent
    total_spent = 0
    if os.path.exists("total_spent.txt"):
        os.remove("total_spent.txt")
    result_label.config(text="All saved data has been deleted.")

def update_background(event):
    new_width = event.width
    new_height = event.height
    canvas.config(width=new_width, height=new_height)

    resized_image = background_image_resized.subsample(int(original_width / new_width), int(original_height / new_height))
    canvas.itemconfig(background, image=resized_image)

def update_animation():
    global current_frame
    current_frame = (current_frame + 1) % num_frames
    canvas.itemconfig(background, image=frames[current_frame])
    canvas.after(50, update_animation)  # Update every 50 milliseconds

# Create main window
root = tk.Tk()
root.title("Pepsi Consumption Calculator")
root.geometry("1280x720")

# Create Canvas widget
canvas = tk.Canvas(root, width=1280, height=720)
canvas.pack()

# Open the GIF file using imageio
gif_path = "pepsimanola.gif"
gif_frames = imageio.mimread(gif_path)
num_frames = len(gif_frames)

# Resize the frames to fit the canvas
frames = [ImageTk.PhotoImage(Image.fromarray(frame).resize((1280, 720), Image.ANTIALIAS)) for frame in gif_frames]

# Add background image to the canvas
background = canvas.create_image(0, 0, anchor=tk.NW, image=frames[0])

# Bind the update_background function to the window resize event
canvas.bind("<Configure>", update_background)

# Labels and entry widgets
label_cans_per_day = tk.Label(canvas, text="Number of Pepsi cans consumed per day:")
label_cans_per_day.place(relx=0.1, rely=0.1)  # Adjust the placement as needed

entry_cans_per_day = tk.Entry(canvas)
entry_cans_per_day.place(relx=0.4, rely=0.1)  # Adjust the placement as needed

label_cost_per_can = tk.Label(canvas, text="Cost per Pepsi can (in SEK):")
label_cost_per_can.place(relx=0.1, rely=0.2)  # Adjust the placement as needed

entry_cost_per_can = tk.Entry(canvas)
entry_cost_per_can.place(relx=0.4, rely=0.2)  # Adjust the placement as needed

# Calculate button
calculate_button = tk.Button(canvas, text="Calculate Total Spent", command=calculate_total)
calculate_button.place(relx=0.3, rely=0.3)  # Adjust the placement as needed

# Delete data button
delete_button = tk.Button(canvas, text="Delete Saved Data", command=delete_saved_data)
delete_button.place(relx=0.3, rely=0.4)  # Adjust the placement as needed

# Result label
result_label = tk.Label(canvas, text="")
result_label.place(relx=0.1, rely=0.5)  # Adjust the placement as needed

# Load total spent from the file
total_spent = load_total_spent()

# Initialize animation variables
current_frame = 0

# Start animation
update_animation()

# Start the Tkinter main loop
root.mainloop()


