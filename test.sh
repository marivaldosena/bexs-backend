export APP_NAME=bexsteste
export SERVER_NAME=localhost:6000
export DEBUG=False
export TESTING=True
export SQLALCHEMY_DATABASE_URI=postgresql://teste:teste@localhost:5433/bexsteste
flask drop-tables && 
flask migrate &&
flask seed &&
flask test