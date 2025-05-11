## 실시간 CCTV 특정구간 추출
![image](https://github.com/user-attachments/assets/ac3b1ee1-f3b1-44f3-9bdb-ee6513dc2fb4)


### 예상 구조
> tee 없이 RTSP에 2회 접속

```
┌──────────────────────────────┐
│          RTSP CCTV           │
└────────────┬─────────────────┘
             │
   ┌─────────▼──────────┐
   │ [파이프라인 1]     │  ← 실시간 뷰어
   │ rtspsrc → decodebin│
   │         → sink     │
   └────────────────────┘

   ┌─────────▼──────────┐
   │ [파이프라인 2]     │  ← 클립 저장용
   │ rtspsrc → decodebin│
   │         → x264enc → mp4mux → filesink │
   └────────────────────┘

```
