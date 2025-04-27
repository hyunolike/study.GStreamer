## Basic tutorial 1: Hello world!
> [공식문서](https://gstreamer.freedesktop.org/documentation/tutorials/basic/hello-world.html?gi-language=c)

### 튜토리얼 요약
![image](https://github.com/user-attachments/assets/5c064ca3-3d36-4c82-8e24-53b39e2264ba)


### 가장 먼저 `GStreamer` 런타임 환경을 구축하자
- 필수 운영체제: 우분투
- 런타임 환경 설치는 공식문서 확인
  - ![image](https://github.com/user-attachments/assets/c0308e2b-f91f-4bc0-b589-19ff3034d8b6)
- 언어: 파이썬 (우분투에 기본적으로 깔려져있음)
  - 필요시 pip, venv 설치 진행 !
 
### 파이썬 연동에 필요한 패키지 설치하기
> [!TIP]
> 중요. python3-gi, python3-gst-1.0 같은 GStreamer Python 바인딩은 apt로만 설치 가능한 경우가 많습니다.
PyPI(pip)에는 없거나, 빌드가 너무 복잡합니다.


```sh
sudo apt install python3-gi python3-gst-1.0 gir1.2-gstreamer-1.0
```

|패키지 명|설명|
|-|-|
|python3-gi|PyGObject: Python에서 GObject 기반 라이브러리 사용 가능하게 해줌|
|python3-gst-1.0|GStreamer Python 바인딩|
|gir1.2-gstreamer-1.0|introspection 데이터를 제공 (동적 바인딩 시 필요)|


#### 추가. 가상환경에서는 바로 접근하기 어렵다! 따라서 가상환경 생성 시 아래와 같이 만들자
```sh
python3 -m venv venv --system-site-packages
```

이렇게 하면 시스템에 설치된 gi 모듈도 가상환경에서 접근 가능 !! 

#### 왜, 이렇게 해야할까?
```
기본적으로 venv는 외부(시스템)의 Python 모듈을 차단해서, 완전히 독립된 환경을 만들어요.
하지만 GStreamer처럼 apt로 설치해야 하는 모듈은 이 차단을 풀어줘야 쓸 수 있는 거예요.

그래서 --system-site-packages 옵션이 필요합니다.
```


### 환경을 그림으로 요약하면?
![image](https://github.com/user-attachments/assets/e9439ee3-8f91-4fba-9182-4e6df83b132c)

### 공식문서에 나와있는 튜토리얼 코드 복붙 후, 실행 결과
![image](https://github.com/user-attachments/assets/c192a5b9-724a-45ff-a3b5-d08a8014d766)
