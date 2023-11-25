# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 00:54:18 2023

@author: alise
"""

#title
#URL
#which tab is open

# tab={'title:"google", url:"https://www.bing.com", tabs:[]}

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


