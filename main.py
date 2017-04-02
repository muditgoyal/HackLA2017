'''
Created on Apr 1, 2017

@author: williamkhaine
'''

import tkinter as tk
from tkinter import messagebox

import data_parse 
import representative
import senator 
import gen_str 
import time 
import bill_summary

UNIV_FONT   = ("Helvetica", 14)
HEADER_FONT = ("Helvetica", 20)
SUBHEADER_FONT = ("Helvetica", 16)
INITIAL_WIDTH   = 500
INITIAL_HEIGHT  = 500
CONSTANT_BKG    = "#FFFFFF"

class CongressionalComprehension: 
    def __init__(self):
        # INITIALIZE TITLE AND WINDOW 
        self._base_win = tk.Tk()
        self._base_win.title('Congressional Comprehension')

    
        # INITIALIZE BASE CONSTANTS
        self._width = INITIAL_WIDTH
        self._height = INITIAL_HEIGHT
                
        # INITIALIZATION OF ADDDRESS REQUIRED TO MAKE FIRST DATA PULL
        self._address=""
        
        # INITIALIZATION OF DISTRICT
        self._district = 0
        
        # INITIALIZATION OF SENATORS AND REPRESENTATIVE
        self._s0 = None 
        self._s1 = None 
        self._r0 = None 
                
        # HEADER AND SUBHEADER
        self._w = tk.StringVar() 
        self._w.set("Congressional Comprehension") 
        self._welcome = tk.Label(master=self._base_win, font=HEADER_FONT, textvariable=self._w, justify=tk.CENTER)
        self._welcome.grid(row = 0, column = 0, padx = 5, pady = 3, sticky=tk.N, columnspan=2)
        
        self._w = tk.StringVar() 
        self._w.set("To track the actions of your congressional representatives,\nenter the following information.") 
        self._welcome2 = tk.Label(master=self._base_win, font=SUBHEADER_FONT, textvariable=self._w, justify=tk.CENTER)
        self._welcome2.grid(row = 1, column = 0, padx = 5, pady = 3, sticky=tk.N, columnspan=2)
                
        # INITIALIZATION OF DISTRICT
        self._district = 0
        
        # REQUEST TEXTS
        self._house_num_prompt = tk.StringVar() 
        self._house_num_prompt.set("Enter your residence number") 
        self._house_num_text = tk.Label(master = self._base_win, font = UNIV_FONT, textvariable = self._house_num_prompt)
        self._house_num_text.grid(row = 2, column = 0, padx = 5, pady = 3)
                
        self._street_address_prompt = tk.StringVar() 
        self._street_address_prompt.set("Enter your street address") 
        self._street_address_text = tk.Label(master = self._base_win, font = UNIV_FONT, textvariable = self._street_address_prompt)
        self._street_address_text.grid(row = 3, column = 0, padx = 5, pady = 3)
        
        self._city_prompt = tk.StringVar() 
        self._city_prompt.set("Enter your city name") 
        self._city_prompt_text = tk.Label(master = self._base_win, font = UNIV_FONT, textvariable = self._city_prompt)
        self._city_prompt_text.grid(row = 4, column = 0, padx = 5, pady = 3)
        
        self._state_prompt = tk.StringVar() 
        self._state_prompt.set("Enter your state") 
        self._state_prompt_text = tk.Label(master = self._base_win, font = UNIV_FONT, textvariable = self._state_prompt)
        self._state_prompt_text.grid(row = 5, column = 0, padx = 5, pady = 3)

        self._zip_code_prompt = tk.StringVar() 
        self._zip_code_prompt.set("Enter your ZIP code") 
        self._zip_code_prompt_text = tk.Label(master = self._base_win, font = UNIV_FONT, textvariable = self._zip_code_prompt)
        self._zip_code_prompt_text.grid(row = 6, column = 0, padx = 5, pady = 3)

        # ENTRY BOXES
        self._house_num_response = tk.Entry(master=self._base_win)
        self._house_num_response.grid(row = 2, column = 1, padx = 5, pady = 3)

        self._street_response = tk.Entry(master=self._base_win)
        self._street_response.insert(0, "e.x. N Highland St")
        self._street_response.grid(row = 3, column = 1, padx = 5, pady = 3)

        self._city_response = tk.Entry(master=self._base_win)
        self._city_response.grid(row = 4, column = 1, padx = 5, pady = 3)

        self._state_response = tk.Entry(master=self._base_win)
        self._state_response.insert(0, "A two letter abbreviation")
        self._state_response.grid(row = 5, column = 1, padx = 5, pady = 3)
        
        self._zip_code_response = tk.Entry(master=self._base_win)
        self._zip_code_response.insert(0,"A five digit integer")
        self._zip_code_response.grid(row = 6, column = 1, padx = 5, pady = 3)

        self._base_win.rowconfigure(0, weight = 1)        
        self._base_win.rowconfigure(1, weight = 1)
        self._base_win.rowconfigure(2, weight = 1)
        self._base_win.rowconfigure(3, weight = 1)
        self._base_win.columnconfigure(0, weight = 1)

        # BUTTON
        self._confirm_address = tk.Button(master = self._base_win, text="Get Updates", relief=tk.GROOVE)
        self._confirm_address.grid(row=7, column=0, columnspan=2, sticky=tk.SE, padx=10, pady=10)
        self._confirm_address.bind('<Button-1>', self._primary_button_clicked)
        
        self._base_win.rowconfigure(0, weight = 1)        
        self._base_win.rowconfigure(1, weight = 1)
        self._base_win.rowconfigure(2, weight = 1)
        self._base_win.rowconfigure(3, weight = 1)
        self._base_win.rowconfigure(4, weight = 1)
        self._base_win.rowconfigure(5, weight = 1)
        self._base_win.rowconfigure(6, weight = 1)

        self._base_win.columnconfigure(0, weight = 1)
        self._base_win.columnconfigure(1, weight = 3)
        
    def _primary_button_clicked(self, e: tk.Event):
        
        if (self._address_valid()): 
            self._can_query = True             
            print("All values valid")
            
            _house_num      = self._house_num_response.get().rstrip() + " "
            _street_address = self._street_response.get().rstrip()+ ", "
            _city           = self._city_response.get().rstrip()+ ", "
            _state_abbrv    = self._state_response.get().rstrip()+ " "
            _zip_code       = self._zip_code_response.get().rstrip()+ " "

            self._address = _house_num + _street_address + _city + _state_abbrv + _zip_code
            print(self._address)
            
            time.sleep(5)
        
            self.make_requests()    
    
    def _address_valid(self):
        valid = True
        
        street_num = self._house_num_response.get().rstrip()
        street_name = self._street_response.get().rstrip()
        city = self._city_response.get().rstrip()
        st_abbrv = self._state_response.get().rstrip()
        zip_code = self._zip_code_response.get().rstrip()
        
        # Test 1: Empty entries
        if street_num == "":
            messagebox.showerror("Error", "Street number field is empty")
            valid = False
        elif street_name == "":
            messagebox.showerror("Error", "Street field is empty")
            valid = False
        elif city == "":
            messagebox.showerror("Error", "City field is empty")
            valid = False
        
        # Test 1 and Test 2: Values are valid 
        elif (len(st_abbrv)) != 2:
            messagebox.showerror("Error", "State field should be 2 characters, not " + str(len(st_abbrv)))
            valid = False
        else:
            if (len(zip_code)) != 5: 
                messagebox.showerror("Error", "Zip Code field should be 5 integers, not " + str(len(zip_code)))
                valid = False
            else:
                try: 
                    int(zip_code)
                except: 
                    messagebox.showerror("Error", "Zip Code field should be 5 integers, not " + zip_code)
                    valid = False
        
        return valid 

        
    def make_requests(self):  
        _state_abbrv = (self._state_response.get().rstrip())
        self._clear_window()
        
        self._district = data_parse.DistrictImport(self._address).get_district_number()
         
        print("Initializing politician objects")

        self._r0 = representative.Representative(str(self._district), _state_abbrv)
        self._s0 = senator.Senator(_state_abbrv, 0)
        self._s1 = senator.Senator(_state_abbrv, 1)

        self._display_political_query_done()
        self._base_win.geometry("1000x600")
        self._base_win.minsize(1000, 600)


        print("Done querying for politicians")
        
        self._display_politicians() 
        
        print("Politicans displayed")

        self._display_votes()
        
        print("Voting history displayed")

    
    
    def _clear_window(self):
        self._house_num_response.destroy()
        self._house_num_text.destroy()
        self._street_response.destroy()
        self._street_address_text.destroy()
        self._city_response.destroy() 
        self._city_prompt_text.destroy()
        self._state_response.destroy() 
        self._state_prompt_text.destroy()
        self._zip_code_response.destroy()
        self._zip_code_prompt_text.destroy()
        self._welcome2.destroy()
        self._welcome.destroy()
        self._confirm_address.destroy()

    
    def _display_political_query_done(self):
        self._politican_confirmation = tk.StringVar() 
        self._politican_confirmation.set("Your request has been completed")
        self._politican_confirmation_l = tk.Label(master=self._base_win, font=UNIV_FONT, 
                                                       textvariable=self._politican_confirmation.set)
        self._politican_confirmation_l.grid(row = 0, column = 0, padx = 10, pady = 5, sticky=tk.N, columnspan=2)

        
        
    def _display_politicians(self):
        self._politican_confirmation_l.grid_forget()
        rep_name = tk.StringVar() 
        rep_name.set(self._r0.get_name() + "\nRepresentative, District " + str(self._district) + "-" + self._address[-9:-7].upper())
        rep = tk.Label(master=self._base_win, font=UNIV_FONT, textvariable=rep_name)
        rep.grid(row = 0, column = 0, padx = 10, pady = 5, sticky=tk.E + tk.W + tk.N)
        rep.grid_propagate(0)

        sen0_name = tk.StringVar() 
        sen0_name.set(self._s0.get_name() + "\nSenator, " + self._address[-9:-7].upper())
        sen0 = tk.Label(master=self._base_win, font=UNIV_FONT, textvariable=sen0_name)
        sen0.grid(row = 0, column = 1, padx = 10, pady = 5, sticky=tk.E + tk.W + tk.N)
        sen0.grid_propagate(0)

        
        sen1_name = tk.StringVar() 
        sen1_name.set(self._s1.get_name() + "\nSenator, " + self._address[-9:-7].upper())
        sen1 = tk.Label(master=self._base_win, font=UNIV_FONT, textvariable=sen1_name)
        sen1.grid(row = 0, column = 2, padx = 10, pady = 5, sticky=tk.E + tk.W + tk.N)        
        sen1.grid_propagate(0)
        
        self._base_win.columnconfigure(0, weight = 1)
        self._base_win.columnconfigure(1, weight = 1)
        self._base_win.columnconfigure(2, weight = 1)


    def _display_votes(self):
        law_font = ("Helvetica", 10)
        
        s0_dates, s0_indiv_vote , _, s0_bill_name , s0_chamber_vote =   self._s0.get_votes()
        s1_dates, s1_indiv_vote , _, s1_bill_name , s1_chamber_vote =   self._s1.get_votes()
        r0_dates, r0_indiv_vote ,_, r0_bill_name , r0_chamber_vote =    self._r0.get_votes()

        # make something that is scrollable
        self._base_win.rowconfigure(0, weight = 4)

        self.summaries = dict()

        i = 1
        x = "a"
        while i < 15:
            sv_r0 = gen_str.gen_ind_vote(r0_indiv_vote[i]) + ": " + gen_str.fix(r0_bill_name[i]) + "\nDate: " \
                      + gen_str.create_nat_lang_date(r0_dates[i]) + "\n"+ gen_str.gen_chamber_vote(r0_chamber_vote[i])
            
            m_r0 = tk.Message(master=self._base_win, text=sv_r0, justify=tk.LEFT, font=law_font, width=300,
                              relief=tk.RAISED) 
            m_r0.grid(row=i, column=0, padx=1, pady=1, sticky=tk.W+tk.N)
            m_r0.bind("<1>", self._r0_bill_selected)
            self.summaries[m_r0] = (i, x)            
            
            i += 1
            sv_s0 = (gen_str.gen_ind_vote(s0_indiv_vote[i]) + ": " + gen_str.fix(s0_bill_name[i])+ "\nDate: " \
                      + gen_str.create_nat_lang_date(s0_dates[i]) + "\n"+ gen_str.gen_chamber_vote(s0_chamber_vote[i]))
            m_s0 = tk.Message(master=self._base_win, text=sv_s0, justify=tk.LEFT, font=law_font, width=300, 
                              relief=tk.RAISED) 
            m_s0.grid(row=i-1, column=1, padx=1, pady=1, sticky=tk.W+tk.N) 
            m_s0.bind("<1>", self._s0_bill_selected)
            self.summaries[m_s0] = (i, x)

            i += 1
            sv_s1 = (gen_str.gen_ind_vote(s1_indiv_vote[i]) +": " + gen_str.fix(s1_bill_name[i]) + "\nDate: " \
                      + gen_str.create_nat_lang_date(s1_dates[i]) + "\n"+ gen_str.gen_chamber_vote(s1_chamber_vote[i]))
            m_s1 = tk.Message(master=self._base_win, text=sv_s1, justify=tk.LEFT, font=law_font, width=300, 
                              relief=tk.RAISED) 
            m_s1.grid(row=i-2, column=2, padx=1, pady=1, sticky=tk.W+tk.N) 
            m_s1.bind("<1>", self._s1_bill_selected)
            self.summaries[m_s1] = (i, x)

            self._base_win.rowconfigure(i-2, weight = 0)

            i += 1
            x += "a"
            
        print(self.summaries)
        
    
    def _s0_bill_selected(self, e):
        try: 
            bill_summary.BillSummary(self._s0, self.summaries[e.widget][0]).run()
        except: 
            pass
        print("{},{}".format(e.x,e.y))
    def _s1_bill_selected(self, e):
        try: 
            bill_summary.BillSummary(self._s1, self.summaries[e.widget][0]).run()
        except: 
            pass
        print("{},{}".format(e.x,e.y))
    def _r0_bill_selected(self, e):
        try: 
            bill_summary.BillSummary(self._r0, self.summaries[e.widget][0]).run()
        except: 
            pass
        print("{},{}".format(e.x,e.y))
    def run(self):
        self._base_win.mainloop()    


if __name__ == "__main__":
    cc = CongressionalComprehension()
    cc.run()
