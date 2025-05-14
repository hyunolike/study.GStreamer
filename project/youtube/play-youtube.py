import subprocess
import sys
import gi

gi.require_version('GLib', '2.0')
gi.require_version('GObject', '2.0')
gi.require_version('Gst', '1.0')

from gi.repository import Gst, GObject, GLib

# GStreamer 초기화
Gst.init(None)

def get_youtube_stream_url(youtube_url):
    # yt-dlp로 유튜브 스트리밍 URL 추출
    command = ['yt-dlp', '-g', '-f', 'best', youtube_url]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    if result.returncode == 0:
        stream_url = result.stdout.strip()
        return stream_url
    else:
        print("Failed to get stream URL")
        print(result.stderr)
        return None

def play_stream(url):
    # playbin을 이용한 영상 재생
    pipeline = Gst.ElementFactory.make("playbin", "player")
    pipeline.set_property("uri", url)

    # 재생 시작
    pipeline.set_state(Gst.State.PLAYING)

    # 이벤트 루프
    loop = GLib.MainLoop()
    bus = pipeline.get_bus()
    bus.add_signal_watch()

    def on_message(bus, message):
        t = message.type
        if t == Gst.MessageType.EOS or t == Gst.MessageType.ERROR:
            pipeline.set_state(Gst.State.NULL)
            loop.quit()

    bus.connect("message", on_message)

    try:
        loop.run()
    except:
        pipeline.set_state(Gst.State.NULL)

if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=LuPg2fjdaPE"  # 원하는 영상 링크로 바꾸세요
    stream_url = get_youtube_stream_url(youtube_url)
    if stream_url:
        print(f"Streaming URL: {stream_url}")
        play_stream(stream_url)
