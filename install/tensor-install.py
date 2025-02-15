
import os
import sys
import pkg_resources

# see what we have
installed = {pkg.key for pkg in pkg_resources.working_set}

os.system("sudo apt update")

cmd = "sudo apt-get -y install python3.6-distutils"
os.system(cmd)

if os.path.exists("/usr/bin/pip3") is False and os.path.exists("/usr/local/bin/pip3") is False:
   os.system("./install-pip.sh")

os.system("sudo python3 -m pip install --upgrade pip")

# pip3.6 
if os.path.exists("/home/ams/amscams/install/get-pip36.py") is False:
   print("GET PIP FOR PYTHON3.6")
   cmd = "wget https://bootstrap.pypa.io/pip/3.6/get-pip.py -O /home/ams/amscams/install/get-pip36.py"
   os.system(cmd)
   cmd = "sudo python3.6 get-pip36.py"
   os.system(cmd)

   os.system("sudo python3.6 -m pip install --upgrade pip")

cmd = "sudo python3.6 get-pip36.py"
print(cmd)
os.system(cmd)




cmd = "sudo apt-get -y install p7zip-full"
os.system(cmd)

if os.path.exists("tensorflow-installed.txt") :
   print("python3.6 with tensorflow is already installed.")

if os.path.exists("/usr/bin/python3.6") is False and os.path.exists("/usr/local/bin/python3.6") is False:
   print("NO PYTHON3.6 INSTALL IT.")
   cmd = "sudo add-apt-repository -y ppa:deadsnakes/ppa"
   os.system(cmd)
   cmd = "sudo apt-get update"
   os.system(cmd)
   cmd = "sudo apt-get -y install python3.6"
   os.system(cmd)

  
if os.path.exists("/home/ams/amscams/install/get-pip36.py") is False:
   print("GET PIP FOR PYTHON3.6")
   cmd = "wget https://bootstrap.pypa.io/pip/3.6/get-pip.py -O /home/ams/amscams/install/get-pip36.py"
   os.system(cmd)
   cmd = "sudo python3.6 get-pip36.py"
   os.system(cmd)

   os.system("sudo python3.6 -m pip install --upgrade pip")
else:
   if "pip" not in installed:
       cmd = "sudo python3.6 get-pip36.py"
       print(cmd)
       os.system(cmd)

#   cmd = "sudo python3.6 get-pip36.py"
#   os.system(cmd)



if os.path.exists("tensorflow-2.4.4-cp36-cp36m-linux_x86_64.whl") is False:
   cmd = "wget https://archive.allsky.tv/AMS9/tensorflow-2.4.4-cp36-cp36m-linux_x86_64.whl"
   os.system(cmd)

try:
   cmd = "sudo python3.6 -m pip install /home/ams/amscams/install/tensorflow-2.4.4-cp36-cp36m-linux_x86_64.whl"
   os.system(cmd)
except:
   print("FAILED TO INSTALL tensorflow!")
   
   
if False:
   cmd = "sudo python3.6 -m pip install --upgrade pillow"
   os.system(cmd)
   cmd = "sudo python3.6 -m pip install --upgrade opencv-python"
   os.system(cmd)
   cmd = "sudo python3.6 -m pip install --upgrade ephem"
   os.system(cmd)
   cmd = "sudo python3.6 -m pip install --upgrade requests"
   os.system(cmd)
   
   
   
   cmd = "sudo python3.6 -m pip install tensorboard"
   os.system(cmd)
   cmd = "sudo python3.6 -m pip install tb-nightly"
   os.system(cmd)
   
   cmd = "sudo python3.6 -m pip install pillow"
   os.system(cmd)
   
   cmd = "sudo python3.6 -m pip install scikit-learn"
   os.system(cmd)
   
   cmd = "sudo python3.6 -m pip install scikit-image"
   os.system(cmd)
   
   cmd = "sudo python3.6 -m pip install pyephem"
   os.system(cmd)
   
   
   cmd = "sudo python3.6 -m pip install scikit-image"
   os.system(cmd)
   
   cmd = "sudo python3.6 -m pip install opencv-python"
   os.system(cmd)
   
   cmd = "sudo python3.6 -m pip install --force-reinstall --upgrade flask"
   os.system(cmd)
   cmd = "sudo python3.6 -m pip install --force-reinstall --upgrade flask_httpauth"
   os.system(cmd)
   cmd = "sudo python3.6 -m pip install requests"
   os.system(cmd)
   
   
   cmd = "sudo python3 -m pip install --force-reinstall --upgrade pillow"
   os.system(cmd)
   cmd = "sudo python3 -m pip install --force-reinstall --upgrade markupsafe"
   os.system(cmd)
   cmd = "sudo python3 -m pip install --force-reinstall --upgrade flask"
   os.system(cmd)
   cmd = "sudo python3 -m pip install --force-reinstall --upgrade Click" 
   os.system(cmd)
   cmd = "sudo python3 -m pip install --force-reinstall --upgrade six"
   os.system(cmd)
   cmd = "sudo python3 -m pip install --force-reinstall --upgrade requests"
   os.system(cmd)
   cmd = "sudo python3 -m pip install --force-reinstall --upgrade flask_httpauth"
   os.system(cmd)
   
   cmd = "touch tensorflow-installed.txt"
   os.system(cmd)
   
   
if os.path.exists("/home/ams/amscams/pipeline/models") is False:
   os.makedirs("/home/ams/amscams/pipeline/models")

cmd = "sudo chown -R ams:ams /home/ams/amscams/pipeline/models"
os.system(cmd)

if os.path.exists("/home/ams/amscams/pipeline/models/ASAI-v2.7z") is False:

   cmd = """sudo su -c "cp /mnt/archive.allsky.tv/AMS1/ML/ASAI-v2.7z /home/ams/amscams/pipeline/models/" -s /bin/sh ams"""
   print(cmd)
   os.system(cmd)

   cmd = """sudo su -c "cp /mnt/archive.allsky.tv/AMS1/ML/star_yn.h5 /home/ams/amscams/pipeline/models/" -s /bin/sh ams"""
   print(cmd)
   os.system(cmd)

   cmd = "cd /home/ams/amscams/pipeline/models; 7z e /home/ams/amscams/pipeline/models/ASAI-v2.7z"
   print(cmd)
   os.system(cmd)
   cmd = "chown -R ams:ams /home/ams/amscams/pipeline/models"
   print(cmd)
   os.system(cmd)
else:
   print("MODELS UP TO DATE ALREADY?")


cmd = "sudo python3 pipper.py"
print(cmd)
os.system(cmd)

cmd = "sudo python3.6 pipper.py"
print(cmd)
os.system(cmd)

