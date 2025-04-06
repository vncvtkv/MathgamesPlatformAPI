FROM node:18

WORKDIR /app

# Копируем и устанавливаем зависимости
COPY package*.json ./
RUN npm install

# Копируем исходный код и собираем
COPY . .
RUN npm run build

# Запускаем сервер для статики на порту 8000
CMD ["npx", "-y", "http-server", "-p", "8000", "dist"]