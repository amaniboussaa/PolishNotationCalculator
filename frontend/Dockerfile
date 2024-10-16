# Base image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy project files
COPY package*.json ./
COPY . .

# Install dependencies
RUN npm install

# Build the project
RUN npm run build

# Serve the app
CMD ["npm", "start"]
