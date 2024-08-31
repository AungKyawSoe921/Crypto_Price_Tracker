import ccxt
import time
import threading
from plyer import notification
import tkinter as tk
from tkinter import messagebox


class BitcoinPriceTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Bitcoin Price Tracker")

        self.is_tracking = False
        self.initial_price = None

        self.create_widgets()

    def create_widgets(self):
        self.start_button = tk.Button(self.root, text="Start Tracking", command=self.start_tracking)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop Tracking", command=self.stop_tracking, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.status_label = tk.Label(self.root, text="Status: Not Tracking")
        self.status_label.pack(pady=10)

    def get_current_price(self):
        exchange = ccxt.binance()
        ticker = exchange.fetch_ticker('BTC/USDT')
        return ticker['last']

    def send_notification(self, title, message):
        notification.notify(
            title=title,
            message=message,
            app_name='Bitcoin Price Tracker',
            timeout=10
        )

    def track_price_drop(self):
        self.initial_price = self.get_current_price()
        self.last_notified_price = self.initial_price
        drop_threshold = 0.01  # 1%

        self.update_status(f"Tracking started. Initial Bitcoin Price: ${self.initial_price:.2f}")

        while self.is_tracking:
            current_price = self.get_current_price()
            price_drop = (self.initial_price - current_price) / self.initial_price

            if price_drop >= drop_threshold:
                self.send_notification(
                    title='Bitcoin Price Alert',
                    message=f'Bitcoin price dropped by {price_drop * 100:.2f}%!\nCurrent Price: ${current_price:.2f}'
                )
                self.update_status(
                    f'Notification sent: Bitcoin price dropped by {price_drop * 100:.2f}%! Current Price: ${current_price:.2f}')
                self.initial_price = current_price  # Reset initial price to current price after notification

            time.sleep(60)  # Check price every 60 seconds

    def start_tracking(self):
        self.is_tracking = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.status_label.config(text="Status: Tracking")
        self.tracking_thread = threading.Thread(target=self.track_price_drop)
        self.tracking_thread.start()

    def stop_tracking(self):
        self.is_tracking = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="Status: Not Tracking")
        self.update_status("Tracking stopped.")

    def update_status(self, message):
        self.status_label.config(text=f"Status: {message}")
        print(message)


if __name__ == "__main__":
    root = tk.Tk()
    app = BitcoinPriceTracker(root)
    root.mainloop()
