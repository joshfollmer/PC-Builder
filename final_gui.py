import tkinter as tk
from PC_picker import Picker
from datetime import datetime

class PC_GUI:
    '''
    Class to make a GUI that will let the user enter a budget, customize the allocations to each part, and scrape the web for pc parts that can be bought with the budget
    '''
    def __init__(self, window):
        #label for entering the budget
        entry_label = tk.Label(window, text= "Enter budget")
        entry_label.place(x = 0, y = 10)

        #text box to enter the budget
        self.entry_box = tk.Entry(window, width = 15)
        self.entry_box.place(x = 80, y = 10)

        #button to find the parts
        entry_button = tk.Button(window, text= "Find parts", command=self.warning)
        entry_button.place(x =40, y = 35 )
        
        #makes labels for each part 
        cpu_label = tk.Label(window, text='CPU:')
        cpu_label.place(x = 0, y = 80)

        cooler_label = tk.Label(window, text= 'Cooler:')
        cooler_label.place(x = 0, y = 120)

        motherboard_label = tk.Label(window, text= 'Motherboard:')
        motherboard_label.place(x = 0, y = 160)

        storage_label = tk.Label(window, text= 'Storage:')
        storage_label.place(x = 0, y = 200)

        memory_label = tk.Label(window, text = 'Memory:')
        memory_label.place(x = 0, y = 240)

        gpu_label = tk.Label(window, text= "GPU:")
        gpu_label.place(x= 0, y = 280)

        case_label = tk.Label(window, text= "Case:")
        case_label.place(x = 0, y = 320)

        power_label = tk.Label(window, text= "Power supply:")
        power_label.place(x = 0, y = 360)
        
        #-----------------------------------------------------------------------------------------------------------------------------

        #makes the spinboxes and labels for each allocation

        cpu_allo = tk.Label(window, text= 'CPU allocation:')
        cpu_allo.place(x = 0, y = 500)

        #sets a default varibale at the start of the program
        self.cpu_var = tk.DoubleVar(value=20)  
        #makes a spinbox, with values between 0 and 100, in incremnts of 5, and it can wrap around from 0 to 100 or vice versa
        self.cpu_percent = tk.Spinbox(window, from_=0, to= 100, wrap = True, width = 5, increment= 5, textvariable=self.cpu_var)
        self.cpu_percent.place(x = 140, y = 500)


        cooler_allo = tk.Label(window, text= 'Cooler allocation:')
        cooler_allo.place(x = 0, y = 530)

        cooler_var = tk.DoubleVar(value=5)  
        self.cooler_percent = tk.Spinbox(window, from_=0, to= 100, wrap = True, width = 5, increment= 5, textvariable=cooler_var)
        self.cooler_percent.place(x = 140, y = 530)


        motherboard_allo = tk.Label(window, text= 'Motherboard allocation:')
        motherboard_allo.place(x = 0, y = 560)

        motherboard_var = tk.DoubleVar(value=15)  
        self.motherboard_percent = tk.Spinbox(window, from_=0, to= 100, wrap = True, width = 5, increment= 5, textvariable=motherboard_var)
        self.motherboard_percent.place(x = 140, y = 560)


        storage_allo = tk.Label(window, text= 'Storage allocation:')
        storage_allo.place(x = 210, y = 500)

        storage_var = tk.DoubleVar(value=15)  
        self.storage_percent = tk.Spinbox(window, from_=0, to= 100, wrap = True, width = 5, increment= 5, textvariable=storage_var)
        self.storage_percent.place(x = 320, y = 500)


        memory_allo = tk.Label(window, text= 'Memory allocation:')
        memory_allo.place(x = 210, y = 530)

        memory_var = tk.DoubleVar(value=10)  
        self.memory_percent = tk.Spinbox(window, from_=0, to= 100, wrap = True, width = 5, increment= 5, textvariable=memory_var)
        self.memory_percent.place(x = 320, y = 530)


        gpu_allo = tk.Label(window, text= 'GPU allocation:')
        gpu_allo.place(x = 210, y = 560)

        gpu_var = tk.DoubleVar(value=25)  
        self.gpu_percent = tk.Spinbox(window, from_=0, to= 100, wrap = True, width = 5, increment= 5, textvariable=gpu_var)
        self.gpu_percent.place(x = 320, y = 560)


        case_allo = tk.Label(window, text= 'Case allocation:')
        case_allo.place(x = 390, y = 500)

        case_var = tk.DoubleVar(value=5)  
        self.case_percent = tk.Spinbox(window, from_=0, to= 100, wrap = True, width = 5, increment= 5, textvariable=case_var)
        self.case_percent.place(x = 530, y = 500)


        power_allo = tk.Label(window, text= 'Power supply allocation:')
        power_allo.place(x = 390, y = 530)

        power_var = tk.DoubleVar(value=5)  
        self.power_percent = tk.Spinbox(window, from_=0, to= 100, wrap = True, width = 5, increment= 5, textvariable=power_var)
        self.power_percent.place(x = 530, y = 530)

        
        



    def warning(self):
        '''
        This method will add up the total of the part allocations, and check if they add to 100. If they don't, it will display a message, if they do, it will save each one as a variable and run findParts()
        '''
        #makes a warnign label 
        allo_warning = tk.Label(window, text = "Allocations must add up to 100%")
        #adds up the total allocations
        allo_total = int(self.cpu_percent.get()) + int(self.cooler_percent.get()) + int(self.motherboard_percent.get()) + int(self.storage_percent.get()) + int(self.memory_percent.get()) + int(self.gpu_percent.get()) + int(self.case_percent.get()) + int(self.power_percent.get())
        
        #if the totals dont add up to 100, places a warning label 
        if allo_total != 100:
            allo_warning.place(x = 600, y = 500)
        else:
            #divides each allocation by 100 so it can be multiplied by the budget
            self.cpu_b = int(self.cpu_percent.get()) / 100
            self.cooler_b = int(self.cooler_percent.get()) / 100
            self.motherboard_b = int(self.motherboard_percent.get()) / 100
            self.storage_b = int(self.storage_percent.get()) / 100
            self.memory_b = int(self.memory_percent.get()) / 100
            self.gpu_b = int(self.gpu_percent.get()) / 100
            self.case_b = int(self.case_percent.get()) / 100
            self.power_b = int(self.power_percent.get()) / 100
            self.findParts()


    def findParts(self):
        '''
        This method will run the method used to scrape for the parts, and display each name, price, and total price in the GUI.  
        '''
        #attemplts to turn trhe budget into a float. if an exception is raised, the GUI will still run but an error message will display in VScode
        try:
            self.budget = float(self.entry_box.get())
        except:
            error_label = tk.Label(window, text = 'Entry must be a number')
            error_label.place(x = 140, y = 10)
            
        #runs splitBudget once and saves the return
        parts_budget = pc.splitBudget(self.budget, self.cpu_b, self.cooler_b, self.motherboard_b, self.storage_b, self.memory_b, self.gpu_b, self.case_b, self.power_b)

        #runs pickPart once for each part, passing it its webpage and its part of the budget
        self.cpu_result = pc.pickPart('https://www.newegg.com/p/pl?Submit=StoreIM&Category=34&PageSize=96', parts_budget[0])
        self.cooler_result = pc.pickPart('https://www.newegg.com/p/pl?Submit=StoreIM&Category=11&Depa=1', parts_budget[1])
        self.motherboard_result = pc.pickPart('https://www.newegg.com/Motherboards/Category/ID-20?cm_sp=Tab_Components_2-_-visnav-_-Motherboards_2', parts_budget[2])
        self.storage_result = pc.pickPart('https://www.newegg.com/p/pl?Submit=StoreIM&Category=15&Depa=1&PageSize=96', parts_budget[3])
        self.memory_result = pc.pickPart('https://www.newegg.com/p/pl?Submit=StoreIM&Category=17&PageSize=96', parts_budget[4])
        self.gpu_result = pc.pickPart('https://www.newegg.com/p/pl?Category=38&N=100006662&PageSize=96', parts_budget[5])
        self.case_result = pc.pickPart('https://www.newegg.com/p/pl?Submit=StoreIM&Category=9&PageSize=96', parts_budget[6])
        self.power_result = pc.pickPart('https://www.newegg.com/p/pl?Submit=StoreIM&Category=32&Depa=1', parts_budget[7])
        #------------------------------------------------------------------------------------------------------------------------------------------------------
        #displays the prices of each part

        cpu_price = tk.Label(window, text = f"${self.cpu_result[1]}")
        cpu_price.place(x = 100, y = 80)

        cooler_price = tk.Label(window, text = f"${self.cooler_result[1]}")
        cooler_price.place(x = 100, y = 120)

        motherboard_price = tk.Label(window, text = f"${self.motherboard_result[1]}")
        motherboard_price.place(x = 100, y = 160)

        storage_price = tk.Label(window, text = f"${self.storage_result[1]}")
        storage_price.place(x = 100, y = 200)

        memory_price = tk.Label(window, text = f"${self.memory_result[1]}")
        memory_price.place(x = 100, y = 240)

        gpu_price = tk.Label(window, text = f"${self.gpu_result[1]}")
        gpu_price.place(x = 100, y = 280)

        case_price = tk.Label(window, text = f"${self.case_result[1]}")
        case_price.place(x = 100, y = 320)

        power_price = tk.Label(window, text = f"${self.power_result[1]}")
        power_price.place(x = 100, y = 360)

        #---------------------------------------------------------------------------------------------------------------------------------------
        #displays the names of each part
        
        cpu_name = tk.Label(window, text= f"{self.cpu_result[0]}")
        cpu_name.place(x = 200, y  = 80)

        cooler_name = tk.Label(window, text= f"{self.cooler_result[0]}")
        cooler_name.place(x = 200, y  = 120)

        motherboard_name = tk.Label(window, text= f"{self.motherboard_result[0]}")
        motherboard_name.place(x = 200, y  = 160)

        storage_name = tk.Label(window, text= f"{self.storage_result[0]}")
        storage_name.place(x = 200, y  = 200)

        memory_name = tk.Label(window, text= f"{self.memory_result[0]}")
        memory_name.place(x = 200, y  = 240)

        gpu_name = tk.Label(window, text= f"{self.gpu_result[0]}")
        gpu_name.place(x = 200, y  = 280)

        case_name = tk.Label(window, text= f"{self.case_result[0]}")
        case_name.place(x = 200, y  = 320)

        power_name = tk.Label(window, text= f"{self.power_result[0]}")
        power_name.place(x = 200, y  = 360)

        #------------------------------------------------------------------------------------------------------------------------------------------
        #adds up the total and displays it, makes a warning if the budgetwas too little, also makes a button to save everything to a file

        self.total_price = self.cpu_result[1] + self.cooler_result[1] + self.motherboard_result[1] + self.storage_result[1] + self.memory_result[1] + self.gpu_result[1] + self.case_result[1] + self.power_result[1]
        total_label = tk.Label(window, text = f"Total price: ${round(self.total_price, 2)}")
        total_label.place(x = 100, y = 400)

        file_button = tk.Button(window, text= "Save to file", command= self.saveToFile)
        file_button.place(x = 120, y = 35)

        #if the total price is greater than the budget, give a warning         
        if self.total_price > self.budget:
            price_warning = tk.Label(window, text= "The budget was not big enough to find some parts, the program has selected the minimum cost in those cases.")
            price_warning.place(x = 50, y = 440)
            
        

    def saveToFile(self):
        '''
        This method will save all names and prices, as well as other information, to pc_parts.txt
        '''
        file_label = tk.Label(window, text= "Contents saved to pc_parts.txt")
        file_label.place(x = 200, y = 40)
        #makes a file to save it to
        with open('pc_parts.txt', 'w') as file:      
            #saves the date and time      
            current_date = datetime.today()
            file.write(f"PC picker results at {current_date}\n")

            #writes the names
            file.write(f"CPU: {self.cpu_result[0]}\n")
            file.write(f"Cooler: {self.cooler_result[0]}\n")
            file.write(f"Motherboard: {self.motherboard_result[0]}\n")
            file.write(f"Storage: {self.storage_result[0]}\n")
            file.write(f"Memory: {self.memory_result[0]}\n")
            file.write(f"GPU: {self.gpu_result[0]}\n")
            file.write(f"Case: {self.case_result[0]}\n")
            file.write(f"Power supply: {self.power_result[0]}\n")

            #writes the prices
            file.write(f"CPU price: {self.cpu_result[1]} \n")
            file.write(f"Cooler price: {self.cooler_result[1]} \n")
            file.write(f"Motherboard price: {self.motherboard_result[1]}\n")
            file.write(f"Storage price: {self.storage_result[1]}\n")
            file.write(f"Memory price: {self.memory_result[1]}\n")
            file.write(f"GPU price: {self.gpu_result[1]}\n")
            file.write(f"Case price: {self.case_result[1]}\n")
            file.write(f"Power supply price: {self.power_result[1]}\n")

            #writes the total price and the difference between it and the budget
            file.write(f"Total price: {round(self.total_price, 2)}\n")
            file.write(f"difference between budget and total: {round((self.budget - self.total_price), 2)}")



window = tk.Tk()
window.title('PC Builder')
window.geometry('1400x600')

budget_pc = PC_GUI(window)
pc = Picker()

window.mainloop()
