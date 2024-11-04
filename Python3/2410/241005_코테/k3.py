# 길을 따라 (0부터 N-1까지 번호가 매겨진) N채의 집이 늘어서 있다. 각 집의 재활용 쓰레기(플라스틱, 유리, 금속)는 별도의 봉투에 넣어 수거된다.
#
# 쓰레기를 수거하는 트럭은 세 대이다. 각각의 트럭은 서로 다른 종류의 쓰레기를 수거한다(첫 번째 트럭은 플라스틱, 두 번째는 유리, 세 번째는 금속). 모든 트럭은 길이 시작되는 지점에서 작업을 시작하고 끝낸다. 출발점에서 0번 집까지 통과하는 데는 D[0]분이 걸린다. K-1번 집과 K번 집 사이를 통과하는 데는 D[K]분이 걸린다(K는 1부터 N-1까지 범위로 함). 봉투 한 개를 트럭에 싣는 데는 1분이 걸린다.
#
# 예를 들어 D = [2, 5]는 출발점과 0번 집 사이를 통과하는 데 2분이 걸리고 0번 집과 1번 집 사이를 통과하는 데 5분이 걸린다는 것을 의미한다.
#
# 각각의 각각의 집에서는 이미 몇 개의 (또는 0개의) 재활용 쓰레기 봉투를 모아 두었다. K번 집이 모은 봉투의 개수는 글자 `P`(플라스틱), `G`(유리), `M`(금속)으로 구성되는 문자열 T[K]에 기록된다. 예를 들어 T[1] = "GMG"는 1번 집이 유리 봉투 두 개와 금속 봉투 한 개를 모아 두었다는 것을 의미한다. 각각의 집은 종류별 봉투를 한 개 이상 모아둘 수 있다.
#
# 모든 트럭은 동시에 작업을 시작한다. 각각의 트럭은 정해진 종류의 쓰레기 봉투를 모두 수거하고 출발점으로 복귀한 후 작업을 끝낸다. 모든 트럭이 모든 작업을 끝낼 때까지 걸리는 시간은 최소 몇 분인가?
# 함수를 작성하십시오:
# `def solution(D, T)`
# 정수 N개로 구성된 배열 D와 문자열 N개로 구성된 배열 T가 주어졌을 때 트럭들이 모든 작업을 끝내는 데 필요한 최소 시간(분)을 반환해야 한다.
#
# 예제:
# 1. D = [2,5], T = ["PGP", "M"]일 때 함수는 15를 반환해야 한다. 플라스틱을 수거하는 트럭은 0번 집으로 가서 두 개의 봉투를 수거하고 돌아가야 하며, 여기에는 2 + 1 + 1 + 2 = 6분이 걸린다. 유리를 수거하는 트럭은 5분이 필요하다: 0번 집으로 가는데 2분, 봉투 한 개를 수거하는 1분, 출발점으로 돌아가는 데 2분이 걸린다. 금속을 수거하는 트럭은 곧장 1번 집으로 가서 한 개의 봉투를 수거하고 돌아가는데 7 + 1 + 7 = 15분이 걸린다. 15분 후에는 모든 쓰레기가 수거되고 모든 트럭이 출발점으로 되돌아가 있을 것이다.
#
# 2. D = [3,2,4], T = ["MPM", "", "G"]일 때 함수는 19를 반환해야 한다. 유리를 수거하는 트럭에 가장 많은 시간이 필요하다 : 3 + 2 + 4 + 1 + 4 + 2 + 3 = 19
#
# 3. D = [2,1,1,1,2], T = ["", "PP", "PP", "GM", ""]일 때 함수는 12를 반환해야 한다. 작업을 끝내는 데 플라스틱을 수거하는 트럭은 12분이 필요하고 유리를 수거하는 트럭과 금속을 수거하는 트럭은 11분이 필요하다.
#
# 다음 가정에 대한 효율적인 알고리즘을 작성하십시오:
# * N은 [1..100000] 범위의 정수입니다.
# * 배열 D의 각 요소는 [1..100] 범위 내의 정수입니다.
# * 배열 T의 각 원소는 글자 `P`, `G` 또는 `M`으로 구성된 문자열입니다.
# * 모든 문자열의 총 길이 S는 [0..100000] 범위의 정수입니다.
#
# 천천히 생각해서 답변해주세요.

def solution(D, T):
    N = len(T)  # 집의 수
    max_plastic_time = -1  # 플라스틱 수거 트럭의 최종 시간
    max_glass_time = -1  # 유리 수거 트럭의 최종 시간
    max_metal_time = -1  # 금속 수거 트럭의 최종 시간

    # 거리를 누적합으로 관리
    cumulative_distance = [0] * N
    cumulative_distance[0] = D[0]
    for i in range(1, N):
        cumulative_distance[i] = cumulative_distance[i - 1] + D[i]

    ap = ''.join(T).count("P")
    ag = ''.join(T).count("G")
    am = ''.join(T).count("M")

    # 각 트럭의 최대 거리를 찾는다
    for i in range(N):
        plastic_count = T[i].count('P')
        glass_count = T[i].count('G')
        metal_count = T[i].count('M')

        if plastic_count > 0:
            # 플라스틱 트럭이 i번 집까지 갔다가 돌아오는 데 걸리는 시간 계산
            travel_time = 2 * cumulative_distance[i]
            collect_time = ap
            max_plastic_time = max(max_plastic_time, travel_time + collect_time)

        if glass_count > 0:
            # 유리 트럭이 i번 집까지 갔다가 돌아오는 데 걸리는 시간 계산
            travel_time = 2 * cumulative_distance[i]
            collect_time = ag
            max_glass_time = max(max_glass_time, travel_time + collect_time)

        if metal_count > 0:
            # 금속 트럭이 i번 집까지 갔다가 돌아오는 데 걸리는 시간 계산
            travel_time = 2 * cumulative_distance[i]
            collect_time = am
            max_metal_time = max(max_metal_time, travel_time + collect_time)

    # 세 트럭 중 가장 오래 걸리는 트럭의 시간을 반환
    return max(max_plastic_time, max_glass_time, max_metal_time)

print(solution([2,1,1,1,2], ["", "PP", "PP", "GM", ""])) #-> 12
print(solution([2,2],["PPPPPPPPPP","PM"])) #-> 19
