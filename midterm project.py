# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 00:54:18 2023

@author: alise
"""

# reference url:
    # https://stackoverflow.com/questions/42825102/how-to-save-python-dictionary-into-json-files
    # https://stackoverflow.com/questions/20199126/reading-json-from-a-file
    # https://www.geeksforgeeks.org/what-is-web-scraping-and-how-to-use-it/
    # https://www.geeksforgeeks.org/python-web-scraping-tutorial/
    
import requests
import json


tabs=[]


def open_tab(): #O(n), n being the length of tabs
    
    # Get the input for creating new tab
    title_input= str(input("Insert Title: "))
    url_input= str(input("Insert URL: "))
    # new tab dictionary
    new_tab= {'title': title_input, 'url': url_input, 'sub_tabs':[], 'opened': True}
    # close last tab opened
    for tab in tabs: #O(n), n being the length of tabs 
        if tab['opened'] == True: 
            tab['opened'] = False
    # add new tab to tabs list   
    tabs.append(new_tab)
    
    
def close_tab(): #O(n^2)
    
    # Check if there are any tabs to close
    if len(tabs) == 0: 
        print("No tabs to close.") 
        return
    
    try:
        tab_index_input= int(input("Insert the index of tab you want to close: "))
        
        # Check if the index is valid
        if 0 <= tab_index_input < len(tabs): 
            # if we are closing an opened tab, open another one if it exists
            closed_tab_was_opened = False
            if tabs[tab_index_input]['opened'] == True:
                closed_tab_was_opened = True
                
            removed_tab= tabs.pop(tab_index_input) #O(n), n being the length of tabs 
            
            if len(tabs) > 0 and closed_tab_was_opened == True:
                tabs[0]['opened'] = True
                
            print(f"Tab {removed_tab['title']} closed. Updated list:", tabs)
        else:
            print("Invalid index. Please insert a valid index.")
            tab_index_input= int(input("Insert the index of tab you want to close: "))
            return
    # if the user did not enter any input   
    except:
        for index, tab in enumerate(tabs): #O(n), n being the length of tabs 
            if tab['opened'] == True:
                tabs.pop(index)
                print('Last opened tab is closed.')
                
    
def switch_tab(): #O (m*n)
     
    try:
        tab_index_input= int(input("Insert the index of tab for displaying its content "))
        # Check if the index is valid
        if 0 <= tab_index_input < len(tabs):
            # get the html content from the url
            html_content = requests.get(tabs[tab_index_input]['url']).content #O (m), m being the time of request
            print(html_content)
        else:
            print('Invalid index. Please insert a valid index.')
            return
     # if the user did not enter any input   
    except:
        for tab in tabs: #O (n), n being the length of tabs
            if tab['opened'] == True:
                html_content = requests.get(tab['url']).content
                print(html_content)
                return
        print("The content of last opened tab is displayed.")
        return
    
    
def display_all_tabs(): #O (n+k)
    
    # Check if there are any tabs to display
    if len(tabs) == 0:
        print("No tabs to display.")
        return
    # Print the titles of all open tabs
    for tab in tabs: #O (n), n being the length of tabs
        print(tab["title"])
        # Display the sub tabs hierarchically
        for sub_tab in tab['sub_tabs']: #O (k), k being the number of sub tabs
            print("--" + sub_tab['title'])
            

def open_nested_tabs(): #O(1) 

    # Check if there are any tabs to create nested tabs
    if len(tabs) == 0:
        print("No tabs available to create nested tabs.")
        return
    
    # Get the index of the parent tab for creating nested tabs
    parent_index = int(input("Enter the index of the parent tab where you want to insert additional tabs: "))

    # Check if the parent index is valid
    if 0 <= parent_index < len(tabs):
        # Prompt the user for the titles and contents of the new tabs
        title_input= str(input("Insert Title: "))
        url_input= str(input("Insert URL: "))
        # create nested tab
        new_tab= {'title': title_input, 'url': url_input}
        tabs[parent_index]['sub_tabs'].append(new_tab)
        
        print("Nested tabs created successfully.")
    else:
        print("Invalid parent index. Please enter a valid index.")  
        
    
def sort_all_tabs(): #O(n^2)
    
    # Check if there are any tabs to sort
    if len(tabs) == 0:
        print("No tabs available to sort.")
        return
    # Selection sort
    border=0
    while border < len(tabs)-1: #O(n), n being the length of the tabs
      minIndex=border 
      for i in range(border+1, len(tabs)): #O (n), n being the length of the tabs
        if tabs[i]['title'].lower() < tabs[minIndex]['title'].lower(): 
           minIndex=i
      #swap the two elements
      temp=tabs[border] 
      tabs[border]=tabs[minIndex]
      tabs[minIndex]=temp

      border=border+1
      
      
def save_tabs():  #O(n), n being the length of the tabs
    
    file_dir = str(input("File directory: "))
    # convert to a file in JSON format
    with open(file_dir, 'w') as file:
        json.dump(tabs, file, indent= 2)  #O(n), n being the length of the tabs
        
        
def import_tabs(): #O(k), k being the size of data in json file
    
    # define global tabs 
    global tabs
    file_dir = str(input("File directory: "))
    # read JSON file and return python object
    with open(file_dir, 'r') as file:
        # assign imported data to tabs list
        tabs= json.load(file) #O(k), k being the size of data in json file
        
        
def mainMenu(): #O(n*m)
 choice = -99  
 while choice != 9: #O(n), n being the number of iteration the user inputs
    print(*tabs, sep='\n') #O(m), m being the length of tabs
    print("Enter: ")
    print("1. To open tab")
    print("2. To close tab")
    print("3. To switch tab")
    print("4. To display all tabs")
    print("5. To open nested tabs")
    print("6. To sort all tabs")
    print("7. To save tabs")
    print("8. To import tabs")
    print("9. To exit")

 
    choice = int(input("Choice: "))
    
    
    if choice==1:
        open_tab()
    elif choice==2:
        close_tab()
    elif choice==3:
        switch_tab()
    elif choice==4:
        display_all_tabs()
    elif choice==5:
        open_nested_tabs()
    elif choice==6:
        sort_all_tabs()
    elif choice==7:
        save_tabs()
    elif choice==8:
        import_tabs()
    elif choice==9:
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice, please insert a valid option.")
        
    
mainMenu()


