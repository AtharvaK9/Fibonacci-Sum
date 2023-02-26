from tkinter import*

root = Tk()
root.title("Fibonacci Sum")
root.geometry("400x400")

label_series = Label(root, text = "Fibonacci Series: ")
txt_input = Entry(root)
label_spiral = Label(root)

def Fibonacci():
    num = int(txt_input.get())
    sum2 = 0
    first_num = 0
    second_num = 1
    sum = 0
    counter = 1
    while(counter <= num):
        sum2 = sum2 + sum
        counter += 1
        first_num = second_num 
        second_num = sum
        sum = first_num + second_num
        label_series['text'] += str(sum2) + " "
        label_spiral['text'] = "Fibonacci Sum: " + str(sum2)
        
btn = Button(root, text = "Show Fibonacci Series", command = Fibonacci)
btn.pack()
txt_input.pack()
label_series.pack()
label_spiral.pack