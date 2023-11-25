# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 00:54:18 2023

@author: alise
"""

#title
#URL
#which tab is open

# tab={'title:"google", url:"https://www.bing.com", tabs:[]}
import requests

tabs=[]


def open_tab():
    title_input= str(input("Insert Title: "))
    url_input= str(input("Insert URL: "))
    
    new_tab= {'title': title_input, 'url': url_input, 'sub_tabs':[], 'opened': True}
    
    for tab in tabs:
        if tab['opened'] == True:
            tab['opened'] = False
        
    tabs.append(new_tab)
    
def close_tab():
    
    # Check if there are any tabs to close
    if len(tabs) == 0:
        print("No tabs to close.")
        return
    
    print(tabs)
    try:
        tab_index_input= int(input("Insert the index of tab you want to close: "))
    except:
        print("Data is not provided")
        return
    
    if 0 <= tab_index_input < len(tabs):
        closed_tab_was_opened = False
        if tabs[tab_index_input]['opened'] == True:
            closed_tab_was_opened = True
            
        removed_tab= tabs.pop(tab_index_input) 
        
        if len(tabs) > 0 and closed_tab_was_opened == True:
            tabs[0]['opened'] = True
            
        print(f"Tab {removed_tab['title']} closed. Updated list:", tabs)
    else:
        print("Invalid index. Please insert a valid index.")
        tab_index_input= int(input("Insert the index of tab you want to close: "))
        return
    
def switch_tab():
    print(tabs)
    try:
        tab_index_input= int(input("Insert the index of tab you want to close: "))
        if 0 <= tab_index_input < len(tabs):
            html_content = requests.get(tabs[tab_index_input]['url']).content
            print(html_content)
        else:
            print('Invalid index. Please insert a valid index.')
            return
        
    except:
        for tab in tabs:
            if tab['opened'] == True:
                html_content = requests.get(tab['url']).content
                print(html_content)
                return
        print("Data is not provided")
        return
    
def display_all_tabs():
    
    # Check if there are any tabs to display
    if len(tabs) == 0:
        print("No tabs to display.")
        return
    for tab in tabs:
        print(tab["title"])
        for sub_tab in tab['sub_tabs']:
            print("--" + sub_tab['title'])

def open_nested_tabs():

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
        
        new_tab= {'title': title_input, 'url': url_input}
        tabs[parent_index]['sub_tabs'].append(new_tab)
        
        print("Nested tabs created successfully.")
    else:
        print("Invalid parent index. Please enter a valid index.")  
print(tabs)
    
def sort_all_tabs():
      border=0
      while border < len(tabs)-1: #O(n), n being the length of the list
        minIndex=border 
        for i in range(border+1, len(tabs)):
          # Compare function checks if tabs[i] is smaller than tabs[minIndex]
          if tabs[i]['title'].lower() < tabs[minIndex]['title'].lower(): #O(1), is the line that specifies the order
             minIndex=i
        #swap the two elements
        temp=tabs[border] #O(1)
        tabs[border]=tabs[minIndex]
        tabs[minIndex]=temp

        border=border+1
      # print(tabs)

def mainMenu(): 
 choice = -99  
 while choice != 9:
    print(tabs)
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
        break
    else:
        print("Invalid choice, please insert a valid option.")
        
    
mainMenu()


