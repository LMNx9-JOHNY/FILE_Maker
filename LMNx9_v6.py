import os,sys,platform,time
v6 = platform.architecture()[0]
if v6 == '64bit':import FILE_MAKER_v6
elif v6 == '32bit':
    os.system("clear")
    os.system('xdg-open https://t.me/TEAM_LMNx9')
    time.sleep(3)
    sys.exit("\n</> Your Device Is Not Supported For Run This Tool..!")
else:
    os.system("clear")
    sys.exit("\n</> Something Went Wrong..! Try Again")
    
