def solution(video_len, pos, op_start, op_end, commands):
    # 영상길이확인 + 오프닝 건너뛰기
    def check_time(time:int) -> int:
        # 영상길이확인
        if time < 0:
            time = 0
        elif time > mm_to_ss(video_len):
            time = mm_to_ss(video_len)
        # 오프닝 건너뛰기
        if mm_to_ss(op_start) <= time and time <= mm_to_ss(op_end):
            time = mm_to_ss(op_end)
        return time
    # mm to ss: str -> int
    def mm_to_ss(time:str) -> int:
        mm = int(time.split(':')[0])
        ss = int(time.split(':')[1])
        return mm*60 + ss
    # ss to mm: int -> str
    def ss_to_mm(time:int) -> str:
        mm = str(time//60).rjust(2,'0')
        ss = str(time%60).rjust(2,'0')
        return ':'.join([mm,ss])
    # 명령수행
    pos = mm_to_ss(pos) # int 변환
    
    pos = check_time(pos)
    for command in commands:
        if command == "prev":
            pos -= 10
        elif command == "next":
            pos += 10
        pos = check_time(pos)
        
    pos = ss_to_mm(pos) # str 변환
    return pos