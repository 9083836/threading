import time
import threading

def create_file(file_number):
    time.sleep(1)
    file_name = f"file_{file_number}.txt"
    with open(file_name, "w") as file:
        file.write(f"This is file number {file_number}")
    print(f"{file_name} has been created")
    return file_name


if __name__ == "__main__":
    start_time = time.time()  # Начало замера времени

    threads = []  # Список для хранения потоков
    for i in range(100):
        #Новый поток для выполнения функкции
        thread = threading.Thread(target=create_file, args=(i,))
        #Добавление потока в список 
        threads.append(thread)
        thread.start()  # Запуск потока

    # Ожидание завершения всех потоков
    for thread in threads:
        thread.join()

    end_time = time.time()  # Конец замера времени
    print(f"Total time: {end_time - start_time} seconds")

