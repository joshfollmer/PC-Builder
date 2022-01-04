import operator
import mechanicalsoup


class Picker:
    def __init__(self):
        #this is here so it doesnt give an indented block error
        self = self

    #technically i could do this in the GUI class, but i wanted this to also work as a standalone class
    def splitBudget(self, budget, cpu_b, cooler_b, motherboard_b, storage_b, memory_b, gpu_b, case_b, power_b):
        '''
        Method to split the budget into sections and return the result
        '''
        cpu_budget = budget * cpu_b
        cooler_budget = budget * cooler_b
        motherboard_budget = budget * motherboard_b
        storage_budget = budget * storage_b
        memory_budget = budget * memory_b
        gpu_budget = budget * gpu_b
        case_budget = budget * case_b
        power_supply_budget = budget * power_b

     

        return [cpu_budget, cooler_budget, motherboard_budget,storage_budget, memory_budget, gpu_budget, case_budget, power_supply_budget]



    def pickPart(self, webpage, part_budget):
        """
        Method to parse name and prices, find the highest price under the given budget, and return that 
        product's name and price
        """
        URL = webpage
        browser = mechanicalsoup.Browser()
        page = browser.get(URL)

        #finds all the prices and names on the page
        soup_prices = page.soup.find_all('li', class_ = 'price-current')
        soup_names = page.soup.find_all('a', class_ = 'item-title')
        #makes lists to put them into
        prices = []
        names = []

       #first puts the names and prices into their lists
        for content in soup_prices:
            #theres a lot going on in this line. First, it selects the text of the prices, which looks like '$544.95\xa0(2 Offers)–'. Then it partitions up the string by the '/xa0'
            #and selects the first part of the list, the prices itself. then it selects everything after the 0 index, which is always a '$', and appends to a list
            prices.append((content.getText().rpartition('\xa0')[0][1:]))
        for content in soup_names:
            names.append((content.getText()))

        #combines the lists like a zipper
        pairs = zip(names, prices)
        #makes a dictionary where the names are the keys and prices are the values
        pairs = dict(pairs)
        
        #Ill be using this every time the dictionary changes length, so that it can be used for a loop that will modify the length
        new_pairs = pairs.copy()
        
        #needs to get rid of empty(out of stock) items
        for i in new_pairs:
            #if a value is empty
            if not pairs[i]:
                #gets rid of the value and key
                pairs.pop(i)
            else:
                #for prices over 1000, they have a comma that needs to be removed before it can be converted
                if ',' in pairs[i]:
                    pairs[i] = pairs[i].replace(',', '')
                    pairs[i] = float(pairs[i])
                else:
                    pairs[i] = float(pairs[i])
            
        #sorts from largest to smallest, need to find the source
        pairs = dict(sorted(pairs.items(), key=operator.itemgetter(1),reverse=True))
        #copies the new list to use in a new loop
        new_pairs = pairs.copy()

        #i wrote this just because of thermal paste thats listed on the same page as the coolers
        #if something is less than 13 dollars, it gets taken out
        for i in new_pairs:
            if pairs[i] < 13:
                pairs.pop(i)
        new_pairs = pairs.copy()

        #this will get rid of all  values greater than the passed budget
        for i in new_pairs:
            if pairs[i] > part_budget:
                pairs.pop(i)
                if len(pairs) == 1:
                    break

        #borrowed from https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
        #this will sort the values from smallest to largest, but im not actually sure how
        pairs = dict(sorted(pairs.items(), key = lambda x:x[1]))

        #returns the name was [0], and the price as [1]
        return [list(pairs.keys())[-1], list(pairs.values())[-1]]
