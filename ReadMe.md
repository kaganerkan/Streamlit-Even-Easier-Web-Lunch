# Streamlit Even Easier Web Lunch (SEEWL)
## How to use it?
### Requirements
	streamlit == 1.37.1
	python_version >= 3.12

To install these requirements you need to run following command:
	
 	pip install streamlit
 
If dosent work or gives error you may try to change version after loading python 3.12 then running command:
	
 	pip install streamlit == 1.37.1


### Configuration
There is two parts of modification this program is allowing at the state it is. One is for Streamlit pages configuration and other is for my code.

**Application Configuration**
```
"application":{

        "applicationName":"Example Title",

        "pageIcon":"🌐",

        "layout":"wide",

        "initialSidebarState":"expanded"

    }
```

Here we have 4 different selections you can make.
- Application Name
	Controls the title on left top and the browser tabs name when site is opened.
- Page Icon, Layout, Initial Sidebar State
	Same as Streamlit.

**Deployment Configuration**
```
"deployRules":{

        "pagesFolderAddress":"pages"

    }
```

Here we have 4 different selections you can make.
- Pages Folder Address
	By editing this you can change name of the folder that holds pages.
