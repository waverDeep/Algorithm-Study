def solution(routes):
    answer = 0
    last_camera = -30001 # 카메라 설치 지점
    routes.sort(key = lambda x:x[1]) # 도착 시간을 기점으로 정렬

# 카메라 설치 기준 점이 route의 진입지점보다 작다면 새로운 카메라를 설치해야 한다.
# 카메라 설치 기준 점이 route의 진인지점보다 크다면 당연히 카메라를 만나므로 고려하지 않아도 된다.(그리디의 정당성 확보)
    for route in routes:
        if last_camera < route[1]:
            last_camera = route[1]
            answer += 1

    return answer