#####################################
# Way Simpler Streamlit Application # => Version 0.1
#####################################

# Module Imports
import streamlit as st
import os,json,time
from datetime import date

# Functions
def log(report,senderFunc,repType):
    print(f"""\n----\n[{senderFunc}]\n[{date.today().strftime("%d/%m/%Y")}/(day/month/year)][{time.strftime("%H:%M:%S", time.localtime())}/{time.timezone}]\n[{repType}]{report}""")

def loadConfig(configFile): # Used for loading config.json file inside 
    try:
        with open(configFile, 'r', encoding='utf-8')  as file:
            config = json.load(file)
            log("Config Is Loaded","Func loadConfig-main.py","Info")
        return config
    except FileNotFoundError:
        log(f"Error: The file {configFile} was not found.","Func loadConfig-main.py","Error")
    except json.JSONDecodeError:
        log(f"Error: Failed to parse {configFile}. Ensure it contains valid JSON.","Func loadConfig-main.py","Error")
    except Exception as e:
        log(f"An unexpected error occurred: {e}","Func loadConfig-main.py","Error")
    return 

def findPageList(): # Gets list of pages that you wanted to put in.

    pageList = os.listdir(config["deployRules"]["pagesFolderAddress"])
    mdPageList = [file for file in pageList if file.endswith('.md')]
    nonMdPageList = [file for file in pageList if not file.endswith('.md')]

    if len(nonMdPageList) >= 1:
        log(f"Error: Files at {config["deployRules"]["pagesFolderAddress"]} adress has files that arent in correct format. Mentioned files: {nonMdPageList}","Func findPageList-main.py","Error")

    if len(mdPageList) >= 1:
        pageList=[]
        for _ in mdPageList: # Create another list for name selection.
            idealName = str(_).replace(".md","").replace("_"," ")
            pageList.append(idealName)
        log(f"Error: Files at {config["deployRules"]["pagesFolderAddress"]} adress has files that arent in correct format. Mentioned files: {nonMdPageList}","Func findPageList-main.py","Success")
        return pageList
    else:
        log(f"Error: Files with correct extention(.md) was not found in the {config["deployRules"]["pagesFolderAddress"]} adress.","Func findPageList-main.py","Error")

def readMarkdownFile(filePath):# Reads markdown files inside the proper folder. 
    try:
        with open(filePath, 'r', encoding='utf-8') as md_file:
            content = md_file.read()
        return content
    except FileNotFoundError:
        if filePath == str(config["deployRules"]["pagesFolderAddress"]+"None.md"):
            log(f"File not found: {filePath}","Func readMarkdownFile-main.py","Error")
    except Exception as e:
        log( f"An unexpected error occurred: {e}","Func readMarkdownFile-main.py","Error")
    return 

# Prep To Lunch
config = loadConfig("config.json")
pagelist = findPageList()

#Application Running

st.set_page_config(
    page_title=config["application"]["applicationName"],
    page_icon=config["application"]["pageIcon"],
    layout=config["application"]["layout"],
    initial_sidebar_state=config["application"]["initialSidebarState"]
)

st.sidebar.title(config["application"]["applicationName"])
selectedPage = st.sidebar.selectbox("Page",options=pagelist)
siteContentPlace = st.empty()
with siteContentPlace:
    st.markdown(readMarkdownFile(config["deployRules"]["pagesFolderAddress"]+"/"+str(selectedPage).replace(" ","_")+".md"))