import pyaudio
import wave

CHUNK = 1024

wf = wave.open('R.wav', 'rb')
p = pyaudio.PyAudio()

# 음성데이터 스트림 열기
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)

# 음성데이터를 입력받아 출력
while data:
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()
p.terminate()
wf.close()