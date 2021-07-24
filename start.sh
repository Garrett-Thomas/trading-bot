#!/bin/zsh
cd client
npm run start &
cd ..
nodemon server.js &

