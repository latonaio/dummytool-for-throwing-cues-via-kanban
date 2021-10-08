import time
import logging
from aion.microservice import main_decorator, Options, WITH_KANBAN

# services.ymlに記載するサービス名
SERVICE_NAME = "dummy-test-kanban"
CONNECTION_KEY = "default"

# @main_decorator は aion-statuskan と接続・マイクロサービスが正常に立ち上がったことを通知する
@main_decorator(SERVICE_NAME, WITH_KANBAN)
def main(opt: Options):
    conn = opt.get_conn()
    try:
        # 5秒置きにデータを送る
        while(1):
            logging.debug("sendmessage for debug")
            conn.output_kanban(
                connection_key = CONNECTION_KEY,
                result = True,
                metadata = {
                    "log": "this is dummy data",
                }
            )
            time.sleep(5)
    except Exception as e:
            logging.error(e)
            raise

if __name__ == "__main__":
    main()


     