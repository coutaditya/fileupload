# Building the docker image
docker build -t coutaditya/fileupload:latest .

# Running the docker container
docker run -p  5000:5000 coutaditya/fileupload:latest

# chmod +x run_container.sh => gives the necessary permissions (+x => add execute permission)
# needed to run the script