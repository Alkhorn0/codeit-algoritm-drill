# greedy(?)
# 인턴에 나갈 사람은 성별 상관없이 아무나 관계없으므로
# 전체학생에서 인턴 나가는 수를 뺀 뒤 팀의 기준인 3으로 나눈수와,
# 팀을 이루기 위한 기준인 여자 2, 남자 1의 비율로 가장 작은 수를 구하면
# 곧 만들 수 있는 팀의 수중 가장 최대의 갯수가 된다(그리디적 사고)

n, m, k = map(int, input().split())
print(min((n+m-k)//3, n//2, m))