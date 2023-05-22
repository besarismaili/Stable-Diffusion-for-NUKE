# **StableDiffusion - Generating AI Images with Stable Diffusion API**

StableDiffusion for Nuke is a simple Nuke plugin that allows you to generate AI images using the stable diffusion API. This plugin is easy to use and can be integrated into your Nuke workflow seamlessly.

## **Getting Started**

### **Installing Python and Requests Module**

1. Visit the official Python website and download the latest version of Python: **[https://www.python.org/downloads/](https://www.python.org/downloads/)**
2. Run the Python installer and follow the installation wizard to install Python on your system. Remember to select the option to add Python to your system PATH during installation.
3. Open a command prompt or terminal and install the Requests module with the following command: **`pip install requests`**
4. Wait for the installation to complete.

### **Adding the Python Path to init.py file**

The init.py file is located under the path **`C:\Users\{USER}\.nuke`**, where **`{USER}`** is your Windows username.

1. Open the file called **`init.py`** in a text editor.
2. Add the following line to the **`init.py`** file, replacing the path with the path to your Python executable. For example:
    
    **`nuke.pluginAddPath("C:/Users/{USER}/AppData/Local/Programs/Python/Python311/Lib/site-packages")`**
    
3. Save the **`init.py`** file.
4. Close and reopen Nuke for the changes to take effect.

### **Setting Up Stable Diffusion API**

Before you can start using StableDiffusion, you need to set up the stable diffusion API.

1. Sign in to [Dream Studio](https://dreamstudio.ai/) (you'll need to create an account if you haven't done so already).
2. Navigate to your account settings and find the API credentials section.
3. Generate a new API key and make sure to keep it safe - you'll need it to use StableDiffusion.

More info [Platform (stability.ai)](https://platform.stability.ai/docs/getting-started/authentication)

## **Using StableDiffusion**

Once you have your API key, you can start using StableDiffusion in your Nuke workflow. Here's how to do it:

1. Copy and paste the code into Nuke Script Editor and execute the code. This will create a new node called ‘Stability’ in the Node Graph
2. A node called ‘Stability’ will appear in your Node Graph. Double-click on the node to open it.
3. Paste your stable diffusion API key into the "API Key" field on the "Account" tab.
4. Save it as a Toolset for easy access.

## **Saving StableDiffusion as a Toolset**

If you plan on using StableDiffusion frequently, you can save it as a toolset for easy access from your toolbar:

1. Right-click on the StableDiffusion node and select "Toolset" and "Create".
2. Enter a name for the toolset and click "OK".
3. The toolset will now be accessible from your toolbar. To use it, simply press 'Tab' and type the name.

## **Conclusion**

StableDiffusion is a simple tool that allows you to generate AI images using the stable diffusion API directly within Nuke. By following the steps outlined in this readme, you can effortlessly incorporate it into your Nuke workflow and start generating AI images with just a few clicks.
