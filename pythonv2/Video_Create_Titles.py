import sys, os
from lib.Video_Title_cv import *    


AMS_ALLSKY_INTRO = "/home/ams/amscams/dist/vids/AMS_ALLSKY.mp4"


if __name__ == "__main__":
    
   if(len(sys.argv)>1):
      cmd = sys.argv[1] 
      #os.system("clear")
   else:
      print("SELECT AN OPTION: main_title, title, allskycams or operators")
      sys.exit()

   if(cmd=="main_title"):
     
      _title         = input("Enter main title: ")  
      _credits       = input("Enter subtitle: ")
      _output_path   = input("Destination (ex: /mnt/ams2/test.mp4): ")
      _size          = input("Type 1 for 1920x108 or 2 for 1280x720: ") or "1"


      _color   = (255,255,255,255) # Optional - it's white by default
      _with_ams_logo_animation   = False
      _with_line_animation       = True # Optional - it's True by default
       
 
      print("Creating the video...")
      create_title_video(_title,_credits,_output_path,_color,_with_ams_logo_animation,_with_line_animation)
      #os.system("clear")

      _add_intro =  'y'
      
      if(_add_intro== 'y'):
         cmd = """ffmpeg -y  -i """+AMS_ALLSKY_INTRO+""" -c copy -bsf:v h264_mp4toannexb -f mpegts /mnt/ams2/intermediate1.ts"""
         os.system(cmd)
         cmd = """ffmpeg -y  -i """+_output_path+""" -c copy -bsf:v h264_mp4toannexb -f mpegts /mnt/ams2/intermediate2.ts"""
         os.system(cmd)         
         cmd = """ffmpeg -y  -i "concat:/mnt/ams2/intermediate1.ts|/mnt/ams2/intermediate2.ts" -c copy -bsf:a aac_adtstoasc """ + _output_path
         os.system(cmd)  
         cmd = """rm -f /mnt/ams2/*.ts"""
         os.system(cmd)  

      if(_size=='2'):
         # Get file name based on path
         filename = os.path.splitext(_output_path)[0]+'1280.mp4'
         resize(_output_path,filename,1280)
         cmd = "rm -f " + _output_path
         os.system(cmd)  
         cmd = "mv " + filename +  " " + _output_path
         os.system(cmd)  

      #os.system("clear")
      print("FILE CREATED: " + _output_path)
       

   elif(cmd=="title"):
      
      _title   = input("Enter main title: ") 
      _subtitle = input("Enter subtitle: ")
      _output_path   = input("Destination: ")
      _size          = input("Type 1 for 1920x108 or 2 for 1280x720: ") or "1"
      print("Creating the video...")
      create_simple_title_video(_title,_subtitle,_output_path)

      if(_size=='2'):
         # Get file name based on path
         filename = os.path.splitext(_output_path)[0]+'1280.mp4'
         resize(_output_path,filename,1280)
         cmd = "rm -f " + _output_path
         os.system(cmd)  
         cmd = "mv " + filename +  " " + _output_path
         os.system(cmd)  

      #os.system("clear")
      print("FILE CREATED: " + _output_path)


   elif(cmd=='allskycams'):

      _title         = "Title"
      _subtitle      = "subtitle"
      _duration      = input("Enter duration in seconds:")
      _duration      = int(_duration)*25 #In frames at 25fps
      _size          = input("Type 1 for 1920x108 or 2 for 1280x720: ") or "1"
      _output_path   = input("Destination: ")
      create_allskycams_video(_title,_subtitle,_duration,_output_path)

      if(_size=='2'):
            # Get file name based on path
            filename = os.path.splitext(_output_path)[0]+'1280.mp4'
            resize(_output_path,filename,1280)
            cmd = "rm -f " + _output_path
            os.system(cmd)  
            cmd = "mv " + filename +  " " + _output_path
            os.system(cmd)  


      #os.system("clear")
      print("FILE CREATED: " + _output_path)
   
   elif(cmd== 'operators'):

      # IF YOU WANT TO CREATE A VIDEO TO THANKS THE OPERATORS:
      _operators = input("Enter each operator separated by a comma: ") 
      _operators = _operators.split(',')
      _duration = 125 # In frames at 25fps
      _output_path   = input("Destination: ")
      _size          = input("Type 1 for 1920x108 or 2 for 1280x720: ") or "1"
      _with_line_animation = True # Optional - it's True by default
      _line_height = 45 # Optional - it's 45 by default, it works well with <=12 operators (one per line)
      _operator_font_size = 30 # Optional - it's 30 by default, it works well with <=12 operators (one per line)

      create_thank_operator_video(_operators, _duration, _output_path,_with_line_animation,_line_height,_operator_font_size)

      if(_size=='2'):
            # Get file name based on path
            filename = os.path.splitext(_output_path)[0]+'1280.mp4'
            resize(_output_path,filename,1280)
            cmd = "rm -f " + _output_path
            os.system(cmd)  
            cmd = "mv " + filename +  " " + _output_path
            os.system(cmd)  
                  
      #os.system("clear")
      print("FILE CREATED: " + _output_path)
