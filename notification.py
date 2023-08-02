import time
from plyer import notification

def set_notification():
    # 指定した時間に通知を表示する関数
    notification_time = input("通知を受け取る時間を入力してください（hh:mm）：")

    try:
        # 指定された時間の時間と分を取得
        hours, minutes = map(int, notification_time.split(':'))

        # 現在の時刻を取得
        current_time = time.localtime()

        # 指定された時間までの残り秒数を計算
        remaining_seconds = (hours - current_time.tm_hour) * 3600 + (minutes - current_time.tm_min) * 60

        if remaining_seconds <= 0:
            print("無効な時間です。未来の時間を入力してください。")
            return

        # 指定された時間まで待機
        time.sleep(remaining_seconds)

        # 通知を表示
        notification.notify(
            title="時間通知",
            message="時間です！",
            app_icon=None,  # 通知にアイコンを表示しない場合はNoneを指定
            timeout=10  # 通知を表示する秒数（デフォルトは10秒）
        )

    except ValueError:
        print("有効な時間を入力してください（hh:mm）")

if __name__ == "__main__":
    set_notification()

