import queue, random

queue = queue.Queue()


# Створюємо заявку із випадковим айді від 1 до 50
def generate_request():
    request_id = random.randint(1, 50)
    queue.put(request_id)
    print(f"Надійшла заявка із ID: {request_id}")


# Обробляємо (видаляємо заявку) з черги
def process_request():
    if queue.empty():
        print("Черга заявок порожня")
    else:
        request_id = queue.get()
        print(f"Обробка та видалення заявки із ID: {request_id}")


def main():
    for _ in range(1, 20):
        generate_request()
        process_request()


if __name__ == "__main__":
    main()
