import schedule
import time
from ftplib import FTP

def check_file_in_directory(ftp_host, ftp_user, ftp_pass, directory_path, file_name):
    try:
        # FTPサーバーに接続
        ftp = FTP(ftp_host)
        ftp.login(ftp_user, ftp_pass)

        # 指定のディレクトリに移動
        ftp.cwd(directory_path)

        # ファイルの一覧を取得
        file_list = []
        ftp.retrlines('NLST', file_list.append)

        # ファイルの存在を確認
        file_exists = file_name in file_list
        if file_exists:
            print(f"ファイル {file_name} はディレクトリ {directory_path} に存在します．")
            # FTPセッションを閉じる
            ftp.quit()
            # ファイルが見つかった場合は関数を終了
            return True

        else:
            print(f"ファイル {file_name} はディレクトリ {directory_path} に存在しません．")

        # FTPセッションを閉じる
        ftp.quit()

        return False

    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return False

# 使用例
ftp_host = '192.168.11.13'
ftp_user = 'pi'
ftp_pass = '0804'
file_path = '/home/pi/Desktop'
file_name = 'dem.txt'

interval_seconds = 5

while True:
    result = check_file_in_directory(ftp_host, ftp_user, ftp_pass, file_path, file_name)
    if result:
        # ファイルを見つけた場合はループを終了
        print('ファイルを見つけたので処理を終了')
        break

    # 定期実行
    schedule.every(interval_seconds).seconds.do(check_file_in_directory, ftp_host, ftp_user, ftp_pass, file_path, file_name)
    time.sleep(interval_seconds)