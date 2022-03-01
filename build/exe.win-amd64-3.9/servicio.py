import psutil, os        

if __name__ == '__main__':
    while True:
        activo = 0
        for proc in psutil.process_iter():
            if proc.name().lower() == 'actividad5.exe':
                activo = 1
                break
        if not activo:
            os.system('Actividad5.exe')