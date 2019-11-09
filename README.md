# mediff_challenge

> record_insertion_webapp(insertion and listing has been handled without using database)

  > steps to run record insertion web app:
  
  OS should be Linux(user should be root user) and python version should be 3.6
  
  go to source folder
  
  use commands:
  
  chmod +x install_record_dep.sh
  
  ./install_record_dep.sh

  Enabling the environment
  
  source /opt/RecordEnv/bin/activate
  
  python3 manage.py runserver 0:8080

  > how to get on browser
  
  use urls:
  
  localhost:8080/myapi/insert-record (for record insertion)
  
  localhost:8080/myapi/show-records (for listing the records)
  


