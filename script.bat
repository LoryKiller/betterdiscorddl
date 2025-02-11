@echo on
set downloadpathdiscorddl=%1
cd %downloadpathdiscorddl%
:: prova>prova.txt

pnpm install && pnpm build && echo starting injecting && pnpm inject && taskkill /f /im discord.exe && C:\Users\loren\AppData\Local\Discord\Update.exe --processStart Discord.exe && cd .. && timeout /T 3 && rmdir /s /q %downloadpathdiscorddl%