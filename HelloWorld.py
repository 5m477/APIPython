#Import the required module to handle Windows API Calls
import ctypes

#Grab a handle to User32.dll $ kernel32.dll
user_handle = ctypes.WinDLL ("User32.dll")
k_handle = ctypes.WinDLL("Kernel32.dll")


#Win API Calls
#Int MessageBoxA(
#HWND hWnd,
#LPCSTR lpText,
#LPCSTR lpCaption,
#UINT, uType
#);

# setting up the params
hWnd = None
lpText = "Hello World"
lpCaption = "Hello Students!"
uType = 0x00000001

# Calling the windows API Call
response = user_handle.MessageBoxW(hWnd, lpText, lpCaption, uType) 

#Check for Errors
error = k_handle.GetLastError()
if error !=0:
    print ("Error Code: (0)".format(error))
    ext(1)
if response == 1:
    print("Student Clicked Okay!")
elif response == 2:
    print("Student Clicked Cancel")