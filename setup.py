try:
  import requests
  import os

  name_dir = "Dand_Crop"
  first_dir = os.getcwd()
  try:
    os.mkdir(name_dir)
    os.chdir(name_dir)
    one_path = os.getcwd()
  except FileExistsError:
    pass


  def download_file_from_github(file_name):
    try:
      url = f"https://raw.githubusercontent.com/BSNIKYT/Background_changing_script/main/{name_file}"

      def download_file(url):
        local_filename = url.split('/')[-1]
        with requests.get(url, stream=True, allow_redirects=True) as r:
          r.raise_for_status()
          with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
              f.write(chunk)
        return local_filename

      file_name = download_file(url)
      pass
    except Exception as err:
      return err


  def update():
    file_names = ['main.py', 'setup.py']
    er = ''
    for file_name in file_names:
      er = er + "\n" + file_name + "\n" + str(
        download_file_from_github(file_name))


  #   import time
  #   time.sleep(2)
  #return er

  update()
  with open("start.bat", "w") as outfile:
    outfile.write(f"cd {os.getcwd()} \npython main.py")
    pass
  print("Установка завершена!")
  import time

  time.sleep(2)


  os.chdir(first_dir)
  os.remove(__file__)
except PermissionError as err:
  print(f"Установка не была завершена [PermissionError]: {err}")
except Exception as err:
  print(f"Установка не была завершена [Exception]: {err}")
