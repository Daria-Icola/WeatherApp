# Установка и настройка веб-сервера Торнадо#

# Установка виртуальной среды
pip install virtualenv
# Создание виртуальной среды с названием Electron
virtualenv Electron
# Активация виртуальной среды
source Electron/bin/activate
# Установка Торнадо
pip install tornado

# Установка библиотеки с погодой
pip install pyowm
# Установка библиотеки с датой
pip install DateTime


#####################
# Установка Node.js
curl "https://nodejs.org/dist/latest/node-${VERSION:-$(wget -qO- https://nodejs.org/dist/latest/ | sed -nE 's|.*>node-(.*)\.pkg</a>.*|\1|p')}.pkg" > "$HOME/Downloads/node-latest.pkg" && sudo installer -store -pkg "$HOME/Downloads/node-latest.pkg" -target "/"
# Установка Electron
npm install --save-dev electron

# Запуск приложения
npm start





