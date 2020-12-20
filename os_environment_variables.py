import os 

# set OS environment variable in ~/.bash_profile
# export DB_USER="db_user"
# export DB_PASS="db_pass_123!"

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASS')

print(db_user)
print(db_password)
