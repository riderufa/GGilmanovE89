1. mkdir someapp
2. cd someapp
3. git init
4. git pull https://github.com/riderufa/GGilmanovE89
5. sudo docker-compose build
6. sudo docker-compose up
7. Из другого терминала, не закрывая предыдущий, sudo docker exec -it someapp_db_1 psql -U postgres -c "create database test"
8. Из предыдущего терминала ^C
9. sudo docker-compose up