import os
import threading
import queue
import subprocess
from yt_dlp import YoutubeDL

# def downloadVideo(url, outputFolder, videoId, episode):
#     fileName = f"{videoId}-{episode}"
#     ydlOptions = {
#         'format': 'best',
#         'outtmpl': os.path.join(outputFolder, f'{fileName}.%(ext)s'),
#     }
#     with YoutubeDL(ydlOptions) as ydl:
#         ydl.download([url])

# yt-dlpで動画情報を取得
def getTitle(url):
    info = YoutubeDL().extract_info(url, download=False)  # 動画情報を取得
    videoTitle = info.get("title", "unknown_title")  # タイトル取得
    return videoTitle

def downloadVideo(url, outputFolder, videoId, episode):
    fileName = f"{getTitle(url)}-{videoId}-{episode}"
    filePath = os.path.join(outputFolder, f'{fileName}.%(ext)s')

    # yt-dlpコマンドをサブプロセスで実行
    # なぜか知らないけど連続でプログラムとしてyt-dlpを使ってabemaをDL使用とすると出来なくなる
    command = [
        'yt-dlp',
        '-f', 'best',
        '-o', filePath,
        url
    ]
    
    # サブプロセスでyt-dlpを実行
    subprocess.run(command, check=True)

def worker(queue):
    while not queue.empty():
        task = queue.get()
        if task is None:
            break
        url, outputFolder, videoId, episode = task
        
        print(f"Start Downloading {url} ...")
        
        try:
            downloadVideo(url, outputFolder, videoId, episode)
        except Exception as e:
            print(f"Error downloading episode {episode}: {e}")
        finally:
            queue.task_done()

def createDownloader():
    videoId = input("動画IDを入力してください: ")
    title = input("タイトルを入力してください: ")
    episodeStart = int(input("エピソードの始まり番号を入力してください: "))
    episodeEnd = int(input("エピソードの終わり番号を入力してください: "))


    # 保存フォルダを作成
    outputFolder = os.path.join(os.getcwd(), title)
    os.makedirs(outputFolder, exist_ok=True)

    # タスクキューを作成
    taskQueue = queue.Queue()

    # ダウンロードタスクをキューに追加
    baseUrl = "https://abema.tv/video/episode"
    for episode in range(episodeStart, episodeEnd + 1):
        episodeUrl = f"{baseUrl}/{videoId}_p{episode}"
        taskQueue.put((episodeUrl, outputFolder, videoId, episode))

    # テスト用
    # for i in range(taskQueue.qsize()):
    #     worker(taskQueue)

    # スレッドを作成して開始
    threads = []
    maxThreads = 2  # 最大スレッド数
    for _ in range(maxThreads):
        thread = threading.Thread(target=worker, args=(taskQueue,))
        thread.setDaemon(True)
        thread.start()
        threads.append(thread)

    # キューが空になるまで待機
    taskQueue.join()

    # スレッドの終了を待機
    for thread in threads:
        thread.join()

    print("全てのダウンロードが完了しました！")

if __name__ == "__main__":
    createDownloader()
