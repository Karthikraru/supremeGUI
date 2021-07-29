import tkinter
from info import keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    StaleElementReferenceException
from selenium import webdriver
import time

class bot:
    def __init__(self, master):
        self.master = master
        self.main = tkinter.Frame(self.master, background='grey')
        self.main.pack(fill=tkinter.BOTH, expand=True)

        self.logText = tkinter.StringVar()
        self.logText.trace('w', self.build_log)

        self.build_grid()
        self.build_logo()
        self.build_categories()
        self.build_category_input()
        self.build_log()

    def build_grid(self):
        self.main.columnconfigure(0, weight=0)
        self.main.columnconfigure(1, weight=1)
        self.main.rowconfigure(0, weight=0)
        self.main.rowconfigure(1, weight=0)
        self.main.rowconfigure(2, weight=0)
        self.main.rowconfigure(3, weight=0)
        self.main.rowconfigure(4, weight=0)
        self.main.rowconfigure(5, weight=0)
        self.main.rowconfigure(6, weight=0)
        self.main.rowconfigure(7, weight=0)
        self.main.rowconfigure(8, weight=1)

    def build_log(self, *args):
        log = tkinter.Label(self.main, background='dark grey', foreground='white', text=self.logText.get(), font=30)
        log.grid(row=8, column=1, sticky='nsew', pady=10, padx=10)

    def build_logo(self):
        self.logo = tkinter.Label(self.main, background='red', foreground='white', text='Supreme Bot', font=(40))
        self.logo.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)

    def build_categories(self):
        self.category = tkinter.Label(self.main, background='dark grey', foreground='white', text="Category: ", font=(30))
        self.productName = tkinter.Label(self.main, background='dark grey', foreground='white', text="Product Name: ", font=(30))
        self.productColor = tkinter.Label(self.main, background='dark grey', foreground='white', text="Product Color: ", font=(30))
        self.size = tkinter.Label(self.main, background='dark grey', foreground='white', text="Product Size: ", font=(30))
        self.refreshDelay = tkinter.Label(self.main, background='dark grey', foreground='white', text="Refresh Delay: ", font=(30))
        self.restockDelay = tkinter.Label(self.main, background='dark grey', foreground='white', text="Restock Delay: ", font=(30))
        log = tkinter.Label(self.main, background='dark grey', foreground='white', text="Log: ", font=(30))

        self.category.grid(row=1, column=0, sticky='nsew', pady=10, padx=10)
        self.productName.grid(row=2, column=0, sticky='nsew', pady=10, padx=10)
        self.productColor.grid(row=3, column=0, sticky='nsew', pady=10, padx=10)
        self.size.grid(row=4, column=0, sticky='nsew', pady=10, padx=10)
        self.refreshDelay.grid(row=5, column=0, sticky='nsew', pady=10, padx=10)
        self.restockDelay.grid(row=6, column=0, sticky='nsew', pady=10, padx=10)
        log.grid(row=8, column=0, sticky='nsew', pady=10, padx=10)

        self.submitButton = tkinter.Button(self.main, bg='red', foreground='red', text='Create and Start Task', command=self.startTask)
        self.submitButton.grid(row=7, column=1, sticky='nsew', pady=10, padx=10)

    def build_category_input(self):
        self.categoryInput = tkinter.Entry(self.main, width=50, background='dark grey', borderwidth=0)
        self.productNameInput = tkinter.Entry(self.main, width=50, background='dark grey', borderwidth=0)
        self.productColorInput = tkinter.Entry(self.main, width=50, background='dark grey', borderwidth=0)
        self.sizeInput = tkinter.Entry(self.main, width=50, background='dark grey', borderwidth=0)
        self.refreshDelayInput = tkinter.Entry(self.main, width=50, background='dark grey', borderwidth=0)
        self.restockDelayInput = tkinter.Entry(self.main, width=50, background='dark grey', borderwidth=0)

        self.categoryInput.grid(row=1, column=1, sticky='nsew', pady=10, padx=10)
        self.productNameInput.grid(row=2, column=1, sticky='nsew', pady=10, padx=10)
        self.productColorInput.grid(row=3, column=1, sticky='nsew', pady=10, padx=10)
        self.sizeInput.grid(row=4, column=1, sticky='nsew', pady=10, padx=10)
        self.refreshDelayInput.grid(row=5, column=1, sticky='nsew', pady=10, padx=10)
        self.restockDelayInput.grid(row=6, column=1, sticky='nsew', pady=10, padx=10)

    def validateInput(self, cat, refresh, restock):
        categoryInput = True
        # Cat = category
        cat = cat.lower()
        if (cat == 'jackets') or (cat == 'shirts') or (cat == 'tops/sweaters') or (cat == 'sweatshirts') or (
                cat == 'pants') or (cat == 't-shirt') or (cat == 'hats') or (cat == 'bags') or (
                cat == 'accessories') or (cat == 'skate') or (cat=='shoes'):
            pass
        else:
            self.logText.set('Category: Invalid. Note: Must be typed exactly as seen on site\n')
            categoryInput = False


        try:
            refresh = float(refresh)
        except ValueError:
            self.logText.set(
                '{}Refresh Delay: Invalid. Must be in seconds- Ex: .5\n'.format(self.logText.get()))
            categoryInput = False

        try:
            restock = float(restock)
        except ValueError:
            self.logText.set(
                '{}Restock Delay: Invalid. Must be in seconds- Ex: .5\n'.format(self.logText.get()))
            categoryInput = False

        return categoryInput

    def startTask(self):
        self.logText.set("")
        cat = self.categoryInput.get()
        prod = self.productNameInput.get()
        color = self.productColorInput.get()
        size = self.sizeInput.get()
        refresh = self.refreshDelayInput.get()
        restock = self.restockDelayInput.get()
        if(self.validateInput(cat, refresh, restock)):
            refresh = float(refresh)
            restock = float(restock)
            driver = webdriver.Chrome('./chromedriver')
            #Log into gmail. Disabled at the moment due to changes in google security.
            '''
            driver.get("https://www.google.com/")
            while True:
                try:
                    driver.find_element_by_xpath('//*[@id="gb"]/div/div[2]/a').click()
                    break
                except ElementNotInteractableException:
                    pass
                except StaleElementReferenceException:
                    pass
                except NoSuchElementException:
                    pass
            while True:
                try:
                    driver.find_element_by_xpath('//INPUT[@id="identifierId"]').send_keys(keys['emailUser'])
                    break
                except ElementNotInteractableException:
                    pass
                except StaleElementReferenceException:
                    pass
                except NoSuchElementException:
                    pass
            driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
            while True:
                try:
                    driver.find_element_by_xpath('//INPUT[@type="password"]').send_keys(keys['emailPass'])
                    driver.find_element_by_xpath("(//DIV[@class='VfPpkd-RLmnJb'])[1]").click()
                    break
                except ElementNotInteractableException:
                    pass
                except StaleElementReferenceException:
                    pass
            #Logged in
            '''
            driver.get('https://www.supremenewyork.com/shop/all/{}'.format(cat))
            # Click Product
            while True:
                try:
                    driver.find_element_by_partial_link_text(prod).click()
                    break
                except NoSuchElementException:
                    driver.refresh()
                    time.sleep(refresh)
                    pass

            start = int(round(time.time() * 1000))
            # Pick Color
            iterationVar = 1
            while True:
                try:
                    if color == "":
                        break
                    color = driver.find_element_by_xpath('//*[@id="details"]/ul/li[{}]/button[1]'.format(iterationVar))
                    if color.get_attribute("data-style-name") == color:
                        color.click()
                        if color.get_attribute('data-sold-out') == 'false':
                            break
                    else:
                        iterationVar = iterationVar + 1
                except NoSuchElementException:
                    pass
                end = int(round(time.time() * 1000))
                if (end - start) / 1000 > 2:
                    print('tim out')
                    break
                print('wrong color')

            #Pick size
            startSize = int(round(time.time() * 1000))
            while True:
                if size == '':
                    break
                try:
                    driver.find_element_by_xpath('//*[@id="s"]').click()
                    driver.find_element_by_xpath('//*[@id="s"]/option[{}]'.format(size)).click()
                    break
                except NoSuchElementException:
                    pass
                except StaleElementReferenceException:
                    pass
                endsize = int(round(time.time() * 1000))
                if (endsize - startSize) / 1000 > 1:
                    print('Timed out.')
                    break

            # Add to Cart
            while True:
                try:
                    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
                    break
                except NoSuchElementException:
                    pass
                except StaleElementReferenceException:
                    pass
                try:
                    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/b')
                    time.sleep(restock)
                    driver.refresh()
                    pass
                except NoSuchElementException:
                    pass
                except StaleElementReferenceException:
                    pass

            while True:
                try:
                    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
                    break
                except ElementNotInteractableException:
                    pass

            #Submit Info

            # Name
            driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(keys['name'])

            # Email
            driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(keys['email'])

            # PhoneNumber
            driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(keys['telephone'])

            # Address
            driver.find_element_by_xpath('//*[@id="bo"]').send_keys(keys['address'])

            # Zip
            driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(keys['zip'])

            # CardNum
            driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(keys['cardNum'])

            # CardMonth
            driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[{}]'.format(keys["cardMonth"])).click()

            # CardYear
            driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[{}]'.format(keys["cardYear"])).click()

            # CardCVV
            driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(keys["cardCVV"])

            # Terms and Conditions
            driver.find_element_by_xpath("//*[contains(text(), 'I have read and agree to the ')]").click()
            # Process Payment
            driver.find_element_by_xpath('//*[@id="pay"]/input').click()
        else:
            pass


if __name__ == '__main__':
    root = tkinter.Tk()
    root.title('Supreme Bot')
    bot(root)
    root.mainloop()
