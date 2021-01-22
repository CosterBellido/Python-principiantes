# Notificación de escritorio
import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = 'ALERT!!!',
            message = 'Toma un descanso! Ha pasdo una hora',
            timeout = 10)
        time.sleep(3600)