import sys
import json
import requests
import gi

gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib

# GStreamer 초기화
Gst.init(sys.argv[1:])

def fetch_cctv_url():
    api_url = "https://openapi.its.go.kr:9443/cctvInfo"
    params = {
        "apiKey": "국가교통정보센터에서 발급받은 API 키",
        "type": "lts",
        "cctvType": "1",
        "minX": "129.07",
        "maxX": "130.07",
        "minY": "37.6",
        "maxY": "38.6",
        "getType": "json"
    }

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()

        # 전체 JSON 응답 로그 출력
        print("[DEBUG] 전체 응답 JSON:")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))

        data = response.json()
        cctv_info = data.get("response", {}).get("data", {})
        if not cctv_info:
            print("[ERROR] CCTV 데이터가 없습니다.")
            return None

        print(f"[INFO] 선택된 CCTV 이름: {cctv_info.get('cctvname')}")
        print(f"[INFO] CCTV 형식: {cctv_info.get('cctvformat')}")

        return cctv_info.get("cctvurl")
    except Exception as e:
        print(f"[ERROR] API 호출 실패: {e}")
        return None

def play_stream(cctv_url):
    print(f"[INFO] 재생할 CCTV 주소: {cctv_url}")
    pipeline = Gst.parse_launch(f"playbin uri=\"{cctv_url}\"")
    pipeline.set_state(Gst.State.PLAYING)

    # 종료 메시지 대기
    bus = pipeline.get_bus()
    msg = bus.timed_pop_filtered(
        Gst.CLOCK_TIME_NONE,
        Gst.MessageType.ERROR | Gst.MessageType.EOS
    )

    print("[INFO] 영상 재생 종료")
    pipeline.set_state(Gst.State.NULL)

if __name__ == "__main__":
    stream_url = fetch_cctv_url()
    if stream_url:
        play_stream(stream_url)
    else:
        print("[ERROR] CCTV URL을 가져올 수 없습니다.")
